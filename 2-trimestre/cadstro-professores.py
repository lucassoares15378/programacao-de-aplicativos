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
    conexao.commit() 
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

    
    cursor.execute(f'''
    INSERT INTO professores (nome_professor, telefone_professor, materia_professor, idade_professor, cpf_professor, salario_professor, nome_da_escola)
    VALUES ('{nome_professor}', '{telefone_professor}', '{materia_professor}', {idade_professor}, '{cpf_professor}', '{salario_professor}', '{nome_da_escola}')
    ''')
    conexao.commit()
    print("Professor cadastrado com sucesso!")

def listar_professores(cursor, conexao=None): 
    print("---LISTA DE PROFESSORES---")
    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall() 

    if not professores:
        print("Nenhum professor cadastrado...")
        return

    for prof in professores:
        print(f"ID: {prof[0]} | Nome: {prof[1]} | Tel: {prof[2]} | Matéria: {prof[3]} | Idade: {prof[4]} | CPF: {prof[5]} | Salário: R${prof[6]} | Escola: {prof[7]}")

def editar_professor(cursor, conexao):
    print("--- ALTERAR PROFESSOR ---")
    listar_professores(cursor) 
    id_prof = input("Digite o ID do professor que deseja alterar: ")

    nome_professor = input("Novo Nome Completo: ")
    telefone_professor = input("Novo Telefone: ")
    materia_professor = input("Nova Matéria: ")
    idade_professor = int(input("Nova Idade: "))
    cpf_professor = input("Novo CPF: ")
    salario_professor = input("Novo Salário: R$")
    nome_da_escola = input("Nova Escola: ")

    cursor.execute(f'''
    UPDATE professores SET 
        nome_professor = '{nome_professor}', 
        telefone_professor = '{telefone_professor}', 
        materia_professor = '{materia_professor}', 
        idade_professor = {idade_professor}, 
        cpf_professor = '{cpf_professor}', 
        salario_professor = '{salario_professor}', 
        nome_da_escola = '{nome_da_escola}'
    WHERE id_professor = {id_prof}
    ''')
    conexao.commit()
    print("Dados alterados com sucesso!")

def excluir_professor(cursor, conexao):
    print("--- EXCLUIR PROFESSOR ---")
    listar_professores(cursor) 
    id_prof = input("\nDigite o ID do professor que deseja excluir: ")

    cursor.execute(f"DELETE FROM professores WHERE id_professor = {id_prof}")
    conexao.commit()
    print("Professor excluído com sucesso!")

def Menu():
    conexao, cursor = conectar()
    
    while True:
        print("---MENU ESCOLA---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Alterar")
        print("4. Excluir")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_professor(cursor, conexao)
        elif opcao == '2':
            listar_professores(cursor, conexao)
        elif opcao == '3':
            editar_professor(cursor, conexao)
        elif opcao == '4':
            excluir_professor(cursor, conexao)
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")
            
    conexao.close()

if __name__ == "__main__":
    Menu()
