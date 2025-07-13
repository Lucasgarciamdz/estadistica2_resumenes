# Unidad 3: Conceptos Clave

El vocabulario de ANOVA se centra en la descomposición de la varianza. Es esencial entender cada componente para interpretar correctamente los resultados.

---

*   **Factor:** La variable categórica independiente que se utiliza para definir los grupos o tratamientos que se están comparando. Por ejemplo, en un estudio que compara tres métodos de enseñanza, el "método de enseñanza" es el factor.

*   **Niveles (o Tratamientos):** Las diferentes categorías o valores que puede tomar el factor. Si el factor es "método de enseñanza", los niveles podrían ser "Método A", "Método B" y "Método C". El número de niveles se denota por $k$.

*   **Variable de Respuesta:** La variable continua (cuantitativa) que se mide para cada observación y que se utiliza para evaluar el efecto de los tratamientos. Por ejemplo, la "puntuación en el examen".

*   **Gran Media ($\bar{\bar{X}}$):** La media de todas las observaciones en el estudio, sin importar a qué grupo pertenecen.

*   **Hipótesis en ANOVA:**
    *   **Hipótesis Nula ($H_0$):** Las medias de todos los grupos (poblacionales) son iguales. No hay efecto del tratamiento. 
        $H_0: \mu_1 = \mu_2 = ... = \mu_k$
    *   **Hipótesis Alternativa ($H_1$):** No todas las medias son iguales. Al menos una media es diferente de las demás. Es importante notar que $H_1$ no dice que *todas* las medias son diferentes, solo que al menos dos de ellas lo son.

*   **Suma de Cuadrados Total (SCT):** Mide la variabilidad total de los datos. Se calcula como la suma de las desviaciones al cuadrado de cada observación individual ($X_{ij}$) respecto a la gran media ($\bar{\bar{X}}$).
    $$ SCT = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{\bar{X}})^2 $$
    Tiene $N-1$ grados de libertad, donde $N$ es el número total de observaciones.

*   **Suma de Cuadrados del Tratamiento (SCTr) (o Entre Grupos):** Mide la variabilidad que es "explicada" por el factor. Cuantifica la dispersión de las medias de cada grupo ($\bar{X}_i$) respecto a la gran media ($\bar{\bar{X}}$), ponderada por el tamaño de cada grupo.
    $$ SCTr = \sum_{i=1}^{k} n_i (\bar{X}_i - \bar{\bar{X}})^2 $$
    Tiene $k-1$ grados de libertad.

*   **Suma de Cuadrados del Error (SCE) (o Dentro de los Grupos):** Mide la variabilidad "no explicada" o aleatoria. Cuantifica la dispersión de las observaciones individuales ($X_{ij}$) respecto a la media de su propio grupo ($\bar{X}_i$).
    $$ SCE = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)^2 $$
    Tiene $N-k$ grados de libertad.

*   **Cuadrado Medio del Tratamiento (CMTr):** Es la varianza estimada entre los grupos. Se calcula como:
    $$ CMTr = \frac{SCTr}{k-1} $$

*   **Cuadrado Medio del Error (CME):** Es la varianza estimada dentro de los grupos. Representa la variabilidad aleatoria o "ruido". Se calcula como:
    $$ CME = \frac{SCE}{N-k} $$
    El CME es un estimador combinado (pooled) de la varianza poblacional común $\sigma^2$.

*   **Estadístico F:** El estadístico de prueba para ANOVA. Es el cociente de la varianza entre grupos y la varianza dentro de los grupos.
    $$ F = \frac{CMTr}{CME} $$
    Sigue una distribución F de Snedecor con $k-1$ (grados de libertad del numerador) y $N-k$ (grados de libertad del denominador) grados de libertad.

*   **Tabla ANOVA:** Una tabla que resume los resultados del análisis. Es el formato estándar para reportar un ANOVA e incluye las fuentes de variación (Tratamiento, Error, Total), las sumas de cuadrados, los grados de libertad, los cuadrados medios, el estadístico F y, a menudo, el p-valor.

*   **Supuestos de ANOVA:**
    1.  **Independencia:** Las observaciones deben ser independientes entre sí.
    2.  **Normalidad:** Las poblaciones de las que se extraen las muestras deben seguir una distribución normal.
    3.  **Homocedasticidad (Igualdad de Varianzas):** Todas las poblaciones de los grupos deben tener la misma varianza ($\sigma^2_1 = \sigma^2_2 = ... = \sigma^2_k$). Este es un supuesto crítico.
