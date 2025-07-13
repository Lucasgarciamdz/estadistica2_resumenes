# Unidad 7: Conceptos Clave

Esta sección define la terminología fundamental para describir y analizar sistemas que evolucionan aleatoriamente en el tiempo.

---

*   **Proceso Estocástico (o Proceso Aleatorio):** Una familia de variables aleatorias ${X(t) : t \in T}$ indexada por un parámetro $t$, que usualmente representa el tiempo. Para cada instante $t$, $X(t)$ es una variable aleatoria.

*   **Espacio de Estados (S):** El conjunto de todos los posibles valores que las variables aleatorias $X(t)$ pueden tomar. Los valores individuales se llaman **estados**.

*   **Tiempo Discreto/Continuo:**
    *   **Tiempo Discreto:** El parámetro $t$ toma valores de un conjunto contable (e.g., $t = 0, 1, 2, ...$). El proceso se observa en instantes específicos.
    *   **Tiempo Continuo:** El parámetro $t$ toma valores de un intervalo continuo (e.g., $t \ge 0$). El proceso se observa en todo momento.

*   **Realización (o Trayectoria):** Una única secuencia de valores observados del proceso estocástico a lo largo del tiempo. Es una de las posibles "rutas" que el proceso puede seguir.

--- 

### Para Cadenas de Markov

*   **Cadena de Markov:** Un proceso estocástico (generalmente de tiempo discreto) que posee la **Propiedad de Markov**.

*   **Propiedad de Markov (o Carencia de Memoria):** La distribución de probabilidad condicional de los estados futuros del proceso, dado el estado presente y los estados pasados, depende únicamente del estado presente. El pasado no aporta información sobre el futuro si ya conocemos el presente.
    $$ P(X_{t+1} = j | X_t = i, X_{t-1}=i_{t-1}, ...) = P(X_{t+1} = j | X_t = i) $$

*   **Probabilidad de Transición de un Paso ($p_{ij}$):** La probabilidad de que el proceso pase del estado $i$ al estado $j$ en el siguiente paso de tiempo.
    $$ p_{ij} = P(X_{t+1} = j | X_t = i) $$

*   **Matriz de Transición (P):** Una matriz cuadrada de tamaño $k \times k$ (donde $k$ es el número de estados) que contiene todas las probabilidades de transición de un paso. El elemento en la fila $i$ y columna $j$ es $p_{ij}$.
    *   **Propiedades:**
        1.  $0 \le p_{ij} \le 1$ para todo $i, j$.
        2.  $\sum_{j=1}^{k} p_{ij} = 1$ para cada fila $i$ (la suma de las probabilidades de salir de un estado debe ser 1).

*   **Vector de Estado (o Vector de Probabilidad):** Un vector fila, $\pi^{(t)}$, cuyos componentes son las probabilidades de que el proceso se encuentre en cada uno de los estados en el tiempo $t$. La suma de sus componentes es 1.

*   **Ecuación de Chapman-Kolmogorov:** Relaciona las probabilidades de transición de $n$ pasos con las de un paso. Afirma que la matriz de transición de $n$ pasos, $P^{(n)}$, es simplemente la $n$-ésima potencia de la matriz de un paso, $P$. 
    $$ P^{(n)} = P^n $$
    El elemento $(i,j)$ de esta matriz es $p_{ij}^{(n)} = P(X_{t+n}=j | X_t=i)$.

*   **Estado Absorbente:** Un estado $i$ es absorbente si es imposible salir de él. Esto significa que su probabilidad de transición a sí mismo es 1 ($p_{ii} = 1$).

*   **Cadena de Markov Regular:** Una cadena de Markov es regular si existe alguna potencia de su matriz de transición, $P^k$, que tiene todas sus entradas estrictamente positivas. Esto implica que es posible llegar desde cualquier estado a cualquier otro estado en algún número de pasos.

*   **Distribución Estacionaria (o de Equilibrio, $\pi$):** Un vector de probabilidad $\pi$ que describe el comportamiento a largo plazo de una cadena de Markov regular. Si el proceso alcanza esta distribución, se mantendrá en ella para siempre. Se caracteriza por la ecuación:
    $$ \pi P = \pi $$
    El vector $\pi$ es el vector propio (eigenvector) izquierdo de la matriz $P$ asociado con el valor propio (eigenvalue) 1.
