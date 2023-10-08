import random

# Se utiliza representación por permutación, tomando el índice como fila y el valor como columna
ini_subjects = [random.sample(range(8), 8) for i in range(0, 20)]


# Como no se pueden atacar en filas o columna, solo nos interesa encontrar ataques en diagonal
def ataques(subject):
    attacks = 0
    for i in range(7):
        if abs(subject[i] - subject[i + 1]) == 1:
            attacks = attacks + 1
    return int(attacks)

print(ataques(ini_subjects[1]), ini_subjects[1])
