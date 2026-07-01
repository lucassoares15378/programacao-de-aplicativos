import sqlite3

def cadastrar_turma(nome,id_serie,id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreing_keys = ON;")
    try:
        cursor.execute("INSERT INTO turmas (nome_turma,id_serie,id_professor) VALUES (?,?,?)"), (nome , id_serie , id_prof)
        conexao.commit()
    except sqlite3.IntegrityError:
        ("Professor ou série não existe.")
    finally:
        conexao.close()

#colocamos os try, except junto com o erro , pq o id_prof nao existe
# se acontecer o erro tanto o commit tanto o close não é executado
