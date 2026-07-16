import mysql.connector


def conectar():
    conexao = mysql.connector.connect(
        host = 'localhost', #endereço do servidor
        user = 'root',
        password = 'capcon166',
        database = 'estoque'
    )
    return conexao