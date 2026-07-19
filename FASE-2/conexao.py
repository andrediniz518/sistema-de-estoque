import mysql.connector


def conectar():
    conexao = mysql.connector.connect(
        host = 'localhost', #endereço do servidor
        user = 'root',
        password = 'sua_senha',
        database = 'seu_database'
    )
    return conexao
