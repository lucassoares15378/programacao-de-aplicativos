import escola
import turma
import aluno

def menu_escolas():
    opcao = 0
    while opcao != 5:
        print("\n--- MENU ESCOLAS ---")
        print("1. Cadastrar Escola")
        print("2. Listar Escolas")
        print("3. Alterar Escola")
        print("4. Excluir Escola")
        print("5. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1: escola.cadastrar()
        elif opcao == 2: escola.listar()
        elif opcao == 3: escola.alterar()
        elif opcao == 4: escola.excluir()

def menu_turmas():
    opcao = 0
    while opcao != 5:
        print("\n--- MENU TURMAS ---")
        print("1. Cadastrar Turma")
        print("2. Listar Turmas")
        print("3. Alterar Turma")
        print("4. Excluir Turma")
        print("5. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1: turma.cadastrar()
        elif opcao == 2: turma.listar()
        elif opcao == 3: turma.alterar()
        elif opcao == 4: turma.excluir()

def menu_alunos():
    opcao = 0
    while opcao != 5:
        print("\n--- MENU ALUNOS ---")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Alterar Aluno")
        print("4. Excluir Aluno")
        print("5. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1: aluno.cadastrar()
        elif opcao == 2: aluno.listar()
        elif opcao == 3: aluno.alterar()
        elif opcao == 4: aluno.excluir()

def menu_principal():
    opcao = 0
    while opcao != 4:
        print("  SISTEMA DE GESTAO ESCOLAR  ")
        print("1. Gerenciar Escolas")
        print("2. Gerenciar Turmas")
        print("3. Gerenciar Alunos")
        print("4. Sair")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1:
            menu_escolas()
        elif opcao == 2:
            menu_turmas()
        elif opcao == 3:
            menu_alunos()
        elif opcao == 4:
            print("Saindo do sistema...")

if __name__ == "__main__":
    menu_principal()