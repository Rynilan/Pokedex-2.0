from mysql.connector import connect


def conectar(com_banco: bool = True):
    banco = connect(host='localhost',
                    user='root',
                    password='',
                    database='' if not com_banco else 'Pokedex')
    return banco, banco.cursor()


def campos() -> tuple[str]:
    banco, cursor = conectar()
    cursor.execute('describe tb_pokemons;')
    resultados = tuple(campo[0] for campo in cursor.fetchall())
    cursor.close()
    banco.close()
    return resultados


def tipos() -> list[str]:
    banco, cursor = conectar()
    cursor.execute('select nome from tb_tipos;')
    resultados = list(elemento[0] for elemento in cursor.fetchall())
    cursor.close()
    banco.close()
    return resultados


def regioes() -> tuple[str]:
    banco, cursor = conectar()
    cursor.execute('select nome from tb_regioes;')
    resultados = cursor.fetchall()
    cursor.close()
    banco.close()
    return resultados


def select_join(
    pesquisa: bool = False,
    campos: tuple[str] = (),
    valores: tuple[any] = ()
) -> tuple[str]:
    banco, cursor = conectar()
    filtro = ''
    if len(campos) == len(valores) and campos and valores:
        filtro += 'where '
        for index in range(len(campos)):
            filtro += 'tb_pokemons.' + campos[index] + '=' + str(valores[index]) + ' and '
        filtro = filtro.removesuffix('and ')
    cursor.execute(
        'SELECT tb_pokemons.numero_geral, tb_pokemons.nome, tipo1.nome AS tipo1_nome, tipo2.nome AS tipo2_nome, tb_pokemons.foto, tb_pokemons.vida, tb_pokemons.defesa, tb_pokemons.ataque, tb_regioes.nome AS regiao_nome, tb_pokemons.descrição FROM tb_pokemons JOIN tb_tipos AS tipo1 ON tb_pokemons.tipo_1 = tipo1.id LEFT JOIN tb_tipos AS tipo2 ON tb_pokemons.tipo_2 = tipo2.id JOIN tb_regioes ON tb_pokemons.região = tb_regioes.id ' + filtro + ' order by numero_geral;'
    )
    resultados = cursor.fetchall()
    cursor.close()
    banco.close()
    return resultados


def insert(valores: tuple[str],
           campos: tuple[str] = '*'):
    banco, cursor = conectar()
    valores = list(valores)
    parametro = ''
    for indice, valor in enumerate(valores):
        if valor in regioes():
            cursor.execute('select id from tb_regioes where nome = %s;',
                           (valor, ))
            valores[indice] = cursor.fetchall()[0][0]
        elif valor in tipos():
            cursor.execute('select id from tb_tipos where nome = %s;',
                           (valor, ))
            valores[indice] = cursor.fetchall()
        parametro += ' %s'

    cursor.execute('insert into tb_pokemons {} values {};'.format(
        campos.__str__(), valores.__str__()
    ))
    banco.commit()
    cursor.close()
    banco.close()
