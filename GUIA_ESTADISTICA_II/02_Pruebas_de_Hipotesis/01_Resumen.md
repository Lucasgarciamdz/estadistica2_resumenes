# Unidad 2: Resumen de Pruebas de Hipótesis

En esta unidad pasamos de la estimación a la toma de decisiones. Una prueba de hipótesis es un procedimiento formal para verificar una afirmación sobre un parámetro poblacional. En lugar de preguntar "¿cuál es el valor de la media?", preguntamos "¿es plausible que la media sea igual a un valor específico?".

---

### La Lógica Fundamental

El proceso es análogo a un juicio. Partimos de una presunción de inocencia, la **Hipótesis Nula ($H_0$)**, que es la afirmación que queremos poner a prueba. Generalmente, es una afirmación de "no efecto" o "no diferencia" (ej. $\mu = 20$).

Luego, planteamos una **Hipótesis Alternativa ($H_1$ o $H_a$)**, que es lo que creeríamos si la evidencia nos obliga a rechazar la hipótesis nula (ej. $\mu \neq 20$, $\mu > 20$ o $\mu < 20$).

El proceso consiste en recolectar evidencia (una muestra) y calcular qué tan probable es obtener esa evidencia si la Hipótesis Nula fuera cierta. Si la evidencia es muy "rara" o "extrema" bajo la suposición de que $H_0$ es verdadera, entonces la rechazamos en favor de $H_1$.

### Los Pasos de una Prueba de Hipótesis

Toda prueba de hipótesis, sin importar el parámetro que se esté probando, sigue estos 5 pasos:

1.  **Formular las Hipótesis:**
    *   **Hipótesis Nula ($H_0$):** Siempre contiene el signo de igualdad ($=, \le, \ge$). Es el status quo que se asume como cierto.
    *   **Hipótesis Alternativa ($H_1$):** Nunca contiene la igualdad ($\neq, <, >$). Es la afirmación que el investigador busca respaldar.

2.  **Establecer el Nivel de Significancia ($\alpha$):**
    *   Es la probabilidad de cometer un **Error de Tipo I**: rechazar la hipótesis nula cuando en realidad es verdadera. Es el umbral de "rareza".
    *   Valores comunes son 0.05, 0.01 o 0.10. Un $\alpha$ de 0.05 significa que estamos dispuestos a aceptar un 5% de probabilidad de equivocarnos al rechazar $H_0$.

3.  **Calcular el Estadístico de Prueba:**
    *   Es un valor calculado a partir de la muestra que mide qué tan lejos está nuestra estimación muestral del valor postulado en la hipótesis nula.
    *   La fórmula específica depende del parámetro que se prueba ($\mu, p, \sigma^2$), del tamaño de la muestra y de si se conocen ciertos parámetros poblacionales (como $\sigma^2$). Ejemplos comunes son el estadístico Z o el estadístico t.

4.  **Determinar la Regla de Decisión:**
    *   Consiste en definir la **región de rechazo**. Esta es el área en la cola (o colas) de la distribución de muestreo del estadístico de prueba. Si nuestro estadístico de prueba cae en esta región, rechazamos $H_0$.
    *   Se puede definir de dos maneras:
        *   **Método del Valor Crítico:** Se compara el estadístico de prueba con un valor de tabla (ej. $Z_{\alpha}$ o $t_{\alpha, n-1}$). Si el estadístico es más extremo que el valor crítico, se rechaza $H_0$.
        *   **Método del p-valor:** El p-valor es la probabilidad de obtener un estadístico de prueba tan extremo o más extremo que el observado, asumiendo que $H_0$ es cierta. Si $p-valor < \alpha$, se rechaza $H_0$.

5.  **Tomar una Decisión y Concluir:**
    *   Se aplica la regla de decisión a los resultados.
    *   La conclusión siempre se da en el contexto del problema original. No decimos simplemente "se rechaza $H_0$", sino "existe evidencia estadística suficiente para concluir que el tiempo medio de secado es mayor a 20 minutos".

### Tipos de Pruebas Vistas en la Unidad

Esta unidad cubre las pruebas fundamentales para:

*   **Una media poblacional:** ¿La media es igual a un valor específico? (Prueba Z si $\sigma$ es conocida, Prueba t si $\sigma$ es desconocida).
*   **Una proporción poblacional:** ¿La proporción de elementos con una característica es igual a un valor específico? (Prueba Z para muestras grandes).
*   **Una varianza poblacional:** ¿La varianza es igual a un valor específico? (Prueba Chi-Cuadrado).
*   **Diferencia de dos medias poblacionales:** ¿Son iguales las medias de dos grupos? (Pruebas Z o t para muestras independientes o pareadas).
*   **Diferencia de dos proporciones poblacionales:** ¿Son iguales las proporciones de dos grupos?
*   **Cociente de dos varianzas poblacionales:** ¿Son iguales las varianzas de dos grupos? (Prueba F).
