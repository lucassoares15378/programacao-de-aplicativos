
import banco
import sqlite3

def cadastrar():
    try:
        nome = input("Nome da escola: ").strip()
        cidade = input("Cidade da escola: ").strip()
        
        assert nome != "", "O nome da escola nao pode ser vazio."
        assert cidade != "", "A cidade da escola nao pode ser vazia."
        
        conexao, cursor = banco.conectar()
        cursor.execute("INSERT INTO escolas (nome, cidade) VALUES (?, ?)", (nome, cidade))
        conexao.commit()
        conexao.close()
        print("Escola cadastrada com sucesso!")
        
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

def listar():
    try:
        conexao, cursor = banco.conectar()
        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()
        conexao.close()
        
        if len(escolas) == 0:
            print("Nenhuma escola cadastrada.")
        else:
            print("\n--- LISTA DE ESCOLAS ---")
            for escola in escolas:
                print(f"ID: {escola[0]} | Nome: {escola[1]} | Cidade: {escola[2]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")

def alterar():
    try:
        id_busca = int(input("ID da escola para alterar: "))
        nome = input("Novo nome da escola: ").strip()
        cidade = input("Nova cidade da escola: ").strip()
        
        assert nome != "", "O nome nao pode ser vazio."
        assert cidade != "", "A cidade nao pode ser vazia."
        
        conexao, cursor = banco.conectar()
        cursor.execute("UPDATE escolas SET nome = ?, cidade = ? WHERE id = ?", (nome, cidade, id_busca))
        conexao.commit()
        conexao.close()
        print("Escola alterada com sucesso!")
    except ValueError:
        print("Erro: O ID precisa ser um numero.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")

def excluir():
    try:
        id_busca = int(input("ID da escola para excluir: "))
        conexao, cursor = banco.conectar()
        cursor.execute("DELETE FROM escolas WHERE id = ?", (id_busca,))
        conexao.commit()
        conexao.close()
        print("Escola excluida!")
    except ValueError:
        print("Erro: O ID precisa ser um numero.")
    except sqlite3.Error:
        print("Erro: Nao foi possivel excluir. Verifique se ha turmas vinculadas a ela.")








