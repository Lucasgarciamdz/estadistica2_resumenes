# Resolución del Examen Teórico: Unidad 7 - Procesos Estocásticos

---

### Sección 1: Desarrollo en Pizarrón

**Pregunta 1: Cadena de Markov, Propiedad de Markov y Distribución Estacionaria**

**Concepto de Cadena de Markov:**
Una **Cadena de Markov** es un tipo de proceso estocástico (una secuencia de variables aleatorias que evolucionan en el tiempo) que se caracteriza por su "carencia de memoria". Es decir, el futuro del proceso depende únicamente de su estado presente, y no de cómo llegó a ese estado.

**Propiedad de Markov (o de Carencia de Memoria):**
La probabilidad de que el proceso se mueva a un estado futuro $j$, dado el estado actual $i$ y todos los estados pasados, es la misma que la probabilidad de moverse al estado $j$ conociendo únicamente el estado presente $i$.

$$ P(X_{t+1} = j | X_t = i, X_{t-1}=i_{t-1}, ..., X_0=i_0) = P(X_{t+1} = j | X_t = i) $$

Esta propiedad simplifica enormemente el análisis, ya que no necesitamos rastrear toda la historia del proceso.

**Predicción del Estado Futuro (Ecuación de Chapman-Kolmogorov):**
Sea $\pi^{(t)}$ el vector de probabilidad de estado en el tiempo $t$, donde $\pi_i^{(t)}$ es la probabilidad de que el sistema esté en el estado $i$ en el tiempo $t$. Sea $P$ la matriz de transición de un paso, donde $p_{ij}$ es la probabilidad de ir del estado $i$ al estado $j$ en un paso.

Para predecir el vector de estado en el siguiente paso ($t+1$):
$$ \pi^{(t+1)} = \pi^{(t)} P $$

Para predecir el vector de estado en $n$ pasos futuros ($t+n$):
$$ \pi^{(t+n)} = \pi^{(t)} P^n $$

La **Ecuación de Chapman-Kolmogorov** establece que la matriz de transición de $n$ pasos, $P^{(n)}$, es simplemente la $n$-ésima potencia de la matriz de transición de un paso, $P$.
$$ P^{(n)} = P^n $$
El elemento $(i,j)$ de la matriz $P^n$, denotado $p_{ij}^{(n)}$, representa la probabilidad de transitar del estado $i$ al estado $j$ en exactamente $n$ pasos.

**Cómo encontrar la Distribución Estacionaria ($\pi$):**
Para una Cadena de Markov **regular** (aquella en la que es posible llegar de cualquier estado a cualquier otro estado en algún número de pasos), existe una única distribución de probabilidad $\pi = [\pi_1, \pi_2, ..., \pi_k]$ que describe el comportamiento a largo plazo del sistema. Esta distribución es independiente del estado inicial y se conoce como **distribución estacionaria** o de equilibrio.

Se encuentra resolviendo el siguiente sistema de ecuaciones:

1.  **Ecuación de Equilibrio:**
    $$ \pi P = \pi $$
    Esto significa que si el sistema ya está en la distribución $\pi$, permanecerá en ella después de un paso de transición.

2.  **Condición de Normalización:**
    $$ \sum_{i=1}^{k} \pi_i = 1 $$
    (La suma de las probabilidades de estar en cada estado debe ser 1).

Se resuelve el sistema de $k$ ecuaciones lineales (tomando $k-1$ de la primera y la condición de normalización) para encontrar los valores de $\pi_1, \pi_2, ..., \pi_k$.

---

### Sección 2: Defensa Oral

**Pregunta 2.1:** "Has explicado la Propiedad de Markov. Dame un ejemplo de un proceso del mundo real que creas que **cumple** razonablemente bien con la Propiedad de Markov y otro que claramente **no la cumple**. Justifica tu elección."

**Respuesta Modelo:**
"*   **Proceso que cumple la Propiedad de Markov:** El **clima diario** (soleado, nublado, lluvioso). La probabilidad de que llueva mañana probablemente depende mucho más del clima de hoy que del clima de la semana pasada. Es decir, el 'futuro' (clima de mañana) está fuertemente condicionado por el 'presente' (clima de hoy), y el 'pasado' (clima de anteayer) no añade mucha información adicional una vez que sabemos el clima de hoy.

*   **Proceso que NO cumple la Propiedad de Markov:** El **estado de ánimo de una persona**. El estado de ánimo de hoy no solo depende del de ayer, sino que puede estar influenciado por eventos traumáticos de hace años, patrones de pensamiento a largo plazo, o incluso la acumulación de estrés a lo largo de una semana. El 'pasado' (eventos o estados de ánimo anteriores) tiene una influencia acumulativa y no se 'olvida' al conocer solo el presente."

**Pregunta 2.2:** "Si tienes una matriz de transición $P$ para una cadena de Markov, ¿qué representa el elemento $p_{ij}$? ¿Y qué representa el elemento $(P^n)_{ij}$?"

**Respuesta Modelo:**
"*   El elemento $p_{ij}$ (en la fila $i$ y columna $j$) de la matriz de transición $P$ representa la **probabilidad de transitar del estado $i$ al estado $j$ en un solo paso de tiempo**.

*   El elemento $(P^n)_{ij}$ (en la fila $i$ y columna $j$) de la matriz $P^n$ (la matriz de transición elevada a la potencia $n$) representa la **probabilidad de transitar del estado $i$ al estado $j$ en exactamente $n$ pasos de tiempo**."

**Pregunta 2.3:** "¿Qué significa que una Cadena de Markov es 'regular'? ¿Por qué esta propiedad es importante para la existencia y unicidad de la distribución estacionaria?"

**Respuesta Modelo:**
"Una Cadena de Markov es **regular** si existe alguna potencia de su matriz de transición, $P^k$, que tiene todas sus entradas estrictamente positivas. Esto significa que es posible llegar desde cualquier estado a cualquier otro estado en algún número de pasos $k$.

Esta propiedad es crucial porque garantiza que la cadena es 'irreducible' (todos los estados se comunican entre sí) y 'aperiódica' (no hay ciclos que impidan que el sistema se asiente en un equilibrio). Si una cadena es regular, entonces se garantiza que existe una **única distribución estacionaria** y que el sistema convergerá a esa distribución a largo plazo, independientemente del estado inicial."

**Pregunta 2.4:** "Si el vector de distribución estacionaria de un sistema de clima (Soleado, Nublado, Lluvioso) es $\pi = [0.5, 0.3, 0.2]$, ¿qué significa esto en términos prácticos? ¿Qué implicación tiene para la predicción del clima a muy largo plazo?"

**Respuesta Modelo:**
"En términos prácticos, si el vector de distribución estacionaria es $\pi = [0.5, 0.3, 0.2]$, significa que, a muy largo plazo, el sistema de clima pasará el 50% del tiempo en el estado 'Soleado', el 30% en el estado 'Nublado' y el 20% en el estado 'Lluvioso'. Estas son las proporciones de tiempo que el sistema pasará en cada estado en el equilibrio.

La implicación para la predicción del clima a muy largo plazo es que, independientemente del clima de hoy, la probabilidad de que un día futuro muy lejano sea soleado será del 50%, nublado del 30% y lluvioso del 20%. El estado inicial pierde su influencia a medida que el tiempo avanza, y el sistema converge a esta distribución de equilibrio."

---

### Sección 3: Preguntas Rápidas

**Pregunta 3.1 (Opción Múltiple):** Un proceso estocástico es una secuencia de variables aleatorias indexadas por:

**a) Un parámetro de tiempo.**
b) Un espacio de estados.
c) Una matriz de transición.
d) Una distribución de probabilidad.

**Justificación:** La definición de un proceso estocástico es una colección de variables aleatorias indexadas por un parámetro, usualmente el tiempo.

**Pregunta 3.2 (Respuesta Corta):** ¿Qué es una "realización" o "trayectoria" de un proceso estocástico?

**Respuesta Modelo:** Una **realización** o **trayectoria** de un proceso estocástico es una única secuencia de valores observados del proceso a lo largo del tiempo. Es una de las posibles "rutas" que el proceso puede seguir.

**Pregunta 3.3 (Verdadero/Falso):** En una matriz de transición de una Cadena de Markov, la suma de los elementos de cada columna debe ser igual a 1. ¿Verdadero o Falso? Justifica.

**Respuesta Modelo:** **Falso.** La suma de los elementos de **cada FILA** debe ser igual a 1, ya que representa la probabilidad total de transitar desde un estado dado a *cualquier* otro estado (incluido él mismo). La suma de las columnas no necesariamente es 1.

**Pregunta 3.4 (Respuesta Corta):** ¿Qué es un "estado absorbente" en una Cadena de Markov? Da un ejemplo.

**Respuesta Modelo:** Un **estado absorbente** en una Cadena de Markov es un estado del cual, una vez que se entra, es imposible salir. Esto significa que la probabilidad de transitar de ese estado a sí mismo es 1 ($p_{ii} = 1$). Un ejemplo sería el estado de "muerte" en un modelo de salud: una vez que un individuo llega a ese estado, no puede transitar a ningún otro estado.
