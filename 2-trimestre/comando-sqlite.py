import sqlite3
conexao = sqlite3.connetc('escola.demonstracao.db'):
cursor = conexao.cursor()

cursor.execute('''ALTER TABLE alunos ADD COLUMNS
    endereco TEXT,
    cidade TEXT,
    estado TEXT
    ''')