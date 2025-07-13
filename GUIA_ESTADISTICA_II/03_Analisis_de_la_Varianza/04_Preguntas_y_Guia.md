# Unidad 3: Preguntas y Guía de Estudio

El objetivo de esta sección es asegurar que puedes interpretar una salida de ANOVA y que comprendes profundamente los supuestos que deben cumplirse para que la prueba sea válida.

---

### Preguntas Teóricas de Autoevaluación

1.  **El Nombre Engañoso:** Si ANOVA significa "Análisis de la Varianza", ¿por qué la usamos para probar hipótesis sobre las medias? Explica la lógica.

2.  **El Problema de las Múltiples Pruebas:** Un investigador quiere comparar 4 grupos y te dice: "Simplemente haré 6 pruebas t. Es más fácil de entender". ¿Cuál es el principal argumento estadístico que usarías para convencerlo de que use ANOVA en su lugar?

3.  **Interpretando el Estadístico F:** ¿Qué representa conceptualmente el cociente F? Si en un análisis obtienes un F = 0.85, ¿qué te dice eso sobre la relación entre la variabilidad entre grupos y la variabilidad dentro de los grupos? ¿Esperarías rechazar la hipótesis nula con ese valor?

4.  **Los Supuestos Clave:** Enumera los tres supuestos de ANOVA. ¿Cuál de ellos consideras el más crítico? ¿Qué prueba podrías usar para verificarlo? (Pista: piensa en pruebas de la Unidad 2).

5.  **Después de ANOVA:** Supongamos que realizas un ANOVA para 5 grupos y obtienes un p-valor de 0.01. Rechazas la hipótesis nula. ¿Qué has concluido exactamente? ¿Qué pregunta importante queda sin responder y qué tipo de análisis harías a continuación?

6.  **La Tabla ANOVA:** Te presentan una tabla ANOVA incompleta. Si te dan la Suma de Cuadrados del Tratamiento (SCTr) y la Suma de Cuadrados Total (SCT), ¿cómo calcularías la Suma de Cuadrados del Error (SCE)? Si te dan los Cuadrados Medios (CMTr y CME), ¿cómo calcularías el estadístico F?

---

### Guía de Estudio y Puntos Clave

*   **La Tabla ANOVA es tu Hoja de Ruta:** Debes ser capaz de mirar una tabla ANOVA y entender cada número. 
    *   **Fuentes de Variación:** Entre Grupos (Tratamiento), Dentro de Grupos (Error), Total.
    *   **Sumas de Cuadrados (SC):** Miden la variabilidad. Recuerda que $SCT = SCTr + SCE$.
    *   **Grados de Libertad (gl):** $k-1$ para el tratamiento, $N-k$ para el error, $N-1$ para el total. También son aditivos.
    *   **Cuadrados Medios (CM):** Son las varianzas. $CM = SC / gl$.
    *   **Estadístico F:** Es el cociente de los cuadrados medios, $F = CMTr / CME$.
    *   **p-valor:** Te dice si el F es significativo.

*   **El Flujo de Trabajo de ANOVA:**
    1.  **Verificar Supuestos:** Antes de confiar en los resultados, debes verificar (al menos conceptualmente) los supuestos. El más importante es la **homocedasticidad** (igualdad de varianzas). Puedes usar una **Prueba F** o, más comúnmente, la **Prueba de Levene** para comparar las varianzas de los grupos. La normalidad se puede verificar con gráficos (Q-Q plots) o pruebas como Shapiro-Wilk.
    2.  **Realizar la Prueba F:** Si los supuestos se mantienen, realizas el ANOVA y miras el p-valor.
    3.  **Interpretar el Resultado:**
        *   Si $p-valor \ge \alpha$: No rechazas $H_0$. Concluyes que no hay evidencia de una diferencia entre las medias de los grupos.
        *   Si $p-valor < \alpha$: Rechazas $H_0$. Concluyes que **al menos un grupo tiene una media diferente**. 

*   **El Paso Post-Hoc:** ¡Rechazar $H_0$ no es el final! Es el principio. Si encuentras una diferencia significativa, el siguiente paso es averiguar **qué grupos son diferentes entre sí**. Esto se hace con **pruebas post-hoc** o de **comparaciones múltiples** (como la prueba de Tukey, Bonferroni, etc.), que se verán en detalle más adelante (Unidad 6).

*   **Conexión con la Regresión:** ANOVA es en realidad un caso especial del modelo lineal general (regresión). El "factor" categórico puede ser representado por variables dummy en un modelo de regresión. Entender esto te dará una visión mucho más profunda de la estadística.
