# Unidad 2: Conceptos Clave

Dominar el vocabulario de las pruebas de hipótesis es fundamental. Cada término tiene un significado preciso que es crucial para aplicar y comunicar los resultados correctamente.

---

*   **Hipótesis Nula ($H_0$):** Es la afirmación sobre un parámetro poblacional que se somete a prueba. Generalmente representa el *status quo*, la ausencia de un efecto o una diferencia. Siempre contiene un signo de igualdad (e.g., $\mu = 50$, $p \ge 0.4$). Se asume verdadera hasta que la evidencia muestral sugiera lo contrario.

*   **Hipótesis Alternativa ($H_1$ o $H_a$):** Es la afirmación que se aceptará si se rechaza la hipótesis nula. Representa la conclusión que el investigador intenta demostrar. Nunca contiene un signo de igualdad (e.g., $\mu \neq 50$, $p < 0.4$).

*   **Prueba Unilateral (o de una cola):** Una prueba en la que la hipótesis alternativa especifica una dirección (e.g., $H_1: \mu > 50$ o $H_1: \mu < 50$). La región de rechazo se encuentra en una sola de las colas de la distribución del estadístico de prueba.

*   **Prueba Bilateral (o de dos colas):** Una prueba en la que la hipótesis alternativa no especifica una dirección (e.g., $H_1: \mu \neq 50$). La región de rechazo se divide en dos partes, una en cada cola de la distribución.

*   **Nivel de Significancia ($\alpha$):** La probabilidad máxima, fijada por el investigador, de cometer un Error de Tipo I. Es el umbral para decidir si el p-valor es suficientemente pequeño como para rechazar $H_0$. Típicamente $\alpha = 0.05$ o $\alpha = 0.01$.

*   **Error de Tipo I:** Ocurre si se **rechaza la hipótesis nula ($H_0$) cuando esta es verdadera**. La probabilidad de cometer este error es $\alpha$. Es el error de "falso positivo" (concluir que hay un efecto cuando no lo hay).

*   **Error de Tipo II:** Ocurre si **no se rechaza la hipótesis nula ($H_0$) cuando esta es falsa**. La probabilidad de cometer este error se denota por $\beta$. Es el error de "falso negativo" (no detectar un efecto que sí existe).

*   **Potencia de la Prueba ($1 - \beta$):** Es la probabilidad de **rechazar correctamente la hipótesis nula cuando esta es falsa**. Es la capacidad de la prueba para detectar un efecto real. Una prueba potente es aquella con una alta probabilidad de llevar a la conclusión correcta.

*   **Estadístico de Prueba:** Un valor calculado a partir de los datos de la muestra que se utiliza para decidir si se rechaza o no la hipótesis nula. Mide la diferencia entre el valor observado en la muestra y el valor esperado bajo la hipótesis nula, en unidades de error estándar.

*   **Valor Crítico:** El punto de corte en la distribución del estadístico de prueba que define la región de rechazo. Si el estadístico de prueba es más extremo que el valor crítico, se rechaza $H_0$. Se obtiene de las tablas de distribución (Z, t, $\chi^2$, F) para un $\alpha$ dado.

*   **Región de Rechazo (o Región Crítica):** El conjunto de valores del estadístico de prueba que llevan al rechazo de la hipótesis nula. Su área total es igual a $\alpha$.

*   **p-valor (o valor p):** La probabilidad de obtener un resultado muestral al menos tan extremo como el que se observó, suponiendo que la hipótesis nula es verdadera. Es el nivel de significancia más pequeño al que se podría rechazar $H_0$ para los datos observados.
    *   **Regla de decisión:** Si $p-valor \le \alpha$, se rechaza $H_0$.
    *   **Interpretación:** Un p-valor pequeño indica que los datos observados son muy improbables si $H_0$ fuera cierta, lo que proporciona fuerte evidencia en contra de $H_0$.

*   **Prueba Z:** Una prueba de hipótesis que utiliza el estadístico Z y la distribución normal estándar. Se usa típicamente para pruebas sobre medias cuando la varianza poblacional ($\sigma^2$) es conocida, o para pruebas sobre proporciones con muestras grandes.

*   **Prueba t (o t de Student):** Una prueba de hipótesis que utiliza el estadístico t y la distribución t. Se usa para pruebas sobre medias cuando la varianza poblacional ($\sigma^2$) es desconocida y se estima con la varianza muestral ($S^2$). La distribución t tiene en cuenta la incertidumbre adicional de estimar $\sigma^2$.

*   **Prueba de Chi-Cuadrado ($\chi^2$):** Se utiliza para pruebas de hipótesis sobre una única varianza poblacional.

*   **Prueba F:** Se utiliza para pruebas de hipótesis sobre la igualdad de dos varianzas poblacionales. Es la base del Análisis de la Varianza (ANOVA).
