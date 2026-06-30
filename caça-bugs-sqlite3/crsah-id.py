import sqlite3
def vincular_aluno_turma():
    nome = input("Nome do aluno: ")

    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("Error no banco de dados!")
    except ValueError:
        print("Error: O id precisa ser um número inteiro.") #faltou criar um except para o valor que seria digitado errado
    finally:
        conexao.close()