import random


# Se creó una función para mutación de mezcla en un archivo aparte,
# no afecta a los extremos de la lista
def mutacion(board):
    alelos = random.sample(range(1, 7), 6)
    for i in range(0, 5):
        gen1 = board[alelos[i]]
        gen2 = board[alelos[i + 1]]
        board[alelos[i + 1]] = gen1
        board[alelos[i]] = gen2
    return board
