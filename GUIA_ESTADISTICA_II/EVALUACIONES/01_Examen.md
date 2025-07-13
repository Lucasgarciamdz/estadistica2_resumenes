# Examen Teórico: Unidad 1 - Conceptos Fundamentales

**Instrucciones:** Prepárate para una evaluación oral. Lee cada sección y piensa cómo responderías en tiempo real. Para la Sección 1, imagina que tienes un pizarrón a tu disposición.

---

### Sección 1: Desarrollo en Pizarrón (15 minutos)

**Pregunta 1:**
Desarrolle y demuestre formalmente por qué el estimador Varianza Muestral, $S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2$, se considera un estimador insesgado de la varianza poblacional $\sigma^2$. Preste especial atención a la justificación del divisor $n-1$.

*(Tómate tu tiempo para escribir la derivación matemática completa en el pizarrón imaginario. Una vez que termines, prepárate para la defensa oral.)*

---

### Sección 2: Defensa Oral (10 minutos)

*El examinador mira tu desarrollo en el pizarrón y comienza a preguntar:*

**Pregunta 2.1:** "Excelente. Ahora, explícame conceptualmente, como si se lo explicaras a alguien que no sabe matemáticas, por qué si dividiéramos por $n$ en lugar de $n-1$, estaríamos subestimando sistemáticamente la verdadera varianza de la población. ¿Qué tiene que ver la media muestral $\bar{X}$ en todo esto?"

**Pregunta 2.2:** "Mencionaste los 'grados de libertad'. ¿Qué significa exactamente que se 'pierde un grado de libertad' en este contexto? ¿Dónde se fue?"

**Pregunta 2.3:** "Has demostrado que $S^2$ es un estimador insesgado de $\sigma^2$. ¿Significa esto que $S$ (la desviación estándar muestral) es también un estimador insesgado de $\sigma$ (la desviación estándar poblacional)? Justifica tu respuesta."

**Pregunta 2.4:** "Si la población de la que proviene la muestra no fuera normal, ¿seguiría siendo válida tu demostración? ¿Qué partes del desarrollo se verían afectadas?"

---

### Sección 3: Preguntas Rápidas (5 minutos)

*El examinador cambia de tema para evaluar la amplitud de tus conocimientos.*

**Pregunta 3.1 (Opción Múltiple):** El Teorema Central del Límite es crucial en estadística porque nos dice que:

a) Para muestras grandes, la distribución de la población se aproxima a una normal.
b) La distribución de muestreo de la media muestral se aproxima a una normal, sin importar la distribución de la población.
c) La media muestral es siempre un estimador insesgado de la media poblacional.
d) La varianza de la media muestral es $\sigma^2/n$.

**Pregunta 3.2 (Respuesta Corta):** Entre dos estimadores insesgados para el mismo parámetro, ¿cómo decides cuál es el "mejor"? ¿Qué propiedad buscas?

**Pregunta 3.3 (Verdadero/Falso):** Un estimador consistente es aquel que, para cualquier tamaño de muestra, siempre dará una estimación muy cercana al parámetro real. ¿Verdadero o Falso? Justifica.

**Pregunta 3.4 (Respuesta Corta):** ¿Qué mide el Error Estándar de la media y por qué es inversamente proporcional a la raíz cuadrada de $n$?
