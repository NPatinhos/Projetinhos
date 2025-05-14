import sqlite3

# Criação do banco e da tabela se não existir
conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

# Cria a tabela caso não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

print("✅ Banco de dados e tabela criados com sucesso!")

conexao.commit()
conexao.close()
