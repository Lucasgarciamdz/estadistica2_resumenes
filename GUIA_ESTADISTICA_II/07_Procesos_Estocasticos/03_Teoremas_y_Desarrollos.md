# Unidad 7: Teoremas y Desarrollos

Los desarrollos matemáticos en esta unidad se centran en cómo predecir el comportamiento de un sistema a lo largo del tiempo. Los dos pilares son la Ecuación de Chapman-Kolmogorov para el comportamiento a corto y mediano plazo, y el concepto de distribución estacionaria para el comportamiento a largo plazo.

---

### 1. Evolución del Sistema: Predicción de Estados Futuros

**Objetivo:** Si conocemos el estado del sistema hoy, ¿cuál es la probabilidad de que esté en cada estado posible mañana, o en $n$ días?

**Desarrollo:**
Sea $\pi^{(t)}$ el vector de probabilidad de estado en el tiempo $t$. Sus componentes, $\pi_i^{(t)}$, son la probabilidad de que el sistema esté en el estado $i$ en el tiempo $t$. $P$ es la matriz de transición de un paso.

*   **Para predecir el estado en el tiempo $t+1$:**
    La probabilidad de estar en un estado $j$ en el tiempo $t+1$ se calcula sumando las probabilidades de todas las formas posibles de llegar a $j$. Se puede llegar a $j$ desde el estado 1, desde el estado 2, etc. 
    $$ \pi_j^{(t+1)} = P(X_{t+1}=j) = \sum_{i} P(X_{t+1}=j | X_t=i) P(X_t=i) = \sum_{i} p_{ij} \pi_i^{(t)} $$
    Esta operación es exactamente el producto de un vector por una matriz. Por lo tanto, para obtener el vector de estado en el siguiente paso, simplemente multiplicamos el vector de estado actual por la matriz de transición:
    $$ \pi^{(t+1)} = \pi^{(t)} P $$

*   **Para predecir el estado en el tiempo $t+n$:**
    Podemos aplicar la misma lógica repetidamente:
    $\pi^{(t+1)} = \pi^{(t)} P$
    $\pi^{(t+2)} = \pi^{(t+1)} P = (\pi^{(t)} P) P = \pi^{(t)} P^2$
    ...y así sucesivamente.
    $$ \pi^{(t+n)} = \pi^{(t)} P^n $$

**Teorema (Ecuación de Chapman-Kolmogorov):**
Este desarrollo lleva directamente a la ecuación de Chapman-Kolmogorov, que establece que la matriz de transición de $n$ pasos, $P^{(n)}$, es la $n$-ésima potencia de la matriz de transición de un paso, $P$.
$$ P^{(n)} = P^n $$
El elemento $(i,j)$ de la matriz $P^n$, denotado $p_{ij}^{(n)}$, da la probabilidad de transitar del estado $i$ al estado $j$ en exactamente $n$ pasos.

**Porqué es Importante:** Este resultado es increíblemente poderoso. Nos permite calcular la evolución de un sistema a cualquier número de pasos en el futuro con una simple (aunque computacionalmente intensa) exponenciación de matrices, en lugar de tener que enumerar todos los posibles caminos que el proceso podría haber tomado.

---

### 2. Comportamiento a Largo Plazo: La Distribución Estacionaria

**Objetivo:** Para ciertos tipos de cadenas (las regulares), el sistema eventualmente alcanza un equilibrio donde las probabilidades de estar en cada estado se vuelven constantes y ya no cambian con el tiempo. Queremos encontrar este vector de probabilidades de equilibrio, llamado distribución estacionaria ($\pi$).

**Desarrollo y Teorema:**
Si una cadena de Markov es regular, entonces existe un único vector de probabilidad $\pi$ tal que:
$$ \pi P = \pi $$
Este vector $\pi$ es la distribución estacionaria de la cadena.

**Cómo encontrar $\pi$:**
La ecuación $\pi P = \pi$ es un sistema de ecuaciones lineales. Si $k$ es el número de estados, $\pi$ es un vector de $k$ componentes ($\pi_1, \pi_2, ..., \pi_k$) y $P$ es una matriz de $k \times k$. La ecuación matricial nos da $k$ ecuaciones lineales. 

Sin embargo, estas $k$ ecuaciones no son linealmente independientes (una es redundante). Para encontrar una solución única, necesitamos una ecuación adicional. Esta ecuación proviene del hecho de que $\pi$ es un vector de probabilidad, y por lo tanto, la suma de sus componentes debe ser 1.
$$ \sum_{i=1}^{k} \pi_i = 1 $$

**Procedimiento de Solución:**
1.  Escribir el sistema de ecuaciones a partir de $\pi P = \pi$.
2.  Reemplazar una de las ecuaciones (usualmente la más compleja) por la ecuación $\sum \pi_i = 1$.
3.  Resolver el sistema de $k$ ecuaciones lineales con $k$ incógnitas para encontrar los valores de $\pi_1, \pi_2, ..., \pi_k$.

**Porqué es Importante:**
La distribución estacionaria describe el comportamiento promedio del sistema a largo plazo. Por ejemplo, si $\pi_1 = 0.6$ para el estado "Soleado", significa que, a largo plazo, el 60% de los días serán soleados, independientemente de si hoy está lloviendo o no. Esto es fundamental para el análisis de colas, la modelización de mercados, la bioinformática y muchas otras áreas donde se necesita entender el equilibrio de un sistema dinámico.
