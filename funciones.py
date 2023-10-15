import random


# Se creó un archivo separado en donde crear las funciones necesarias para el proyecto

def ataques(subject):
    attacks = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(subject[i] - subject[j]) == abs(j - i):
                attacks = attacks + 1
    return int(attacks)


def mutacion(board):
    alelos = random.sample(range(1, 7), 6)
    for i in range(0, 5):
        gen1 = board[alelos[i]]
        gen2 = board[alelos[i + 1]]
        board[alelos[i + 1]] = gen1
        board[alelos[i]] = gen2
    return board
