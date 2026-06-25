import sqlite3
conexao = sqlite3.connect('escola.demonstracao.db')
cursor = conexao.cursor()


def cadastrar_professor():
    nome_completo = input("Digite o nome completo: ")
    telefone_professor = input("Digite o telefone: ")
    materia = input("Digite a Materia: ")
    idade_professor = int(input("Digite a idade: "))
    cpf = input("Digite o cpf: ")
    salario = (input("Digite seu salario: "))
    escola = (input("Digite o nome da escola: "))
    endereco = input("Digite o endereço: ")

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT, 
        turma TEXT, 
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL,
        salario TEXT NOT NULL,
        escola TEXT,
        endereco
    )
    ''')
    comando_inserir = f'''
        INSERT INTO professores(nome, telefone, turma, idade, cpf, salario, escola, endereco)
        VALUES('{nome_completo}', '{telefone_professor}', '{materia}', '{idade_professor}', '{cpf}', '{salario}', '{escola}', '{endereco}')'''

    cursor.execute(comando_inserir)
    conexao.commit()


def listar():
    conexao.commit()
    cursor.execute("SELECT * FROM professores")
    for linha in cursor.fetchall():
        print(linha)
    print("\n")



def atualizar():
    id_professor = input("Digite o id do professor: ")
    novo_nome = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo telefone: ")
    nova_materia = input("Digite a nova materia: ")
    nova_idade = input("Digite a nova idade: ")
    novo_cpf = input("Digite o novo CPF: ")
    novo_salario = (input("Digite seu salario: "))
    nova_escola = (input("Digite o nome da escola: "))
    novo_endereco = input("Digite o novo endereço: ") 

    cursor.execute('''
                   UPDATE professores
                   SET nome = ?, telefone = ?, turma = ?, idade = ?, cpf = ?, salario = ?, escola = ?, endereco = ?, WHERE id = ?''', (novo_nome, novo_telefone, nova_materia, nova_idade, novo_cpf, novo_salario, nova_escola, novo_endereco. id_professor))
    conexao.commit()
    print("Dados atualizados com sucesso! ")



def excluir():
    id_professor = input("Digite o ID do professor que deseja excluir: ")
    cursor.execute(
        "DELETE FROM professores WHERE id = ?", (id_professor,)
    )

    conexao.commit()
    if cursor.rowcount > 0 :
        print("Professor excluido com sucesso.")
    else:
        print("Nenhum professor encontrado com esse ID. ")


def menu():
    while True:
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Alterar Professor")
        print("4. Excluir Professor")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_professor()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            atualizar()
        elif opcao == '4':
            excluir()
        elif opcao == '5':
            print("Saindo")
            break
        else:
            print("Opção inválida! Tente novamente.")
            
    conexao.close()

if __name__ == "__main__":
    menu()

