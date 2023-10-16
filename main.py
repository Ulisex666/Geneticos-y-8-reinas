import random
import math
import matplotlib.pyplot as plt
from funciones import ataques, mutacion, cruza1, cruza2, tablero

# Se utiliza representación por permutación, tomando el índice como fila y el valor como columna
ini_subjects = [random.sample(range(8), 8) for i in range(0, 50)]
generaciones = 100
ataques_promedio = []
random.seed(10042000)
for j in range(generaciones):
    # Se aplicará el método de selección "Sobrante estocástico", utilizando la función de ataque
    # para calcular el fitness
    padres = ini_subjects
    fitness_list = [1 / (ataques(padres[i]) + 1) for i in range(len(padres))]
    fitness_mean = sum(fitness_list)/len(fitness_list)
    val_esp = [fitness_list[i]/fitness_mean for i in range(len(fitness_list))]

    # Se crean dos listas, una tomando los tableros cuyo valor esperado tiene parte entera mayor
    # que 0 y otra tomando los tableros restantes con un volado.
    padres1 = [padres[i] for i in range(len(padres)) if math.trunc(val_esp[i]) > 0]
    padres2 = [padres[i] for i in range(len(padres)) if int(val_esp[i]) == 0
               and random.random() > 0.5]

    # Se crea una sola lista para los padres 1 y padres 2, seleccionándolos de forma aleatoria
    padres = padres1 + padres2
    hijos = []
    indices_padres = list(range(len(padres)))

    # Se utiliza un ciclo while para el caso cuando el número de padres sea impar
    while indices_padres:
        selected_padres = random.sample(indices_padres, 2)
        indices_padres.remove(selected_padres[0])
        indices_padres.remove(selected_padres[1])

        papa_1 = padres[selected_padres[0]]
        papa_2 = padres[selected_padres[1]]

        ciclos = cruza1(papa_1, papa_2)
        hijo1 = cruza2(ciclos, papa_1, papa_2)
        hijo2 = cruza2(ciclos, papa_2, papa_1)
        hijos.append(hijo1)
        hijos.append(hijo2)

        if len(indices_padres) == 1:
            break

    # Se reemplazarán a los padres por los hijos y se mutaran de acuerdo a un bolado

    padres = hijos
    for i in range(len(hijos)):
        if random.random() > 0.5:
            padres[i] = mutacion(padres[i])

    ataques_generacion = [ataques(padres[i]) for i in range(len(padres))]
    ataques_promedio.append(sum(ataques_generacion) / len(ataques_generacion))

    for i in range(len(ataques_generacion)):
        if ataques_generacion[i] == 0:
            print(tablero(padres[i]))
            print('Generación no. :', j)
        break
plt.plot(ataques_promedio, 'b')
plt.show()
