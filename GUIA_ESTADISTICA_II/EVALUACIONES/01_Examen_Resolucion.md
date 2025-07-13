# Resolución del Examen Teórico: Unidad 1 - Conceptos Fundamentales

---

### Sección 1: Desarrollo en Pizarrón

**Pregunta 1: Demostración de la Insesgadez de la Varianza Muestral ($S^2$)

Para demostrar que $E(S^2) = \sigma^2$, donde $S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2$, necesitamos partir de la definición de varianza y de las propiedades de la esperanza.

Sabemos que $\sum_{i=1}^{n}(X_i - \bar{X})^2 = \sum_{i=1}^{n}X_i^2 - n\bar{X}^2$.

Entonces, $S^2 = \frac{1}{n-1}\left(\sum_{i=1}^{n}X_i^2 - n\bar{X}^2\right)$.

Ahora, aplicamos el operador esperanza:

$E(S^2) = E\left[\frac{1}{n-1}\left(\sum_{i=1}^{n}X_i^2 - n\bar{X}^2\right)\right]$

Por linealidad de la esperanza:

$E(S^2) = \frac{1}{n-1}\left[E\left(\sum_{i=1}^{n}X_i^2\right) - nE(\bar{X}^2)\right]$

Consideremos cada término por separado:

**Término 1: $E\left(\sum_{i=1}^{n}X_i^2\right)$**

Sabemos que $Var(X) = E(X^2) - [E(X)]^2$. Por lo tanto, $E(X^2) = Var(X) + [E(X)]^2$.

Para una variable aleatoria $X_i$ de la población, $E(X_i) = \mu$ y $Var(X_i) = \sigma^2$.

Así, $E(X_i^2) = \sigma^2 + \mu^2$.

Entonces, $E\left(\sum_{i=1}^{n}X_i^2\right) = \sum_{i=1}^{n}E(X_i^2) = \sum_{i=1}^{n}(\sigma^2 + \mu^2) = n(\sigma^2 + \mu^2)$.

**Término 2: $E(\bar{X}^2)$**

Sabemos que $Var(\bar{X}) = E(\bar{X}^2) - [E(\bar{X})]^2$. Por lo tanto, $E(\bar{X}^2) = Var(\bar{X}) + [E(\bar{X})]^2$.

De la Unidad 1, sabemos que $E(\bar{X}) = \mu$ y $Var(\bar{X}) = \frac{\sigma^2}{n}$.

Así, $E(\bar{X}^2) = \frac{\sigma^2}{n} + \mu^2$.

**Sustituyendo ambos términos en la expresión de $E(S^2)$:**

$E(S^2) = \frac{1}{n-1}\left[n(\sigma^2 + \mu^2) - n\left(\frac{\sigma^2}{n} + \mu^2\right)\right]$

$E(S^2) = \frac{1}{n-1}\left[n\sigma^2 + n\mu^2 - \sigma^2 - n\mu^2\right]$

$E(S^2) = \frac{1}{n-1}\left[n\sigma^2 - \sigma^2\right]$

$E(S^2) = \frac{1}{n-1}\left[(n-1)\sigma^2\right]$

$E(S^2) = \sigma^2$

**Conclusión:** Hemos demostrado que el valor esperado de la varianza muestral $S^2$ es igual a la varianza poblacional $\sigma^2$, lo que significa que $S^2$ es un estimador insesgado de $\sigma^2$.

---

### Sección 2: Defensa Oral

**Pregunta 2.1:** "Excelente. Ahora, explícame conceptualmente, como si se lo explicaras a alguien que no sabe matemáticas, por qué si dividiéramos por $n$ en lugar de $n-1$, estaríamos subestimando sistemáticamente la verdadera varianza de la población. ¿Qué tiene que ver la media muestral $\bar{X}$ en todo esto?"

**Respuesta Modelo:**
"Imagina que queremos saber qué tan dispersos están los datos en toda la población. Si tuviéramos acceso a todos los datos de la población, calcularíamos la varianza usando la media real de la población ($\mu$).

Pero en la práctica, solo tenemos una muestra. Y para calcular la varianza de esa muestra, no usamos la media real de la población (porque no la conocemos), sino que usamos la media de nuestra propia muestra ($\bar{X}$). El problema es que la media de la muestra ($\bar{X}$) siempre estará, por definición, lo más cerca posible de los datos de esa muestra. Es como si los datos se 'agruparan' un poco más alrededor de su propia media muestral de lo que lo harían alrededor de la verdadera media poblacional.

Entonces, si calculamos la suma de las desviaciones al cuadrado usando $\bar{X}$ en lugar de $\mu$, esa suma tenderá a ser un poco más pequeña de lo que realmente debería ser para representar la dispersión de la población. Si dividimos esa suma por $n$, estaríamos subestimando sistemáticamente la verdadera varianza poblacional. Dividir por $n-1$ es una 'corrección' que compensa esta subestimación, asegurando que, en promedio, nuestra estimación de la varianza muestral sea igual a la varianza poblacional. Es como darle un pequeño 'empujón' hacia arriba para que sea una estimación justa."

**Pregunta 2.2:** "Mencionaste los 'grados de libertad'. ¿Qué significa exactamente que se 'pierde un grado de libertad' en este contexto? ¿Dónde se fue?"

**Respuesta Modelo:**
"Los grados de libertad se refieren al número de valores en un cálculo que son libres de variar. Cuando calculamos la varianza muestral, necesitamos estimar la media poblacional ($\mu$) con la media muestral ($\bar{X}$) a partir de los mismos datos de la muestra. Una vez que hemos calculado $\bar{X}$, ya no todos los $n$ valores de la muestra son independientes para el cálculo de las desviaciones.

Por ejemplo, si tienes 5 números y sabes su media, y conoces 4 de esos números, el quinto número está automáticamente determinado para que la media sea la que es. Es decir, hay $n-1$ valores que son 'libres' de variar. Al usar $\bar{X}$ en la fórmula de la varianza, hemos 'gastado' un grado de libertad, y por eso dividimos por $n-1$ en lugar de $n$. Ese grado de libertad 'se fue' en la estimación de la media."

**Pregunta 2.3:** "Has demostrado que $S^2$ es un estimador insesgado de $\sigma^2$. ¿Significa esto que $S$ (la desviación estándar muestral) es también un estimador insesgado de $\sigma$ (la desviación estándar poblacional)? Justifica tu respuesta."

**Respuesta Modelo:**
"No, no significa que $S$ sea un estimador insesgado de $\sigma$. La insesgadez es una propiedad de la esperanza, y la esperanza de una función no lineal (como la raíz cuadrada) no es la función de la esperanza. Es decir, $E(\sqrt{X}) \neq \sqrt{E(X)}$.

Dado que $S = \sqrt{S^2}$, y la raíz cuadrada es una función no lineal, el hecho de que $E(S^2) = \sigma^2$ no implica que $E(S) = \sigma$. De hecho, $S$ es un estimador sesgado de $\sigma$, aunque el sesgo tiende a ser pequeño para muestras grandes."

**Pregunta 2.4:** "Si la población de la que proviene la muestra no fuera normal, ¿seguiría siendo válida tu demostración? ¿Qué partes del desarrollo se verían afectadas?"

**Respuesta Modelo:**
"Sí, la demostración de la insesgadez de $S^2$ seguiría siendo válida. La demostración se basa únicamente en las propiedades de la esperanza y la varianza de variables aleatorias, y en el hecho de que las $X_i$ son independientes e idénticamente distribuidas (iid) con una media y varianza finitas. No se asume en ningún momento que la distribución subyacente de la población sea normal.

Las partes del desarrollo que se verían afectadas si asumiéramos normalidad serían las relacionadas con la distribución de muestreo de $S^2$ (que sigue una distribución Chi-Cuadrado si la población es normal), pero no la propiedad de insesgadez en sí misma."

---

### Sección 3: Preguntas Rápidas

**Pregunta 3.1 (Opción Múltiple):** El Teorema Central del Límite es crucial en estadística porque nos dice que:

a) Para muestras grandes, la distribución de la población se aproxima a una normal.
**b) La distribución de muestreo de la media muestral se aproxima a una normal, sin importar la distribución de la población.**
c) La media muestral es siempre un estimador insesgado de la media poblacional.
d) La varianza de la media muestral es $\sigma^2/n$.

**Justificación:** La opción (b) es la definición precisa del TCL. La opción (a) es incorrecta; el TCL no dice nada sobre la distribución de la población. Las opciones (c) y (d) son propiedades de la media muestral, pero no son el contenido principal del TCL.

**Pregunta 3.2 (Respuesta Corta):** Entre dos estimadores insesgados para el mismo parámetro, ¿cómo decides cuál es el "mejor"? ¿Qué propiedad buscas?

**Respuesta Modelo:** Se busca el estimador que sea más **eficiente**. La eficiencia se mide por la **menor varianza**. Un estimador más eficiente tiene una menor dispersión alrededor del verdadero valor del parámetro.

**Pregunta 3.3 (Verdadero/Falso):** Un estimador consistente es aquel que, para cualquier tamaño de muestra, siempre dará una estimación muy cercana al parámetro real. ¿Verdadero o Falso? Justifica.

**Respuesta Modelo:** **Falso.** La consistencia es una propiedad asintótica, es decir, se refiere al comportamiento del estimador a medida que el tamaño de la muestra ($n$) tiende a infinito. Un estimador consistente es aquel que, a medida que $n$ aumenta, la probabilidad de que la estimación se aleje del parámetro real tiende a cero. No garantiza una estimación cercana para *cualquier* tamaño de muestra, sino que mejora con el aumento del tamaño de la muestra.

**Pregunta 3.4 (Respuesta Corta):** ¿Qué mide el Error Estándar de la media y por qué es inversamente proporcional a la raíz cuadrada de $n$?

**Respuesta Modelo:** El Error Estándar de la media ($\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$) mide la **precisión** de la media muestral como estimador de la media poblacional. Es la desviación estándar de la distribución de muestreo de la media. Es inversamente proporcional a la raíz cuadrada de $n$ porque a medida que el tamaño de la muestra ($n$) aumenta, la variabilidad de las medias muestrales alrededor de la media poblacional disminuye. Las muestras más grandes tienden a ser más representativas de la población, y por lo tanto, sus medias están más cerca de la verdadera media poblacional.
