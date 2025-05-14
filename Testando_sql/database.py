import sqlite3

# Função para conectar ao banco de dados
def conectar():
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()
    return conexao, cursor

# Função para desconectar do banco de dados
def desconectar(conexao):
    conexao.close()