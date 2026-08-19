import sqlite3

try:
    conexao = sqlite3.connect('armazem.db')
    cursor = conexao.cursor()
except sqlite3.Error as erro:
    print(f"Erro ao conectar o banco de dados: {erro}")
    exit()



def cadastrar_operadores(razao_social, inscricao_estadual):
    try:
    
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS operadores_logisticos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            razao_social TEXT NOT NULL,
            inscricao_estadual INTEGER
        )
        ''')

        comando_inserir = f'''
        INSERT INTO operadores_logisticos(razao_social, inscricao_estadual)
        VALUES('{razao_social}', '{inscricao_estadual}')
        '''

        cursor.execute(comando_inserir)
        conexao.commit()
        print("Cadastro feito com sucesso!")
        return razao_social, inscricao_estadual
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados ao cadastrar: {erro}")

assert cadastrar_operadores("mercado livre", "234235") == ("mercado livre", "234235")
print("Correto")