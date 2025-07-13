# Unidad 6: Resumen de ANOVA y Diseños Experimentales

Esta unidad expande los conceptos de ANOVA vistos en la Unidad 3 para abordar situaciones experimentales más complejas y realistas. Mientras que el ANOVA de un factor es útil, a menudo necesitamos controlar otras fuentes de variabilidad o estudiar el efecto de múltiples factores simultáneamente.

---

### 1. Más Allá del ANOVA Simple: La Necesidad de Mejores Diseños

El ANOVA de un factor (o diseño completamente al azar) asume que toda la variabilidad no explicada por los tratamientos es "ruido" aleatorio. Sin embargo, en muchos experimentos, existen otras fuentes de variabilidad conocidas que pueden oscurecer el efecto real del tratamiento que nos interesa. Los diseños experimentales avanzados nos permiten aislar y remover estas fuentes de variabilidad, haciendo que la prueba sea más precisa y potente.

### 2. Diseño de Bloques Completos al Azar (DBCA)

*   **Propósito:** Controlar **una** fuente de variabilidad externa (un "factor de bloqueo" o "variable de molestia"). Se usa cuando las unidades experimentales no son homogéneas.
*   **Lógica:** Se agrupan las unidades experimentales en **bloques** homogéneos. Dentro de cada bloque, las unidades son lo más parecidas posible entre sí. Luego, todos los tratamientos se asignan al azar a las unidades dentro de cada bloque. De esta forma, las comparaciones entre tratamientos se hacen dentro de un entorno más controlado, eliminando la variabilidad que existe *entre* los bloques.
*   **Ejemplo:** Se quiere probar la eficacia de 4 fertilizantes (tratamientos) en el crecimiento de plantas. Se sabe que la calidad del suelo varía de una zona a otra del campo. Se divide el campo en 5 zonas (bloques) según su calidad. En cada zona, se plantan 4 parcelas y se asigna aleatoriamente cada uno de los 4 fertilizantes a una parcela.
*   **Análisis:** El ANOVA para un DBCA descompone la Suma de Cuadrados Total (SCT) en tres partes:
    $$ SCT = SCTr (Tratamientos) + SCB (Bloques) + SCE (Error) $$
    Al aislar la Suma de Cuadrados de los Bloques (SCB), se reduce la Suma de Cuadrados del Error (SCE). Un SCE más pequeño resulta en un Cuadrado Medio del Error (CME) más pequeño, lo que a su vez produce un **estadístico F más grande** para el tratamiento, aumentando la potencia de la prueba.

### 3. Diseños Factoriales

*   **Propósito:** Estudiar el efecto de **dos o más factores** (variables independientes) sobre una variable de respuesta, y, lo que es más importante, analizar si existe una **interacción** entre ellos.
*   **Lógica:** En lugar de hacer un experimento para cada factor, un diseño factorial prueba todas las combinaciones posibles de los niveles de todos los factores.
*   **Ejemplo:** Un ingeniero quiere estudiar el efecto de la **Temperatura** (niveles: 100°, 150°, 200°) y la **Presión** (niveles: 50 psi, 100 psi) sobre la resistencia de un material. Un diseño factorial completo probaría las $3 \times 2 = 6$ combinaciones de tratamiento.
*   **Interacción:** Ocurre una interacción cuando el efecto de un factor sobre la variable de respuesta **depende del nivel** del otro factor. Por ejemplo, puede que aumentar la temperatura solo aumente la resistencia cuando la presión es alta, pero no cuando es baja. Este es un concepto crucial que no se puede estudiar analizando cada factor por separado.
*   **Análisis:** Un ANOVA de dos factores descompone la SCT en:
    $$ SCT = SCA (Factor A) + SCB (Factor B) + SCAB (Interacción) + SCE (Error) $$
    Se calculan tres estadísticos F: uno para probar el efecto principal del Factor A, otro para el Factor B y un tercero para probar la significancia de la interacción AB.

### 4. ¿Y si ANOVA es Significativo? Pruebas Post-Hoc

Rechazar la hipótesis nula en un ANOVA solo nos dice que **al menos una media es diferente**, pero no nos dice **cuál o cuáles**. Para responder a esta pregunta, se utilizan las **pruebas de comparaciones múltiples** o **pruebas post-hoc**.

*   **Propósito:** Realizar comparaciones par a par entre las medias de los grupos después de que un ANOVA ha resultado significativo, controlando el error de Tipo I global.
*   **Pruebas Comunes:**
    *   **Prueba de Tukey (o HSD - Honest Significant Difference):** Una de las más populares. Compara todas las posibles parejas de medias y es muy buena para controlar el error de Tipo I cuando los tamaños de muestra son iguales.
    *   **Corrección de Bonferroni:** Un método muy simple y conservador. Divide el nivel de significancia $\alpha$ por el número de comparaciones que se van a hacer. Es muy estricto y puede tener baja potencia.
