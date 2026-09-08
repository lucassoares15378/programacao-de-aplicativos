import banco
import sqlite3

def cadastrar():
    try:
        nome_turma = input("Nome da turma: ").strip()
        id_escola = int(input("ID da Escola: "))
        
        assert nome_turma != "", "O nome da turma nao pode ser vazio."
        assert id_escola > 0, "ID da escola deve ser maior que zero."
        
        conexao, cursor = banco.conectar()
        cursor.execute("INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)", (nome_turma, id_escola))
        conexao.commit()
        conexao.close()
        print("Turma cadastrada com sucesso!")
        
    except ValueError:
        print("Erro: Digite apenas numeros para o ID da escola.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Erro: Essa escola nao existe no banco de dados.")

def listar():
    try:
        conexao, cursor = banco.conectar()
        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()
        conexao.close()
        
        if len(turmas) == 0:
            print("Nenhuma turma cadastrada.")
        else:
            print("\n--- LISTA DE TURMAS ---")
            for turma in turmas:
                print(f"ID: {turma[0]} | Turma: {turma[1]} | ID Escola: {turma[2]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")

def alterar():
    try:
        id_busca = int(input("ID da turma para alterar: "))
        nome_turma = input("Novo nome da turma: ").strip()
        id_escola = int(input("Novo ID da escola: "))
        
        assert nome_turma != "", "O nome da turma nao pode ser vazio."
        assert id_escola > 0, "ID da escola deve ser maior que zero."
        
        conexao, cursor = banco.conectar()
        cursor.execute("UPDATE turmas SET nome_turma = ?, id_escola = ? WHERE id = ?", (nome_turma, id_escola, id_busca))
        conexao.commit()
        conexao.close()
        print("Turma alterada!")
    except ValueError:
        print("Erro: Digite numeros validos.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Erro: Nao foi possivel alterar. Verifique se a escola existe.")

def excluir():
    try:
        id_busca = int(input("ID da turma para excluir: "))
        conexao, cursor = banco.conectar()
        cursor.execute("DELETE FROM turmas WHERE id = ?", (id_busca,))
        conexao.commit()
        conexao.close()
        print("Turma excluida!")
    except ValueError:
        print("Erro: O ID precisa ser um numero.")
    except sqlite3.Error:
        print("Erro: Nao foi possivel excluir. Verifique se ha alunos vinculados a ela.")











