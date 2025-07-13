# Resolución del Examen Teórico: Unidad 4 - Pruebas No Paramétricas

---

### Sección 1: Desarrollo en Pizarrón

**Pregunta 1: Lógica y Procedimiento de la Prueba U de Mann-Whitney**

**Objetivo:** La Prueba U de Mann-Whitney (también conocida como Prueba de la Suma de Rangos de Wilcoxon para dos muestras independientes) se utiliza para probar la hipótesis nula de que dos muestras independientes provienen de la misma población o de poblaciones con la misma mediana (o, más generalmente, la misma distribución). Es el análogo no paramétrico de la prueba t para muestras independientes.

**Lógica de la Prueba:**
La prueba se basa en la idea de que si las dos poblaciones son idénticas, entonces al combinar y ordenar todos los datos de ambas muestras, los rangos de las observaciones de la primera muestra deberían estar mezclados aleatoriamente con los rangos de las observaciones de la segunda muestra. Si los rangos de una muestra tienden a ser sistemáticamente más bajos o más altos que los de la otra, esto sugiere que las poblaciones son diferentes.

**Procedimiento (Pasos):**
1.  **Combinar y Ordenar:** Se combinan todas las observaciones de ambas muestras en un solo conjunto de datos. Luego, se ordenan estas $n_1 + n_2$ observaciones de menor a mayor.
2.  **Asignar Rangos:** Se asigna un rango a cada observación en el conjunto combinado. El valor más pequeño recibe el rango 1, el siguiente el rango 2, y así sucesivamente. Si hay valores empatados, se les asigna el rango promedio de las posiciones que ocuparían.
3.  **Sumar Rangos por Grupo:** Se calcula la suma de los rangos ($R_1$ y $R_2$) para cada una de las dos muestras originales.
4.  **Calcular los Estadísticos U:** Se calculan dos estadísticos U, uno para cada muestra:
    $$ U_1 = n_1 n_2 + \frac{n_1(n_1+1)}{2} - R_1 $$
    $$ U_2 = n_1 n_2 + \frac{n_2(n_2+1)}{2} - R_2 $$
    Alternativamente, se puede calcular $U_2 = n_1 n_2 - U_1$.
5.  **Estadístico de Prueba:** El estadístico de prueba para la prueba de Mann-Whitney es el menor de los dos valores calculados: $U = \min(U_1, U_2)$.
6.  **Decisión:** Se compara el valor de $U$ con un valor crítico de una tabla de Mann-Whitney (para muestras pequeñas) o se utiliza una aproximación a la distribución normal (para muestras grandes) para calcular un p-valor. Un valor de $U$ muy pequeño (o muy grande, dependiendo de la formulación) indica una diferencia significativa entre las poblaciones.

**Interpretación del Estadístico U:**
El estadístico $U_1$ (o $U_2$) representa el número de veces que una observación de la muestra 1 precede a una observación de la muestra 2 en la lista ordenada combinada. Si las poblaciones son idénticas, esperaríamos que los valores de $U_1$ y $U_2$ fueran similares. Un valor de $U$ muy pequeño (cercano a 0) sugiere que los valores de una muestra tienden a ser consistentemente menores que los de la otra, lo que indica una diferencia entre las poblaciones.

**Comparación con la Prueba t para Muestras Independientes:**

| Característica        | Prueba t para Muestras Independientes | Prueba U de Mann-Whitney             |
| :-------------------- | :------------------------------------ | :----------------------------------- |
| **Supuestos**         | 1. Normalidad de las poblaciones.     | 1. Muestras aleatorias independientes. |
|                       | 2. Homocedasticidad (varianzas iguales). | 2. Las distribuciones tienen la misma forma (simetría, dispersión), difiriendo solo en la ubicación (mediana). |
|                       | 3. Muestras aleatorias independientes. |                                      |
| **Parámetro de Interés** | Medias ($\mu_1, \mu_2$)              | Medianas ($\eta_1, \eta_2$) o distribuciones completas |
| **Tipo de Datos**     | Cuantitativos (intervalo/razón)       | Cuantitativos (intervalo/razón) u ordinales |
| **Potencia**          | Más potente si los supuestos se cumplen. | Menos potente que la prueba t si los supuestos de la t se cumplen. Más robusta si no se cumplen. |

**Conclusión:** La prueba de Mann-Whitney es una alternativa robusta a la prueba t cuando los supuestos de normalidad o homocedasticidad no se cumplen, o cuando se trabaja con datos ordinales. Aunque es menos potente bajo condiciones ideales para la prueba t, su validez no depende de la forma de la distribución, lo que la hace muy útil en muchas situaciones prácticas.

---

### Sección 2: Defensa Oral

**Pregunta 2.1:** "Has explicado la prueba de Mann-Whitney. Ahora, ¿cuándo usarías la Prueba de los Rangos con Signo de Wilcoxon en lugar de la Prueba U de Mann-Whitney? ¿Cuál es la diferencia fundamental en el tipo de datos o diseño experimental que abordan?"

**Respuesta Modelo:**
"Usaría la **Prueba de los Rangos con Signo de Wilcoxon** cuando tengo **muestras pareadas** (por ejemplo, mediciones 'antes y después' en los mismos sujetos, o pares de sujetos emparejados). Es el análogo no paramétrico de la prueba t para muestras pareadas. Se enfoca en las diferencias dentro de cada par.

En contraste, la **Prueba U de Mann-Whitney** se usa para comparar **dos muestras independientes**. Es decir, los sujetos de un grupo no tienen ninguna relación con los sujetos del otro grupo. La diferencia fundamental radica en el diseño experimental: Wilcoxon para datos dependientes/pareados, Mann-Whitney para datos independientes."

**Pregunta 2.2:** "Si tienes 4 grupos independientes y no se cumple el supuesto de normalidad, ¿qué prueba no paramétrica usarías para comparar sus medianas? Explica brevemente su lógica y cuál es su análogo paramétrico."

**Respuesta Modelo:**
"Para 4 grupos independientes sin normalidad, usaría la **Prueba H de Kruskal-Wallis**. Su lógica es una extensión de la prueba de Mann-Whitney: se combinan todos los datos de todos los grupos, se les asignan rangos, y luego se calcula la suma de rangos para cada grupo. Si las medianas de las poblaciones son iguales, esperaríamos que las sumas de rangos de cada grupo fueran similares. Si hay diferencias significativas en las sumas de rangos, se rechaza la hipótesis nula.

Su análogo paramétrico es el **ANOVA de un factor**."

**Pregunta 2.3:** "¿Qué significa que una prueba no paramétrica es 'menos potente' que su análoga paramétrica? ¿Implica esto que nunca deberíamos usarlas?"

**Respuesta Modelo:**
"Que una prueba no paramétrica sea 'menos potente' significa que, si los supuestos de la prueba paramétrica (como la normalidad) se cumplen, la prueba paramétrica tiene una mayor probabilidad de detectar un efecto real (es decir, de rechazar correctamente una hipótesis nula falsa) que la prueba no paramétrica. En otras palabras, la prueba paramétrica es más eficiente en el uso de la información de los datos.

Sin embargo, esto **no implica que nunca debamos usarlas**. Las pruebas no paramétricas son indispensables cuando los supuestos de las pruebas paramétricas no se cumplen (por ejemplo, datos muy asimétricos, presencia de outliers extremos, o datos ordinales). En estas situaciones, la prueba paramétrica podría dar resultados inválidos o engañosos, mientras que la prueba no paramétrica, aunque menos potente, sigue siendo válida y robusta. Es un 'trade-off' entre potencia y robustez/validez."

**Pregunta 2.4:** "La Prueba de Rachas no es una prueba sobre la tendencia central o la dispersión. ¿Qué propiedad de una secuencia de datos evalúa? Da un ejemplo de una secuencia que tendría muy pocas rachas y otra que tendría muchas rachas."

**Respuesta Modelo:**
"La Prueba de Rachas evalúa la **aleatoriedad** de una secuencia de datos. No se enfoca en los valores en sí, sino en el patrón o el orden en que aparecen los valores.

*   Una secuencia con **muy pocas rachas** sugiere una tendencia o un agrupamiento. Por ejemplo, si lanzamos una moneda y obtenemos: `CCCCCCCSSSSSSS` (7 caras seguidas, luego 7 sellos seguidos). Aquí solo hay 2 rachas (una de C y una de S).
*   Una secuencia con **muchas rachas** sugiere una alternancia excesiva o un patrón no aleatorio. Por ejemplo: `CSCSCSCSCSCSCS` (cara, sello, cara, sello...). Aquí hay 14 rachas. Una secuencia verdaderamente aleatoria debería tener un número de rachas intermedio, ni muy pocas ni demasiadas."

---

### Sección 3: Preguntas Rápidas

**Pregunta 3.1 (Opción Múltiple):** ¿Cuál de las siguientes situaciones es una razón principal para usar una prueba no paramétrica?

a) La varianza poblacional es desconocida.
b) El tamaño de la muestra es muy grande.
**c) Los datos no cumplen el supuesto de normalidad.**
d) Se desea comparar más de dos medias.

**Justificación:** La opción (a) es una razón para usar la prueba t en lugar de la Z, pero ambas son paramétricas. La opción (b) a menudo relaja el supuesto de normalidad para pruebas paramétricas (TCL). La opción (d) es el objetivo de ANOVA o Kruskal-Wallis, pero no es la razón principal para elegir no paramétrica. La opción (c) es la razón fundamental para recurrir a métodos no paramétricos.

**Pregunta 3.2 (Respuesta Corta):** ¿Qué es un "rango" en el contexto de las pruebas no paramétricas y por qué es tan fundamental para su funcionamiento?

**Respuesta Modelo:** Un **rango** es la posición ordinal de una observación dentro de un conjunto de datos cuando estos se ordenan de menor a mayor. Es fundamental porque al transformar los datos originales en rangos, las pruebas no paramétricas eliminan la dependencia de la forma específica de la distribución de los datos, permitiendo que se hagan inferencias válidas incluso cuando los supuestos de normalidad no se cumplen.

**Pregunta 3.3 (Verdadero/Falso):** Si una prueba no paramétrica arroja un resultado no significativo, significa que las medianas de los grupos son exactamente iguales. ¿Verdadero o Falso? Justifica.

**Respuesta Modelo:** **Falso.** Un resultado no significativo (p-valor > $\alpha$) en cualquier prueba de hipótesis (paramétrica o no paramétrica) significa que **no hay evidencia estadística suficiente para rechazar la hipótesis nula**. No significa que la hipótesis nula sea verdadera o que las medianas sean *exactamente* iguales. Simplemente no pudimos demostrar una diferencia con la evidencia disponible.

**Pregunta 3.4 (Respuesta Corta):** ¿Qué es la "eficiencia relativa" de una prueba no paramétrica? Si la eficiencia relativa de la mediana es del 64% respecto a la media, ¿qué significa eso?

**Respuesta Modelo:** La **eficiencia relativa** de una prueba no paramétrica es una medida de su potencia en comparación con una prueba paramétrica análoga, bajo las condiciones ideales para la prueba paramétrica. Se expresa como la relación entre el tamaño de muestra necesario para que la prueba paramétrica alcance una cierta potencia y el tamaño de muestra necesario para que la prueba no paramétrica alcance la misma potencia.

Si la eficiencia relativa de la mediana es del 64% respecto a la media, significa que para obtener la misma precisión o potencia en la estimación de la tendencia central, la mediana (como estimador no paramétrico) necesitaría una muestra aproximadamente $1/0.64 \approx 1.56$ veces más grande que la media (como estimador paramétrico), asumiendo que los datos son normales.
