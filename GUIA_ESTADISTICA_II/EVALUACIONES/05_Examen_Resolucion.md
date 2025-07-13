# Resolución del Examen Teórico: Unidad 5 - Bondad de Ajuste e Independencia

---

### Sección 1: Desarrollo en Pizarrón

**Pregunta 1: Lógica y Procedimiento de la Prueba de Independencia Chi-Cuadrado**

**Objetivo:** La Prueba de Independencia Chi-Cuadrado se utiliza para determinar si existe una asociación estadísticamente significativa entre dos variables categóricas en una población, o si son independientes.

**Lógica de la Prueba:**
La prueba compara las frecuencias observadas en una tabla de contingencia con las frecuencias que se esperarían si las dos variables fueran realmente independientes. Si las frecuencias observadas se desvían significativamente de las esperadas, se concluye que las variables están asociadas.

**Procedimiento:**
1.  **Formular las Hipótesis:**
    *   $H_0$: Las dos variables categóricas son independientes en la población.
    *   $H_1$: Las dos variables categóricas no son independientes (están asociadas) en la población.

2.  **Construir la Tabla de Contingencia:** Organizar los datos de la muestra en una tabla de $r$ filas (para las categorías de una variable) y $c$ columnas (para las categorías de la otra variable). Cada celda $(i,j)$ contendrá la frecuencia observada ($F_{o,ij}$). Calcular los totales de fila, totales de columna y el gran total ($n$).

3.  **Calcular las Frecuencias Esperadas ($F_e$):**
    Bajo la hipótesis nula de independencia, la probabilidad de que una observación caiga en una celda específica $(i,j)$ es el producto de la probabilidad de su fila y la probabilidad de su columna. Por lo tanto, la frecuencia esperada para cada celda $(i,j)$ se calcula como:
    $$ F_{e,ij} = \frac{(\text{Total Fila } i) \times (\text{Total Columna } j)}{\text{Gran Total}} $$
    Este cálculo se realiza para cada celda de la tabla.

4.  **Calcular el Estadístico de Prueba Chi-Cuadrado ($\chi^2$):**
    El estadístico $\chi^2$ mide la discrepancia total entre las frecuencias observadas y las esperadas:
    $$ \chi^2 = \sum_{\text{todas las celdas}} \frac{(F_{o,ij} - F_{e,ij})^2}{F_{e,ij}} $$

5.  **Determinar los Grados de Libertad ($gl$):**
    Los grados de libertad para una prueba de independencia en una tabla de contingencia de $r$ filas y $c$ columnas se calculan como:
    $$ gl = (r-1)(c-1) $$
    Esto se debe a que, una vez que los totales marginales (totales de fila y columna) están fijos, solo $(r-1)(c-1)$ celdas pueden ser llenadas libremente; el resto quedan determinadas.

6.  **Tomar una Decisión:**
    Se compara el valor calculado de $\chi^2$ con un valor crítico de la tabla de Chi-Cuadrado (para un nivel de significancia $\alpha$ y los $gl$ calculados) o se calcula el p-valor. Si $\chi^2_{obs} > \chi^2_{crit}$ (o $p-valor < \alpha$), se rechaza la hipótesis nula.

**Condición Crítica para la Validez:**
La prueba de Chi-Cuadrado es una prueba aproximada. Para que la aproximación a la distribución Chi-Cuadrado sea válida, la **frecuencia esperada ($F_e$) en cada celda debe ser de al menos 5**. Si esta condición no se cumple, la prueba puede no ser fiable y se deben considerar alternativas (como la Prueba Exacta de Fisher para tablas 2x2).

---

### Sección 2: Defensa Oral

**Pregunta 2.1:** "Has explicado la prueba de independencia. Ahora, ¿cuál es la diferencia fundamental entre la Prueba de Independencia y la Prueba de Bondad de Ajuste, ambas basadas en el estadístico Chi-Cuadrado? ¿Qué tipo de hipótesis nula se plantea en cada una?"

**Respuesta Modelo:**
"La diferencia fundamental radica en el número de variables categóricas que se analizan y la pregunta que se intenta responder:

*   La **Prueba de Bondad de Ajuste** analiza **una única variable categórica**. La pregunta es: ¿Se ajusta la distribución de frecuencias observadas de esta variable a una distribución de probabilidad teórica o esperada? La hipótesis nula ($H_0$) plantea que la distribución observada *sí* se ajusta a la distribución teórica (e.g., $H_0$: las proporciones de categorías son 25%, 25%, 50%).

*   La **Prueba de Independencia** analiza la relación entre **dos variables categóricas**. La pregunta es: ¿Existe una asociación entre estas dos variables, o son independientes? La hipótesis nula ($H_0$) plantea que las dos variables *son independientes* entre sí."

**Pregunta 2.2:** "Mencionaste la condición crítica para la validez de la prueba Chi-Cuadrado. ¿Qué sucede si no se cumple esta condición (por ejemplo, si tienes celdas con frecuencias esperadas muy bajas)? ¿Qué alternativas existen?"

**Respuesta Modelo:**
"Si la frecuencia esperada ($F_e$) en alguna celda es menor a 5, la aproximación del estadístico Chi-Cuadrado a la distribución Chi-Cuadrado no es fiable. Esto puede llevar a un p-valor incorrecto y, por lo tanto, a una conclusión errónea. El problema es que la distribución Chi-Cuadrado es continua, y la distribución de las frecuencias observadas es discreta; la aproximación funciona bien solo con suficientes datos.

Las alternativas incluyen:
*   **Agrupar categorías:** Si tiene sentido conceptualmente, se pueden combinar categorías con bajas frecuencias esperadas para aumentar el $F_e$.
*   **Recopilar más datos:** Aumentar el tamaño de la muestra para que las frecuencias esperadas aumenten.
*   **Prueba Exacta de Fisher:** Para tablas de contingencia 2x2 con bajas frecuencias esperadas, la Prueba Exacta de Fisher es una alternativa precisa que no se basa en aproximaciones."

**Pregunta 2.3:** "Si rechazas la hipótesis nula en una Prueba de Independencia, ¿qué significa eso? ¿La prueba te dice dónde reside la asociación? ¿Qué análisis adicional podrías realizar para identificar las celdas que más contribuyen a la significancia?"

**Respuesta Modelo:**
"Si rechazas la hipótesis nula en una Prueba de Independencia, significa que **existe una asociación estadísticamente significativa entre las dos variables categóricas**. Es decir, la distribución de una variable *no* es la misma para todos los niveles de la otra variable.

Sin embargo, la prueba Chi-Cuadrado **no te dice dónde reside esa asociación específica**. Solo te dice que existe una. Para identificar las celdas que más contribuyen a la significancia (es decir, dónde las frecuencias observadas se desvían más de las esperadas), se pueden analizar los **residuos estandarizados** (o residuos de Pearson) para cada celda. Un residuo estandarizado grande (típicamente mayor a 2 o menor a -2) indica una contribución significativa a la discrepancia general, señalando una asociación particular en esa celda."

**Pregunta 2.4:** "Explica conceptualmente por qué el estadístico Chi-Cuadrado es siempre de cola derecha. ¿Qué significa un valor de Chi-Cuadrado cercano a cero?"

**Respuesta Modelo:**
"El estadístico Chi-Cuadrado es siempre de cola derecha porque mide la **discrepancia** o la **diferencia** entre las frecuencias observadas y las esperadas. La fórmula implica elevar al cuadrado las diferencias, lo que siempre resulta en valores no negativos. Un valor de 0 significaría una coincidencia perfecta entre lo observado y lo esperado, lo cual es el escenario más consistente con la hipótesis nula.

Un valor de Chi-Cuadrado cercano a cero significa que las frecuencias observadas son muy similares a las frecuencias esperadas bajo la hipótesis nula. Esto indica un **buen ajuste** (en la prueba de bondad de ajuste) o una **fuerte evidencia de independencia** (en la prueba de independencia). En este caso, no tendríamos evidencia para rechazar la hipótesis nula."

---

### Sección 3: Preguntas Rápidas

**Pregunta 3.1 (Opción Múltiple):** En una tabla de contingencia de 3 filas y 4 columnas, los grados de libertad para una prueba de independencia Chi-Cuadrado son:

a) 12
b) 7
**c) 6**
d) 5

**Justificación:** $gl = (r-1)(c-1) = (3-1)(4-1) = 2 \times 3 = 6$.

**Pregunta 3.2 (Respuesta Corta):** ¿Qué representan las "frecuencias observadas" y las "frecuencias esperadas" en una prueba Chi-Cuadrado?

**Respuesta Modelo:** Las **frecuencias observadas ($F_o$)** son los conteos reales de los datos en cada categoría o celda de la muestra. Las **frecuencias esperadas ($F_e$)** son los conteos que se esperarían en cada categoría o celda si la hipótesis nula (e.g., de ajuste a una distribución teórica o de independencia entre variables) fuera verdadera.

**Pregunta 3.3 (Verdadero/Falso):** La prueba de Bondad de Ajuste Chi-Cuadrado se utiliza para determinar si la media de una variable continua se ajusta a un valor específico. ¿Verdadero o Falso? Justifica.

**Respuesta Modelo:** **Falso.** La prueba de Bondad de Ajuste Chi-Cuadrado se utiliza para determinar si la **distribución de frecuencias de una variable categórica** se ajusta a una distribución de probabilidad teórica. No se aplica a variables continuas ni a la comparación de medias.

**Pregunta 3.4 (Respuesta Corta):** ¿Por qué se eleva al cuadrado la diferencia $(F_o - F_e)$ en la fórmula del estadístico Chi-Cuadrado?

**Respuesta Modelo:** La diferencia $(F_o - F_e)$ se eleva al cuadrado por dos razones principales:
1.  Para asegurar que todas las contribuciones a la suma sean **positivas**, ya que las diferencias pueden ser tanto positivas como negativas, y no queremos que se anulen entre sí.
2.  Para **penalizar más fuertemente las grandes desviaciones**. Una diferencia de 5 unidades al cuadrado (25) contribuye mucho más que una diferencia de 1 unidad al cuadrado (1), lo que refleja que las grandes discrepancias son más importantes para la significancia estadística.
