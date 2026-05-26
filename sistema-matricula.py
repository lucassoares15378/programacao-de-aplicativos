import json
import os

DADOS_BANCO = 'escola.json'

def cadastrar():
    if os.path.exists(DADOS_BANCO):

        with open(DADOS_BANCO, 'r', encoding='utf-8') as dados:
            escola = json.load(dados)
            
    else:
        escola = []

    estudante = {
        'id': int(input("ID: ")),
        'nome': input("Nome: "),
        'telefone': input("Telefone: "),
        'turma': input("Turma: "),
        'idade': int(input("Idade: ")),
        'cpf': input("CPF: "),
    }

    escola.append(estudante)

    with open(DADOS_BANCO, 'w', encoding='utf-8') as dados:
        json.dump(escola, dados, indent=4)

    print("Lista atualizada!")

def listar():
    if os.path.exists(DADOS_BANCO):
        with open(DADOS_BANCO, 'r', encoding='utf-8') as dados:
            escola = json.load(dados)
    else:
        alunos = []
    if not escola:
        print("Nenhm aluno cadastrado!")
        return 

    for dados in escola:
        print(f"ID: {dados['id']} Nome: {dados['nome']} | Telefone: {dados['telefone']} | Turma: {dados['turma']} | Idade: {dados['idade']} | CPF: {dados['cpf']}  ")

def editar():
    if not os.path.exists(DADOS_BANCO):
        print("Nenhum aluno cadastrado no sistema!")
        return
    with open(DADOS_BANCO, 'r', encoding='utf-8')as dados:
        escola = json.load(dados)
        id_busca = input("Qual o ID do aluno que você deseja alterar? ")
    
    for dados in escola:
        if dados['id'] == id_busca:
            print(f"Editando dados de: {escola['nome']}")
            escola['nome'] = input(f"Novo Nome ({escola['nome']}): ") or escola['nome']
            escola['telefone'] = input(f"Novo Telefone ({escola['telefone']}): ") or escola['telefone']
            escola['turma'] = input(f"Nova Turma ({escola['turma']}): ") or escola['turma']
            escola['idade'] = int(input(f"Nova Idade ({escola['idade']}): ") or escola['idade'])
            escola['cpf'] = input(f"Novo CPF ({escola['cpf']}): ") or escola['cpf']

            with open(DADOS_BANCO, 'w', encoding='utf-8') as dados:
                json.dump(escola, dados, indent=4)
            print("aluno atualizado!")
            return 
    else:
        print("Aluno não encontrado!")

def menu():
    if not os.path.exists(DADOS_BANCO):
        with open(DADOS_BANCO, 'w', encoding='utf-8') as dados:
            json.dump([], dados)
    while True:
        print("-----Sistema Escolar-----")
        print("1- Cadastrar")
        print("2- Listar")
        print("3- Editar")
        print("4- Excluir")
        print("5- Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': editar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else:
            print("Opção Inválida")
menu()
