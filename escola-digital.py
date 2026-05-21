import json

arquivo_nome = "alunos.json"

while True:
    print("\n1.Cadastrar | 2.Listar | 3.Editar | 4.Excluir | 5.Sair")
    opçao = input("Opçao: ")

    if opçao == "1":
        cpf = input("CPF: ")
        if (aluno["cpf"] == cpf for aluno in lista):
            print("Erro! CPF já existe")
        else:
            cadastro = {
                "cpf": cpf,
                "nome": input("Nome: "),
                "telefone": input ("Telefone: "),
                "turma": input("Turma:"),
                "idade": input("Idade:"),
            }
            lista.append(cadastro)
            json.dump(lista, open(arquivo_nome, 'w'))
            print("Salvo")