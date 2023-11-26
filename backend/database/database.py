import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Crie a tabela para o cronograma
cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        activity TEXT NOT NULL
    )
''')

# Crie a tabela para as tarefas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0
    )
''')

# Salve as alterações e feche a conexão
conn.commit()
conn.close()