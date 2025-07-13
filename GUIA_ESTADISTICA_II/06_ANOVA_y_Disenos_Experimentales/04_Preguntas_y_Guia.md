# Unidad 6: Preguntas y Guía de Estudio

Esta sección final se enfoca en la aplicación práctica y la interpretación de los diseños de ANOVA avanzados. El dominio de estos conceptos te permitirá diseñar experimentos robustos y extraer conclusiones válidas y detalladas.

---

### Preguntas Teóricas de Autoevaluación

1.  **Bloquear o no Bloquear:** Estás diseñando un experimento para probar 3 tipos de dietas en ratones. Tienes ratones de diferentes edades (jóvenes, adultos, viejos). ¿Por qué sería una buena idea usar la "edad" como un factor de bloqueo? ¿Qué ganas al hacerlo en términos de potencia estadística?

2.  **La Interacción es Clave:** En un diseño factorial 2x2 (Factor A, Factor B), el análisis de ANOVA muestra que el efecto de interacción AB es altamente significativo (p < 0.001), pero los efectos principales de A y B no son significativos (p > 0.3). ¿Cómo interpretas este resultado? ¿Sería correcto concluir que los factores A y B no son importantes?

3.  **Gráfico de Interacción:** Dibuja un gráfico de interacción que represente:
    a) Un caso con dos efectos principales fuertes pero sin interacción.
    b) Un caso con una fuerte interacción pero sin efectos principales claros.

4.  **ANOVA vs. Post-Hoc:** ¿Cuál es la diferencia fundamental en la pregunta que responden la prueba F de un ANOVA y una prueba post-hoc como la de Tukey?

5.  **El Dilema Post-Hoc:** Un investigador realiza un ANOVA con 6 grupos y obtiene un resultado no significativo (p = 0.25). Decepcionado, decide de todas formas realizar comparaciones de pares con la prueba de Tukey y encuentra que la diferencia entre el Grupo 2 y el Grupo 5 es "casi" significativa (p = 0.06). Te pide tu opinión. ¿Qué le dirías? ¿Es válido su procedimiento?

6.  **Modelo Matemático:** Escribe y explica los componentes del modelo matemático para un Diseño de Bloques Completos al Azar. ¿Qué término del modelo representa la variabilidad que estás tratando de eliminar?

---

### Guía de Estudio y Puntos Clave

*   **El Flujo de Trabajo del Diseño Experimental:**
    1.  **Identifica tu objetivo:** ¿Qué quieres comparar? (Tratamientos).
    2.  **Identifica fuentes de variabilidad:** ¿Hay alguna variable de molestia que puedas controlar? (Factor de Bloqueo). ¿Quieres estudiar múltiples factores a la vez? (Diseño Factorial).
    3.  **Elige el diseño correcto:** DCA, DBCA, Factorial.
    4.  **Realiza el ANOVA** y examina la tabla.

*   **Interpretación en Diseños Factoriales (¡MUY IMPORTANTE!):**
    *   **Paso 1: Mira la interacción PRIMERO.**
        *   **Si la interacción ES significativa:** ¡Detente! No interpretes los efectos principales de forma aislada. La interacción es la historia principal. Describe cómo el efecto de un factor cambia según el nivel del otro. Usa el gráfico de interacción para explicarlo.
        *   **Si la interacción NO es significativa:** Puedes proceder a interpretar los efectos principales. Si el efecto principal del Factor A es significativo, puedes decir que, en general, el Factor A tiene un efecto sobre la respuesta.

*   **El Poder del Bloqueo:** Recuerda siempre que el objetivo de un diseño de bloques es **reducir el Cuadrado Medio del Error (CME)**. Al hacerlo, el denominador de tu estadístico F para los tratamientos se hace más pequeño, lo que aumenta el valor de F y, por lo tanto, la potencia de la prueba. El bloqueo es una de las herramientas más importantes para mejorar la precisión de un experimento.

*   **Cuándo usar Pruebas Post-Hoc:**
    *   **SOLO úsalas si el resultado general del ANOVA para ese factor es significativo.** Si la prueba F te dice que no hay diferencia entre las medias, no tiene sentido ir a buscar diferencias entre pares. Hacerlo se conoce como "ir de pesca" (fishing for significance) y es una mala práctica estadística.
    *   **Tukey HSD es tu opción por defecto** para comparaciones de todos los pares en un ANOVA de un factor. Es el estándar de la industria.

*   **Revisa los supuestos:** Los supuestos de ANOVA (Normalidad, Homocedasticidad, Independencia) siguen siendo válidos y cruciales en estos diseños más complejos. La homocedasticidad (igualdad de varianzas entre todas las celdas/grupos) sigue siendo el más importante.
