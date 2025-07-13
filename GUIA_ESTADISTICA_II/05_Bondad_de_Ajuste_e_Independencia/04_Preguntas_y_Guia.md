# Unidad 5: Preguntas y Guía de Estudio

El dominio de esta unidad reside en saber distinguir claramente entre los dos tipos de prueba de Chi-Cuadrado y en aplicar correctamente las fórmulas para las frecuencias esperadas y los grados de libertad en cada caso.

---

### Preguntas Teóricas de Autoevaluación

1.  **La Pregunta Clave:** ¿Cuál es la diferencia fundamental en la pregunta que intentan responder la prueba de **bondad de ajuste** y la prueba de **independencia**? Describe un ejemplo para cada una.

2.  **Frecuencias Esperadas:** Explica con tus propias palabras cómo se calcula la frecuencia esperada ($F_e$) en:
    a) Una prueba de bondad de ajuste para un dado de 6 caras que se sospecha está cargado.
    b) Una prueba de independencia para analizar la relación entre el género (hombre/mujer) y ser fumador (sí/no).

3.  **Grados de Libertad:** ¿Por qué la fórmula para los grados de libertad es diferente en ambas pruebas? Explica la lógica detrás de $k-1-m$ y $(r-1)(c-1)$.

4.  **La Regla del 5:** Un investigador realiza una prueba de independencia en una tabla de contingencia de 3x4. Al calcular las frecuencias esperadas, nota que dos de las 12 celdas tienen una $F_e$ de 3.5. ¿Qué problema representa esto y qué debería considerar hacer el investigador?

5.  **Interpretación del Rechazo:**
    a) Si rechazas $H_0$ en una prueba de bondad de ajuste, ¿qué concluyes?
    b) Si rechazas $H_0$ en una prueba de independencia, ¿qué concluyes? ¿Qué puedes examinar a continuación para entender mejor la relación?

6.  **Naturaleza de los Datos:** ¿Para qué tipo de datos (nominales, ordinales, de intervalo, de razón) son apropiadas las pruebas de Chi-Cuadrado? ¿Por qué no usarías una prueba $\chi^2$ para comparar las medias de dos grupos?

---

### Guía de Estudio y Puntos Clave

*   **El Mapa de Decisión Chi-Cuadrado:**
    *   ¿Estoy analizando **UNA** variable categórica para ver si se ajusta a un patrón? -> **Prueba de Bondad de Ajuste**.
    *   ¿Estoy analizando la relación entre **DOS** variables categóricas? -> **Prueba de Independencia**.

*   **El Mantra del $\chi^2$:**
    1.  **Plantea las hipótesis.** ($H_0$: Se ajusta al modelo / $H_0$: Son independientes).
    2.  **Organiza los datos.** (Una lista para bondad de ajuste, una tabla de contingencia para independencia).
    3.  **Calcula las Frecuencias Esperadas ($F_e$)** usando la fórmula correcta para tu tipo de prueba.
    4.  **Verifica la regla del 5.** Todas las $F_e$ deben ser $\ge 5$. Si no, la prueba no es fiable.
    5.  **Calcula el estadístico $\chi^2$:** $\sum \frac{(F_o - F_e)^2}{F_e}$.
    6.  **Calcula los grados de libertad ($gl$)** usando la fórmula correcta para tu tipo de prueba.
    7.  **Busca el valor crítico** en la tabla de $\chi^2$ con tu $\alpha$ y $gl$, o calcula el p-valor.
    8.  **Concluye.** Si $\chi^2_{obs} > \chi^2_{crit}$ (o si $p-valor < \alpha$), rechaza $H_0$.

*   **El Análisis Post-Rechazo (para Independencia):** Si rechazas la hipótesis de independencia, significa que hay una asociación. ¡Pero la prueba no te dice dónde está esa asociación! Para entenderla, debes volver a la tabla y examinar los **residuos estandarizados** de cada celda:
    $$ \text{Residuo}_{ij} = \frac{F_{o,ij} - F_{e,ij}}{\sqrt{F_{e,ij}}} $$
    Celdas con residuos grandes (típicamente > 2 o < -2) son las que más contribuyen a la significancia del $\chi^2$. Un residuo grande y positivo significa que en esa celda hay muchas más observaciones de las que se esperarían por azar. Uno grande y negativo, muchas menos. Esto te permite describir la naturaleza de la relación.

*   **Bondad de Ajuste vs. Kruskal-Wallis:** No confundas las pruebas. Kruskal-Wallis (Unidad 4) también usa la distribución $\chi^2$ para muestras grandes, pero compara la **mediana** de una variable **continua** entre varios grupos. La prueba de bondad de ajuste de $\chi^2$ analiza la distribución de frecuencias de **una única variable categórica**.
