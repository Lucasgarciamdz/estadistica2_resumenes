# Resolución del Examen Teórico: Unidad 2 - Pruebas de Hipótesis

---

### Sección 1: Desarrollo en Pizarrón

**Pregunta 1: Construcción del Estadístico t de Student**

**Contexto:** Queremos probar una hipótesis sobre la media poblacional $\mu$, pero **no conocemos** la varianza poblacional $\sigma^2$. Debemos estimarla usando la varianza muestral $S^2$.

**El Problema de Sustituir $\sigma$ por $S$ en el Estadístico Z:**
Si simplemente reemplazamos la $\sigma$ desconocida por su estimador $S$ en la fórmula del estadístico Z, la distribución resultante ya no es exactamente una Normal Estándar:

$$ \frac{\bar{X} - \mu}{S / \sqrt{n}} \nsim N(0,1) $$

Esto se debe a que hemos introducido una nueva fuente de variabilidad: la estimación de $\sigma$ a través de $S$. $S$ es una variable aleatoria que cambiará de muestra en muestra, añadiendo incertidumbre. La distribución t de Student es la que describe correctamente esta nueva situación.

**Teorema (Definición de la distribución t de Student):**
Si $Z$ es una variable aleatoria Normal Estándar ($Z \sim N(0,1)$) y $U$ es una variable aleatoria Chi-Cuadrado con $k$ grados de libertad ($U \sim \chi^2_k$), y además $Z$ y $U$ son independientes, entonces la variable $T$ definida como:

$$ T = \frac{Z}{\sqrt{U/k}} $$

sigue una distribución t de Student con $k$ grados de libertad.

**Desarrollo del Estadístico t:**
Nuestro objetivo es mostrar que $\frac{\bar{X} - \mu}{S / \sqrt{n}}$ sigue esta estructura.

1.  **El Numerador (Z):** Ya sabemos que, bajo la hipótesis nula ($H_0: \mu = \mu_0$), la cantidad $Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$ es $N(0,1)$.

2.  **El Denominador (U):** Un teorema fundamental de la estadística establece que, si la población es normal, la cantidad $\frac{(n-1)S^2}{\sigma^2}$ sigue una distribución Chi-Cuadrado con $n-1$ grados de libertad.
    $$ U = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1} $$

3.  **Armando el Estadístico T:** Sustituyamos estos componentes en la definición de la distribución t, con $k = n-1$ grados de libertad.
    $$ T = \frac{Z}{\sqrt{U/k}} = \frac{ \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}} }{ \sqrt{ \frac{(n-1)S^2}{\sigma^2} / (n-1) } } $$
    Simplificando el denominador:
    $$ \sqrt{ \frac{(n-1)S^2}{\sigma^2 (n-1)} } = \sqrt{ \frac{S^2}{\sigma^2} } = \frac{S}{\sigma} $$
    Ahora, sustituimos de nuevo en la expresión de T:
    $$ T = \frac{\frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}}{\frac{S}{\sigma}} = \frac{(\bar{X} - \mu_0) \cdot \sigma}{(\sigma / \sqrt{n}) \cdot S} = \frac{(\bar{X} - \mu_0) \cdot \sqrt{n}}{S} $$
    Así, el estadístico de prueba es:
    $$ t = \frac{\bar{X} - \mu_0}{S / \sqrt{n}} $$

**Conclusión:** Hemos demostrado que la expresión que usamos para la prueba t sigue, en efecto, una distribución t de Student con $n-1$ grados de libertad. Esta distribución es similar a la normal pero con colas más "pesadas", lo que refleja la mayor incertidumbre al no conocer $\sigma$ y tener que estimarlo de la muestra.

**Supuestos Clave para la Prueba t:**
1.  **Muestreo Aleatorio Simple:** Las observaciones son independientes e idénticamente distribuidas.
2.  **Normalidad de la Población:** La población de la que se extrae la muestra debe seguir una distribución normal. (Este supuesto es menos crítico para muestras grandes debido al TCL).
3.  **Varianza Poblacional Desconocida:** La razón principal para usar la prueba t en lugar de la Z.

---

### Sección 2: Defensa Oral

**Pregunta 2.1:** "Has explicado la diferencia entre Z y t. Ahora, ¿cuál es la relación entre la distribución t y la distribución normal estándar? ¿Qué sucede con la distribución t a medida que los grados de libertad aumentan?"

**Respuesta Modelo:**
"La distribución t de Student es una familia de distribuciones que se asemeja a la distribución normal estándar, pero tiene colas más 'pesadas' o 'gordas'. Esto significa que tiene más probabilidad en los extremos y menos en el centro en comparación con la normal estándar. Esta mayor dispersión refleja la incertidumbre adicional que tenemos al estimar la varianza poblacional a partir de la muestra.

A medida que los grados de libertad (que están directamente relacionados con el tamaño de la muestra, $n-1$) aumentan, la distribución t se vuelve cada vez más parecida a la distribución normal estándar. Para grados de libertad mayores a 30 (o a veces 120, dependiendo de la fuente), la distribución t es prácticamente indistinguible de la normal estándar. Esto tiene sentido, ya que con muestras muy grandes, nuestra estimación de la varianza poblacional ($S^2$) se vuelve muy precisa, y la incertidumbre adicional disminuye."

**Pregunta 2.2:** "En el contexto de una prueba de hipótesis, ¿qué es un Error de Tipo I y un Error de Tipo II? ¿Cómo se relacionan con el nivel de significancia ($\alpha$) y la potencia de la prueba ($\beta$)?"

**Respuesta Modelo:**
"Un **Error de Tipo I** ocurre cuando rechazamos la hipótesis nula ($H_0$) cuando en realidad es verdadera. Es como un 'falso positivo'. La probabilidad de cometer este error se denota por $\alpha$, que es el nivel de significancia que fijamos al inicio de la prueba. Por ejemplo, si $\alpha = 0.05$, hay un 5% de probabilidad de rechazar $H_0$ erróneamente.

Un **Error de Tipo II** ocurre cuando no rechazamos la hipótesis nula ($H_0$) cuando en realidad es falsa. Es como un 'falso negativo'. La probabilidad de cometer este error se denota por $\beta$.

La **Potencia de la Prueba** es la probabilidad de rechazar correctamente la hipótesis nula cuando es falsa, es decir, $1 - \beta$. Es la capacidad de la prueba para detectar un efecto real si existe. Hay una relación inversa entre $\alpha$ y $\beta$: para un tamaño de muestra fijo, si disminuimos $\alpha$ (haciéndonos más estrictos para rechazar $H_0$), aumentamos $\beta$ (disminuimos la potencia), y viceversa."

**Pregunta 2.3:** "Si un p-valor es de 0.001, ¿qué significa eso en términos de la evidencia en contra de la hipótesis nula? ¿Y si el p-valor es de 0.45?"

**Respuesta Modelo:**
"Un p-valor de 0.001 significa que, si la hipótesis nula fuera verdadera, la probabilidad de observar los datos de nuestra muestra (o datos aún más extremos) sería de solo 0.1%. Esto es una probabilidad muy, muy baja, lo que proporciona una **evidencia muy fuerte en contra de la hipótesis nula**. Nos llevaría a rechazar $H_0$ con un alto grado de confianza.

Por otro lado, un p-valor de 0.45 significa que, si la hipótesis nula fuera verdadera, la probabilidad de observar nuestros datos (o datos más extremos) sería del 45%. Esta es una probabilidad alta, lo que indica que los datos observados son bastante consistentes con la hipótesis nula. Por lo tanto, **no tendríamos evidencia suficiente para rechazar la hipótesis nula**."

**Pregunta 2.4:** "¿Es posible tener una prueba con un Error de Tipo I muy bajo y un Error de Tipo II también muy bajo al mismo tiempo? ¿Qué factor es el más influyente para lograr esto?"

**Respuesta Modelo:**
"Sí, es posible, pero no para un tamaño de muestra fijo. Para un tamaño de muestra fijo, hay un compromiso entre $\alpha$ y $\beta$. Sin embargo, el factor más influyente para lograr que ambos errores sean bajos (es decir, alta potencia y bajo $\alpha$) es **aumentar el tamaño de la muestra ($n$)**. Al aumentar $n$, el error estándar de los estimadores disminuye, lo que hace que la distribución de muestreo del estadístico de prueba sea más estrecha y nos permite distinguir más fácilmente entre $H_0$ y $H_1$ si $H_1$ es verdadera."

---

### Sección 3: Preguntas Rápidas

**Pregunta 3.1 (Opción Múltiple):** Si el p-valor de una prueba de hipótesis es 0.03 y el nivel de significancia ($\alpha$) es 0.05, la decisión correcta es:

a) Aceptar la hipótesis nula.
**b) Rechazar la hipótesis nula.**
c) No hay suficiente información para tomar una decisión.
d) El resultado no es estadísticamente significativo.

**Justificación:** La regla de decisión es: si p-valor $\le \alpha$, se rechaza $H_0$. Como $0.03 \le 0.05$, se rechaza $H_0$.

**Pregunta 3.2 (Respuesta Corta):** ¿Cuál es la principal diferencia entre una prueba unilateral y una bilateral en términos de la región de rechazo?

**Respuesta Modelo:** En una **prueba unilateral**, la región de rechazo se encuentra completamente en una de las colas de la distribución (izquierda o derecha), ya que la hipótesis alternativa especifica una dirección (e.g., $\mu > \mu_0$). En una **prueba bilateral**, la región de rechazo se divide entre ambas colas de la distribución, ya que la hipótesis alternativa no especifica una dirección (e.g., $\mu \neq \mu_0$).

**Pregunta 3.3 (Verdadero/Falso):** La potencia de una prueba es la probabilidad de no cometer un Error de Tipo II. ¿Verdadero o Falso? Justifica.

**Respuesta Modelo:** **Verdadero.** La potencia de la prueba se define como $1 - \beta$, donde $\beta$ es la probabilidad de cometer un Error de Tipo II. Por lo tanto, $1 - \beta$ es la probabilidad de no cometer un Error de Tipo II (es decir, de rechazar $H_0$ cuando es falsa, que es la decisión correcta).

**Pregunta 3.4 (Respuesta Corta):** ¿Por qué es importante establecer el nivel de significancia ($\alpha$) *antes* de realizar la prueba de hipótesis?

**Respuesta Modelo:** Es crucial establecer $\alpha$ *antes* de realizar la prueba para evitar el sesgo del investigador. Si se elige $\alpha$ *después* de ver el p-valor, se podría seleccionar un $\alpha$ que justifique la conclusión deseada, lo que comprometería la objetividad y la validez de la inferencia estadística. Establecerlo de antemano asegura la imparcialidad del proceso de decisión.
