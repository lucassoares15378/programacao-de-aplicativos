import sqlite3

try:
    conexao = sqlite3.connect('armazem.db')
    cursor = conexao.cursor()
except sqlite3.Error as erro:
    print(f"Erro ao conectar o banco de dados: {erro}")
    exit()

def excluir_operadores():
    try:
        id_operador = int(input("Qual o ID para realizar a exclusão? "))

        cursor.execute(f"SELECT * FROM operadores_logisticos WHERE id = {id_operador}")
        operador_existe = cursor.fetchone()

        if operador_existe is None:
            print("Nenhum operador encontrado")
        else:
            cursor.execute(f"DELETE FROM operadores_logisticos WHERE id = {id_operador}")
            conexao.commit()
            print("Operador excluído com sucesso!")
            return True
    except ValueError:
        print("O ID precisa ser um número inteiro!")
    except sqlite3.Error as erro:
        print(f"Erro ao excluir registro: {erro}")
        return False
assert excluir_operadores() == True