import random
import math
from funciones import ataques, mutacion
# Se utiliza representación por permutación, tomando el índice como fila y el valor como columna
ini_subjects = [random.sample(range(8), 8) for i in range(0, 20)]

# Se aplicará el método de selección "Sobrante estocástico", utilizando la función de ataque
# para calcular el fitness
fitness_list = [1 / (ataques(ini_subjects[i]) + 1) for i in range(len(ini_subjects))]
fitness_mean = sum(fitness_list)/len(fitness_list)
val_esp = [fitness_list[i]/fitness_mean for i in range(len(fitness_list))]
# Se crean dos listas, una tomando los tableros cuyo valor esperado tiene parte entera mayor
# que 0 y otra tomando los tableros restantes con un volado.
padres1 = [ini_subjects[i] for i in range(len(ini_subjects)) if math.trunc(val_esp[i]) > 0]
padres2 = [ini_subjects[i] for i in range(len(ini_subjects)) if int(val_esp[i]) == 0
           and random.random() > 0.5]
print(val_esp)