import sqlite3

def atualizar_aluno(id_aluno, novo_nome, novo_cpf):
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    
    sql = """
    UPDATE alunos 
    SET nome = ?, cpf = ? 
    WHERE id = ?
    """
    
    cursor.execute(sql, (novo_nome, novo_cpf, id_aluno))
    conexao.commit()
    print("Dados atualizados com sucesso!\n")

    cursor.execute("SELECT * FROM alunos")
    print("Lista atualizada: ")

    todos_alunos = cursor.fetchall()
    
    if not todos_alunos:
        print("Nenhum aluno cadastrado!")
    else:
        for aluno in todos_alunos:
            print(f"ID:{aluno[0]} | Nome: {aluno[1]} | Telefone: {aluno[2]} | Turma: {aluno[3]} | Idade: {aluno[4]} | CPF: {aluno[5]}")
    
    conexao.close()


print("--- SISTEMA DE ATUALIZAÇÃO DE ALUNOS ---")
id = input("Digite o ID do aluno que deseja alterar: ")
nome_aluno = input("Digite o NOVO nome do aluno: ")
cpf_aluno = input("Digite o NOVO CPF do aluno: ")

atualizar_aluno(id, nome_aluno, cpf_aluno)