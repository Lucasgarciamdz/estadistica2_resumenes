# Unidad 4: Preguntas y Guía de Estudio

Esta es una de las unidades más importantes. El objetivo aquí es que puedas decidir con confianza cuándo abandonar una prueba paramétrica y cuál es la alternativa no paramétrica correcta para cada situación.

---

### Preguntas Teóricas de Autoevaluación

1.  **La Decisión Clave:** Estás analizando un conjunto de datos de una muestra pequeña (n=15). Un gráfico Q-Q plot muestra una clara curvatura que se aleja de la línea de normalidad. ¿Qué te indica esto y qué tipo de prueba deberías usar para analizar la tendencia central de los datos? ¿Por qué?

2.  **Pérdida de Información:** Al convertir tus datos a rangos, ¿qué información se pierde y qué se gana? Explica el "trade-off".

3.  **Signos vs. Wilcoxon:** Tienes datos de un experimento "antes y después" (muestras pareadas). Tienes dos pruebas a tu disposición: la Prueba de los Signos y la Prueba de Rangos con Signo de Wilcoxon. ¿Cuál es la diferencia fundamental entre ellas? ¿Qué prueba es generalmente más potente y por qué? ¿Bajo qué supuesto adicional funciona la prueba de Wilcoxon?

4.  **ANOVA en Rangos:** Explica con tus propias palabras por qué se dice que la prueba de Kruskal-Wallis es como "un ANOVA sobre los rangos". ¿Cuál es el análogo paramétrico directo de la prueba de Kruskal-Wallis?

5.  **Aleatoriedad:** ¿Qué significa que una secuencia sea "aleatoria"? Describe un escenario del mundo real donde querrías usar la Prueba de Rachas para verificar la aleatoriedad.

6.  **Empates (Ties):** ¿Cómo se manejan los empates (observaciones con el mismo valor) al asignar rangos en las pruebas de Wilcoxon o Mann-Whitney? ¿Qué efecto tienen los empates en la prueba?

---

### Guía de Estudio y Puntos Clave

*   **El Cuadro de Mando No Paramétrico:** La decisión más importante es elegir la prueba correcta. Ten este cuadro siempre en mente.

| **Objetivo de la Prueba**                               | **Análogo Paramétrico**                | **Alternativa No Paramétrica**                               |
| :------------------------------------------------------ | :------------------------------------- | :----------------------------------------------------------- |
| Comparar la tendencia central de **1 grupo** con un valor | Prueba t (1 muestra)                   | **Prueba de los Signos** o **Prueba de Wilcoxon** (más potente) |
| Comparar **2 grupos PAREADOS** (antes/después)          | Prueba t (muestras pareadas)           | **Prueba de los Signos** o **Prueba de Wilcoxon** (más potente) |
| Comparar **2 grupos INDEPENDIENTES**                    | Prueba t (muestras indep.)             | **Prueba U de Mann-Whitney** (o Suma de Rangos de Wilcoxon)    |
| Comparar **3 o más grupos INDEPENDIENTES**              | ANOVA de 1 Factor                      | **Prueba H de Kruskal-Wallis**                               |
| Probar la **aleatoriedad** de una secuencia             | (No hay)                               | **Prueba de Rachas**                                         |

*   **El Flujo de Trabajo:**
    1.  **Verifica los supuestos de la prueba paramétrica.** Principalmente, la **normalidad**. Usa un test como Shapiro-Wilk o un gráfico Q-Q.
    2.  **Si no se cumple la normalidad (o tienes datos ordinales), elige la alternativa no paramétrica correcta** según el cuadro anterior.
    3.  **Plantea las hipótesis.** Recuerda que las pruebas no paramétricas a menudo se plantean en términos de la **mediana ($\eta$)** en lugar de la media ($\mu$).
        *   $H_0$: Las medianas son iguales / La mediana es igual a $\eta_0$.
        *   $H_1$: Las medianas no son iguales / La mediana es diferente de $\eta_0$.
    4.  **Calcula el estadístico de prueba** (W, U, H, etc.) siguiendo los pasos de ordenamiento y asignación de rangos.
    5.  **Compara el estadístico con el valor crítico de su tabla** (para muestras pequeñas) o **calcula el p-valor usando la aproximación a la normal o Chi-Cuadrado** (para muestras grandes).
    6.  **Concluye en el contexto del problema.**

*   **No tires la toalla con las pruebas paramétricas demasiado rápido.** Si tu tamaño de muestra es grande ($n > 30$ o 40), el Teorema Central del Límite a menudo "salva" el supuesto de normalidad para las pruebas sobre medias (como la prueba t). Las pruebas no paramétricas son más cruciales para muestras pequeñas donde la normalidad no se puede garantizar.

*   **Potencia:** Recuerda siempre que si los datos *sí* son normales, la prueba t o el ANOVA serán más potentes. Al usar una prueba no paramétrica, estás sacrificando algo de potencia para ganar robustez frente a la falta de normalidad. Es un compromiso necesario.
