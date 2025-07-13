# Unidad 5: Teoremas y Desarrollos

El desarrollo teórico de esta unidad se centra en justificar por qué el estadístico $\chi^2$ sigue la distribución de Chi-Cuadrado y cómo se calculan correctamente los componentes clave de la prueba: las frecuencias esperadas y los grados de libertad.

---

### 1. Justificación del Estadístico de Prueba $\chi^2$

**Teorema (de Karl Pearson, 1900):**
Dadas $k$ frecuencias observadas ($F_{o1}, F_{o2}, ..., F_{ok}$) de una muestra aleatoria de tamaño $n$ proveniente de una población, y sus correspondientes frecuencias esperadas ($F_{e1}, F_{e2}, ..., F_{ek}$) calculadas bajo una hipótesis nula, el estadístico:

$$ \chi^2 = \sum_{i=1}^{k} \frac{(F_{oi} - F_{ei})^2}{F_{ei}} $$

sigue, aproximadamente, una distribución de Chi-Cuadrado con $k-1$ grados de libertad, siempre que $n$ sea suficientemente grande.

**Desarrollo Conceptual:**
1.  **Base en la Normal:** Para una única categoría, la frecuencia observada $F_o$ sigue una distribución Binomial. Si $n$ es grande, esta Binomial puede ser aproximada por una Normal.
2.  **Estandarización:** La variable estandarizada $Z = \frac{F_o - E(F_o)}{\sqrt{Var(F_o)}}$ seguiría una distribución normal estándar.
3.  **Cuadrado de una Normal:** El cuadrado de una variable normal estándar, $Z^2$, sigue una distribución Chi-Cuadrado con 1 grado de libertad.
4.  **Suma de Chi-Cuadrados:** Pearson demostró que la suma de estas desviaciones al cuadrado estandarizadas para las $k$ categorías se aproxima a una distribución Chi-Cuadrado. El estadístico $\chi^2$ es, en esencia, la suma de las desviaciones al cuadrado entre los datos observados y los valores que la hipótesis nula predice, normalizadas por la magnitud de los valores esperados.

La razón por la que los grados de libertad son $k-1$ es que existe una restricción: la suma de las frecuencias observadas debe ser igual a la suma de las esperadas ($\sum F_o = \sum F_e = n$). Esto significa que si conocemos $k-1$ de las frecuencias, la última queda determinada. Se pierde un grado de libertad.

---

### 2. Desarrollo de la Prueba de Bondad de Ajuste

*   **Cálculo de Frecuencias Esperadas ($F_e$):**
    La hipótesis nula especifica la probabilidad $p_i$ para cada una de las $k$ categorías. La frecuencia esperada para una categoría es simplemente la probabilidad de esa categoría multiplicada by el tamaño total de la muestra.
    $$ F_{ei} = n \times p_i $$
    Este cálculo es directo y se deriva de la definición de probabilidad.

*   **Cálculo de Grados de Libertad ($gl$):**
    La fórmula general es $gl = k - 1 - m$.
    *   $k$: número de categorías.
    *   $1$: se resta siempre por la restricción de que $\sum F_o = n$.
    *   $m$: número de parámetros poblacionales que han sido **estimados a partir de los datos de la muestra** para poder calcular las probabilidades $p_i$. 
        *   Si $H_0$ especifica todas las probabilidades (e.g., "el dado es justo", $p_i=1/6$), entonces $m=0$ y $gl = k-1$.
        *   Si $H_0$ postula que los datos siguen una distribución de Poisson, pero no se conoce el parámetro $\lambda$ de la Poisson y se debe estimar a partir de la media de la muestra, entonces $m=1$ y $gl = k-1-1 = k-2$.
        *   Si se postula que siguen una Normal y se deben estimar $\mu$ y $\sigma$ de la muestra, entonces $m=2$ y $gl = k-1-2 = k-3$.

---

### 3. Desarrollo de la Prueba de Independencia

*   **Cálculo de Frecuencias Esperadas ($F_e$):**
    La hipótesis nula es que las dos variables (fila y columna) son independientes. 
    1.  **Probabilidad de la Fila $i$:** La mejor estimación de la probabilidad de que una observación caiga en la fila $i$ es la proporción de observaciones en esa fila: $P(\text{Fila } i) = \frac{\text{Total Fila } i}{n}$.
    2.  **Probabilidad de la Columna $j$:** De forma análoga, $P(\text{Columna } j) = \frac{\text{Total Columna } j}{n}$.
    3.  **Probabilidad Conjunta (bajo independencia):** Si dos eventos son independientes, la probabilidad de que ambos ocurran es el producto de sus probabilidades: 
        $P(\text{Fila } i \text{ y Columna } j) = P(\text{Fila } i) \times P(\text{Columna } j) = \frac{\text{Total Fila } i}{n} \times \frac{\text{Total Columna } j}{n}$.
    4.  **Frecuencia Esperada:** Para obtener la frecuencia esperada en la celda $(i,j)$, multiplicamos esta probabilidad conjunta por el tamaño total de la muestra, $n$:
        $$ F_{e,ij} = n \times \left( \frac{\text{Total Fila } i}{n} \times \frac{\text{Total Columna } j}{n} \right) = \frac{(\text{Total Fila } i) \times (\text{Total Columna } j)}{n} $$
    Esta es la fórmula fundamental para las frecuencias esperadas en una prueba de independencia.

*   **Cálculo de Grados de Libertad ($gl$):**
    La fórmula es $gl = (r-1)(c-1)$, donde $r$ es el número de filas y $c$ es el número de columnas.
    **Justificación:** Los grados de libertad representan el número de celdas que podemos llenar "libremente" en una tabla de $r \times c$ antes de que el resto de los valores queden determinados por los totales marginales (los totales de fila y columna). 
    Imagina una tabla 2x2. Una vez que fijas los totales de fila y columna, si llenas el valor de **una sola celda**, los otros tres valores de las celdas quedan automáticamente determinados para que los totales cuadren. Por lo tanto, solo tienes 1 grado de libertad. 
    $gl = (2-1)(2-1) = 1 \times 1 = 1$.
    Esta lógica se extiende a tablas más grandes.
