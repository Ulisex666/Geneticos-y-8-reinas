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


def cruza1(sujeto_1, sujeto_2):
    alelos_1 = {i: sujeto_1[i] for i in range(len(sujeto_1))}  # Diccionario de los alelos del primer sujeto
    alelos_2 = {i: sujeto_2[i] for i in range(len(sujeto_2))}  # Diccionario de los alelos del segundo sujeto
    ciclos = []  # lista de ciclos vacía
    while alelos_1:
        alelo = next(iter(alelos_1))  # Toma la primera llave disponible en alelos 1
        gen = alelos_2[alelo]  # Busca ese alelo en alelos2 y da ese gen
        ciclo = []  # El ciclo individual se crea vacío
        while True:
            ciclo.append(alelo)  # se agrega el alelo al ciclo
            del alelos_1[alelo]  # se borra el alelo del diccionario
            gen = alelos_2[alelo]  # se cambia el valor del gen al valor del alelo actual
            alelo = gen  # se guarda el valor del gen en el alelo
            if gen in alelos_1.values():  # se verifica que el gen esté en los disponibles
                alelo = list(alelos_1.keys())[list(alelos_1.values()).index(alelo)]
            else:
                break
        ciclos.append(ciclo)
    return ciclos


def cruza2(ciclos, sujeto_1, sujeto_2):
    hijo = [0 for i in range(len(sujeto_1))]
    for i in range(len(ciclos)):
        if i % 2 == 0:
            for j in range(len(ciclos[i])):
                hijo[ciclos[i][j]] = sujeto_1[ciclos[i][j]]
        else:
            for j in range(len(ciclos[i])):
                hijo[ciclos[i][j]] = sujeto_2[ciclos[i][j]]
    return hijo
