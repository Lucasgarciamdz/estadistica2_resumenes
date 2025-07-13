# Unidad 5: Resumen de Bondad de Ajuste e Independencia

Esta unidad se adentra en el análisis de datos categóricos. A diferencia de las unidades anteriores que se centraban en mediciones numéricas (medias, varianzas), aquí trabajamos con **frecuencias**: contamos cuántas observaciones caen en cada categoría. La herramienta principal para este análisis es la **prueba de Chi-Cuadrado ($\\chi^2$)**.

La idea central de la prueba $\\chi^2$ es siempre la misma: **comparar las frecuencias que observamos en nuestra muestra (Frecuencias Observadas, $F_o$) con las frecuencias que esperaríamos tener si la hipótesis nula fuera cierta (Frecuencias Esperadas, $F_e$)**.

---

### El Estadístico de Prueba Chi-Cuadrado

La fórmula del estadístico $\\chi^2$ cuantifica la discrepancia total entre lo observado y lo esperado:

$$ \\chi^2 = \\sum_{\\text{todas las celdas}} \\frac{(F_o - F_e)^2}{F_e} $$

*   **$(F_o - F_e)$:** La diferencia para cada categoría.
*   **$(F_o - F_e)^2$:** Se eleva al cuadrado para que las diferencias positivas y negativas no se anulen y para magnificar las grandes desviaciones.
*   **$\\frac{(\\dots)^2}{F_e}$:** Se divide por la frecuencia esperada para ponderar la diferencia. Una diferencia de 10 es mucho más significativa si esperabas 20 que si esperabas 1000.

Un valor de $\\chi^2$ cercano a cero indica un buen ajuste entre lo observado y lo esperado (apoya a $H_0$). Un valor grande indica una gran discrepancia (evidencia en contra de $H_0$). Por lo tanto, la prueba $\\chi^2$ es siempre de cola derecha.

### Dos Aplicaciones Principales

Esta unidad cubre dos escenarios de prueba distintos pero que usan el mismo estadístico.

#### 1. Prueba de Bondad de Ajuste

*   **Pregunta:** ¿Sigue la distribución de una **única variable categórica** un patrón o distribución teórica específica?
*   **Ejemplo:** Un dado es lanzado 600 veces. ¿Se puede considerar que el dado es justo? (Es decir, ¿se ajustan las frecuencias observadas de cada cara a una distribución uniforme donde cada cara tiene una probabilidad de 1/6?).
*   **Hipótesis:**
    *   $H_0$: La distribución de la población sigue el modelo teórico (e.g., $p_1=1/6, p_2=1/6, ...$).
    *   $H_1$: La distribución de la población no sigue el modelo teórico.
*   **Frecuencias Esperadas ($F_e$):** Se calculan aplicando las probabilidades teóricas de $H_0$ al tamaño total de la muestra ($n$). $F_e = n \\times p_i$ para cada categoría $i$.
*   **Grados de Libertad:** $gl = k - 1 - m$, donde $k$ es el número de categorías y $m$ es el número de parámetros que se han estimado a partir de los datos de la muestra para poder calcular las frecuencias esperadas.

#### 2. Prueba de Independencia

*   **Pregunta:** ¿Existe una asociación entre **dos variables categóricas** en una población, o son independientes?
*   **Ejemplo:** ¿Existe una relación entre el nivel de estudios de una persona (primario, secundario, universitario) y su preferencia por un candidato político (A, B, C)?
*   **Datos:** Se organizan en una **tabla de contingencia**, donde las filas representan las categorías de una variable y las columnas las de la otra.
*   **Hipótesis:**
    *   $H_0$: Las dos variables son independientes.
    *   $H_1$: Las dos variables no son independientes (están asociadas).
*   **Frecuencias Esperadas ($F_e$):** Se calculan bajo el supuesto de independencia. La probabilidad de que dos eventos independientes ocurran juntos es el producto de sus probabilidades. La frecuencia esperada para la celda en la fila $i$ y la columna $j$ es:
    $$ F_e = \\frac{(\\text{Total Fila } i) \\times (\\text{Total Columna } j)}{\\text{Gran Total}} $$
*   **Grados de Libertad:** $gl = (\\text{nº de filas} - 1) \\times (\\text{nº de columnas} - 1)$.
