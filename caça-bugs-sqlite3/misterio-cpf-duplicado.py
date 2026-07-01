import _sqlite3 

def cadastrar_professor (nome, cpf):
    conexao = _sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS professores (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   cpf UNIQUE TEXT
                   )
                   ''')
    
# o erro era pq o cpf é unico, e não foi usado o unique
