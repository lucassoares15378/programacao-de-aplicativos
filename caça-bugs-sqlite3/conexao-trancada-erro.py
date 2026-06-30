import sqlite3
def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("INSERT INTO trumas (nome_turmas, id_serie, id_professores) VALUES (?, ?, ?)", (nome, id_serie, id_prof))
    conexao.commit()
    conexao.close()