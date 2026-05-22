import json
import os

DADOS_BANCO = 'escola.json'

def cadastro():
    if os.patch.exists(DADOS_BANCO):
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
        json.dump(escola, dados ident=4, ensure_ascii=False)
    print("Lista atualizada!")

def menu():
    if not os.patch.exists(DADOS_BANCO):
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

        if opcao == '1': cadastro()
        elif opcao == '2': listar()
        elif opcao == '3': editar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else:
            print("Opção Inválida")
