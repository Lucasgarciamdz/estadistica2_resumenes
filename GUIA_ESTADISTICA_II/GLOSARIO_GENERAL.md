# Glosario General de Conceptos Clave - Estadística Aplicada II

Este glosario consolida y define los términos fundamentales de todas las unidades de Estadística Aplicada II. Es una herramienta esencial para el repaso rápido y para asegurar un dominio completo del vocabulario técnico de la materia.

---

*   **Asociación:** Lo contrario de la independencia. Dos variables están asociadas o relacionadas si la distribución de una variable cambia según el nivel de la otra.

*   **Bloque:** Un grupo de unidades experimentales que son homogéneas con respecto al factor de bloqueo. Ejemplo: un grupo de pacientes de la misma edad; un conjunto de experimentos realizados el mismo día.

*   **Bondad de Ajuste:** El grado en que un conjunto de frecuencias observadas se ajusta a un conjunto de frecuencias esperadas teóricas. La prueba evalúa si las discrepancias son lo suficientemente pequeñas como para ser atribuidas al azar del muestreo.

*   **Cadena de Markov:** Un proceso estocástico (generalmente de tiempo discreto) que posee la **Propiedad de Markov**.

*   **Cadena de Markov Regular:** Una cadena de Markov es regular si existe alguna potencia de su matriz de transición, $P^k$, que tiene todas sus entradas estrictamente positivas. Esto implica que es posible llegar desde cualquier estado a cualquier otro estado en algún número de pasos.

*   **Condición para la Prueba $\chi^2$:** Una regla general importante es que la prueba de Chi-Cuadrado es apropiada solo si la **frecuencia esperada ($F_e$) en cada celda es de al menos 5**. Si esta condición no se cumple, especialmente en tablas de 2x2, se deben usar alternativas como la Prueba Exacta de Fisher.

*   **Consistente:** Un estimador es consistente si, a medida que el tamaño de la muestra ($n$) aumenta, el valor del estimador converge al valor del parámetro. $\lim_{n \to \infty} P(|\hat{\theta} - \theta| < \epsilon) = 1$.

*   **Contraste:** Una combinación lineal de las medias de los grupos que se utiliza para probar hipótesis específicas. Por ejemplo, en un estudio con 4 grupos, un contraste podría usarse para comparar la media del grupo de control con el promedio de las medias de los 3 grupos de tratamiento. Los contrastes se planifican *antes* del experimento (a priori), a diferencia de las pruebas post-hoc que son *a posteriori*.

*   **Corrección de Bonferroni:** Un método muy general y simple para controlar la tasa de error familiar. Se realiza una serie de pruebas t estándar, pero se usa un nivel de significancia ajustado: $\alpha_{ajustado} = \frac{\alpha_{FW}}{\text{nº de comparaciones}}$. Es un método muy conservador (reduce la potencia) y a menudo no es la mejor opción, pero es fácil de aplicar.

*   **Cuadrado Medio del Error (CME):** Es la varianza estimada dentro de los grupos. Representa la variabilidad aleatoria o "ruido". Se calcula como:
    $$ CME = \frac{SCE}{N-k} $$
    El CME es un estimador combinado (pooled) de la varianza poblacional común $\sigma^2$.

*   **Cuadrado Medio del Tratamiento (CMTr):** Es la varianza estimada entre los grupos. Se calcula como:
    $$ CMTr = \frac{SCTr}{k-1} $$

*   **Datos Categóricos:** Datos que representan categorías o etiquetas y no pueden ser medidos en una escala numérica continua. Ejemplos: color de ojos (azul, verde, marrón), nivel de satisfacción (bajo, medio, alto), tipo de producto (A, B, C).

*   **Diseño Completamente al Azar (DCA):** El diseño más simple de ANOVA (visto en la Unidad 3). Los tratamientos se asignan a las unidades experimentales de forma completamente aleatoria. Asume que todas las unidades experimentales son homogéneas.

*   **Diseño de Bloques Completos al Azar (DBCA):** Un diseño donde las unidades experimentales se agrupan en bloques, y luego los tratamientos se asignan al azar a las unidades *dentro* de cada bloque. Cada bloque contiene todos los tratamientos.

*   **Diseño Factorial:** Un diseño experimental en el que se investigan los efectos de dos o más factores simultáneamente. En un diseño factorial completo, se prueban todas las combinaciones posibles de los niveles de todos los factores.

*   **Distribución de Chi-Cuadrado ($\\chi^2$):** Una familia de distribuciones de probabilidad continuas. Es la distribución del estadístico de prueba $\\chi^2$ bajo la hipótesis nula. 
    *   Está definida solo para valores positivos.
    *   Es asimétrica a la derecha.
    *   Su forma depende de un solo parámetro: los **grados de libertad (gl)**. A medida que los grados de libertad aumentan, la distribución se vuelve más simétrica y se aproxima a una distribución normal.

*   **Distribución de Muestreo:** La distribución de probabilidad de un estadístico (como $\bar{X}$ o $S^2$) cuando se considera sobre todas las posibles muestras de tamaño $n$ de una población. Es el fundamento teórico para la inferencia estadística.

*   **Distribución Estacionaria (o de Equilibrio, $\pi$):** Un vector de probabilidad $\pi$ que describe el comportamiento a largo plazo de una cadena de Markov regular. Si el proceso alcanza esta distribución, se mantendrá en ella para siempre. Se caracteriza por la ecuación:
    $$ \pi P = \pi $$
    El vector $\pi$ es el vector propio (eigenvector) izquierdo de la matriz $P$ asociado con el valor propio (eigenvalue) 1.

*   **Distribución Teórica:** El modelo o patrón de probabilidad que se postula en la hipótesis nula. Puede ser una distribución uniforme (todas las categorías son igualmente probables) o cualquier otra distribución discreta (e.g., Binomial, Poisson, o proporciones específicas como 40%, 30%, 30%).

*   **Ecuación de Chapman-Kolmogorov:** Relaciona las probabilidades de transición de $n$ pasos con las de un paso. Afirma que la matriz de transición de $n$ pasos, $P^{(n)}$, es simplemente la $n$-ésima potencia de la matriz de un paso, $P$. 
    $$ P^{(n)} = P^n $$
    El elemento $(i,j)$ de esta matriz es $p_{ij}^{(n)} = P(X_{t+n}=j | X_t=i)$.

*   **Efecto Principal:** El efecto promedio de un factor sobre la variable de respuesta, ignorando los efectos de los otros factores. En un diseño de dos factores (A y B), hay un efecto principal para A y un efecto principal para B.

*   **Eficiencia Relativa:** Una medida de la potencia de una prueba en comparación con otra. A menudo se usa para comparar una prueba no paramétrica con su análoga paramétrica. Una eficiencia del 95% significa que la prueba no paramétrica necesita una muestra de tamaño 100 para lograr la misma potencia que la prueba paramétrica con una muestra de tamaño 95 (asumiendo que los supuestos de la prueba paramétrica se cumplen).

*   **Eficiente:** Entre dos estimadores insesgados, el más eficiente es el que tiene la menor varianza. Una menor varianza implica que las estimaciones estarán, en general, más cerca del valor real del parámetro.

*   **Error de Tipo I:** Ocurre si se **rechaza la hipótesis nula ($H_0$) cuando esta es verdadera**. La probabilidad de cometer este error es $\alpha$. Es el error de "falso positivo" (concluir que hay un efecto cuando no lo hay).

*   **Error de Tipo II:** Ocurre si **no se rechaza la hipótesis nula ($H_0$) cuando esta es falsa**. La probabilidad de cometer este error se denota por $\beta$. Es el error de "falso negativo" (no detectar un efecto que sí existe).

*   **Error Estándar:** Es la desviación estándar de la distribución de muestreo de un estimador. Mide la precisión de un estimador. Por ejemplo, el error estándar de la media muestral es $SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}$. Indica cuánto varían las medias muestrales alrededor de la media poblacional.

*   **Espacio de Estados (S):** El conjunto de todos los posibles valores que las variables aleatorias $X(t)$ pueden tomar. Los valores individuales se llaman **estados**.

*   **Estadístico F:** El estadístico de prueba para ANOVA. Es el cociente de la varianza entre grupos y la varianza dentro de los grupos.
    $$ F = \frac{CMTr}{CME} $$
    Sigue una distribución F de Snedecor con $k-1$ (grados de libertad del numerador) y $N-k$ (grados de libertad del denominador) grados de libertad.

*   **Estadístico de Prueba:** Un valor calculado a partir de los datos de la muestra que se utiliza para decidir si se rechaza o no la hipótesis nula. Mide la diferencia entre el valor observado en la muestra y el valor esperado bajo la hipótesis nula, en unidades de error estándar.

*   **Estadístico de Prueba Chi-Cuadrado ($\\chi^2$):** La medida que cuantifica la diferencia global entre las frecuencias observadas y las esperadas.
    $$ \chi^2 = \sum \frac{(F_o - F_e)^2}{F_e} $$

*   **Estimación:** Un valor numérico específico que toma un estimador para una muestra particular. Ejemplo: Si $\bar{X} = 25.4$ para una muestra, ese es el valor de la estimación.

*   **Estimador (o Estadístico) ($\hat{\theta}$):** Una función de los datos de la muestra que se utiliza para estimar un parámetro poblacional. Es una **variable aleatoria**, ya que su valor cambia de una muestra a otra. Ejemplo: $\bar{X}$ es un estimador de $\mu$.

*   **Factor:** La variable categórica independiente que se utiliza para definir los grupos o tratamientos que se están comparando. Por ejemplo, en un estudio que compara tres métodos de enseñanza, el "método de enseñanza" es el factor.

*   **Factor de Bloqueo (o Variable de Molestia):** Una variable que no es de interés principal para el investigador, pero que se sabe (o se sospecha) que tiene un efecto sobre la variable de respuesta. Se controla para reducir el error experimental.

*   **Frecuencia Esperada ($F_e$ o $E_{ij}$):** El número de observaciones que *se esperaría* que cayeran en una categoría o celda si la hipótesis nula ($H_0$) fuera cierta. Este es un valor calculado, no observado.

*   **Frecuencia Observada ($F_o$ o $O_{ij}$):** El número de observaciones de la muestra que caen en una categoría particular o en una celda específica de una tabla de contingencia. Es un conteo directo de los datos.

*   **Grados de Libertad (gl) en la Prueba de Independencia:** Se calculan como $gl = (r-1)(c-1)$, donde $r$ es el número de filas y $c$ es el número de columnas. Representa el número de celdas en la tabla cuyo valor se puede elegir "libremente" una vez que los totales marginales están fijos.

*   **Gran Media ($\\bar{\bar{X}}$):** La media de todas las observaciones en el estudio, sin importar a qué grupo pertenecen.

*   **Gráfico de Interacción:** Una herramienta visual clave para detectar interacciones. Se grafica la media de la variable de respuesta para cada nivel de un factor, con líneas separadas para cada nivel del otro factor. **Líneas no paralelas sugieren una interacción.**

*   **Hipótesis Alternativa ($H_1$ o $H_a$):** Es la afirmación que se aceptará si se rechaza la hipótesis nula. Representa la conclusión que el investigador intenta demostrar. Nunca contiene un signo de igualdad (e.g., $\mu \neq 50$, $p < 0.4$).

*   **Hipótesis en ANOVA:**
    *   **Hipótesis Nula ($H_0$):** Las medias de todos los grupos (poblacionales) son iguales. No hay efecto del tratamiento. 
        $H_0: \mu_1 = \mu_2 = ... = \mu_k$
    *   **Hipótesis Alternativa ($H_1$):** No todas las medias son iguales. Al menos una media es diferente de las demás. Es importante notar que $H_1$ no dice que *todas* las medias son diferentes, solo que al menos dos de ellas lo son.

*   **Hipótesis Nula ($H_0$):** Es la afirmación sobre un parámetro poblacional que se somete a prueba. Generalmente representa el *status quo*, la ausencia de un efecto o una diferencia. Siempre contiene un signo de igualdad (e.g., $\mu = 50$, $p \ge 0.4$). Se asume verdadera hasta que la evidencia muestral sugiere lo contrario.

*   **Independencia Estadística:** Dos variables son independientes si la ocurrencia de un nivel de una variable no afecta la probabilidad de ocurrencia de ningún nivel de la otra variable. En el contexto de una tabla de contingencia, esto significa que la distribución de la variable de fila es la misma para todas las columnas (y viceversa).

*   **Insesgado:** Un estimador es insesgado si su valor esperado es igual al parámetro que se desea estimar. $E(\hat{\theta}) = \theta$. Esto significa que, en promedio, el estimador no sobreestima ni subestima el parámetro.

*   **Interacción:** Ocurre cuando el efecto de un factor sobre la variable de respuesta **cambia** dependiendo del nivel de otro factor. Es el concepto más importante en los diseños factoriales. Si la interacción es significativa, los efectos principales pueden ser engañosos y deben interpretarse con cautela.

*   **Matriz de Transición (P):** Una matriz cuadrada de tamaño $k \times k$ (donde $k$ es el número de estados) que contiene todas las probabilidades de transición de un paso. El elemento en la fila $i$ y columna $j$ es $p_{ij}$.
    *   **Propiedades:**
        1.  $0 \le p_{ij} \le 1$ para todo $i, j$.
        2.  $\sum_{j=1}^{k} p_{ij} = 1$ para cada fila $i$ (la suma de las probabilidades de salir de un estado debe ser 1).

*   **Marginales de Fila/Columna:** Los totales de cada fila y cada columna en una tabla de contingencia. Representan la distribución de frecuencias de cada variable por separado.

*   **Muestra:** Un subconjunto de la población, seleccionado para ser estudiado y a partir del cual se inferirán propiedades de la población. Se denota con $n$.

*   **Muestreo Aleatorio Simple (M.A.S.):** Un método de selección de muestras donde cada posible muestra de tamaño $n$ tiene la misma probabilidad de ser seleccionada. Esto asegura que la muestra sea representativa y elimina sesgos de selección.

*   **Nivel de Significancia ($\\alpha$):** La probabilidad máxima, fijada por el investigador, de cometer un Error de Tipo I. Es el umbral para decidir si el p-valor es suficientemente pequeño como para rechazar $H_0$. Típicamente $\alpha = 0.05$ o $\alpha = 0.01$.

*   **Niveles (o Tratamientos):** Las diferentes categorías o valores que puede tomar el factor. Si el factor es "método de enseñanza", los niveles podrían ser "Método A", "Método B" y "Método C". El número de niveles se denota por $k$.

*   **Parámetro ($\\theta$):** Una medida numérica que describe una característica de la **población**. Es un valor constante pero usualmente desconocido. Ejemplos: $\mu$ (media poblacional), $\sigma^2$ (varianza poblacional), $p$ (proporción poblacional).

*   **p-valor (o valor p):** La probabilidad de obtener un resultado muestral al menos tan extremo como el que se observó, suponiendo que la hipótesis nula es verdadera. Es el nivel de significancia más pequeño al que se podría rechazar $H_0$ para los datos observados.
    *   **Regla de decisión:** Si $p-valor \le \alpha$, se rechaza $H_0$.
    *   **Interpretación:** Un p-valor pequeño indica que los datos observados son muy improbables si $H_0$ fuera cierta, lo que proporciona fuerte evidencia en contra de $H_0$.

*   **Población:** El universo total de elementos o resultados de interés para un estudio. Se denota con $N$.

*   **Potencia de la Prueba ($1 - \beta$):** Es la probabilidad de **rechazar correctamente la hipótesis nula cuando esta es falsa**. Es la capacidad de la prueba para detectar un efecto real. Una prueba potente es aquella con una alta probabilidad de llevar a la conclusión correcta.

*   **Probabilidad de Transición de un Paso ($p_{ij}$):** La probabilidad de que el proceso pase del estado $i$ al estado $j$ en el siguiente paso de tiempo.
    $$ p_{ij} = P(X_{t+1} = j | X_t = i) $$

*   **Proceso Estocástico (o Proceso Aleatorio):** Una familia de variables aleatorias $X(t) : t \in T$ indexada por un parámetro $t$, que usualmente representa el tiempo. Para cada instante $t$, $X(t)$ es una variable aleatoria.

*   **Propiedad de Markov (o Carencia de Memoria):** La distribución de probabilidad condicional de los estados futuros del proceso, dado el estado presente y los estados pasados, depende únicamente del estado presente. El pasado no aporta información sobre el futuro si ya conocemos el presente.
    $$ P(X_{t+1} = j | X_t = i, X_{t-1}=i_{t-1}, ...) = P(X_{t+1} = j | X_t = i) $$

*   **Prueba Bilateral (o de dos colas):** Una prueba en la que la hipótesis alternativa no especifica una dirección (e.g., $H_1: \mu \neq 50$). La región de rechazo se divide en dos partes, una en cada cola de la distribución.

*   **Prueba de Chi-Cuadrado ($\\chi^2$):** Se utiliza para pruebas de hipótesis sobre una única varianza poblacional.

*   **Prueba de la Suma de Rangos de Wilcoxon / Prueba U de Mann-Whitney:**
    *   **Propósito:** Comparar las medianas (o más generalmente, las distribuciones) de dos poblaciones **independientes**. Es el análogo no paramétrico de la prueba t para muestras independientes.
    *   **Lógica:** Combina ambas muestras, las ordena y les asigna rangos. Luego, suma los rangos pertenecientes a una de las muestras ($R_1$ o $R_2$). Si las poblaciones son idénticas, los rangos deberían estar bien mezclados y las sumas de rangos deberían ser similares.
    *   **Estadístico de Prueba:** La suma de rangos $R_1$ o, más comúnmente, el estadístico **U de Mann-Whitney**, que se calcula a partir de las sumas de rangos. Un valor de U muy pequeño o muy grande indica una diferencia entre los grupos.

*   **Prueba de los Rangos con Signo de Wilcoxon:**
    *   **Propósito:** Similar a la prueba de los signos, pero más potente. Prueba hipótesis sobre la mediana de una población simétrica o compara dos poblaciones con muestras pareadas.
    *   **Lógica:** Además de usar el signo de las diferencias, incorpora la **magnitud** de estas a través de sus rangos. Calcula las diferencias, las ordena por su valor absoluto, les asigna rangos y luego suma los rangos de las diferencias positivas ($W^+$) y/o negativas ($W^-$).
    *   **Estadístico de Prueba:** $W = \min(W^+, W^-)$. Una suma de rangos muy pequeña para uno de los signos sugiere que la mediana es diferente.

*   **Prueba de los Signos:**
    *   **Propósito:** Probar hipótesis sobre la mediana de una única población o comparar medianas de dos poblaciones con muestras pareadas.
    *   **Lógica:** Convierte los datos en signos (+) o (-). Para una muestra, compara cada valor con la mediana hipotética ($H_0: \eta = \eta_0$). Para muestras pareadas, calcula la diferencia de cada par y anota su signo. Ignora los empates (diferencias de cero).
    *   **Estadístico de Prueba:** El número de signos positivos (o negativos). Bajo $H_0$, se espera que la mitad de los valores sean `+` y la mitad `-`. La prueba se basa en la distribución Binomial.

*   **Prueba de Rachas (o Corridas):**
    *   **Propósito:** Evaluar la **aleatoriedad** de una secuencia de datos. No prueba un parámetro, sino el orden en que se han obtenido los datos.
    *   **Lógica:** Una racha es una secuencia de símbolos idénticos precedida y seguida por un símbolo diferente o por nada. La prueba cuenta el número total de rachas en una secuencia. 
        *   **Muy pocas rachas** sugiere una tendencia o agrupamiento (e.g., AAAAAABBBBBB).
        *   **Demasiadas rachas** sugiere una alternancia sistemática (e.g., ABABABABAB).
    *   **Estadístico de Prueba (R):** El número de rachas. Se compara con los valores críticos esperados para una secuencia aleatoria.

*   **Prueba F:** Se utiliza para pruebas de hipótesis sobre la igualdad de dos varianzas poblacionales. Es la base del Análisis de la Varianza (ANOVA).

*   **Prueba H de Kruskal-Wallis:**
    *   **Propósito:** Comparar las medianas de **tres o más poblaciones independientes**. Es el análogo no paramétrico del ANOVA de un factor.
    *   **Lógica:** Generaliza la idea de la prueba de Mann-Whitney. Combina todos los datos de todos los grupos, les asigna rangos y luego calcula la suma de rangos para cada grupo. Compara la variabilidad de las sumas de rangos entre los grupos con la variabilidad que se esperaría por azar.
    *   **Estadístico de Prueba (H):** Se basa en las sumas de rangos de cada grupo. Si las poblaciones son idénticas, H es pequeño. Si al menos una población es diferente, H tiende a ser grande. Bajo $H_0$, el estadístico H sigue aproximadamente una distribución Chi-Cuadrado con $k-1$ grados de libertad (donde $k$ es el número de grupos).

*   **Prueba HSD de Tukey (Honest Significant Difference):** Una de las pruebas post-hoc más comunes y recomendadas. Calcula un único valor crítico (la "diferencia honestamente significativa") para evaluar las diferencias entre todas las posibles parejas de medias. Es más potente que otras pruebas como Bonferroni cuando los tamaños de muestra son iguales.

*   **Prueba No Paramétrica (o de Distribución Libre):** Un método de inferencia estadística que no requiere supuestos sobre la forma de la distribución de probabilidad de la población de la cual se extraen los datos.

*   **Prueba t (o t de Student):** Una prueba de hipótesis que utiliza el estadístico t y la distribución t. Se usa para pruebas sobre medias cuando la varianza poblacional ($\sigma^2$) es desconocida y se estima con la varianza muestral ($S^2$). La distribución t tiene en cuenta la incertidumbre adicional de estimar $\sigma^2$.

*   **Prueba Unilateral (o de una cola):** Una prueba en la que la hipótesis alternativa especifica una dirección (e.g., $H_1: \mu > 50$ o $H_1: \mu < 50$). La región de rechazo se encuentra en una sola de las colas de la distribución del estadístico de prueba.

*   **Prueba Z:** Una prueba de hipótesis que utiliza el estadístico Z y la distribución normal estándar. Se usa típicamente para pruebas sobre medias cuando la varianza poblacional ($\sigma^2$) es conocida, o para pruebas sobre proporciones con muestras grandes.

*   **Pruebas Post-Hoc (o de Comparaciones Múltiples):** Pruebas estadísticas que se realizan **después** de que un ANOVA ha arrojado un resultado significativo. Su objetivo es determinar qué pares específicos de medias de grupo son significativamente diferentes entre sí.

*   **Rango:** La posición numérica que ocupa una observación dentro de un conjunto de datos cuando estos se ordenan de menor a mayor. Es la base de la mayoría de las pruebas no paramétricas.

*   **Realización (o Trayectoria):** Una única secuencia de valores observados del proceso estocástico a lo largo del tiempo. Es una de las posibles "rutas" que el proceso puede seguir.

*   **Región de Rechazo (o Región Crítica):** El conjunto de valores del estadístico de prueba que llevan al rechazo de la hipótesis nula. Su área total es igual a $\alpha$.

*   **Suma de Cuadrados del Error (SCE) (o Dentro de los Grupos):** Mide la variabilidad "no explicada" o aleatoria. Cuantifica la dispersión de las observaciones individuales ($X_{ij}$) respecto a la media de su propio grupo ($\bar{X}_i$).
    $$ SCE = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)^2 $$
    Tiene $N-k$ grados de libertad.

*   **Suma de Cuadrados del Tratamiento (SCTr) (o Entre Grupos):** Mide la variabilidad que es "explicada" por el factor. Cuantifica la dispersión de las medias de cada grupo ($\bar{X}_i$) respecto a la gran media ($\bar{\bar{X}}$), ponderada por el tamaño de cada grupo.
    $$ SCTr = \sum_{i=1}^{k} n_i (\bar{X}_i - \bar{\bar{X}})^2 $$
    Tiene $k-1$ grados de libertad.

*   **Suma de Cuadrados Total (SCT):** Mide la variabilidad total de los datos. Se calcula como la suma de las desviaciones al cuadrado de cada observación individual ($X_{ij}$) respecto a la gran media ($\bar{\bar{X}}$).
    $$ SCT = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{\bar{X}})^2 $$
    Tiene $N-1$ grados de libertad, donde $N$ es el número total de observaciones.

*   **Suficiente:** Un estimador es suficiente si utiliza toda la información relevante contenida en la muestra sobre el parámetro.

*   **Supuestos de ANOVA:**
    1.  **Independencia:** Las observaciones deben ser independientes entre sí.
    2.  **Normalidad:** Las poblaciones de las que se extraen las muestras deben seguir una distribución normal.
    3.  **Homocedasticidad (Igualdad de Varianzas):** Todas las poblaciones de los grupos deben tener la misma varianza ($\sigma^2_1 = \sigma^2_2 = ... = \sigma^2_k$). Este es un supuesto crítico.

*   **Tabla ANOVA:** Una tabla que resume los resultados del análisis. Es el formato estándar para reportar un ANOVA e incluye las fuentes de variación (Tratamiento, Error, Total), las sumas de cuadrados, los grados de libertad, los cuadrados medios, el estadístico F y, a menudo, el p-valor.

*   **Tabla de Contingencia (o Tabla de Doble Entrada):** Una tabla utilizada para mostrar la distribución de frecuencias de dos variables categóricas simultáneamente. Las filas corresponden a las categorías de una variable y las columnas a las categorías de la otra. La celda en la intersección de una fila y una columna muestra la frecuencia conjunta de esas dos categorías.

*   **Tasa de Error Familiar (o Tasa de Error Experimental, $\alpha_{FW}$):** La probabilidad de cometer **al menos un** Error de Tipo I en el conjunto (la "familia") de todas las comparaciones que se realizan. Las pruebas post-hoc están diseñadas para controlar esta tasa de error, manteniéndola en el nivel de significancia deseado (e.g., 0.05).

*   **Tasa de Error por Comparación ($\\alpha_{PC}$):** La probabilidad de cometer un Error de Tipo I en una única comparación de pares. Es el $\alpha$ que se usaría en una prueba t simple.

*   **Teorema Central del Límite (TCL):** Establece que, para una población con media $\mu$ y varianza $\sigma^2$, la distribución de muestreo de la media muestral $\bar{X}$ se aproxima a una distribución normal con media $\mu$ y varianza $\frac{\sigma^2}{n}$ cuando el tamaño de la muestra $n$ es suficientemente grande ($n \ge 30$ es una regla común), independientemente de la forma de la distribución de la población original.

*   **Tiempo Discreto/Continuo:**
    *   **Tiempo Discreto:** El parámetro $t$ toma valores de un conjunto contable (e.g., $t = 0, 1, 2, ...$). El proceso se observa en instantes específicos.
    *   **Tiempo Continuo:** El parámetro $t$ toma valores de un intervalo continuo (e.g., $t \ge 0$). El proceso se observa en todo momento.

*   **Unidad Experimental:** La entidad física o sujeto al que se le aplica un tratamiento. Ejemplo: una parcela de tierra, un paciente, un lote de producción.

*   **Valor Crítico:** El punto de corte en la distribución del estadístico de prueba que define la región de rechazo. Si el estadístico de prueba es más extremo que el valor crítico, se rechaza $H_0$. Se obtiene de las tablas de distribución (Z, t, $\\chi^2$, F) para un $\alpha$ dado.

*   **Variable de Respuesta:** La variable continua (cuantitativa) que se mide para cada observación y que se utiliza para evaluar el efecto de los tratamientos. Por ejemplo, la "puntuación en el examen".

*   **Vector de Estado (o Vector de Probabilidad):** Un vector fila, $\pi^{(t)}$, cuyos componentes son las probabilidades de que el proceso se encuentre en cada uno de los estados en el tiempo $t$. La suma de sus componentes es 1.
