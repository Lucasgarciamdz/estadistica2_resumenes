# Unidad 4: Detalles Matemáticos para el Profesor Exigente

Esta sección profundiza en los "porqués" de los desarrollos matemáticos de la Unidad 4 (Pruebas No Paramétricas), abordando los puntos que un profesor detallista podría preguntar para evaluar una comprensión más allá de la mera memorización.

---

### 1. La Lógica de los Rangos: ¿Por qué y qué se gana/pierde?

**Contexto:** La mayoría de las pruebas no paramétricas operan sobre los rangos de los datos en lugar de los valores originales.

**El Detalle Fino:**
*   **Ganancia (Robustez y Validez):** Al transformar los datos a rangos, eliminamos la dependencia de la forma específica de la distribución de la población. La distribución de los rangos es conocida y predecible (generalmente uniforme si la hipótesis nula es verdadera), lo que permite construir estadísticos de prueba y calcular p-valores sin asumir normalidad. Esto hace que las pruebas no paramétricas sean robustas a la no normalidad y a la presencia de valores atípicos (outliers).
*   **Pérdida (Información y Potencia):** Al usar rangos, se pierde información sobre la **magnitud** de las diferencias entre las observaciones. Por ejemplo, la diferencia entre 1 y 2 es la misma que entre 100 y 101 en términos de rango, pero no en magnitud. Esta pérdida de información se traduce en una menor **potencia** de la prueba si los supuestos de la prueba paramétrica análoga (como la normalidad) se cumplen. Es decir, si los datos son normales, una prueba paramétrica tendrá una mayor probabilidad de detectar un efecto real.

**¿Por qué es importante para el profesor?**
*   Demuestra una comprensión del fundamento de las pruebas no paramétricas y su razón de ser.
*   Resalta el "trade-off" entre robustez y potencia, un concepto clave en la elección de la prueba estadística adecuada.

---

### 2. Manejo de Empates (Ties) en la Asignación de Rangos

**Contexto:** ¿Qué sucede cuando dos o más observaciones tienen el mismo valor y, por lo tanto, deberían tener el mismo rango?

**El Detalle Fino:** Cuando hay empates, la práctica estándar es asignar el **rango promedio** a cada una de las observaciones empatadas. Por ejemplo, si los valores 5, 6, 6, 7 se van a clasificar y el 6 ocupa las posiciones 2 y 3, a ambos 6 se les asigna el rango $(2+3)/2 = 2.5$.

**¿Por qué es importante para el profesor?**
*   Muestra atención al detalle en el procedimiento de cálculo. Un manejo incorrecto de los empates puede alterar el estadístico de prueba y el p-valor.
*   Aunque la mayoría del software estadístico lo maneja automáticamente, entender el principio demuestra una comprensión más profunda del algoritmo subyacente.

---

### 3. Aproximaciones a la Normal o Chi-Cuadrado: ¿Cuándo y por qué?

**Contexto:** Para muestras grandes, los estadísticos de prueba no paramétricos (como W de Wilcoxon, U de Mann-Whitney, H de Kruskal-Wallis) a menudo se aproximan a distribuciones conocidas (Normal o Chi-Cuadrado).

**El Detalle Fino:**
*   **Base Combinatoria:** Para muestras pequeñas, la distribución exacta de estos estadísticos se deriva de la combinatoria de todas las posibles asignaciones de rangos bajo la hipótesis nula. Estas distribuciones son discretas y están tabuladas.
*   **Convergencia Asintótica:** A medida que el tamaño de la muestra aumenta, la distribución de estos estadísticos se vuelve más suave y se aproxima a una distribución continua conocida. Esto es análogo al Teorema Central del Límite, donde la suma de muchas variables aleatorias (en este caso, los rangos) tiende a una distribución normal.
*   **Condiciones de Aproximación:** Generalmente, se requieren tamaños de muestra mínimos (e.g., $n > 20$ para Wilcoxon, $n_1, n_2 > 10$ para Mann-Whitney, $n_i > 5$ para Kruskal-Wallis) para que estas aproximaciones sean válidas. Si los tamaños de muestra son muy pequeños, se deben usar las tablas de distribución exactas.

**¿Por qué es importante para el profesor?**
*   Demuestra que entiendes la base teórica detrás de las pruebas no paramétricas y por qué se usan tablas diferentes para muestras pequeñas y grandes.
*   Resalta la conexión con conceptos de probabilidad y el comportamiento asintótico de los estadísticos.

---

### 4. Eficiencia Relativa: El "Costo" de la Robustez

**Contexto:** Las pruebas no paramétricas son robustas, pero a menudo menos eficientes que sus contrapartes paramétricas.

**El Detalle Fino:** La eficiencia relativa de una prueba no paramétrica se refiere a la proporción del tamaño de muestra que se necesita para que la prueba no paramétrica tenga la misma potencia que la prueba paramétrica análoga, *cuando los supuestos de la prueba paramétrica se cumplen*. Por ejemplo, la eficiencia relativa de la prueba de Mann-Whitney respecto a la prueba t es de aproximadamente 0.95 para distribuciones normales. Esto significa que la prueba de Mann-Whitney necesita una muestra un 5% más grande para alcanzar la misma potencia que la prueba t, si los datos son normales.

**¿Por qué es importante para el profesor?**
*   Muestra una comprensión matizada de la elección de la prueba. No es que una sea "mejor" que la otra en todas las circunstancias, sino que hay un compromiso.
*   Subraya que la robustez (validez bajo menos supuestos) a menudo viene con un costo en términos de potencia (capacidad para detectar efectos reales).
