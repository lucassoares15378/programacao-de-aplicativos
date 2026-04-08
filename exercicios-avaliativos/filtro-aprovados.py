alunos = ["ana", "carlos", "isabelly", "lucas", "luis"]
notas = [60, 70, 100, 80, 55]
for nota in notas:

    if nota >= 60:
        indice = notas.index(nota)
        print(alunos[indice])
print(f"nova atual: {alunos}")