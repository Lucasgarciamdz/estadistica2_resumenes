# Formulario Consolidado de Fórmulas y Estadísticos - Estadística Aplicada II

Este formulario compila las fórmulas y estadísticos más importantes de cada unidad. Es una herramienta de referencia rápida para el estudio y la resolución de problemas.

---

## Unidad 1: Conceptos Fundamentales

*   **Media Muestral:**
    $$ \bar{X} = \frac{1}{n}\sum_{i=1}^{n}X_i $$

*   **Varianza Muestral (Insesgada):**
    $$ S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2 $$

*   **Error Estándar de la Media:**
    $$ SE(\bar{X}) = \frac{\sigma}{\sqrt{n}} $$

*   **Teorema Central del Límite (TCL) para la Media Muestral:**
    $$ \bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{para } n \text{ grande} $$

---

## Unidad 2: Pruebas de Hipótesis

*   **Estadístico Z para la Media ($\sigma$ conocida):**
    $$ Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}} $$

*   **Estadístico t para la Media ($\sigma$ desconocida):**
    $$ t = \frac{\bar{X} - \mu_0}{S / \sqrt{n}} $$
    Grados de libertad: $gl = n-1$

*   **Estadístico Z para la Proporción (muestra grande):**
    $$ Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} $$

*   **Estadístico Chi-Cuadrado para la Varianza:**
    $$ \chi^2 = \frac{(n-1)S^2}{\sigma_0^2} $$
    Grados de libertad: $gl = n-1$

*   **Estadístico F para el Cociente de Varianzas:**
    $$ F = \frac{S_1^2}{S_2^2} $$
    Grados de libertad: $gl_1 = n_1-1$, $gl_2 = n_2-1$

---

## Unidad 3: Análisis de la Varianza (ANOVA)

*   **Teorema Fundamental de ANOVA:**
    $$ SCT = SCTr + SCE $$

*   **Suma de Cuadrados Total (SCT):**
    $$ SCT = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{\bar{X}})^2 $$

*   **Suma de Cuadrados del Tratamiento (SCTr):**
    $$ SCTr = \sum_{i=1}^{k} n_i (\bar{X}_i - \bar{\bar{X}})^2 $$

*   **Suma de Cuadrados del Error (SCE):**
    $$ SCE = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)^2 $$

*   **Cuadrado Medio del Tratamiento (CMTr):**
    $$ CMTr = \frac{SCTr}{k-1} $$

*   **Cuadrado Medio del Error (CME):**
    $$ CME = \frac{SCE}{N-k} $$

*   **Estadístico F para ANOVA:**
    $$ F = \frac{CMTr}{CME} $$
    Grados de libertad: $gl_1 = k-1$, $gl_2 = N-k$

---

## Unidad 4: Pruebas No Paramétricas

*   **Prueba de los Rangos con Signo de Wilcoxon (Aproximación Normal):**
    *   Media de W: $E(W) = \mu_W = \frac{n(n+1)}{4}$
    *   Varianza de W: $Var(W) = \sigma_W^2 = \frac{n(n+1)(2n+1)}{24}$
    *   Estadístico Z: $Z = \frac{W - \mu_W}{\sigma_W}$

*   **Prueba U de Mann-Whitney (Aproximación Normal):**
    *   Media de U: $E(U) = \mu_U = \frac{n_1 n_2}{2}$
    *   Varianza de U: $Var(U) = \sigma_U^2 = \frac{n_1 n_2 (n_1+n_2+1)}{12}$
    *   Estadístico Z: $Z = \frac{U - \mu_U}{\sigma_U}$

*   **Prueba H de Kruskal-Wallis:**
    $$ H = \left[ \frac{12}{N(N+1)} \sum_{i=1}^{k} \frac{R_i^2}{n_i} \right] - 3(N+1) $$
    Grados de libertad: $gl = k-1$

---

## Unidad 5: Bondad de Ajuste e Independencia

*   **Estadístico de Prueba Chi-Cuadrado ($\chi^2$):**
    $$ \chi^2 = \sum_{\text{todas las celdas}} \frac{(F_o - F_e)^2}{F_e} $$

*   **Frecuencia Esperada ($F_e$) para Bondad de Ajuste:**
    $$ F_{ei} = n \times p_i $$

*   **Grados de Libertad ($gl$) para Bondad de Ajuste:**
    $$ gl = k - 1 - m $$

*   **Frecuencia Esperada ($F_e$) para Independencia:**
    $$ F_{e,ij} = \frac{(\text{Total Fila } i) \times (\text{Total Columna } j)}{\text{Gran Total}} $$

*   **Grados de Libertad ($gl$) para Independencia:**
    $$ gl = (r-1)(c-1) $$

---

## Unidad 6: ANOVA y Diseños Experimentales

*   **Descomposición de SCT para DBCA:**
    $$ SCT = SCTr + SCB + SCE $$

*   **Grados de Libertad para DBCA:**
    *   $gl_{Tr} = k-1$
    *   $gl_{B} = b-1$
    *   $gl_{E} = (k-1)(b-1)$

*   **Descomposición de SCT para Diseño Factorial (dos factores A y B):**
    $$ SCT = SCA + SCB + SCAB + SCE $$

*   **Valor Crítico HSD de Tukey:**
    $$ HSD = q_{\alpha, k, gl_E} \sqrt{\frac{CME}{n}} $$

*   **Corrección de Bonferroni:**
    $$ \alpha_{ajustado} = \frac{\alpha_{FW}}{\text{nº de comparaciones}} $$

---

## Unidad 7: Procesos Estocásticos

*   **Evolución del Vector de Estado:**
    $$ \pi^{(t+1)} = \pi^{(t)} P $$
    $$ \pi^{(t+n)} = \pi^{(t)} P^n $$

*   **Ecuación de Chapman-Kolmogorov:**
    $$ P^{(n)} = P^n $$

*   **Ecuación para la Distribución Estacionaria ($\pi$):**
    $$ \pi P = \pi $$
    $$ \sum_{i=1}^{k} \pi_i = 1 $$
