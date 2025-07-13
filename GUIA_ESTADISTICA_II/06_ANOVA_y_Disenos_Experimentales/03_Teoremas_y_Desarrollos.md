# Unidad 6: Teoremas y Desarrollos

Los desarrollos en esta unidad extienden el teorema fundamental de ANOVA a modelos más complejos, particionando la variabilidad total en más componentes para aislar diferentes fuentes de variación.

---

### 1. Desarrollo del Diseño de Bloques Completos al Azar (DBCA)

**Modelo Matemático:**
$$ X_{ij} = \mu + \tau_i + \beta_j + \epsilon_{ij} $$
*   $X_{ij}$: La observación del tratamiento $i$ en el bloque $j$.
*   $\mu$: La gran media poblacional.
*   $\tau_i$: El efecto del $i$-ésimo tratamiento.
*   $\beta_j$: El efecto del $j$-ésimo bloque.
*   $\epsilon_{ij}$: El error aleatorio, asumido $N(0, \sigma^2)$.

**Descomposición de la Suma de Cuadrados:**
El teorema fundamental se expande. La Suma de Cuadrados Total (SCT) se descompone ahora en tres partes:

$$ SCT = SCTr + SCB + SCE $$

*   **SCT (Total):** Mide la variabilidad de todas las observaciones respecto a la gran media. Idéntica al ANOVA de un factor.
    $$ SCT = \sum_{i=1}^{k} \sum_{j=1}^{b} (X_{ij} - \bar{\bar{X}})^2 $$
    (con $k$ tratamientos y $b$ bloques)

*   **SCTr (Tratamiento):** Mide la variabilidad entre las medias de los tratamientos.
    $$ SCTr = b \sum_{i=1}^{k} (\bar{X}_{i.} - \bar{\bar{X}})^2 $$
    (donde $\bar{X}_{i.}$ es la media del tratamiento i)

*   **SCB (Bloques):** Mide la variabilidad entre las medias de los bloques. Esta es la variabilidad que estamos aislando.
    $$ SCB = k \sum_{j=1}^{b} (\bar{X}_{.j} - \bar{\bar{X}})^2 $$
    (donde $\bar{X}_{.j}$ es la media del bloque j)

*   **SCE (Error):** Es la variabilidad restante, después de haber quitado la del tratamiento y la del bloque. Se calcula por sustracción:
    $$ SCE = SCT - SCTr - SCB $$

**Grados de Libertad y Tabla ANOVA:**
La lógica de los grados de libertad también se expande:
*   $gl_{Tr} = k-1$
*   $gl_{B} = b-1$
*   $gl_{Total} = N-1 = kb-1$
*   $gl_{E} = gl_{Total} - gl_{Tr} - gl_{B} = (kb-1) - (k-1) - (b-1) = kb - k - b + 1 = (k-1)(b-1)$

La tabla ANOVA tendrá ahora una fila para los Bloques, y se calculan dos estadísticos F:
*   $F_{Tr} = \frac{CMTr}{CME}$ para probar el efecto del tratamiento.
*   $F_{B} = \frac{CMB}{CME}$ para probar si el bloqueo fue efectivo.

**Porqué es Importante:** Al incluir los bloques en el modelo, la Suma de Cuadrados de los Bloques (SCB) "absorbe" una parte de la variabilidad que en un diseño de un factor estaría dentro de la SCE. Esto hace que el CME (el denominador del estadístico F del tratamiento) sea más pequeño, lo que aumenta la potencia para detectar diferencias entre los tratamientos.

---

### 2. Desarrollo del Diseño Factorial de Dos Factores

**Modelo Matemático (con interacción):**
$$ X_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \epsilon_{ijk} $$
*   $\alpha_i$: Efecto principal del nivel $i$ del Factor A.
*   $\beta_j$: Efecto principal del nivel $j$ del Factor B.
*   $(\alpha\beta)_{ij}$: Efecto de la interacción entre el nivel $i$ de A y el nivel $j$ de B.

**Descomposición de la Suma de Cuadrados:**
$$ SCT = SCA + SCB + SCAB + SCE $$
*   **SCA (Factor A):** Mide la variabilidad entre las medias de los niveles del Factor A.
*   **SCB (Factor B):** Mide la variabilidad entre las medias de los niveles del Factor B.
*   **SCAB (Interacción):** Mide la variabilidad que no puede ser explicada por los efectos principales solos. Se calcula como $SCAB = SCTr - SCA - SCB$, donde SCTr es la suma de cuadrados de todas las celdas (combinaciones de tratamiento).
*   **SCE (Error):** Variabilidad dentro de cada celda. Requiere tener más de una observación por celda ($n>1$).

**Pruebas F:** Se realizan tres pruebas F, una para cada efecto (A, B y AB), siempre usando el CME en el denominador.

---

### 3. Desarrollo de la Prueba HSD de Tukey

**Objetivo:** Comparar todas las posibles parejas de medias ($\mu_i$ vs $\mu_j$) después de un ANOVA significativo, manteniendo la tasa de error familiar $\alpha_{FW}$.

**Lógica y Estadístico:**
La prueba de Tukey se basa en la **distribución del rango estudentizado (q)**. Esta distribución describe la diferencia entre la media más grande y la más pequeña de un conjunto de $k$ medias muestrales, en unidades de error estándar.

1.  **Se calcula la diferencia absoluta** para cada par de medias: $|\bar{X}_i - \bar{X}_j|$.

2.  **Se calcula el valor crítico HSD (Honest Significant Difference):**
    $$ HSD = q_{\alpha, k, gl_E} \sqrt{\frac{CME}{n}} $$
    *   $q_{\alpha, k, gl_E}$: El valor crítico de la distribución del rango estudentizado, que se busca en una tabla específica. Depende de $\alpha$, el número de grupos $k$, y los grados de libertad del error del ANOVA ($gl_E$).
    *   $CME$: El Cuadrado Medio del Error del ANOVA original.
    *   $n$: El tamaño de la muestra por grupo (la fórmula es para el caso balanceado).

3.  **Regla de Decisión:**
    Se compara cada diferencia de medias con el valor HSD.
    *   Si $|\bar{X}_i - \bar{X}_j| > HSD$, se concluye que la diferencia entre ese par de medias es estadísticamente significativa.
    *   Si $|\bar{X}_i - \bar{X}_j| \le HSD$, no hay evidencia suficiente para declarar una diferencia entre ese par.

**Porqué es Importante:**
A diferencia de hacer múltiples pruebas t, el uso del estadístico $q$ (que considera el número total de medias que se están comparando) permite que la prueba de Tukey mantenga la tasa de error familiar en el nivel $\alpha$ deseado. Es el método preferido para comparaciones post-hoc en ANOVA de un factor.

