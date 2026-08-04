import sqlite3
def conectar():
    conexao = sqlite3.connect("hospital.db")
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao


def criar_tabelas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS hospitais (
            id_hospital INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crm TEXT NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        )
        """)

        conexao.commit()
        conexao.close()
        return conexao, cursor
    except sqlite3.Error as erro:
        print("Erro ao criar as tabelas:", erro)

def cadastrar_medico(cursor, conexao):
    try:
        print("-----CADASTRO MÉDICO----")
        try:    
            id_hospital = int(input("Qual o ID do Hospital: "))
        except ValueError:
            print("O ID precisa ser um número inteiro.")
            cursor.execute(f"SELECT FROM id_hospital WHERE id = {id_hospital}")
    
    
    
    
    except Exception as e:
        print(f"ERRO DESCONHECIDO {e}")
