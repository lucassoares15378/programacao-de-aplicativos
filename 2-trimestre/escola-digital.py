import json  #serve para pegar os arquivos de texto e mexer neles
import os #serve para procurar os arquivos 

BANCO_DADOS = 'alunos.json' #é aonde vamos salvar as informações

def cadastrar(): #é chamada a função de cadastar
    print("\n--- Novo Cadastro ---") #mostra a mensagem no terminal
    
    if os.path.exists(BANCO_DADOS): #ve se o caderno ja existe
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo, lê e deixa alinhado no terminal
            alunos = json.load(f) #converte em uma variavel
    else:
        alunos = [] #se ele não existir cria um novo

    novo_aluno = { #cria um objeto para cadastrar um novo aluno
        "nome": input("Nome: "), #pede o nome
        "telefone": input("Telefone: "), #pede o telefone
        "turma": input("Turma: "), #pede a turma
        "idade": int(input("Idade: ")), # pede a idade
        "cpf": input("CPF: ") #pede o cpf
    }
    
    alunos.append(novo_aluno) #adiciona os dados no final do arquivo

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abre o arquivo e substitui os dados antigos pelos novos
        json.dump(alunos, f, indent=4, ensure_ascii=False) #salva a lista organizada e assentuada 
        
    print("Aluno cadastrado com sucesso!") #mostra a mensagem no terminal

def listar(): #chama a função de listar
    print("\n--- Lista de Alunos ---") #mostra a mensagem no terminal 
    
    if os.path.exists(BANCO_DADOS): #ve se o cadastro que já existe
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo em formato de leitura e deixa organizado
            alunos = json.load(f) #converte em uma variavel
    else:
        alunos = [] #se nao existir ele cria uma nova

    if not alunos: #verifica a lista ta vazia
        print("Nenhum aluno cadastrado.") #mostra no terminal
        return #encerra a função 

    for aluno in alunos: #inicia um laço para percorrer toda lista
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") #imprime todos os dados de todos os alunos da lista

def atualizar(): #chama a função de atualizar 
    print("\n--- Atualizar Aluno ---") #mostra no terminal
    if not os.path.exists(BANCO_DADOS): #verifica se os dados exitem
        print("Nenhum aluno cadastrado no sistema.") #mostra no terminal
        return #encerra a função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo em formato de leitura e organizado
        alunos = json.load(f) #converte em uma variavel
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) #busca o cpf do aluno para ver qual o usuario quer substituir
    
    for aluno in alunos: #percorre o arquivo em forma de laço
        if aluno['cpf'] == cpf_busca: #se o cpf do aluno for igual o cpf digitado
            print(f"Editando dados de: {aluno['nome']}") #vai mostrar qual aluno foi editado
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] #pede o novo nome
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] #pede o novo telefone
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']#pede uma nova turma
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])#pede uma nova idade
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']#pede um novo cpf
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:# abre o arquivo em forma de sobrescrever e organiza
                json.dump(alunos, f, indent=4, ensure_ascii=False)#atualiza o arquivo com as novas informações
            print("Dados atualizados com sucesso!")#mostra no terminal
            return#encerra a função
            
    print("Aluno não encontrado.")#mostra no terminal se o cpf nao tiver cadastrado anteriormente

def excluir():#chama a função de excluir
    print("\n--- Excluir Aluno ---")#mostra no terminal
    if not os.path.exists(BANCO_DADOS): #verifica se os dados não existem
        print("Nenhum aluno cadastrado no sistema.") #mostra no terminal
        return #encerra a função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo em forma de leitura e deixa organizado
        alunos = json.load(f) #converte o arquivo em variavel
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))#pede o cpf do aluno que ele deseja excluir
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] #cria uma nova lista com os alunos que nao tem o cpf
    
    if len(nova_lista) < len(alunos):#verfica se a lista dos removidos é menor que a lista principal
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abre o arquivo para sobrescrever a nova atualização
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) #converte a nova lista em arquivo
        print("Aluno removido com sucesso!")#mostra no terminal
    else: #se não existir o cpf, ele mostra aluno não encontrado
        print("Aluno não encontrado.")

def menu(): #chama a função do menu
    if not os.path.exists(BANCO_DADOS): #verifica se o arquivo tem dados
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abre o arquivo em função de sobrescrever
            json.dump([], f) #converte em arquivo

    while True: #inicia o laço infinito para manter o código sempre rodando
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ") #le a resposta do usario
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()#inicia o sistema