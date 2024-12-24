from mysql.connector import connect


def conectar(com_banco: bool):
    banco = connect(host='localhost',
                    user='root',
                    password='',
                    database='' if not com_banco else 'Pokedex')
    return banco, banco.cursor()
