import sqlite3

def conectar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
    )
    ''')
    return conexao, cursor

def cadastrar_aluno(cursor, conexao):
    print("--- CADASTRAR ALUNO ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    turma = input("Turma: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")

    comando = "INSERT INTO alunos (nome, telefone, turma, idade, cpf) VALUES (?, ?, ?, ?, ?)"
    try:
        cursor.execute(comando, (nome, telefone, turma, idade, cpf))
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Este CPF já está cadastrado!")

def listar_alunos(cursor):
    print("--- LISTA DE ALUNOS ---")
    cursor.execute("SELECT * FROM alunos")
    todos_alunos = cursor.fetchall()
    
    if not todos_alunos:
        print("Nenhum aluno cadastrado!")
        return False
    
    for aluno in todos_alunos:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Telefone: {aluno[2]} | Turma: {aluno[3]} | Idade: {aluno[4]} | CPF: {aluno[5]}")
    return True

def editar_aluno(cursor, conexao):
    print("--- EDITAR ALUNO ---")
    if not listar_alunos(cursor):
        return

    id_aluno = int(input("\nDigite o ID do aluno que deseja editar: "))
    
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (id_aluno,))
    if not cursor.fetchone():
        print("Erro: ID não encontrado!")
        return

    print("Digite os novos dados:")
    novo_nome = input("Novo Nome: ")
    novo_telefone = input("Novo Telefone: ")
    nova_turma = input("Nova Turma: ")
    nova_idade = int(input("Nova Idade: "))
    novo_cpf = input("Novo CPF: ")

    comando = '''
    UPDATE alunos 
    SET nome = ?, telefone = ?, turma = ?, idade = ?, cpf = ? 
    WHERE id = ?
    '''
    try:
        cursor.execute(comando, (novo_nome, novo_telefone, nova_turma, nova_idade, novo_cpf, id_aluno))
        conexao.commit()
        print("Aluno atualizado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Este novo CPF já pertence a outro aluno!")

def excluir_aluno(cursor, conexao):
    print("\n--- EXCLUIR ALUNO ---")
    if not listar_alunos(cursor):
        return

    id_aluno = int(input("\nDigite o ID do aluno que deseja excluir: "))
    
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (id_aluno,))
    if not cursor.fetchone():
        print("Erro: ID não encontrado!")
        return

    comando = "DELETE FROM alunos WHERE id = ?"
    cursor.execute(comando, (id_aluno,))
    conexao.commit()
    print("Aluno removido com sucesso!")

conexao, cursor = conectar()

while True:
    print("\n===== MENU ESCOLA =====")
    print("[1] Cadastrar Aluno")
    print("[2] Listar Alunos")
    print("[3] Atualizar Aluno")
    print("[4] Excluir Aluno")
    print("[0] Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar_aluno(cursor, conexao)
    elif opcao == '2':
        listar_alunos(cursor)
    elif opcao == '3':
        editar_aluno(cursor, conexao)
    elif opcao == '4':
        excluir_aluno(cursor, conexao)
    elif opcao == '0':
        break
    else:
        print("Opção inválida! Tente novamente.")

conexao.close()