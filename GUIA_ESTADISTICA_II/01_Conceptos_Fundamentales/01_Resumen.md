# Unidad 1: Conceptos Fundamentales - El Puente hacia la Inferencia

## 1.1 Introducción: De Describir a Inferir

Esta unidad establece los cimientos indispensables para la **Estadística Aplicada II**. El objetivo primordial es trascender la **estadística descriptiva** —el arte de resumir y presentar datos— para adentrarnos de lleno en la **estadística inferencial**, la ciencia de extraer conclusiones válidas sobre una **población** completa a partir de una **muestra** representativa.

Aquí repasaremos y profundizaremos en los conceptos que nos permiten hacer esta transición de manera rigurosa. Entenderemos por qué no basta con calcular un promedio o una desviación estándar de nuestros datos, sino que debemos cuantificar la incertidumbre inherente al proceso de muestreo.

## 1.2 El Dilema Central: Población vs. Muestra

El problema fundamental de la inferencia estadística radica en la imposibilidad práctica de estudiar a todos los individuos de una población de interés (debido a costos, tiempo o accesibilidad). La solución es trabajar con una muestra, pero esto introduce una pregunta clave: **¿Hasta qué punto los resultados de mi muestra reflejan la realidad de la población?**

- **Población (`N`):** El universo completo de todos los elementos de interés. Sus características fijas y (generalmente) desconocidas se denominan **parámetros** (e.g., la media poblacional $\mu$, la varianza poblacional $\sigma^2$).
- **Muestra (`n`):** Un subconjunto de la población, seleccionado para ser analizado. Las características calculadas a partir de la muestra se llaman **estimadores** o **estadísticos** (e.g., la media muestral $\bar{X}$, la varianza muestral $S^2$).

El objetivo es utilizar los estimadores para hacer afirmaciones probabilísticas sobre los parámetros desconocidos.

## 1.3 Estimadores: Las Herramientas del Oficio

Un **estimador** es una regla o fórmula (una variable aleatoria) que se utiliza para estimar un parámetro poblacional. Una **estimación** es el valor numérico que toma el estimador para una muestra concreta.

No todos los estimadores son igualmente buenos. Para que nuestras inferencias sean fiables, buscamos estimadores con propiedades deseables:

1.  **Insesgadez:** Un estimador es insesgado si su valor esperado coincide con el parámetro que busca estimar. En promedio, no sobreestima ni subestima el valor real.
    -   $E(\hat{\theta}) = \theta$
2.  **Eficiencia:** Entre dos estimadores insesgados, el más eficiente es el que tiene menor varianza. Proporciona estimaciones más consistentes y cercanas al valor real.
3.  **Consistencia:** Un estimador es consistente si, a medida que el tamaño de la muestra (`n`) aumenta, la estimación converge en probabilidad al verdadero valor del parámetro.

## 1.4 La Piedra Angular: El Teorema Central del Límite (TCL)

El **Teorema Central del Límite** es, sin exageración, el resultado más importante de la estadística inferencial. Nos proporciona el puente teórico que necesitábamos para conectar la muestra con la población.

El TCL establece que, bajo condiciones muy generales (una muestra aleatoria de tamaño `n` de una población con media $\mu$ y varianza $\sigma^2$ finitas), la distribución de la **media muestral** ($\bar{X}$) se aproxima a una distribución **Normal**, sin importar la forma de la distribución original de la población, siempre que `n` sea suficientemente grande.

$$
\bar{X} \xrightarrow{\text{aprox.}} N\left(\mu, \frac{\sigma^2}{n}\right)
$$

Este teorema es poderoso porque nos permite utilizar la conocida distribución Normal para calcular probabilidades y construir intervalos de confianza y pruebas de hipótesis para la media poblacional, incluso si no sabemos nada sobre la distribución de los datos originales. La estandarización de la media muestral nos lleva a un resultado fundamental que usaremos constantemente:

$$
Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)
$$

Este resumen sienta las bases. Cada uno de estos puntos será desglosado con mayor detalle en los siguientes documentos, con un enfoque en el "porqué" matemático y conceptual.