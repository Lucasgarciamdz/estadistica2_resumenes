# Unidad 5: Conceptos Clave

Las pruebas de esta unidad se basan en un conjunto de conceptos específicos para manejar datos categóricos y de frecuencia. Es vital entenderlos para aplicar e interpretar correctamente las pruebas de Chi-Cuadrado.

---

*   **Datos Categóricos:** Datos que representan categorías o etiquetas y no pueden ser medidos en una escala numérica continua. Ejemplos: color de ojos (azul, verde, marrón), nivel de satisfacción (bajo, medio, alto), tipo de producto (A, B, C).

*   **Frecuencia Observada ($F_o$ o $O_{ij}$):** El número de observaciones de la muestra que caen en una categoría particular o en una celda específica de una tabla de contingencia. Es un conteo directo de los datos.

*   **Frecuencia Esperada ($F_e$ o $E_{ij}$):** El número de observaciones que *se esperaría* que cayeran en una categoría o celda si la hipótesis nula ($H_0$) fuera cierta. Este es un valor calculado, no observado.

*   **Distribución de Chi-Cuadrado ($\chi^2$):** Una familia de distribuciones de probabilidad continuas. Es la distribución del estadístico de prueba $\chi^2$ bajo la hipótesis nula. 
    *   Está definida solo para valores positivos.
    *   Es asimétrica a la derecha.
    *   Su forma depende de un solo parámetro: los **grados de libertad (gl)**. A medida que los grados de libertad aumentan, la distribución se vuelve más simétrica y se aproxima a una distribución normal.

*   **Estadístico de Prueba Chi-Cuadrado ($\chi^2$):** La medida que cuantifica la diferencia global entre las frecuencias observadas y las esperadas.
    $$ \chi^2 = \sum \frac{(F_o - F_e)^2}{F_e} $$

--- 

### Para la Prueba de Bondad de Ajuste

*   **Bondad de Ajuste:** El grado en que un conjunto de frecuencias observadas se ajusta a un conjunto de frecuencias esperadas teóricas. La prueba evalúa si las discrepancias son lo suficientemente pequeñas como para ser atribuidas al azar del muestreo.

*   **Distribución Teórica:** El modelo o patrón de probabilidad que se postula en la hipótesis nula. Puede ser una distribución uniforme (todas las categorías son igualmente probables) o cualquier otra distribución discreta (e.g., Binomial, Poisson, o proporciones específicas como 40%, 30%, 30%).

--- 

### Para la Prueba de Independencia

*   **Tabla de Contingencia (o Tabla de Doble Entrada):** Una tabla utilizada para mostrar la distribución de frecuencias de dos variables categóricas simultáneamente. Las filas corresponden a las categorías de una variable y las columnas a las categorías de la otra. La celda en la intersección de una fila y una columna muestra la frecuencia conjunta de esas dos categorías.

*   **Independencia Estadística:** Dos variables son independientes si la ocurrencia de un nivel de una variable no afecta la probabilidad de ocurrencia de ningún nivel de la otra variable. En el contexto de una tabla de contingencia, esto significa que la distribución de la variable de fila es la misma para todas las columnas (y viceversa).

*   **Asociación:** Lo contrario de la independencia. Dos variables están asociadas o relacionadas si la distribución de una variable cambia según el nivel de la otra.

*   **Marginales de Fila/Columna:** Los totales de cada fila y cada columna en una tabla de contingencia. Representan la distribución de frecuencias de cada variable por separado.

*   **Grados de Libertad (gl) en la Prueba de Independencia:** Se calculan como $gl = (r-1)(c-1)$, donde $r$ es el número de filas y $c$ es el número de columnas. Representa el número de celdas en la tabla cuyo valor se puede elegir "libremente" una vez que los totales marginales están fijos.

*   **Condición para la Prueba $\chi^2$:** Una regla general importante es que la prueba de Chi-Cuadrado es apropiada solo si la **frecuencia esperada ($F_e$) en cada celda es de al menos 5**. Si esta condición no se cumple, especialmente en tablas de 2x2, se deben usar alternativas como la Prueba Exacta de Fisher.
