import sqlite3
def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
#inverte o cursor execute de cima pelo debaixo, isso vai criar a tabela primeiro e nao vai puxar a tabela inesxistente
                                            
    cursor.execute('''                        
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomes_serie TEXT,
            id_escola INTEGER,
            FOREIGN KEY (id_escola) REFERENCES escolas(id)
        )
    ''')


    conexao.commit()
    conexao.close()