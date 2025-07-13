# Resolución del Examen Final Integrador - Estadística Aplicada II

---

### Sección 1: Desarrollo en Pizarrón

**Pregunta 1: Diseño Experimental y Análisis para Comparar Tres Medicamentos**

1.  **Diseño Experimental más Adecuado:**
    El diseño más adecuado es un **Diseño Completamente al Azar (DCA)**. 
    *   **Justificación:** Los pacientes son asignados aleatoriamente a los grupos de tratamiento, lo que asegura que, en promedio, los grupos sean comparables al inicio del estudio y que cualquier diferencia observada al final pueda atribuirse al efecto del medicamento y no a otras variables. Es un diseño simple y efectivo para comparar múltiples tratamientos cuando las unidades experimentales (pacientes) se consideran homogéneas.

2.  **Hipótesis Estadísticas:**
    Dado que queremos comparar las medias de reducción de colesterol de tres grupos, las hipótesis serían:
    *   **Hipótesis Nula ($H_0$):** Las medias de reducción de colesterol de los tres medicamentos son iguales.
        $$ H_0: \mu_1 = \mu_2 = \mu_3 $$
    *   **Hipótesis Alternativa ($H_1$):** Al menos una de las medias de reducción de colesterol es diferente de las demás.
        $$ H_1: \text{No todas las } \mu_i \text{ son iguales} $$

3.  **Descomposición de la Variabilidad (Suma de Cuadrados Total):**
    La variabilidad total en la reducción del colesterol (SCT) se descompondrá en dos componentes:
    $$ SCT = SCTr + SCE $$
    *   **SCT (Suma de Cuadrados Total):** Mide la variabilidad total de las puntuaciones de reducción de colesterol de todos los pacientes respecto a la gran media general.
        $$ SCT = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{\bar{X}})^2 $$
    *   **SCTr (Suma de Cuadrados del Tratamiento o Entre Grupos):** Mide la variabilidad en la reducción del colesterol que es atribuible a las diferencias entre las medias de los tres grupos de medicamentos. Si los medicamentos tienen efectos diferentes, esta suma de cuadrados será grande.
        $$ SCTr = \sum_{i=1}^{k} n_i (\bar{X}_i - \bar{\bar{X}})^2 $$
    *   **SCE (Suma de Cuadrados del Error o Dentro de los Grupos):** Mide la variabilidad en la reducción del colesterol que no puede ser explicada por las diferencias entre los medicamentos. Representa la variabilidad aleatoria o el "ruido" dentro de cada grupo de tratamiento.
        $$ SCE = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)^2 $$

4.  **Estadístico de Prueba y su Distribución:**
    El estadístico de prueba adecuado para comparar las medias de tres o más grupos es el **Estadístico F** del Análisis de la Varianza (ANOVA).
    $$ F = \frac{CMTr}{CME} = \frac{SCTr / (k-1)}{SCE / (N-k)} $$
    Bajo la hipótesis nula ($H_0$), este estadístico F sigue una **distribución F de Snedecor** con $gl_1 = k-1$ grados de libertad en el numerador y $gl_2 = N-k$ grados de libertad en el denominador.
    En este caso: $k=3$ (medicamentos), $N=60$ (pacientes).
    $gl_1 = 3-1 = 2$
    $gl_2 = 60-3 = 57$
    Así, $F \sim F_{(2, 57)}$.

5.  **Supuestos Clave para la Validez del Análisis (ANOVA):**
    1.  **Independencia:** Las observaciones (reducción de colesterol de cada paciente) deben ser independientes entre sí. Esto se logra con la asignación aleatoria de pacientes a los grupos.
    2.  **Normalidad:** Las poblaciones de las que provienen las muestras (es decir, la reducción de colesterol para cada medicamento) deben seguir una distribución normal.
    3.  **Homocedasticidad (Igualdad de Varianzas):** Las varianzas de la reducción de colesterol deben ser iguales para los tres grupos de medicamentos ($\sigma^2_1 = \sigma^2_2 = \sigma^2_3$).

---

### Sección 2: Defensa Oral

**Pregunta 2.1:** "Excelente desarrollo. Ahora, supongamos que usted realiza el análisis y el p-valor resultante es de 0.008. ¿Qué conclusión extrae de este p-valor? ¿Qué pregunta importante queda sin responder y qué análisis adicional realizaría para responderla? Explique la lógica de ese análisis adicional."

**Respuesta Modelo:**
"Un p-valor de 0.008 es menor que el nivel de significancia común de 0.05 (o incluso 0.01). Por lo tanto, **rechazaría la hipótesis nula**. La conclusión es que existe evidencia estadística significativa para afirmar que **al menos uno de los medicamentos tiene una media de reducción de colesterol diferente** a los demás. Es decir, no todos los medicamentos son igualmente efectivos.

La pregunta importante que queda sin responder es **cuál o cuáles de los medicamentos son significativamente diferentes entre sí**. El ANOVA solo nos dice que hay *alguna* diferencia, pero no nos dice dónde. Para responder a esto, realizaría **pruebas post-hoc** (o de comparaciones múltiples). La lógica de estas pruebas es realizar comparaciones por pares entre las medias de los grupos (Nuevo vs. Existente 1, Nuevo vs. Existente 2, Existente 1 vs. Existente 2) pero ajustando el nivel de significancia para controlar la tasa de error de Tipo I global (la probabilidad de cometer al menos un falso positivo en todas las comparaciones). Una prueba post-hoc común y recomendada para este escenario sería la **Prueba HSD de Tukey**, ya que compara todas las posibles parejas de medias y es robusta."

**Pregunta 2.2:** "Durante la verificación de supuestos, usted encuentra que los datos de reducción de colesterol no siguen una distribución normal en uno de los grupos, y el tamaño de la muestra por grupo es de solo 20. ¿Qué implicaciones tiene esto para la validez de su análisis original? ¿Qué alternativa estadística no paramétrica podría considerar para este estudio y por qué?"

**Respuesta Modelo:**
"La no normalidad en uno de los grupos, especialmente con un tamaño de muestra de 20 (que no es muy grande), implica que el supuesto de normalidad del ANOVA podría estar violado. Aunque el ANOVA es relativamente robusto a desviaciones moderadas de la normalidad con tamaños de muestra iguales, una violación clara podría afectar la validez del p-valor y, por ende, la fiabilidad de la conclusión.

En este escenario, consideraría una **alternativa estadística no paramétrica**: la **Prueba H de Kruskal-Wallis**. La elegiría porque:
1.  Es el análogo no paramétrico del ANOVA de un factor.
2.  No requiere el supuesto de normalidad de las poblaciones.
3.  Se utiliza para comparar las medianas (o distribuciones) de tres o más grupos independientes.

Aunque la prueba de Kruskal-Wallis es generalmente menos potente que el ANOVA si los supuestos de este último se cumplen, es una opción más robusta y válida cuando la normalidad es un problema, especialmente con muestras de este tamaño."

**Pregunta 2.3:** "Si en lugar de comparar tres medicamentos, la empresa quisiera estudiar el efecto de la dosis del medicamento (baja, media, alta) y la frecuencia de administración (diaria, semanal) sobre la reducción del colesterol, ¿qué tipo de diseño experimental propondría? ¿Qué concepto estadístico crucial podría investigar con este nuevo diseño que no podría con el anterior?"

**Respuesta Modelo:**
"Propondría un **Diseño Factorial de Dos Factores (Dosis x Frecuencia)**. Este diseño permitiría estudiar simultáneamente el efecto de la dosis y el efecto de la frecuencia de administración sobre la reducción del colesterol.

El concepto estadístico crucial que podría investigar con este nuevo diseño, y que no podría con el anterior (ANOVA de un factor), es la **interacción** entre la dosis y la frecuencia de administración. Una interacción significativa significaría que el efecto de la dosis sobre la reducción del colesterol no es el mismo para todas las frecuencias de administración, o viceversa. Por ejemplo, una dosis alta podría ser muy efectiva si se administra diariamente, pero no si se administra semanalmente. Este tipo de relación compleja solo puede ser detectada y analizada con un diseño factorial."

**Pregunta 2.4:** "En un contexto completamente diferente, si usted estuviera modelando el comportamiento de los clientes de una tienda online, donde los clientes pueden estar en estados como 'navegando', 'añadiendo al carrito' o 'comprando', y el estado de un cliente en un momento dado solo depende de su estado anterior, ¿qué tipo de proceso estocástico utilizaría para modelar esto? ¿Qué propiedad fundamental de este proceso lo hace adecuado para este escenario?"

**Respuesta Modelo:**
"Utilizaría una **Cadena de Markov** para modelar el comportamiento de los clientes. La propiedad fundamental que la hace adecuada para este escenario es la **Propiedad de Markov (o de carencia de memoria)**. Esta propiedad establece que la probabilidad de que un cliente pase a un estado futuro (e.g., de 'navegando' a 'añadiendo al carrito') depende únicamente de su estado actual (e.g., 'navegando') y no de cómo llegó a ese estado (e.g., si llegó a 'navegando' desde 'comprando' o desde 'añadiendo al carrito' previamente). Esto simplifica el modelado al no requerir el historial completo del cliente."

---

### Sección 3: Preguntas Rápidas

**Pregunta 3.1 (Opción Múltiple):** Si en una prueba de independencia Chi-Cuadrado, una celda tiene una frecuencia esperada de 2.5, la acción más apropiada sería:

a) Ignorar esa celda.
b) Aumentar el nivel de significancia.
**c) Agrupar categorías o considerar una prueba exacta.**
d) Concluir que las variables son independientes.

**Justificación:** La condición para la validez de la prueba Chi-Cuadrado es que todas las frecuencias esperadas sean al menos 5. Si no se cumple, la aproximación no es fiable, y se deben agrupar categorías o usar una prueba exacta como la de Fisher.

**Pregunta 3.2 (Respuesta Corta):** ¿Cuál es la principal diferencia entre un parámetro y un estimador?

**Respuesta Modelo:** Un **parámetro** es una medida numérica que describe una característica de la **población** (es un valor fijo y desconocido). Un **estimador** es una medida numérica que describe una característica de la **muestra** y se utiliza para inferir sobre el parámetro (es una variable aleatoria).

**Pregunta 3.3 (Verdadero/Falso):** La potencia de una prueba es la probabilidad de cometer un Error de Tipo I. ¿Verdadero o Falso? Justifica.

**Respuesta Modelo:** **Falso.** La potencia de una prueba es la probabilidad de **no cometer un Error de Tipo II** (es decir, de rechazar correctamente la hipótesis nula cuando es falsa). La probabilidad de cometer un Error de Tipo I es el nivel de significancia ($\alpha$).

**Pregunta 3.4 (Respuesta Corta):** ¿Qué mide el p-valor y cuál es la regla de decisión general basada en él?

**Respuesta Modelo:** El **p-valor** mide la probabilidad de obtener un resultado muestral tan extremo o más extremo que el observado, asumiendo que la hipótesis nula es verdadera. La regla de decisión general es: **Si el p-valor es menor o igual que el nivel de significancia ($\alpha$), se rechaza la hipótesis nula ($H_0$).**

**Pregunta 3.5 (Opción Múltiple):** La corrección de Bessel ($n-1$ en el denominador de la varianza muestral) se aplica para asegurar que el estimador sea:

a) Consistente.
b) Eficiente.
**c) Insesgado.**
d) Suficiente.

**Justificación:** Dividir por $n-1$ corrige el sesgo de la varianza muestral, haciéndola un estimador insesgado de la varianza poblacional.

**Pregunta 3.6 (Respuesta Corta):** ¿Cuándo usarías una Prueba de los Rangos con Signo de Wilcoxon en lugar de una Prueba U de Mann-Whitney?

**Respuesta Modelo:** Usaría la **Prueba de los Rangos con Signo de Wilcoxon** cuando tengo **muestras pareadas** (datos dependientes, como mediciones antes y después en los mismos sujetos). Usaría la Prueba U de Mann-Whitney para **muestras independientes**.

**Pregunta 3.7 (Verdadero/Falso):** En una Cadena de Markov, la suma de las probabilidades de transición de cada columna de la matriz de transición debe ser igual a 1. ¿Verdadero o Falso? Justifica.

**Respuesta Modelo:** **Falso.** La suma de las probabilidades de transición de **cada FILA** de la matriz de transición debe ser igual a 1, ya que representa la probabilidad total de transitar desde un estado dado a *cualquier* otro estado (incluido él mismo).

**Pregunta 3.8 (Respuesta Corta):** ¿Qué significa que un estimador es "consistente"?

**Respuesta Modelo:** Un estimador es **consistente** si, a medida que el tamaño de la muestra ($n$) aumenta indefinidamente, el valor del estimador converge en probabilidad al verdadero valor del parámetro que está estimando. En términos más simples, con una muestra suficientemente grande, la estimación será muy cercana al valor real del parámetro.