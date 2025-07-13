# Unidad 2: Teoremas y Desarrollos Matemáticos

En esta sección se desglosa la construcción de los estadísticos de prueba más importantes. Entender su derivación es clave para saber cuándo y por qué se utiliza cada uno.

---

### 1. Construcción del Estadístico Z para la Media ($\sigma$ conocida)

**Contexto:** Queremos probar una hipótesis sobre la media poblacional $\mu$, y conocemos la varianza poblacional $\sigma^2$.

**Teorema Base:** El Teorema Central del Límite (TCL).
El TCL nos dice que, para una muestra grande, la distribución de muestreo de la media muestral ($\bar{X}$) sigue una distribución normal:

$$ \bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) $$

**Desarrollo del Estadístico:**
El objetivo de un estadístico de prueba es estandarizar el estimador ($ar{X}$) para que siga una distribución conocida (la normal estándar, N(0,1)) bajo la suposición de que $H_0$ es cierta.

1.  **Partimos de la distribución del estimador:** $\bar{X}$
2.  **Restamos la media de su distribución:** $\bar{X} - E(\bar{X}) = \bar{X} - \mu$
3.  **Dividimos por la desviación estándar de su distribución (el error estándar):** $\frac{\bar{X} - \mu}{SE(\bar{X})} = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}$

Este resultado, por definición de estandarización, sigue una distribución normal estándar:

$$ Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0,1) $$

**Aplicación en Pruebas de Hipótesis:**
Cuando formulamos la hipótesis nula, por ejemplo $H_0: \mu = \mu_0$, estamos **suponiendo** que el verdadero valor de $\mu$ es $\mu_0$. Por lo tanto, para calcular el estadístico de prueba bajo esta suposición, simplemente reemplazamos $\mu$ por $\mu_0$ en la fórmula:

$$ Z_{obs} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}} $$

Este valor $Z_{obs}$ nos dice cuántos errores estándar de distancia se encuentra nuestra media muestral observada ($\bar{X}$) del valor que hipotetizamos para la media poblacional ($\mu_0$). Si esta distancia es "grande" (es decir, si $Z_{obs}$ cae en la región de rechazo), concluimos que nuestra suposición inicial de que $\mu = \mu_0$ era incorrecta.

---

### 2. Construcción del Estadístico t para la Media ($\sigma$ desconocida)

**Contexto:** Es el caso más realista. Queremos probar una hipótesis sobre $\mu$, pero **no conocemos** la varianza poblacional $\sigma^2$. Debemos estimarla usando la varianza muestral $S^2$.

**El Problema:**
Si en la fórmula del estadístico Z simplemente reemplazamos la $\sigma$ desconocida por su estimador $S$, la distribución resultante ya no es exactamente una Normal Estándar.

$$ \frac{\bar{X} - \mu}{S / \sqrt{n}} \nsim N(0,1) $$

Esto se debe a que hemos introducido una nueva fuente de variabilidad: la estimación de $\sigma$ a través de $S$. $S$ es una variable aleatoria que cambiará de muestra en muestra. La distribución t de Student es la que describe correctamente esta nueva situación.

**Teorema (Definición de la distribución t de Student):**
Si $Z$ es una variable aleatoria Normal Estándar ($Z \sim N(0,1)$) y $U$ es una variable aleatoria Chi-Cuadrado con $k$ grados de libertad ($U \sim \chi^2_k$), y además $Z$ y $U$ son independientes, entonces la variable $T$ definida como:

$$ T = \frac{Z}{\sqrt{U/k}} $$

sigue una distribución t de Student con $k$ grados de libertad.

**Desarrollo del Estadístico t:**
Nuestro objetivo es mostrar que $\frac{\bar{X} - \mu}{S / \sqrt{n}}$ sigue esta estructura.

1.  **El Numerador (Z):** Ya sabemos que $Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}$ es $N(0,1)$.

2.  **El Denominador (U):** Hay un teorema fundamental que establece que, si la población es normal, la cantidad $\frac{(n-1)S^2}{\sigma^2}$ sigue una distribución Chi-Cuadrado con $n-1$ grados de libertad.
    $$ U = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1} $$

3.  **Armando el Estadístico T:** Sustituyamos estos componentes en la definición de la distribución t, con $k = n-1$ grados de libertad.
    $$ T = \frac{Z}{\sqrt{U/k}} = \frac{ \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} }{ \sqrt{ \frac{(n-1)S^2}{\sigma^2} / (n-1) } } = \frac{ \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} }{ \sqrt{ \frac{S^2}{\sigma^2} } } = \frac{ \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} }{ S / \sigma } = \frac{\bar{X} - \mu}{S / \sqrt{n}} $$

**Conclusión y Porqué es Importante:**
Hemos demostrado que la expresión que usamos para la prueba t sigue, en efecto, una distribución t de Student con $n-1$ grados de libertad. Esta distribución es similar a la normal pero con colas más "pesadas", lo que refleja la mayor incertidumbre al no conocer $\sigma$. La diferencia entre la t y la Z disminuye a medida que $n$ aumenta, porque con más datos, nuestra estimación $S$ se vuelve cada vez más precisa.

---

### 3. Relación entre Errores ($\alpha$ y $\beta$) y Potencia

*   **Compromiso (Trade-off):** Para un tamaño de muestra fijo, no se pueden disminuir ambos errores simultáneamente. Si se hace más estricto el criterio para rechazar $H_0$ (disminuyendo $\alpha$), se hace más difícil rechazarla, lo que aumenta la probabilidad de no rechazar una $H_0$ falsa (aumenta $\beta$).

*   **Potencia ($1-\beta$):** Es la probabilidad de tomar la decisión correcta cuando $H_1$ es verdadera. Depende de varios factores:
    *   **$\alpha$:** A mayor $\alpha$, mayor potencia.
    *   **Tamaño del efecto:** La diferencia real entre el parámetro poblacional y el valor nulo. Es más fácil detectar una diferencia grande que una pequeña.
    *   **Tamaño de la muestra ($n$):** A mayor $n$, el error estándar disminuye, y la prueba se vuelve más potente. **Aumentar el tamaño de la muestra es la forma más común de aumentar la potencia de una prueba.**
