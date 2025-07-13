# Unidad 4: Teoremas y Desarrollos

El desarrollo en las pruebas no paramétricas se enfoca en la lógica de construcción de los estadísticos de prueba basados en rangos y en cómo se determinan sus distribuciones bajo $H_0$. A diferencia de las pruebas paramétricas, no se derivan de un supuesto de normalidad, sino de la combinatoria y las propiedades de los rangos.

---

### 1. Prueba de los Rangos con Signo de Wilcoxon (Una Muestra o Muestras Pareadas)

**Objetivo:** Probar $H_0: \eta = \eta_0$ para una población simétrica.

**Lógica de Construcción del Estadístico:**
La prueba busca determinar si las desviaciones respecto a la mediana hipotética están simétricamente distribuidas alrededor de cero. No solo mira el signo (como la Prueba de los Signos), sino también la magnitud de la desviación a través de su rango.

**Pasos:**
1.  Para cada observación $X_i$, calcular la diferencia $D_i = X_i - \eta_0$.
2.  Ignorar las diferencias que son cero.
3.  Ordenar los valores absolutos de las diferencias, $|D_i|$, de menor a mayor.
4.  Asignar rangos a estas diferencias absolutas. Si hay empates, se asigna el rango promedio.
5.  Crear $W^+$, la suma de los rangos correspondientes a las diferencias $D_i$ positivas.
6.  Crear $W^-$, la suma de los rangos correspondientes a las diferencias $D_i$ negativas.
7.  El estadístico de prueba es $W = \min(W^+, W^-)$.

**Distribución bajo $H_0$:**
Si $H_0$ es cierta, las diferencias positivas y negativas deberían estar mezcladas aleatoriamente. La suma total de los rangos es una constante: $W^+ + W^- = \frac{n(n+1)}{2}$.
Para muestras pequeñas, la distribución de $W$ está tabulada. Se compara el $W$ observado con un valor crítico de la tabla de Wilcoxon.

**Aproximación Normal (Muestras Grandes, n > 20):**
Para muestras grandes, el estadístico $W$ se aproxima a una distribución normal.
*   **Media de W:** $E(W) = \mu_W = \frac{n(n+1)}{4}$
*   **Varianza de W:** $Var(W) = \sigma_W^2 = \frac{n(n+1)(2n+1)}{24}$

El estadístico Z estandarizado es:
$$ Z = \frac{W - \mu_W}{\sigma_W} $$

---

### 2. Prueba U de Mann-Whitney (Dos Muestras Independientes)

**Objetivo:** Probar $H_0$: Las dos poblaciones tienen distribuciones idénticas.

**Lógica de Construcción del Estadístico:**
Si las dos poblaciones son idénticas, al combinar y ordenar todos los datos, los rangos del grupo 1 deberían estar mezclados aleatoriamente con los del grupo 2. La prueba mide si los rangos de un grupo tienden a ser sistemáticamente más bajos o más altos que los del otro.

**Pasos:**
1.  Combinar las dos muestras (de tamaños $n_1$ y $n_2$) en un solo conjunto.
2.  Ordenar el conjunto combinado de menor a mayor y asignar rangos.
3.  Calcular $R_1$, la suma de los rangos de las observaciones que vinieron de la muestra 1.
4.  Calcular el estadístico $U_1$:
    $$ U_1 = n_1 n_2 + \frac{n_1(n_1+1)}{2} - R_1 $$
5.  Calcular $R_2$ y el estadístico $U_2$ de forma análoga, o más fácil, usando la propiedad $U_1 + U_2 = n_1 n_2$.
6.  El estadístico de prueba es $U = \min(U_1, U_2)$.

**Interpretación de U:** El estadístico $U_1$ cuenta el número de veces que una observación de la muestra 2 precede a una observación de la muestra 1 en la lista ordenada. Un valor de U muy pequeño indica una separación clara entre los rangos de los dos grupos, lo que es evidencia en contra de $H_0$.

**Distribución bajo $H_0$:**
Para muestras pequeñas, la distribución de U está tabulada. Se compara el U observado con un valor crítico.

**Aproximación Normal (Muestras Grandes, $n_1, n_2 > 10$):**
*   **Media de U:** $E(U) = \mu_U = \frac{n_1 n_2}{2}$
*   **Varianza de U:** $Var(U) = \sigma_U^2 = \frac{n_1 n_2 (n_1+n_2+1)}{12}$

El estadístico Z estandarizado es:
$$ Z = \frac{U - \mu_U}{\sigma_U} $$

---

### 3. Prueba H de Kruskal-Wallis (k Muestras Independientes)

**Objetivo:** Probar $H_0$: Las $k$ poblaciones tienen distribuciones idénticas.

**Lógica de Construcción del Estadístico:**
Es una generalización de la prueba de Mann-Whitney. Compara la suma de rangos de cada grupo con la suma de rangos que se esperaría si los rangos estuvieran distribuidos uniformemente entre los grupos.

**Pasos:**
1.  Combinar las $k$ muestras en un solo conjunto de tamaño $N$.
2.  Asignar rangos a todo el conjunto.
3.  Calcular $R_i$, la suma de los rangos para cada uno de los $k$ grupos.
4.  Calcular el estadístico H:
    $$ H = \left[ \frac{12}{N(N+1)} \sum_{i=1}^{k} \frac{R_i^2}{n_i} \right] - 3(N+1) $$

**Distribución bajo $H_0$:**
Si $H_0$ es cierta y los tamaños de muestra $n_i$ son suficientemente grandes (generalmente > 5), el estadístico H sigue aproximadamente una **distribución Chi-Cuadrado ($\chi^2$) con $k-1$ grados de libertad**.

**Porqué es Importante:**
La prueba H es esencialmente un ANOVA realizado sobre los rangos de los datos. La fórmula del estadístico H mide la suma de las desviaciones al cuadrado de las sumas de rangos de cada grupo respecto a la media de los rangos esperada. Un valor grande de H indica que al menos un grupo tiene una suma de rangos significativamente diferente de los demás, lo que lleva al rechazo de $H_0$. Es siempre una prueba de cola derecha.
