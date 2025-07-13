# Unidad 3: Teoremas y Desarrollos Matemáticos

El pilar matemático de ANOVA es el teorema que permite descomponer la variabilidad total de un conjunto de datos en fuentes distintas. Entender esta descomposición es entender ANOVA.

---

### Teorema Fundamental del Análisis de la Varianza (Descomposición de la Suma de Cuadrados)

**Enunciado:** La Suma de Cuadrados Total (SCT) se puede descomponer aditivamente en la Suma de Cuadrados del Tratamiento (SCTr) y la Suma de Cuadrados del Error (SCE).

$$ SCT = SCTr + SCE $$

$$ \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{\bar{X}})^2 = \sum_{i=1}^{k} n_i (\bar{X}_i - \bar{\bar{X}})^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)^2 $$

**Demostración:**
El truco de la demostración es tomar la desviación total de una observación ($X_{ij} - \bar{\bar{X}}$), y sumar y restar la media de su grupo, $\bar{X}_i$, para luego desarrollar el cuadrado.

1.  **Partimos de la desviación total y aplicamos el truco:**
    $$(X_{ij} - \bar{\bar{X}}) = (X_{ij} - \bar{X}_i + \bar{X}_i - \bar{\bar{X}}) = (X_{ij} - \bar{X}_i) + (\bar{X}_i - \bar{\bar{X}})$$
    Aquí hemos separado la desviación total en dos partes: la desviación de la observación a la media de su grupo (componente de error) y la desviación de la media del grupo a la gran media (componente de tratamiento).

2.  **Elevamos al cuadrado ambos lados:**
    $$(X_{ij} - \bar{\bar{X}})^2 = \left[ (X_{ij} - \bar{X}_i) + (\bar{X}_i - \bar{\bar{X}}) \right]^2$$
    Usando $(a+b)^2 = a^2 + 2ab + b^2$, obtenemos:
    $$(X_{ij} - \bar{\bar{X}})^2 = (X_{ij} - \bar{X}_i)^2 + 2(X_{ij} - \bar{X}_i)(\bar{X}_i - \bar{\bar{X}}) + (\bar{X}_i - \bar{\bar{X}})^2$$

3.  **Aplicamos la doble sumatoria a toda la ecuación para obtener la SCT:**
    $$ \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{\bar{X}})^2 = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} 2(X_{ij} - \bar{X}_i)(\bar{X}_i - \bar{\bar{X}}) + \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{X}_i - \bar{\bar{X}})^2 $$

4.  **Analizamos cada término:**
    *   **Primer término:** Es, por definición, la Suma de Cuadrados del Error (SCE).
        $$ \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)^2 = SCE $$
    *   **Tercer término:** El término $(\bar{X}_i - \bar{\bar{X}})^2$ es una constante para la sumatoria interna (sobre $j$). Por lo tanto, la suma interna es $n_i (\bar{X}_i - \bar{\bar{X}})^2$. Esto nos deja con la definición de la Suma de Cuadrados del Tratamiento (SCTr).
        $$ \sum_{i=1}^{k} n_i (\bar{X}_i - \bar{\bar{X}})^2 = SCTr $$
    *   **Segundo término (el producto cruzado):** Este término es la clave. Vamos a demostrar que es igual a cero.
        $$ \sum_{i=1}^{k} \sum_{j=1}^{n_i} 2(X_{ij} - \bar{X}_i)(\bar{X}_i - \bar{\bar{X}}) $$
        Podemos sacar las constantes de la sumatoria interna ($j$):
        $$ \sum_{i=1}^{k} 2(\bar{X}_i - \bar{\bar{X}}) \left[ \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i) \right] $$
        El término dentro del corchete, $\sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)$, es la suma de las desviaciones de las observaciones de un grupo con respecto a su propia media. Una propiedad fundamental de la media es que esta suma **siempre es cero**.
        $$ \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i) = \sum X_{ij} - \sum \bar{X}_i = n_i \bar{X}_i - n_i \bar{X}_i = 0 $$
        Por lo tanto, todo el producto cruzado se anula.

5.  **Juntamos los resultados:**
    La ecuación del paso 3 se simplifica a:
    $$ SCT = SCE + 0 + SCTr $$
    $$ SCT = SCTr + SCE $$

**Conclusión y Porqué es Importante:**
Esta demostración prueba que la variabilidad total en un conjunto de datos se puede partir limpiamente en dos piezas: una parte que se debe a las diferencias *entre* los grupos (el efecto que estudiamos) y otra parte que se debe a la variabilidad natural *dentro* de los grupos (el error aleatorio). Esta partición es lo que nos permite construir el cociente F para comparar estas dos fuentes de varianza y decidir si el efecto del tratamiento es significativamente mayor que el ruido de fondo.

### Valor Esperado de los Cuadrados Medios

Un resultado teórico crucial para entender por qué funciona el estadístico F es el de los valores esperados de los cuadrados medios.

*   **Valor Esperado del Cuadrado Medio del Error (CME):**
    $$ E(CME) = \sigma^2 $$
    El CME es **siempre** un estimador insesgado de la varianza poblacional común, $\sigma^2$, sin importar si $H_0$ es verdadera o no. Representa el "ruido" de fondo.

*   **Valor Esperado del Cuadrado Medio del Tratamiento (CMTr):**
    $$ E(CMTr) = \sigma^2 + \frac{\sum n_i (\mu_i - \mu)^2}{k-1} $$
    Donde $\mu_i$ son las medias poblacionales de los grupos y $\mu$ es la gran media poblacional.

**Análisis de E(CMTr):**
*   **Si $H_0$ es verdadera:** Todas las medias poblacionales son iguales ($\mu_1 = \mu_2 = ... = \mu$), por lo que el segundo término se anula. En este caso, $E(CMTr) = \sigma^2$. Tanto CMTr como CME estiman la misma cantidad.
*   **Si $H_0$ es falsa:** Al menos una $\mu_i$ es diferente, por lo que el segundo término es un valor positivo. Esto significa que $E(CMTr) > \sigma^2$. El CMTr sobreestima la varianza poblacional porque incluye la variabilidad del tratamiento además de la del error.

**El Cociente F:**
$$ F = \frac{CMTr}{CME} $$
Bajo $H_0$, esperamos que $F \approx \frac{\sigma^2}{\sigma^2} = 1$.
Bajo $H_1$, esperamos que $F > 1$.

Esto justifica por qué una valor grande de F es evidencia en contra de la hipótesis nula.
