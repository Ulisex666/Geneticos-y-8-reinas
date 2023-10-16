# Geneticos-y-8-reinas
Desarrollo de un programa para encontrar soluciones al "Problema de las 8 Reinas", utilizando algoritmos genéticos.

## Introducción

El problema de las 8 reinas consiste en colocar, como el nombre lo indica, 8 diferentes reinas en un tablero de ajedrez de tal forma que no se ataquen entre ellas. Recordemos que una reina de ajedrez es libre de moverse en todas las filas, columnas y diagonales adyacentes a ella, el número de casillas que desee. Fue propuesto en 1848 por Max Bezzel, y actualmente a través de métodos matemáticos se conocen exactamente las soluciones para un tablero estándar de 8X8 casillas, siendo este número 92. 

Encontrar una de las soluciones para este problema con métodos computacionales tradicionales tomaría una cantidad importante de poder computacional, ya que existen $C^{64}_8$ formas de acomodar (64 elige 8) las reinas en un tablero, es decir, 4 426 165 368 diferentes arreglos para la reina. El limitarse al caso donde solo hay una reina por cada fila (o equivalentemente columna) reduce en gran medida el número de casos posibles. Aún así, este problema resulta óptimo para ser resuelto con algoritmos genéticos, y utilizando una representación de permutaciones.

Estos algoritmos son inspirados en la evolución de las especies en el mundo real, y específicamente en el proceso de selcción natural. Las mutaciones naturales del ADN se sustituyen por alteraciones aleatorias a cada tablero y para llevar a cabo el proceso de selección se establece un 'fitness', una medida de que tanto se acerca cada tablero a resolver nuestro problema. En nuestro caso, este fitness es el número de ataques entre reinas por tablero, y como se busca reducirlo, nuestro fitness debe de acercarse a 0. Además, se seleccionaran a los sujetos de acuerdo con este fitness, y dará lugar a un proceso de cruza entre dos sujetos, de tal forma que el descendiente mantiene parte de la información de cada uno, una forma de adaptar el proceso de cruza de individuos y creación de nuevas generaciones del mundo natural.  La idea es que aquellos individuos mejor adaptados a su ambiente -en este casos aquellos con mejor fitness- logren sobrevivir y transmitirle su material genético a sus decendientes. Con suficientes generaciones, cada una mejor adaptada que la otra, se debería llegar a una (o varias) soluciones para nuestro problema sin que tengamos que buscar ninguna solución específica.

Los algoritmos genéticos se pueden dividir en 5 etapas: Inicialización, donde se crea una población inicial de forma aleatoria o se crea un individuo aleatorio y se repite n veces. Selección de padres, donde se elige a aquellos individuos que se cruzarán con otros para dar lugar a una descendencia. Cruza, en este pasó se intercambian elementos de entre 2 de los padres seleccionados anteriormente, de forma que se optimice el fitness. Mutación, donde se añaden pequeños cambio a sujetos de forma aleatoria. Y finalmente descendientes, donde se eligen a aquellos individuos que se utilizarán para repetir el proceso nuevamante. Cada repetición es una generación, y el número de generaciones depende de cada problema en específico.

En este caso se utilizó el lenguaje de programación Python 3, con el entorno de programación PyCharm y a su vez se utiliza el repositorio de GitHub. Este proyecto se desarrollo durante el transcurso de 2 semanas. En la documentación se encontrarn los detalles de las paqueterías externas utilizadas para el programa.

## Tabla de datos
A continuación se encontraré una tabla donde se indica qué técnica se siguió para cada parte del algortimo genético:
| Parte del algoritmo| Técnica utilizada|
|--------------|-----------|
| Representación | Permutacional|
| Inicialización | Aleatoria|
|Selección de padres| Sobrante estocástico|
| Cruza | Cíclica |
|Mutación | Mezcla|
|Reemplazo| Generacional|

En este problema la representación permutacional es la más óptima, no solo porque reduce enormemente el número de casos posibles, sino porque también nos ayuda a manejar de forma más eficiente cada tablero, ya que si se usara la representación por matrices se ocuparía 8 veces más memoria por cada tablero. En este tipo de representación, el índice de nuestra lista nos indica en que fila se ubica nuestra reina, y el elemento ubicado en ese índice indica la columna. Es importante recalcar que los números no se pueden repetir, de esta forma las reinas están siempre en filas y columnas diferentes.

La inicialización aleatoria nos permite tener la mayor variabilidad posible en nuestra población inicial, lo que teóricamente hace más sencillo encontrar una de las posibles soluciones. En nuestro caso esto se llevo a cabo simplemente generando una lista que se compone, a su vez, de listas de 8 números cada una, utilizando listas de comprensión.

``` python
ini_subjects = [random.sample(range(8), 8) for i in range(0, 50)]
```
Para la selección de padres se utilizó el sobrante estocástico, que depende del valor esperado del fitness de cada lista. Este se calcula como 
$\dfrac{x_i}{\bar{x}}$, el fitness de cada elemento sobre el fitness promedio. Así, se asegura que se van a cruzar aquellos que tengan un fitness mayor al promedio, y aquellos que tengan un fitness menor van a sobrevivir o no de acuerdo a un volado.
```python
padres1 = [padres[i] for i in range(len(padres)) if math.trunc(val_esp[i]) > 0]
padres2 = [padres[i] for i in range(len(padres)) if int(val_esp[i]) == 0
               and random.random() > 0.5]
```
La parte más compleja de programar, y la que puede que tenga más errores es la cruza cíclica. El algoritmo es algo compleo de explicar, pero a grandes rasgos consiste en mezclar ambas listas de tal forma que se conserve la mayor información posible sobre la posición en la que se encuentra cada elemento. Para ello, se divide en ciclos, y para cada ciclo se toman elementos de un padre, y elementos del otro padre para el siguiente ciclo. Esos ciclos nos dicen que índices de cada padre se heredan al hijo. En este paso resulto muy útil el uso de diccionarios de Python, para poder alterar los índices de una lista sin perder información sobre que elemento se encontraba en cada índice. A continuación se encuentra el código de la función que se desarrollo para obtener los ciclos, y se creo una segunda función para dar lugar a listas nuevas utilizando estos ciclos.
```python
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
```
Para la mutación de mezcla simplemente se selecciona un subconjunto de los índices y se les permuta de manera aleatoria. En este proyecto se mantuvieron intactos los índices de los extremos, y se permutaron todos los demás. La decisión de qué elementos permutar se dejó a la suerte de un volado, independientemente del fitness de cada tablero.

``` python
def mutacion(board):
    alelos = random.sample(range(1, 7), 6)
    for i in range(0, 5):
        gen1 = board[alelos[i]]
        gen2 = board[alelos[i + 1]]
        board[alelos[i + 1]] = gen1
        board[alelos[i]] = gen2
    return board
```
Y finalmente, para el reemplazo generacional, se eliminan a todos los padres y se reemplazan con los hijos. Se decidió trabajar con una población inicial de 50 tableros, durante el transcurso de 100 generaciones. También se le indico al programa que imprima una matriz cada vez que calcule que está tiene 0 ataques, es decir, es una solución del problema.

##Conclusiones

Empecemos analizando las gráficas de convergencia, la primera nos indica el promedio de ataques de cada generación, y la segunda cuál fue el número mínimo de ataques de cada generación.

![Ataques promedio](https://github.com/Sesilu00/Geneticos-y-8-reinas/blob/main/ataques_promedio.png)

![Ataques mínimos](https://github.com/Sesilu00/Geneticos-y-8-reinas/blob/main/ataques_minimos.png)

Podemos ver que el número de ataques promedio no baja significamente con el paso de las generaciones, de hecho en este caso específico pareciera que tiende a crecer. Sin embargo, intentando con muchas otras diferentes semillas, se nota que la tendencia es que se mantiene alrededor de 5 ataques en promedio. Esto puede deberse a muchos factores: para empezar, como se comento anteriormente, la cruza cíclica es la parte más complicada de este proyevto, por lo que es probable que se haya cometido algún error a la hora de su implementación. Sin embargo, se comprobó muchas veces para asegurarse de que funcionaba correctamente, incluso a la hora de ciclarse.

Otra explicación es el hecho de que este tipo de mezcla no da mucha variabilidad. A la hora del desarrollo de este proyecto se observó que hay muchas situaciones en las que el hijo es exactamente igual a uno de los padres, o solamente cambia en 2 valores. Así, la cruza de los elementos no da cambios siginificativos para mucha de la descendencia. Además, es muy probable que un tablero mute, independientemente del fitness que esta tenga, y la mutación afecta a casi todas las filas, por lo que es muy díficil que los tableros sobresalientes mantengan su información.
