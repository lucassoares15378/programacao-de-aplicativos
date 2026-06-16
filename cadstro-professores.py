import sqlite3

def conectar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores(
        id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_professor TEXT NOT NULL,
        telefone_professor TEXT,
        materia_professor TEXT,
        idade_professor INTEGER,
        cpf_professor TEXT UNIQUE NOT NULL,
        salario_professor TEXT NOT NULL,
        nome_da_escola TEXT
    )
    ''')
    conexao.commit
    return conexao, cursor

def cadastrar_professor(cursor, conexao):
    print("---CADASTRAR PROFESSOR---")
    nome_professor = input("Nome: ")
    telefone_professor = input("Telefone: ")
    materia_professor = input("Matéria: ")
    idade_professor = int(input("Idade: "))
    cpf_professor = input("CPF: ")
    salario_professor = input("Salário: R$")
    nome_da_escola = input("Escola: ")

    cursor.execute(f"SELECT id_professor FROM professores WHERE id")
