import sqlite3

# Cria o banco de dados
connection = sqlite3.connect('database.db')

# Executa o schema
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insere os registros
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
        )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
        )

# Grava as alterações na tabela
connection.commit()
# Encerra a conexão
connection.close()
