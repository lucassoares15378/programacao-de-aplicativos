def procurar(alunos, nome):
    for aluno in alunos:
        if aluno == nome:
            return True

    return False


alunos = ["Ana", "João", "Maria", "Pedro"]

print(procurar(alunos, "Maria"))
