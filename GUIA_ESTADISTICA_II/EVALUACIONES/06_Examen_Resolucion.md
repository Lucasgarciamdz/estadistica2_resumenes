# Resolución del Examen Teórico: Unidad 6 - ANOVA y Diseños Experimentales

---

### Sección 1: Desarrollo en Pizarrón

**Pregunta 1: Interacción en Diseño Factorial de ANOVA**

**Concepto de Interacción:**
En un diseño factorial, la **interacción** ocurre cuando el efecto de un factor sobre la variable de respuesta **depende del nivel** de otro factor. Es decir, el efecto de un factor no es constante a través de todos los niveles del otro factor. Si no hay interacción, el efecto de un factor es el mismo, independientemente del nivel del otro factor.

**Ejemplo Conceptual:**
Supongamos que estamos estudiando el efecto de un fertilizante (Factor A: con/sin) y el tipo de suelo (Factor B: arenoso/arcilloso) en el crecimiento de una planta. Podría ser que el fertilizante funcione muy bien en suelo arenoso, pero no tenga ningún efecto (o incluso sea perjudicial) en suelo arcilloso. En este caso, hay una interacción: el efecto del fertilizante depende del tipo de suelo.

**Descomposición de la Suma de Cuadrados Total (SCT) en un Diseño Factorial de Dos Factores (A y B):**
La variabilidad total en los datos se descompone en componentes atribuibles a cada factor principal, a su interacción, y al error aleatorio.

$$ SCT = SCA + SCB + SCAB + SCE $$

*   **SCA (Suma de Cuadrados del Factor A):** Mide la variabilidad en la variable de respuesta que es atribuible al efecto principal del Factor A (promediando sobre los niveles del Factor B).
*   **SCB (Suma de Cuadrados del Factor B):** Mide la variabilidad en la variable de respuesta que es atribuible al efecto principal del Factor B (promediando sobre los niveles del Factor A).
*   **SCAB (Suma de Cuadrados de la Interacción AB):** Mide la variabilidad que no puede ser explicada por los efectos principales de A y B por sí solos. Es la variabilidad adicional que surge de la combinación específica de los niveles de A y B.
*   **SCE (Suma de Cuadrados del Error):** Mide la variabilidad aleatoria o no explicada dentro de cada combinación de tratamiento (celda).

**Interpretación de la Significancia de la Interacción:**
Para evaluar la significancia de la interacción, se calcula un estadístico F para la interacción (F_AB) que compara el Cuadrado Medio de la Interacción (CMAB) con el Cuadrado Medio del Error (CME).

*   **Si la interacción (F_AB) es significativa (p-valor < $\alpha$):** Esto es el resultado más importante. Significa que el efecto de un factor no es constante a través de los niveles del otro. En este caso, la interpretación de los efectos principales por separado puede ser engañosa o incluso incorrecta. La historia principal es la interacción.
*   **Si la interacción (F_AB) NO es significativa (p-valor $\ge \alpha$):** Significa que no hay evidencia de que los factores interactúen. En este caso, podemos proceder a interpretar los efectos principales de forma independiente, ya que el efecto de un factor es consistente a través de los niveles del otro.

**¿Por qué es crucial examinar la interacción antes que los efectos principales?**
Es crucial porque la presencia de una interacción significativa invalida o complica la interpretación de los efectos principales. Si hay interacción, el efecto de un factor no puede ser descrito por un único valor promedio (el efecto principal), ya que su impacto cambia dependiendo del nivel del otro factor. Ignorar una interacción significativa puede llevar a conclusiones erróneas y a recomendaciones incorrectas. Por lo tanto, la regla general es: **si la interacción es significativa, se interpreta la interacción y no los efectos principales de forma aislada.**

---

### Sección 2: Defensa Oral

**Pregunta 2.1:** "Has hablado de la interacción. Ahora, ¿cuál es la principal ventaja de un Diseño de Bloques Completos al Azar (DBCA) sobre un Diseño Completamente al Azar (DCA)? ¿Cómo afecta el bloqueo a la potencia de la prueba para los tratamientos?"

**Respuesta Modelo:**
"La principal ventaja de un Diseño de Bloques Completos al Azar (DBCA) sobre un Diseño Completamente al Azar (DCA) es su capacidad para **controlar y remover una fuente conocida de variabilidad externa** (el factor de bloqueo) que podría enmascarar el efecto real de los tratamientos. En un DCA, toda la variabilidad no atribuida al tratamiento se considera error aleatorio.

Al agrupar unidades experimentales homogéneas en bloques y aplicar todos los tratamientos dentro de cada bloque, la variabilidad *entre* los bloques se aísla y se elimina del término de error. Esto significa que la Suma de Cuadrados del Error (SCE) se reduce, lo que a su vez disminuye el Cuadrado Medio del Error (CME). Dado que el CME es el denominador del estadístico F para los tratamientos, un CME más pequeño resulta en un **estadístico F más grande** y, por lo tanto, en un **aumento de la potencia de la prueba** para detectar diferencias significativas entre los tratamientos. En resumen, el bloqueo hace que el experimento sea más preciso y sensible."

**Pregunta 2.2:** "Si un ANOVA resulta significativo, ¿por qué no es suficiente y qué tipo de pruebas se necesitan a continuación? Explica la diferencia entre la tasa de error por comparación y la tasa de error familiar, y cómo las pruebas post-hoc controlan esta última."

**Respuesta Modelo:**
"Si un ANOVA resulta significativo, no es suficiente porque solo nos dice que **al menos una de las medias de los grupos es diferente de las demás**, pero no nos especifica *cuál o cuáles* son esas diferencias. Para identificar los pares específicos de medias que difieren significativamente, se necesitan **pruebas post-hoc** (o de comparaciones múltiples).

La **tasa de error por comparación ($\alpha_{PC}$)** es la probabilidad de cometer un Error de Tipo I en una única comparación (por ejemplo, una prueba t entre dos grupos). La **tasa de error familiar ($\alpha_{FW}$)** es la probabilidad de cometer *al menos un* Error de Tipo I en el conjunto de todas las comparaciones que se realizan en un experimento. Si realizamos muchas comparaciones sin corrección, la $\alpha_{FW}$ se infla rápidamente.

Las pruebas post-hoc están diseñadas específicamente para **controlar la tasa de error familiar ($\alpha_{FW}$)**. Lo hacen ajustando el criterio de significancia para cada comparación individual, de modo que la probabilidad de cometer al menos un falso positivo en todo el conjunto de comparaciones se mantenga en el nivel $\alpha$ deseado (por ejemplo, 0.05)."

**Pregunta 2.3:** "Explica la lógica de la Prueba HSD de Tukey. ¿Por qué es preferible a realizar múltiples pruebas t sin corrección? ¿Cuándo usarías Bonferroni en lugar de Tukey?"

**Respuesta Modelo:**
"La **Prueba HSD (Honest Significant Difference) de Tukey** es una prueba post-hoc que permite comparar todas las posibles parejas de medias de grupos después de un ANOVA significativo, controlando la tasa de error familiar. Su lógica se basa en la distribución del rango estudentizado, que considera el número total de medias que se están comparando.

Es preferible a realizar múltiples pruebas t sin corrección porque las pruebas t individuales no controlan la tasa de error familiar. Si hiciéramos muchas pruebas t, la probabilidad de encontrar falsos positivos aumentaría drásticamente. Tukey, en cambio, ajusta el umbral de significancia para asegurar que la probabilidad de cometer al menos un Error de Tipo I en todas las comparaciones se mantenga en el nivel $\alpha$ deseado.

Usaría la **corrección de Bonferroni** en lugar de Tukey en situaciones específicas:
1.  Cuando solo se van a realizar un **número muy pequeño de comparaciones planificadas** (a priori), no todas las posibles parejas.
2.  Cuando se necesita un método **muy conservador** para controlar el Error de Tipo I, incluso a expensas de la potencia. Bonferroni es muy simple de aplicar (simplemente se divide el $\alpha$ global por el número de comparaciones), pero es más conservador que Tukey, lo que significa que es más difícil encontrar diferencias significativas."

**Pregunta 2.4:** "En un diseño factorial, si la interacción no es significativa, ¿cómo se interpretan los efectos principales? ¿Y si la interacción es significativa, pero uno de los efectos principales no lo es?"

**Respuesta Modelo:**
"*   **Si la interacción NO es significativa:** En este caso, podemos interpretar los **efectos principales** de forma independiente. Esto significa que el efecto de un factor es consistente a través de todos los niveles del otro factor. Por ejemplo, si el Factor A es significativo y la interacción no lo es, podemos decir que el Factor A tiene un efecto general sobre la variable de respuesta, independientemente del nivel del Factor B.

*   **Si la interacción ES significativa, pero uno de los efectos principales NO lo es:** La regla general es que **si la interacción es significativa, se interpreta la interacción y no los efectos principales de forma aislada**. El hecho de que un efecto principal no sea significativo cuando la interacción sí lo es, simplemente significa que el efecto promedio de ese factor (promediando sobre los niveles del otro factor) no es significativo. Sin embargo, esto no descarta que el factor tenga un efecto importante en *algunos* niveles del otro factor, debido a la interacción. La interacción es la historia principal y debe ser el foco de la interpretación, a menudo visualizada con un gráfico de interacción."

---

### Sección 3: Preguntas Rápidas

**Pregunta 3.1 (Opción Múltiple):** En un Diseño de Bloques Completos al Azar, el objetivo principal de los bloques es:

a) Aumentar el número de tratamientos.
**b) Reducir la variabilidad del error experimental.**
c) Simplificar el cálculo del estadístico F.
d) Permitir el estudio de interacciones.

**Justificación:** Los bloques se utilizan para agrupar unidades experimentales homogéneas y así aislar y eliminar una fuente de variabilidad externa, lo que reduce el error experimental y aumenta la precisión de la prueba para los tratamientos.

**Pregunta 3.2 (Respuesta Corta):** ¿Qué es un "efecto principal" en un diseño factorial?

**Respuesta Modelo:** Un **efecto principal** en un diseño factorial es el efecto promedio de un factor sobre la variable de respuesta, promediando sobre todos los niveles de los otros factores. Representa el impacto general de ese factor, independientemente de cómo interactúe con los demás.

**Pregunta 3.3 (Verdadero/Falso):** Las pruebas post-hoc deben realizarse siempre, incluso si el ANOVA no es significativo. ¿Verdadero o Falso? Justifica.

**Respuesta Modelo:** **Falso.** Las pruebas post-hoc **solo deben realizarse si el resultado general del ANOVA es significativo** para el factor en cuestión. Si el ANOVA no es significativo, significa que no hay evidencia de diferencias entre las medias de los grupos, y realizar comparaciones post-hoc sería una 'pesca de significancia' (fishing for significance), aumentando la probabilidad de encontrar falsos positivos por azar.

**Pregunta 3.4 (Respuesta Corta):** ¿Qué es un "contraste" en el contexto de ANOVA y en qué se diferencia de una prueba post-hoc?

**Respuesta Modelo:** Un **contraste** es una comparación específica entre las medias de los grupos que se planifica *a priori* (antes de realizar el experimento) y se basa en una hipótesis teórica. Se diferencia de una prueba post-hoc en que los contrastes son comparaciones planificadas y dirigidas, mientras que las pruebas post-hoc son exploratorias y se realizan *a posteriori* (después de un ANOVA significativo) para encontrar dónde residen las diferencias.
