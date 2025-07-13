# Errores Comunes y Preguntas Trampa en Estadística Aplicada II

En un examen oral, los examinadores a menudo buscan no solo lo que sabes, sino cómo manejas la ambigüedad y si comprendes los matices conceptuales. Aquí se detallan errores frecuentes y preguntas "trampa" que suelen aparecer.

---

## Errores Conceptuales Comunes

1.  **Confundir Parámetro con Estimador:**
    *   **Error:** Usar $\mu$ cuando se refiere a $\bar{X}$, o $\sigma^2$ cuando se refiere a $S^2$.
    *   **Clarificación:** Parámetro es de la **población** (fijo, desconocido), estimador es de la **muestra** (variable aleatoria, conocido para una muestra específica).

2.  **Malinterpretar el p-valor:**
    *   **Error:** "El p-valor es la probabilidad de que la hipótesis nula sea verdadera" o "El p-valor es la probabilidad de que mi conclusión sea incorrecta".
    *   **Clarificación:** El p-valor es la probabilidad de observar los datos (o datos más extremos) **si la hipótesis nula fuera verdadera**. No es la probabilidad de $H_0$ ni la probabilidad de error en tu decisión.

3.  **Confundir Significancia Estadística con Significancia Práctica:**
    *   **Error:** Asumir que un resultado estadísticamente significativo es automáticamente importante o relevante en el mundo real.
    *   **Clarificación:** Con muestras muy grandes, incluso diferencias triviales pueden ser estadísticamente significativas. La significancia práctica se evalúa por el tamaño del efecto y el contexto del problema.

4.  **Ignorar los Supuestos de las Pruebas:**
    *   **Error:** Aplicar una prueba paramétrica (t-test, ANOVA) sin verificar la normalidad o la homocedasticidad, o usar una prueba Chi-Cuadrado con frecuencias esperadas bajas.
    *   **Clarificación:** Los supuestos son la base de la validez de la prueba. Si no se cumplen, los resultados pueden ser engañosos. Siempre menciónalos y cómo los verificarías.

5.  **Realizar Múltiples Pruebas t sin Corrección:**
    *   **Error:** Comparar múltiples grupos con pruebas t individuales sin ajustar el nivel de significancia.
    *   **Clarificación:** Esto infla la tasa de error de Tipo I. Usa ANOVA y luego pruebas post-hoc (como Tukey) para controlar el error familiar.

6.  **Interpretar Efectos Principales cuando la Interacción es Significativa (ANOVA Factorial):**
    *   **Error:** Concluir sobre el efecto de un factor sin considerar cómo su efecto cambia con los niveles de otro factor.
    *   **Clarificación:** Si la interacción es significativa, la interpretación debe centrarse en la interacción. Los efectos principales aislados pueden no tener sentido.

7.  **Confundir la Prueba de los Signos con la de Wilcoxon:**
    *   **Error:** Usarlas indistintamente o no saber cuándo una es más potente que la otra.
    *   **Clarificación:** Wilcoxon (rangos con signo) es más potente que la Prueba de los Signos porque incorpora la magnitud de las diferencias, no solo su dirección.

8.  **Confundir Mann-Whitney con Wilcoxon (Rangos con Signo):**
    *   **Error:** Usar Mann-Whitney para muestras pareadas o Wilcoxon para muestras independientes.
    *   **Clarificación:** Mann-Whitney es para **muestras independientes**. Wilcoxon (rangos con signo) es para **muestras pareadas** o una sola muestra.

9.  **Errores en los Grados de Libertad:**
    *   **Error:** Calcular incorrectamente los grados de libertad para Chi-Cuadrado o ANOVA.
    *   **Clarificación:** Los grados de libertad son cruciales para encontrar el valor crítico y el p-valor correcto. Entiende su lógica (número de valores libres de variar).

10. **Malinterpretar la Propiedad de Markov:**
    *   **Error:** Pensar que el estado futuro es completamente independiente del pasado, o que el pasado no tiene ninguna influencia.
    *   **Clarificación:** La Propiedad de Markov dice que el futuro depende *solo* del presente, no del *camino* que se tomó para llegar al presente. El pasado influye en el presente, y el presente influye en el futuro.

---

## Preguntas Trampa Comunes

Estas preguntas están diseñadas para ver si realmente entiendes los conceptos o si solo los has memorizado.

1.  **"¿Por qué dividimos por $n-1$ en la varianza muestral? Explícalo sin usar fórmulas."**
    *   **Trampa:** Busca tu comprensión conceptual de los grados de libertad y el sesgo.
    *   **Respuesta Clave:** La media muestral ya 'consume' un grado de libertad, haciendo que las desviaciones sean menos variables de lo que realmente son respecto a la media poblacional. Dividir por $n-1$ corrige esta subestimación.

2.  **"Si tu p-valor es 0.06 y tu $\alpha$ es 0.05, ¿qué haces? ¿Y si tu jefe te pide que lo hagas significativo?"**
    *   **Trampa:** Evalúa tu ética estadística y tu comprensión de la regla de decisión.
    *   **Respuesta Clave:** No se rechaza $H_0$. Bajo ninguna circunstancia se debe cambiar $\alpha$ *después* de ver los resultados. Se debe reportar el resultado tal cual y quizás sugerir un aumento del tamaño de la muestra para futuros estudios.

3.  **"¿Qué es más importante: significancia estadística o significancia práctica?"**
    *   **Trampa:** Busca tu capacidad de contextualizar los resultados.
    *   **Respuesta Clave:** Ambos son importantes, pero la significancia práctica es a menudo más relevante para la toma de decisiones. Un resultado puede ser estadísticamente significativo pero trivial en la práctica, o viceversa.

4.  **"Si el ANOVA es significativo, ¿significa que todos los grupos son diferentes entre sí?"**
    *   **Trampa:** Evalúa tu comprensión de la naturaleza 'omnibus' del ANOVA.
    *   **Respuesta Clave:** No, solo que *al menos uno* es diferente. Necesitas pruebas post-hoc para identificar cuáles.

5.  **"¿Cuándo usarías una prueba no paramétrica si tu muestra es muy grande (n=1000)?"**
    *   **Trampa:** Evalúa tu comprensión del TCL y los supuestos.
    *   **Respuesta Clave:** Aunque el TCL ayuda con la normalidad en muestras grandes, aún usarías una no paramétrica si los datos son **ordinales** o si hay **outliers extremos** que distorsionan la media y la varianza, o si la distribución es extremadamente no normal y el TCL no es suficiente.

6.  **"¿Qué pasa si una celda en tu tabla Chi-Cuadrado tiene una frecuencia esperada de cero?"**
    *   **Trampa:** Evalúa tu conocimiento de las condiciones de validez.
    *   **Respuesta Clave:** La fórmula del Chi-Cuadrado implica dividir por $F_e$, por lo que un $F_e=0$ haría la fórmula indefinida. Esto indica un problema grave con el modelo o los datos, y la prueba no sería válida. Se necesitaría agrupar categorías o usar una prueba exacta.

7.  **"Si la interacción en un ANOVA factorial no es significativa, ¿qué haces con los efectos principales?"**
    *   **Trampa:** Evalúa tu comprensión de la jerarquía de interpretación en diseños factoriales.
    *   **Respuesta Clave:** Si la interacción no es significativa, entonces se procede a interpretar los efectos principales de forma independiente, ya que el efecto de un factor es consistente a través de los niveles del otro.

8.  **"¿Es la Cadena de Markov un modelo perfecto para predecir el mercado de valores?"**
    *   **Trampa:** Evalúa tu pensamiento crítico sobre las limitaciones de los modelos.
    *   **Respuesta Clave:** Probablemente no. El mercado de valores es un proceso complejo donde el pasado (tendencias, noticias, eventos económicos) a menudo influye en el futuro de formas que van más allá del estado actual. La propiedad de carencia de memoria de Markov sería una simplificación excesiva.

Al estudiar estos errores y preguntas trampa, no solo memorizarás las respuestas, sino que desarrollarás una comprensión más profunda y matizada de la estadística, lo que te permitirá responder con confianza y precisión en cualquier escenario de examen oral.