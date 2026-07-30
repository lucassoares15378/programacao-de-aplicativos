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

#o id_prof nao existe, por isso colocamos o try e o except juntos
# se acontecer o erro tanto o commit tanto o close não é executado
