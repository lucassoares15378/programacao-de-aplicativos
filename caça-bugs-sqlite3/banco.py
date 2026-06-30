import sqlite3
def inicializar_banco():
    conexao = sqlite3.connect('sistema-escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    conexao.commit() #faltou o commit para salvar
    conexao.close()