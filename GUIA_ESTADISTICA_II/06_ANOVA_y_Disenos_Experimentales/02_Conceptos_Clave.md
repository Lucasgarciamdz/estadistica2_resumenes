# Unidad 6: Conceptos Clave

Esta sección define la terminología asociada con los diseños experimentales que van más allá del ANOVA de un factor. La comprensión de estos términos es crucial para diseñar experimentos y analizar sus resultados correctamente.

---

### Conceptos de Diseño Experimental

*   **Unidad Experimental:** La entidad física o sujeto al que se le aplica un tratamiento. Ejemplo: una parcela de tierra, un paciente, un lote de producción.

*   **Diseño Completamente al Azar (DCA):** El diseño más simple de ANOVA (visto en la Unidad 3). Los tratamientos se asignan a las unidades experimentales de forma completamente aleatoria. Asume que todas las unidades experimentales son homogéneas.

*   **Factor de Bloqueo (o Variable de Molestia):** Una variable que no es de interés principal para el investigador, pero que se sabe (o se sospecha) que tiene un efecto sobre la variable de respuesta. Se controla para reducir el error experimental.

*   **Bloque:** Un grupo de unidades experimentales que son homogéneas con respecto al factor de bloqueo. Ejemplo: un grupo de pacientes de la misma edad; un conjunto de experimentos realizados el mismo día.

*   **Diseño de Bloques Completos al Azar (DBCA):** Un diseño donde las unidades experimentales se agrupan en bloques, y luego los tratamientos se asignan al azar a las unidades *dentro* de cada bloque. Cada bloque contiene todos los tratamientos.

*   **Diseño Factorial:** Un diseño experimental en el que se investigan los efectos de dos o más factores simultáneamente. En un diseño factorial completo, se prueban todas las combinaciones posibles de los niveles de todos los factores.

*   **Efecto Principal:** El efecto promedio de un factor sobre la variable de respuesta, ignorando los efectos de los otros factores. En un diseño de dos factores (A y B), hay un efecto principal para A y un efecto principal para B.

*   **Interacción:** Ocurre cuando el efecto de un factor sobre la variable de respuesta **cambia** dependiendo del nivel de otro factor. Es el concepto más importante en los diseños factoriales. Si la interacción es significativa, los efectos principales pueden ser engañosos y deben interpretarse con cautela.
    *   **Gráfico de Interacción:** Una herramienta visual clave para detectar interacciones. Se grafica la media de la variable de respuesta para cada nivel de un factor, con líneas separadas para cada nivel del otro factor. **Líneas no paralelas sugieren una interacción.**

### Conceptos de Análisis Post-Hoc

*   **Pruebas Post-Hoc (o de Comparaciones Múltiples):** Pruebas estadísticas que se realizan **después** de que un ANOVA ha arrojado un resultado significativo. Su objetivo es determinar qué pares específicos de medias de grupo son significativamente diferentes entre sí.

*   **Tasa de Error por Comparación ($\\alpha_{PC}$):** La probabilidad de cometer un Error de Tipo I en una única comparación de pares. Es el $\\alpha$ que se usaría en una prueba t simple.

*   **Tasa de Error Familiar (o Tasa de Error Experimental, $\\alpha_{FW}$):** La probabilidad de cometer **al menos un** Error de Tipo I en el conjunto (la "familia") de todas las comparaciones que se realizan. Las pruebas post-hoc están diseñadas para controlar esta tasa de error, manteniéndola en el nivel de significancia deseado (e.g., 0.05).

*   **Prueba HSD de Tukey (Honest Significant Difference):** Una de las pruebas post-hoc más comunes y recomendadas. Calcula un único valor crítico (la "diferencia honestamente significativa") para evaluar las diferencias entre todas las posibles parejas de medias. Es más potente que otras pruebas como Bonferroni cuando los tamaños de muestra son iguales.

*   **Corrección de Bonferroni:** Un método muy general y simple para controlar la tasa de error familiar. Se realiza una serie de pruebas t estándar, pero se usa un nivel de significancia ajustado: $\\alpha_{ajustado} = \\frac{\\alpha_{FW}}{\\text{nº de comparaciones}}$. Es un método muy conservador (reduce la potencia) y a menudo no es la mejor opción, pero es fácil de aplicar.

*   **Contraste:** Una combinación lineal de las medias de los grupos que se utiliza para probar hipótesis específicas. Por ejemplo, en un estudio con 4 grupos, un contraste podría usarse para comparar la media del grupo de control con el promedio de las medias de los 3 grupos de tratamiento. Los contrastes se planifican *antes* del experimento (a priori), a diferencia de las pruebas post-hoc que son *a posteriori*.

