import sqlite3

try:
    conexao = sqlite3.connect('armazem.db')
    cursor = conexao.cursor()
except sqlite3.Error as erro:
    print(f"Erro ao conectar o banco de dados: {erro}")
    exit()
def listar_operadores():
    try:
        cursor.execute("SELECT * FROM operadores_logisticos")
        linhas = cursor.fetchall()
        if not linhas:
            print("Nenhum cadastro realizado!")
        else:
            for linha in linhas:
                print(f"ID: {linha[0]} | Razão Social: {linha[1]} | Inscrição Estadual: {linha[2]}")
        print("\n")

    except sqlite3.Error as erro:
        print(f"Erro ao listar operadores: {erro}")
