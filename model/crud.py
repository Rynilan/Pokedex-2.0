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


def tipos() -> tuple[str]:
    banco, cursor = conectar()
    cursor.execute('select nome from tb_tipos;')
    resultados = cursor.fetchall()
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
    cursor.execute(
        'SELECT tb_pokemons.numero_geral, tb_pokemons.nome, tipo1.nome AS tipo1_nome, tipo2.nome AS tipo2_nome, tb_pokemons.foto, tb_pokemons.vida, tb_pokemons.defesa, tb_pokemons.ataque, tb_regioes.nome AS regiao_nome, tb_pokemons.descrição FROM tb_pokemons JOIN tb_tipos AS tipo1 ON tb_pokemons.tipo_1 = tipo1.id LEFT JOIN tb_tipos AS tipo2 ON tb_pokemons.tipo_2 = tipo2.id JOIN tb_regioes ON tb_pokemons.região = tb_regioes.id; ' +
        ';' if not (campos and valores) else 'where ' + str(campos[index] + '=' + str(valores[index]) + ' and ' for index in range(len(campos))).removesuffix('and ')
    )
    resultados = cursor.fetchall()
    cursor.close()
    banco.close()
    return resultados
