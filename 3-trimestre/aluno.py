import banco
import sqlite3

def cadastrar():
    try:
        nome = input("Nome do aluno: ").strip()
        idade = int(input("Idade do aluno: "))
        id_turma = int(input("ID da Turma: "))
        
        assert nome != "", "O nome do aluno nao pode ser vazio."
        assert idade >= 3, "A idade do aluno deve ser igual ou superior a 3 anos."
        
        conexao, cursor = banco.conectar()
        cursor.execute("INSERT INTO alunos (nome, idade, id_turma) VALUES (?, ?, ?)", (nome, idade, id_turma))
        conexao.commit()
        conexao.close()
        print("Aluno cadastrado com sucesso!")
        
    except ValueError:
        print("Erro: Idade e ID da turma precisam ser numeros.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Erro: Essa turma nao existe no banco de dados.")

def listar():
    try:
        conexao, cursor = banco.conectar()
        cursor.execute("SELECT * FROM alunos ORDER BY nome ASC;")
        alunos = cursor.fetchall()
        conexao.close()
        
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("--- LISTA DE ALUNOS ---")
            for aluno in alunos:
                print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | ID Turma: {aluno[3]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")

def alterar():
    try:
        id_busca = int(input("ID do aluno para alterar: "))
        nome = input("Novo nome do aluno: ").strip()
        idade = int(input("Nova idade do aluno: "))
        id_turma = int(input("Novo ID da turma: "))
        
        assert nome != "", "O nome nao pode ser vazio."
        assert idade >= 3, "A idade deve ser igual ou maior que 3 anos."
        
        conexao, cursor = banco.conectar()
        cursor.execute("UPDATE alunos SET nome = ?, idade = ?, id_turma = ? WHERE id = ?", (nome, idade, id_turma, id_busca))
        conexao.commit()
        conexao.close()
        print("Aluno alterado!")
    except ValueError:
        print("Erro: Digite dados numericos validos.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Erro: Nao foi possivel alterar. Verifique se a turma existe.")

def excluir():
    try:
        id_busca = int(input("ID do aluno para excluir: "))
        conexao, cursor = banco.conectar()
        cursor.execute("DELETE FROM alunos WHERE id = ?", (id_busca,))
        conexao.commit()
        conexao.close()
        print("Aluno excluido!")
    except ValueError:
        print("Erro: O ID precisa ser um numero.")




