# Unidad 7: Resumen de Procesos Estocásticos

Esta unidad introduce un concepto que extiende la idea de variable aleatoria al dominio del tiempo (o a veces, del espacio). Mientras que una variable aleatoria es un valor que resulta de un experimento, un proceso estocástico es una **secuencia de variables aleatorias** que evolucionan a lo largo del tiempo.

---

### 1. De Variable Aleatoria a Proceso Estocástico

*   Una **variable aleatoria** $X$ es una función que asigna un número a cada resultado de un experimento (e.g., el resultado de lanzar un dado).
*   Un **proceso estocástico** (o proceso aleatorio), $X(t)$, es una colección de variables aleatorias indexadas por un parámetro, usualmente el tiempo $t$. Para cada instante de tiempo $t$, $X(t)$ es una variable aleatoria.

**Ejemplos:**
*   El número de clientes que llegan a un banco cada hora.
*   La temperatura de una ciudad medida cada segundo.
*   El precio de una acción al cierre de cada día de mercado.

Una **realización** del proceso es una de las posibles secuencias de resultados que el proceso puede tomar a lo largo del tiempo. Por ejemplo, una gráfica del precio de una acción durante un año es una realización del proceso estocástico subyacente.

### 2. Cadenas de Markov: El Proceso sin Memoria

Uno de los tipos más importantes y simples de procesos estocásticos es la **Cadena de Markov**. Su característica definitoria es la **Propiedad de Markov**: el futuro del proceso depende **únicamente** del estado presente, y no de cómo se llegó a ese estado.

> **Propiedad de Markov (Sin Memoria):** La probabilidad de pasar a un estado futuro $j$, dado el estado presente $i$ y todos los estados pasados, es la misma que la probabilidad de pasar al estado $j$ conociendo únicamente el estado presente $i$.
> $$ P(X_{t+1} = j | X_t = i, X_{t-1}=i_{t-1}, ...) = P(X_{t+1} = j | X_t = i) $$

**Componentes de una Cadena de Markov (de tiempo discreto):**

*   **Espacio de Estados:** El conjunto de todos los posibles valores o "estados" en los que puede estar el proceso. Puede ser finito (e.g., {soleado, nublado, lluvioso}) o infinito.

*   **Probabilidades de Transición:** La probabilidad de moverse de un estado $i$ a un estado $j$ en un solo paso de tiempo. Se denota como $p_{ij} = P(X_{t+1} = j | X_t = i).

*   **Matriz de Transición (P):** Una matriz cuadrada donde se organizan todas las probabilidades de transición. El elemento en la fila $i$ y la columna $j$ es $p_{ij}.
    *   Las entradas de cada fila deben sumar 1 (desde un estado $i$, se debe transitar a algún estado).
    *   Todas las probabilidades deben estar entre 0 y 1.

**Ejemplo de Matriz de Transición (Clima):**

Supongamos que el clima de mañana depende solo del de hoy.

| Hoy \ Mañana | Soleado | Nublado | Lluvioso |
| :--- | :---: | :---: | :---: |
| **Soleado** | 0.7 | 0.2 | 0.1 |
| **Nublado** | 0.3 | 0.5 | 0.2 |
| **Lluvioso**| 0.2 | 0.6 | 0.2 |

La matriz de transición $P$ sería:
$$ P = \begin{pmatrix} 0.7 & 0.2 & 0.1 \\ 0.3 & 0.5 & 0.2 \\ 0.2 & 0.6 & 0.2 \end{pmatrix} $$

### 3. Propiedades y Análisis

*   **Probabilidades de n-pasos:** Si queremos saber la probabilidad de ir del estado $i$ al $j$ en $n$ pasos, no necesitamos seguir todos los caminos. Simplemente calculamos la $n$-ésima potencia de la matriz de transición, $P^n$. El elemento $(i,j)$ de $P^n$ nos da esa probabilidad.

*   **Distribución Estacionaria (o de Equilibrio):** Para ciertos tipos de cadenas de Markov (llamadas regulares), a medida que el tiempo avanza, la probabilidad de estar en cualquier estado se estabiliza y deja de depender del estado inicial. Este vector de probabilidades de estado estable, $\pi$, es la distribución estacionaria y se encuentra resolviendo la ecuación $\pi P = \pi$.
