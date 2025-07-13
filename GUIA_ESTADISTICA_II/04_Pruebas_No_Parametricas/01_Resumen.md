# Unidad 4: Resumen de Pruebas No Paramétricas

Esta unidad representa un cambio de paradigma fundamental. Hasta ahora, todas las pruebas (Z, t, F) se basaban en supuestos estrictos sobre la distribución de la población subyacente, principalmente el supuesto de **normalidad**. Estas se conocen como **pruebas paramétricas** porque prueban hipótesis sobre parámetros (como $\mu$ o $\sigma^2$).

Pero, ¿qué sucede si no podemos asumir que nuestros datos provienen de una población normal? ¿O si nuestros datos no son numéricos, sino ordinales (rangos, clasificaciones)? Aquí es donde entran en juego las **pruebas no paramétricas**.

---

### 1. ¿Por qué usar Pruebas No Paramétricas?

Las pruebas no paramétricas, también llamadas de distribución libre, son métodos que **no requieren supuestos sobre la forma de la distribución de la población**. Son la herramienta de elección en las siguientes situaciones:

*   **Fallo del Supuesto de Normalidad:** Si una prueba de normalidad (como Shapiro-Wilk) o un gráfico (Q-Q plot) indican que los datos no siguen una distribución normal, especialmente con muestras pequeñas ($n < 30$).
*   **Datos Ordinales:** Cuando los datos representan rangos, órdenes o clasificaciones (e.g., "bajo", "medio", "alto"; clasificaciones de satisfacción del 1 al 5). En estos casos, calcular una media no tiene sentido, pero sí podemos ordenar los datos.
*   **Presencia de Outliers Extremos:** Las pruebas paramétricas como la prueba t son sensibles a los valores atípicos. Las pruebas no paramétricas, al basarse en rangos, son mucho más robustas a la presencia de outliers.
*   **Muestras Muy Pequeñas:** Con muy pocos datos, es difícil verificar el supuesto de normalidad, por lo que una prueba no paramétrica puede ser una opción más segura.

### 2. La Lógica del Rango

La mayoría de las pruebas no paramétricas superan el problema de la distribución desconocida transformando los datos. En lugar de trabajar con los valores numéricos originales, trabajan con sus **rangos** (su posición si se ordenaran de menor a mayor).

Al convertir los datos a rangos, se pierde algo de información (la magnitud de las diferencias), pero se gana una enorme ventaja: la distribución de los rangos es conocida y predecible, sin importar cómo era la distribución original de los datos. Esto nos permite construir estadísticos de prueba y calcular p-valores.

### 3. El Costo: Eficiencia y Potencia

Las pruebas no paramétricas no son una solución mágica. Tienen un costo:

*   **Si los supuestos de la prueba paramétrica se cumplen (especialmente la normalidad), la prueba paramétrica siempre será más potente.** Esto significa que la prueba paramétrica (e.g., la prueba t) tendrá una mayor probabilidad de detectar un efecto real que su contraparte no paramétrica (e.g., Wilcoxon).
*   Se dice que las pruebas no paramétricas son menos "eficientes" porque a menudo requieren un tamaño de muestra mayor para alcanzar la misma potencia que una prueba paramétrica.

**Regla de oro:** Usa la prueba paramétrica si sus supuestos se cumplen. Si no, la prueba no paramétrica es la alternativa correcta y válida.

### 4. Las Pruebas Clave de esta Unidad

Cada prueba paramétrica que hemos visto tiene su análogo no paramétrico:

| Situación de Prueba                               | Prueba Paramétrica (si hay normalidad) | Prueba No Paramétrica (alternativa)          |
| ------------------------------------------------- | -------------------------------------- | -------------------------------------------- |
| **Una muestra** (prueba sobre la mediana)         | Prueba t para una muestra              | Prueba de los Signos, Prueba de Wilcoxon     |
| **Dos muestras independientes** (comparar grupos) | Prueba t para muestras independientes  | Prueba de Mann-Whitney (o U de Wilcoxon)     |
| **Dos muestras pareadas** (antes/después)         | Prueba t para muestras pareadas        | Prueba de los Signos, Prueba de Wilcoxon     |
| **Más de dos muestras independientes**            | ANOVA de un factor                     | Prueba de Kruskal-Wallis                     |
| **Aleatoriedad de una secuencia**                 | (No hay un análogo directo)            | Prueba de Rachas                             |

Esta unidad se dedicará a estudiar cómo se calculan y se interpretan cada una de estas alternativas no paramétricas.
