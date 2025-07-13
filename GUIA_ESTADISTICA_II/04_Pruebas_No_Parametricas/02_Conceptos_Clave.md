# Unidad 4: Conceptos Clave

Esta sección define los términos y las pruebas específicas que componen el arsenal de la estadística no paramétrica. Es crucial entender la finalidad de cada prueba y su estadístico asociado.

---

*   **Prueba No Paramétrica (o de Distribución Libre):** Un método de inferencia estadística que no requiere supuestos sobre la forma de la distribución de probabilidad de la población de la cual se extraen los datos.

*   **Rango:** La posición numérica que ocupa una observación dentro de un conjunto de datos cuando estos se ordenan de menor a mayor. Es la base de la mayoría de las pruebas no paramétricas.

*   **Eficiencia Relativa:** Una medida de la potencia de una prueba en comparación con otra. A menudo se usa para comparar una prueba no paramétrica con su análoga paramétrica. Una eficiencia del 95% significa que la prueba no paramétrica necesita una muestra de tamaño 100 para lograr la misma potencia que la prueba paramétrica con una muestra de tamaño 95 (asumiendo que los supuestos de la prueba paramétrica se cumplen).

--- 

### Pruebas Específicas

*   **Prueba de los Signos:**
    *   **Propósito:** Probar hipótesis sobre la mediana de una única población o comparar medianas de dos poblaciones con muestras pareadas.
    *   **Lógica:** Convierte los datos en signos (+) o (-). Para una muestra, compara cada valor con la mediana hipotética ($H_0: \eta = \eta_0$). Para muestras pareadas, calcula la diferencia de cada par y anota su signo. Ignora los empates (diferencias de cero).
    *   **Estadístico de Prueba:** El número de signos positivos (o negativos). Bajo $H_0$, se espera que la mitad de los valores sean `+` y la mitad `-`. La prueba se basa en la distribución Binomial.

*   **Prueba de los Rangos con Signo de Wilcoxon:**
    *   **Propósito:** Similar a la prueba de los signos, pero más potente. Prueba hipótesis sobre la mediana de una población simétrica o compara dos poblaciones con muestras pareadas.
    *   **Lógica:** Además de usar el signo de las diferencias, incorpora la **magnitud** de estas a través de sus rangos. Calcula las diferencias, las ordena por su valor absoluto, les asigna rangos y luego suma los rangos de las diferencias positivas ($W^+$) y/o negativas ($W^-$).
    *   **Estadístico de Prueba:** $W = \min(W^+, W^-)$. Una suma de rangos muy pequeña para uno de los signos sugiere que la mediana es diferente.

*   **Prueba de la Suma de Rangos de Wilcoxon / Prueba U de Mann-Whitney:**
    *   **Propósito:** Comparar las medianas (o más generalmente, las distribuciones) de dos poblaciones **independientes**. Es el análogo no paramétrico de la prueba t para muestras independientes.
    *   **Lógica:** Combina ambas muestras, las ordena y les asigna rangos. Luego, suma los rangos pertenecientes a una de las muestras ($R_1$ o $R_2$). Si las poblaciones son idénticas, los rangos deberían estar bien mezclados y las sumas de rangos deberían ser similares.
    *   **Estadístico de Prueba:** La suma de rangos $R_1$ o, más comúnmente, el estadístico **U de Mann-Whitney**, que se calcula a partir de las sumas de rangos. Un valor de U muy pequeño o muy grande indica una diferencia entre los grupos.

*   **Prueba H de Kruskal-Wallis:**
    *   **Propósito:** Comparar las medianas de **tres o más poblaciones independientes**. Es el análogo no paramétrico del ANOVA de un factor.
    *   **Lógica:** Generaliza la idea de la prueba de Mann-Whitney. Combina todos los datos de todos los grupos, les asigna rangos y luego calcula la suma de rangos para cada grupo. Compara la variabilidad de las sumas de rangos entre los grupos con la variabilidad que se esperaría por azar.
    *   **Estadístico de Prueba (H):** Se basa en las sumas de rangos de cada grupo. Si las poblaciones son idénticas, H es pequeño. Si al menos una población es diferente, H tiende a ser grande. Bajo $H_0$, el estadístico H sigue aproximadamente una distribución Chi-Cuadrado con $k-1$ grados de libertad (donde $k$ es el número de grupos).

*   **Prueba de Rachas (o Corridas):**
    *   **Propósito:** Evaluar la **aleatoriedad** de una secuencia de datos. No prueba un parámetro, sino el orden en que se han obtenido los datos.
    *   **Lógica:** Una racha es una secuencia de símbolos idénticos precedida y seguida por un símbolo diferente o por nada. La prueba cuenta el número total de rachas en una secuencia. 
        *   **Muy pocas rachas** sugiere una tendencia o agrupamiento (e.g., AAAAAABBBBBB).
        *   **Demasiadas rachas** sugiere una alternancia sistemática (e.g., ABABABABAB).
    *   **Estadístico de Prueba (R):** El número de rachas. Se compara con los valores críticos esperados para una secuencia aleatoria.
