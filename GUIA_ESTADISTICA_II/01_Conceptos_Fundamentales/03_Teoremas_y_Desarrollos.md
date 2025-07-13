# Unidad 1: Teoremas Fundamentales y Sus Desarrollos

Este documento se centra en el desarrollo matemático de los resultados teóricos que sustentan la inferencia estadística. La comprensión de estas demostraciones es crucial para justificar la aplicación de las fórmulas en la práctica.

---

## 1. Propiedades de la Media Muestral ($\bar{X}$)

Sea $X_1, X_2, ..., X_n$ una muestra aleatoria simple de una población con media $\mu$ y varianza $\sigma^2$.

### a. Esperanza de la Media Muestral (Demostración de Insesgadez)

El estimador $\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$ es **insesgado** para $\mu$.

**Desarrollo:**

Utilizamos las propiedades de la esperanza matemática. La esperanza de una suma es la suma de las esperanzas, y las constantes pueden salir del operador de esperanza.

$$ E[\bar{X}] = E\left[\frac{1}{n} \sum_{i=1}^{n} X_i\right] $$

$$ = \frac{1}{n} E\left[\sum_{i=1}^{n} X_i\right] \quad \text{(La constante 1/n sale fuera)} $$

$$ = \frac{1}{n} \sum_{i=1}^{n} E[X_i] \quad \text{(La esperanza de la suma es la suma de las esperanzas)} $$

Dado que cada $X_i$ es una observación de la población, la esperanza de cada $X_i$ es la media poblacional $\mu$.

$$ = \frac{1}{n} \sum_{i=1}^{n} \mu \quad \text{(Sustituimos E[X_i] por } \mu) $$

$$ = \frac{1}{n} (n \cdot \mu) \quad \text{(Sumamos } \mu \text{, n veces)} $$

$$ = \mu $$

**Conclusión:** Hemos demostrado que $E[\bar{X}] = \mu$. La media muestral es un estimador insesgado de la media poblacional.

### b. Varianza de la Media Muestral

La varianza del estimador $\bar{X}$ es $\frac{\sigma^2}{n}$.

**Desarrollo:**

Utilizamos las propiedades de la varianza. La varianza de una suma de variables **independientes** es la suma de sus varianzas.

$$ Var(\bar{X}) = Var\left(\frac{1}{n} \sum_{i=1}^{n} X_i\right) $$

Al sacar una constante de la varianza, esta sale elevada al cuadrado.

$$ = \frac{1}{n^2} Var\left(\sum_{i=1}^{n} X_i\right) $$

Como las observaciones $X_i$ en un muestreo aleatorio simple son independientes, la varianza de la suma es la suma de las varianzas.

$$ = \frac{1}{n^2} \sum_{i=1}^{n} Var(X_i) $$

La varianza de cada observación $X_i$ es la varianza de la población, $\sigma^2$.

$$ = \frac{1}{n^2} \sum_{i=1}^{n} \sigma^2 \quad \text{(Sustituimos Var(X_i) por } \sigma^2) $$

$$ = \frac{1}{n^2} (n \cdot \sigma^2) \quad \text{(Sumamos } \sigma^2 \text{, n veces)} $$

$$ = \frac{\sigma^2}{n} $$

**Conclusión:** La variabilidad de la media muestral disminuye a medida que aumenta el tamaño de la muestra `n`. Esto fundamenta la idea de que muestras más grandes producen estimaciones más precisas.

---

## 2. Teorema Central del Límite (TCL)

Este teorema es la justificación para asumir normalidad en la distribución de la media muestral para muestras grandes.

**Enunciado Formal:**

Si $X_1, X_2, ..., X_n$ es una muestra aleatoria de tamaño `n` tomada de una población con media $\mu$ y varianza finita $\sigma^2$, entonces la distribución de la variable aleatoria

$$ Z_n = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} $$

converge en distribución a una variable aleatoria Normal estándar $N(0,1)$ a medida que $n \to \infty$.

**Desarrollo Conceptual (Sin la demostración formal con funciones generadoras de momentos):**

1.  **Punto de Partida:** Tenemos una población cualquiera (puede ser uniforme, exponencial, bimodal, etc.), con su media $\mu$ y su varianza $\sigma^2$.
2.  **El Proceso:** Tomamos una muestra de tamaño `n` y calculamos su media, $\bar{X}_1$. Repetimos este proceso muchísimas veces, obteniendo $\bar{X}_2, \bar{X}_3, ...$
3.  **La Magia:** Si construimos un histograma con todas estas medias muestrales, la forma de ese histograma se parecerá cada vez más a una campana de Gauss (una distribución Normal) a medida que `n` (el tamaño de cada muestra) se hace más grande.
4.  **Parámetros de la Normal:** El teorema no solo nos dice que la forma es Normal, sino que también nos especifica sus parámetros:
    -   La media de esta distribución de medias muestrales será la media poblacional original, $\mu$.
    -   La varianza de esta distribución será la varianza poblacional dividida por el tamaño de la muestra, $\frac{\sigma^2}{n}$.

**Importancia Práctica:** El TCL nos permite usar la distribución Z (Normal estándar) para calcular probabilidades sobre $\bar{X}$ y construir intervalos de confianza, incluso cuando la distribución de la población es desconocida. La regla general es que una muestra de **n > 30** es a menudo suficiente para que la aproximación sea buena.

---

## 3. La Varianza Muestral ($S^2$) y el Factor `n-1`

Se define la varianza muestral insesgada como $S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})^2$.

**Pregunta Clave:** ¿Por qué dividimos por `n-1` en lugar de `n`?

**Respuesta (Desarrollo Conceptual):**

1.  **El Objetivo:** Queremos que el valor esperado de nuestro estimador de la varianza sea igual a la varianza poblacional, es decir, $E[S^2] = \sigma^2$.
2.  **El Problema:** Para calcular la varianza muestral, usamos $\bar{X}$ (la media muestral) en lugar de $\mu$ (la media poblacional, que es desconocida). La media muestral, $\bar{X}$, está calculada **a partir de los mismos datos** $X_i$. Por definición, la suma de las desviaciones respecto a la propia media muestral, $\sum(X_i - \bar{X})$, es siempre cero.
3.  **La Consecuencia:** Esto significa que las desviaciones $(X_i - \bar{X})$ no son completamente independientes. Si conocemos `n-1` de ellas, la última queda determinada. Se dice que tenemos **`n-1` grados de libertad**.
4.  **La Subestimación:** Se puede demostrar matemáticamente que la suma de las desviaciones al cuadrado respecto a la media muestral, $\sum(X_i - \bar{X})^2$, tiende a ser **ligeramente más pequeña** que la suma de las desviaciones al cuadrado respecto a la verdadera media poblacional, $\sum(X_i - \mu)^2$.
5.  **La Corrección de Bessel:** Si dividiéramos la suma de cuadrados por `n`, el estimador resultante estaría **sesgado hacia abajo**; en promedio, subestimaría la verdadera varianza $\sigma^2$. Al dividir por `n-1` (un número un poco más pequeño), estamos inflando ligeramente el resultado. Esta pequeña inflación es exactamente la cantidad necesaria para corregir la subestimación sistemática, logrando así que el estimador sea **insesgado**.

**En resumen:** Dividir por `n-1` es la corrección matemática necesaria para compensar el hecho de que estamos usando una estimación ($\bar{X}$) en lugar del verdadero parámetro ($\mu$) en el cálculo de la varianza, garantizando la propiedad de insesgadez.