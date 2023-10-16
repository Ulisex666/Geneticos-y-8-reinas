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
| Representación | Permutacional     |
| Inicialización      | Aleatoria  |
| Cruza | Cíclica |
|Mutación | Mezcla|
|Reemplazo| Generacional|

En este problema la representación permutacional es la más óptima, no solo porque reduce enormemente el número de casos posibles, sino porque también nos ayuda a manejar de forma más eficiente cada tablero, ya que si se usara la representación por matrices se ocuparía 8 veces más memoria por cada tablero. En este tipo de representación, el índice de nuestra lista nos indica en que fila se ubica nuestra reina, y el elemento ubicado en ese índice indica la columna. Es importante recalcar que los números no se pueden repetir, de esta forma las reinas están siempre en filas y columnas diferentes.

La inicialización aleatoria nos permite tener la mayor variabilidad posible en nuestra población inicial, lo que teóricamente hace más sencillo encontrar una de las posibles soluciones. En nuestro caso esto se llevo a cabo simplemente generando una lista que se compone, a su vez, de listas de 8 números cada una, utilizando listas de comprensión.

``` python
ini_subjects = [random.sample(range(8), 8) for i in range(0, 50)]
```



