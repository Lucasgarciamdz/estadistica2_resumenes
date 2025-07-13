# Unidad 2: Preguntas y Guía de Estudio

Esta sección es para solidificar la comprensión práctica de las pruebas de hipótesis. El objetivo es que puedas elegir la prueba correcta, ejecutarla e interpretar los resultados de manera infalible.

---

### Preguntas Teóricas de Autoevaluación

1.  **Z vs. t:** Estás a punto de realizar una prueba de hipótesis para la media. ¿Cuál es la **única** pregunta que debes hacerte para decidir si usar una prueba Z o una prueba t? ¿Qué supuesto adicional requiere la prueba t, especialmente con muestras pequeñas?

2.  **Errores en Contexto:** Un investigador médico está probando un nuevo fármaco. La hipótesis nula es que el fármaco no tiene efecto. En este contexto, ¿qué es un Error de Tipo I y qué es un Error de Tipo II? ¿Cuáles son las consecuencias prácticas de cada uno? ¿Cuál de los dos errores crees que es más grave en este escenario y por qué?

3.  **El p-valor Malinterpretado:** Un colega te dice: "Obtuve un p-valor de 0.04, así que hay solo un 4% de probabilidad de que mi conclusión sea incorrecta". ¿Es correcta esta interpretación? Si no, ¿cómo le explicarías el significado real del p-valor de una forma sencilla?

4.  **Potencia de la Prueba:** Quieres diseñar un experimento para probar que una nueva aleación de metal es más resistente que la antigua. El presupuesto es limitado. ¿Qué tres factores podrías ajustar para aumentar la potencia de tu prueba y así tener más posibilidades de detectar una mejora si realmente existe?

5.  **Significancia Estadística vs. Importancia Práctica:** En un estudio con una muestra muy grande (n=1,000,000), se encuentra que un programa de entrenamiento aumenta el CI de los participantes en un promedio de 0.05 puntos, con un p-valor de 0.0001. ¿Es el resultado estadísticamente significativo? ¿Es prácticamente importante? ¿Qué nos enseña este ejemplo sobre la interpretación de los resultados?

6.  **Hipótesis Nula:** ¿Por qué la hipótesis nula siempre contiene el signo de igualdad? ¿Qué pasaría si intentáramos formular una hipótesis nula como $H_0: \mu \neq 50$?

---

### Guía de Estudio y Puntos Clave

*   **El Mapa de Decisiones:** Tu primera tarea mental ante un problema es elegir la herramienta correcta. Hazte un diagrama de flujo:
    *   ¿Qué parámetro estoy probando? (Media, Proporción, Varianza)
    *   ¿Cuántas poblaciones/muestras? (Una o dos)
    *   Si es Media, ¿conozco $\sigma$? (Sí -> Z, No -> t)
    *   Si son dos muestras, ¿son independientes o pareadas? (Afecta la fórmula del error estándar).

*   **El Mantra de los 5 Pasos:** Para cada ejercicio, escribe explícitamente los 5 pasos. Es una forma segura de no olvidar nada.
    1.  $H_0$ y $H_1$.
    2.  Nivel de significancia $\alpha$.
    3.  Calcular el estadístico de prueba (fórmula correcta).
    4.  Regla de decisión (comparar con valor crítico o p-valor con $\alpha$).
    5.  Conclusión en el contexto del problema.

*   **p-valor es tu mejor amigo:** En la práctica, la mayoría del software estadístico te dará un p-valor. La regla es simple y universal: **Si el p-valor es bajo, la nula se va (se rechaza)**. (Si p < $\alpha$, rechazo $H_0$).

*   **Cuidado con las colas:** Presta mucha atención a la redacción del problema para definir $H_1$. 
    *   "¿Es la media **diferente** de 50?" -> $H_1: \mu \neq 50$ (Bilateral)
    *   "¿Ha **aumentado** la media?" -> $H_1: \mu > 50$ (Unilateral derecha)
    *   "¿Es la media **menor** de 50?" -> $H_1: \mu < 50$ (Unilateral izquierda)
    Esto afecta a cómo buscas el valor crítico o calculas el p-valor.

*   **Supuestos, Supuestos, Supuestos:** No olvides los supuestos detrás de cada prueba. Para las pruebas t, el más importante es que la **población subyacente sea normal**. Si la muestra es grande ($n > 30$), el TCL nos relaja este supuesto. Pero para muestras pequeñas, es una condición crítica. Esto será el puente hacia las pruebas no paramétricas de la Unidad 4.

