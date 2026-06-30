import sqlite3
def buscar_professor(id_prof):
    conexao = sqlite3.connetc('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,)) #python nao consegue ler com um parametro só dentro dos parenteses, por isso adiciona a virgula
    resultado = cursor.fetchone()
    print(resultado)
    
    conexao.close()