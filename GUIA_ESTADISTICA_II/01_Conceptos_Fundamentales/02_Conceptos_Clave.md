# Unidad 1: Conceptos Clave

A continuación, se definen los conceptos esenciales de esta unidad. La comprensión profunda de cada uno es un requisito no negociable para avanzar en la materia.

---

### 1. Población y Parámetro

- **Población:** Es la totalidad de elementos o individuos sobre los que se desea realizar un estudio. Puede ser finita o infinita. Es el "universo" de interés.
- **Parámetro ($\theta$):** Es una medida numérica que describe una característica de la **población**. Es un valor **fijo y constante**, pero usualmente **desconocido**. La meta de la inferencia es estimarlo.
    - **Ejemplos de Parámetros:**
        - $\mu$: Media poblacional (el verdadero promedio de todos los elementos).
        - $\sigma^2$: Varianza poblacional (la verdadera variabilidad de todos los elementos).
        - $p$: Proporción poblacional (la verdadera proporción de elementos con una característica).

---

### 2. Muestra y Estimador

- **Muestra:** Es un subconjunto **representativo** de la población que se selecciona para el análisis. La calidad de la inferencia depende críticamente de la representatividad de la muestra.
- **Muestreo Aleatorio Simple (MAS):** Es el método de selección de muestras que asegura que cada posible muestra de tamaño `n` tiene la misma probabilidad de ser seleccionada. Esto es fundamental para la validez de las técnicas que estudiaremos.
- **Estimador o Estadístico ($\hat{\theta}$):** Es una **variable aleatoria** cuya fórmula depende de los datos de la muestra. Se utiliza para obtener una aproximación (estimación) del parámetro poblacional.
    - **Ejemplos de Estimadores:**
        - $\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$: Media muestral, estimador de $\mu$.
        - $S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})^2$: Varianza muestral (insesgada), estimador de $\sigma^2$.
        - $\hat{p} = \frac{X}{n}$: Proporción muestral, estimador de $p$.

- **Estimación:** Es el **valor numérico** específico que toma el estimador después de haber recolectado y procesado una muestra concreta. Por ejemplo, si $\bar{X}$ es el estimador, `25.4` podría ser la estimación.

---

### 3. Propiedades de los Estimadores

#### a. Insesgadez (Falta de Sesgo)

Un estimador $\hat{\theta}$ es **insesgado** si su esperanza matemática (el promedio de todas las posibles estimaciones que podría producir) es igual al verdadero valor del parámetro $\theta$.

$$ E(\hat{\theta}) = \theta $$

- **Significado:** El estimador no tiene una tendencia sistemática a sobreestimar o subestimar el parámetro. Sus errores se cancelan en promedio.
- **Ejemplo:** $E(\bar{X}) = \mu$. La media muestral es un estimador insesgado de la media poblacional.

#### b. Eficiencia

Dados dos estimadores insesgados, $\hat{\theta}_1$ y $\hat{\theta}_2$, para el mismo parámetro $\theta$, se dice que $\hat{\theta}_1$ es **más eficiente** que $\hat{\theta}_2$ si su varianza es menor.

$$ Var(\hat{\theta}_1) < Var(\hat{\theta}_2) $$

- **Significado:** Un estimador más eficiente produce estimaciones que están, en promedio, más cerca del valor real del parámetro. Es más preciso.
- **Error Cuadrático Medio (ECM):** Es una medida que combina el sesgo y la varianza: $ECM(\hat{\theta}) = Var(\hat{\theta}) + [Sesgo(\hat{\theta})]^2$. Para estimadores insesgados, el ECM es simplemente la varianza. El mejor estimador es el que minimiza el ECM.

#### c. Consistencia

Un estimador $\hat{\theta}$ es **consistente** si el valor de la estimación se acerca cada vez más al verdadero valor del parámetro a medida que el tamaño de la muestra (`n`) tiende a infinito.

$$ \lim_{n \to \infty} P(|\hat{\theta}_n - \theta| < \epsilon) = 1 \quad \forall \epsilon > 0 $$

- **Significado:** Si tenemos suficientes datos, la estimación será prácticamente idéntica al parámetro. Es una propiedad asintótica (de muestras grandes) y es fundamental para la confianza en nuestros resultados.

---

### 4. Distribución de Muestreo

Es la **distribución de probabilidad de un estimador**. Imaginen que tomamos todas las muestras posibles de tamaño `n` de una población, calculamos un estimador (como $\bar{X}$) para cada muestra, y luego hacemos un histograma de todos esos valores. Ese histograma representa la distribución de muestreo del estimador.

- **¿Por qué es crucial?** Porque para hacer inferencias (como un intervalo de confianza), necesitamos saber cómo se comporta el estimador. La distribución de muestreo nos dice qué valores del estimador son probables y cuáles no, permitiéndonos cuantificar la incertidumbre del muestreo.

- **Error Estándar:** Es la **desviación estándar de la distribución de muestreo de un estimador**. Mide la variabilidad promedio del estimador entre diferentes muestras. Un error estándar más pequeño implica una estimación más precisa.
    - **Error Estándar de la Media:** $\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}