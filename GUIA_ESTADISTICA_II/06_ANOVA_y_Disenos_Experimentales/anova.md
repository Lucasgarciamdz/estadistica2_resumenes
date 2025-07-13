UNIDAD VI   
ANÁLISIS DE   
VARIANZA   
(ANOVA)

# ANÁLISIS DE VARIANZA

Se supone el caso de un fabricante y tres consumidores de latas cuyo fondo tengan al menos 0.25 libras de recubrimiento de estaño.

Mediante un tratamiento químico, se puede medir el peso de este recubrimiento, pero desgraciadamente no se puede repetir la experiencia con la misma muestra en los cuatro laboratorios.

Un ensayo experimental puede consistir en cortar discos a enviar a cada laboratorio, pero puede haber diferencias en el promedio debido: a) diferencias sistemáticas en la técnica de medición, b) variabilidad aleatoria.   
Por otro lado, está la incógnita de cuántos discos deberían cortarse para enviar a cada laboratorio.   
Se supondrá que este número está en el orden de 12 por laboratorio (en total 48 discos).   
La pregunta ahora es cómo seleccionar esos 48 discos de una chapa, lo primero que viene a la mente es enviar según este formato: Si las medias de las mediciones realizadas por cada uno de los laboratorios están muy dispersas, indica falta de consistencia en las mediciones.   
Esto puede ser porque todos miden distinto o quizá porque la distribución del depósito en la chapa es irregular.   
Es decir, se confunde la inconsistencia de los laboratorios con la cantidad de estaño depositado en la tira.


Una solución posible para esto sería numerar aleatoriamente los discos, por medio de una Tabla de Números Aleatorios o con una computadora, destinando a cada uno de los laboratorios los siguientes discos:

Laboratorio A: 3, 10, 22 ….   
Laboratorio B: 33, 42, 8 ….   
Laboratorio A: 15, 12, 28 ….   
Laboratorio A: 45, 21, 35 …. Esta alternativa “disuelve” el patrón de la disposición de estaño sobre la chapa (por ejemplo, más espesor en el centro que en los bordes).   
Al aleatorizar el total de los 48 discos sólo queda atribuir “a variación aleatoria” las causas extrañas.

Otra solución podría ser entregar los 48 de una misma tira (experimentación controlada), pero los resultados serían sólo aplicables a distancias fijas del extremo de la lámina.

En la práctica, los experimentos deberán planearse de tal manera que las fuente conocidas de variabilidad sean deliberadamente consideradas sobre un rango tan amplio como sea necesario.   
Más aún, deberán variarse en tal forma que su variabilidad pueda eliminarse en la estimación de la variable aleatoria.

Un modo es repetir el experimento en varios bloques en los que la fuente conocida de variabilidad (esto es, variables extrañas) se mantienen fijas en cada bloque, pero variando de bloque en bloque:

<html><body><table><tr><td></td><td>Tira1</td><td>Tira2</td><td>Tira3</td><td>Tira4</td></tr><tr><td>Laboratorio A</td><td>8,4,10</td><td>23,24,19</td><td>26,29,35</td><td>37,44,48</td></tr><tr><td>LaboratorioB</td><td>2,6,12</td><td>21,15,22</td><td>34,33,32</td><td>45,43,46</td></tr><tr><td>Laboratorio C</td><td>1,5,11</td><td>16,20,13</td><td>36,29,30</td><td>41,38,47</td></tr><tr><td>Laboratorio D</td><td>7.3.9</td><td>17,18,14</td><td>28,31,25</td><td>39,40,42</td></tr></table></body></html>

De este modo, las diferencias entre medias obtenidas por los 4 laboratorios, no pueden atribuirse a variaciones entre tiras.

# DISEÑOS COMPLETAMENTE ALEATORIOS

Se supone que el experimentador cuenta con los resultados de k muestras aleatorias independientes, cada una de tamaño n, de k diferentes poblaciones (datos relativos a k tratamientos, k grupos, k métodos de producción, etc.).   
Interesa probar la hipótesis de que las medias de esas k poblaciones son todas iguales. Se denota a la j-ésima observación de la i-ésima muestra por y i j.   
El esquema general para un criterio de clasificación es:

<html><body><table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Medias</td></tr><tr><td>Muestra1</td><td>y11</td><td>y12</td><td></td><td>y1i</td><td></td><td>y1n</td><td></td></tr><tr><td>Muestra 2</td><td>y21</td><td>y22</td><td></td><td>y2i</td><td></td><td>y2n</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Muestra i</td><td>yi1</td><td>yi2</td><td></td><td>Yii</td><td>…</td><td>yin</td><td></td></tr><tr><td></td><td></td><td>…</td><td></td><td></td><td>·</td><td></td><td></td></tr><tr><td>Muestra k</td><td>yk1</td><td>yk2</td><td></td><td>yki</td><td></td><td>Ykn</td><td>yk</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html>

Bajo este esquema experimental, en referencia al ejemplo tratado, yij (i=1,2,..,4; j=1,2,…, 12) es la j-ésima medición del peso del revestimiento del iésimo laboratorio, e

es la media global (o gran media) de las 48 observaciones.   
Para pruebas de hipótesis (medias iguales) se supondrá estar trabajando con poblaciones normales de la misma $\sigma ^ { 2 }$ .

$\mathrm { S i } \mu _ { \mathrm { i } }$ es la media de la población i-ésima y $\sigma ^ { 2 }$ es la varianza común de las k poblaciones, se puede expresar cada observación $\mathbf { y _ { i j } }$ como $\mu _ { \mathrm { i } }$ más el valor del componente aleatorio:

$\varepsilon _ { \mathrm { i , j } }$ es una variable aleatoria con dis tribución normal, $\mu { = } 0 \gamma \sigma ^ { 2 }$ común. Para dar uniformidad a las ecuaciones, se reemplaza $\mu _ { \mathrm { i } } \mathsf { p o r } \mu ^ { + } \alpha _ { \mathrm { i } }$ , donde $\mu$ es la media de las $\mu _ { \mathrm { i } } \mathrm { y } \alpha _ { \mathrm { i } }$ es el efecto del i-ésimo tratamiento, de aquí que

$$
\sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } \alpha _ { \mathrm { i } } = 0
$$

esto surge de:

$$
\mu = \frac { 1 } { \mathrm { k } } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } { \mu _ { \mathrm { i } } \mathrm { = } \frac { 1 } { \mathrm { k } } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } { \left( \mu + \alpha _ { \mathrm { i } } \right) } } = \mathrm { k } \cdot \frac { \mu } { \mathrm { k } } + \frac { 1 } { \mathrm { k } } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } { \alpha _ { \mathrm { i } } }
$$

luego, la expresión de $\mathbf { y _ { i j } }$ queda:

$$
\mathrm { y } _ { \mathrm { i } , \mathrm { j } } = \mu + \alpha _ { \mathrm { { i } } } + \varepsilon _ { \mathrm { { i } , \mathrm { j } } } \qquad \mathsf { p a r a i } - 1 , 0 , . . . , \mathsf { k } ; \mathsf { j } = 1 , 2 , . . . , \mathsf { n }
$$

Por lo tanto, la Hipótesis Nula (las medias de las k poblaciones iguales) se reemplaza por la Hipótesis Nula de que $\alpha _ { 1 } = \alpha _ { 2 } = . . . = \alpha _ { \mathrm { k } } = 0$ .

La Hipótesis Alterna de que al menos dos de las medias son distintas equivale a que $\alpha _ { \mathrm { i } } < >$ 0 para alguna i.

Para probar la Hipótesis Nula, se comparan las estimaciones de $\sigma ^ { 2 }$ (una en base a la observación de las medias muestrales y la otra con la variación dentro de la muestra).

Ya que cada muestra viene de una población con varianza $\sigma ^ { 2 }$ , la varianza se puede estimar de cualquiera de las muestras:

$$
{ \mathrm { ~ s _ { i } ' = \frac { 1 } { n - 1 } \cdot \sum _ { j = 1 } ^ { n } ~ \left( y _ { i j } - \overline { { y _ { i } } } \right) ^ { 2 } } }
$$

y entonces también por su media:

$$
{ \widehat { \widetilde { \mathbf { v } } } } _ { \mathrm { W } } ^ { 2 } = { \frac { 1 } { \mathrm { k } } } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } { \widehat { \mathbf { \Omega } } } _ { \mathrm { s i } } ^ { 2 } = { \frac { 1 } { \mathrm { k } \cdot ( \mathrm { n } - 1 ) } } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } { \sum _ { \mathrm { j } = 1 } ^ { \mathrm { n } } { \left( \mathrm { y } _ { \mathrm { i j } } - { \overline { { \mathrm { y } } } } _ { \mathrm { i } } ^ { 2 } \right) ^ { 2 } } }
$$

Cada una de las varianzas muestrales $\mathbf { s } _ { \mathbf { i } } ^ { 2 }$ está basada en (n-1) grados de libertad y entonces

está basada en k.(n-1) grados de libertad.

Por otro lado, la varianza de las k medias muestrales está dada por:

$$
s \overline { { \mathbf { x } } } ^ { 2 } = \frac { 1 } { \mathbf { k } - 1 } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathbf { k } } \ \left( \overline { { \mathbf { y _ { i } } } } - \overline { { \mathbf { y _ { . } } } } \right) ^ { 2 }
$$

y si la hipótesis es verdadera, esta expresión da una estimación de $\sigma ^ { 2 / } \mathrm { n y }$ así una estimación de $\sigma ^ { 2 }$ , pero basada en la diferencia entre las medias, está dada por

$$
\widehat { \widetilde { \mathrm { \scriptsize ~ C } } } _ { \mathrm { \scriptsize ~ H } } ^ { 2 } = \boldsymbol { \mathrm { \scriptsize ~ n } } \cdot \boldsymbol { s } \ : \overline { { \boldsymbol { \mathrm { \scriptsize ~ x } } } } ^ { 2 } = \frac { \boldsymbol { \mathrm { \scriptsize ~ n } } } { \boldsymbol { \mathrm { \scriptsize ~ k } } - 1 } \cdot \sum _ { \mathrm { \scriptsize ~ i = 1 } } ^ { \boldsymbol { \mathrm { \scriptsize ~ k } } } \ : \ : \left( \overline { { y _ { \mathrm { i } } } } - \overline { { y } } _ { \mathrm { \scriptsize . } } \right) ^ { 2 }
$$

basada en (k-1) grados de libertad.

Si Ho es cierta,se puede demostrar que ${ \widehat { \sigma } _ { \mathrm { \tiny ~ W } } } ^ { 2 }$ ${ \widehat { \sigma } _ { \mathrm { \scriptsize ~ H } } } ^ { 2 }$ son estimaciones independientes de $\sigma ^ { 2 }$ ypor ello:

es una variable aleatoria con distribución F con $\mathbf { \boldsymbol { v } } _ { 1 } = \mathbf { \boldsymbol { k } }$ - 1 y $\scriptstyle \prime \mathbf { v } _ { 2 } = \mathbf { k } . ( \mathbf { n } - 1 )$ grados de libertad

${ \widehat { \sigma } } _ { \mathrm { H } } ^ { \mathrm { ~ \tiny ~ 2 ~ } }$ muestras, wdHslassiF

Con el argumento anterior se ha indicado cómo la prueba de las k medias se puede fundamentar en la comparación de dos estimaciones de varianzas.

Es notable el hecho de que las dos estimaciones en cuestión [excepto para los divisores (k-1) y k.(n-1)] pueden obtenerse “partiendo” o analizando la varianza total de las n.k observaciones en dos partes.

La varianza muestral de las n.k observaciones está dada por:

$$
s ^ { 2 } = { \frac { 1 } { \operatorname { k cdot n } - 1 } } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } \sum _ { \mathrm { j } = 1 } ^ { \mathrm { n } } { \binom { - { \mathrm { \sqrt { j } } } - { \mathrm { \sqrt { j } } } ^ { 2 } } { \mathrm { i } = 1 } } ^ { 2 }
$$

Se puede probar el siguiente teorema respecto del numerador, llamado Suma de Cuadrados Total:

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { k } } \sum _ { \mathrm { j = 1 } } ^ { \mathrm { n } } \left( \mathrm { y _ { i j } - \mathrm { \overline { { y } } . } } \right) ^ { 2 } = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { k } } \sum _ { \mathrm { j = 1 } } ^ { \mathrm { n } } \left( \mathrm { y _ { i j } - \mathrm { \overline { { y _ { i } } } } } \right) ^ { 2 } + \mathrm { n . \sum _ { \mathrm { i = 1 } } ^ { \mathrm { k } } \left( \mathrm { \overline { { y _ { i } } } - \mathrm { \overline { { y } } . } } \right) ^ { 2 } }
$$

Demostración:

$$
\begin{array} { r l } & { \displaystyle \sum _ { i = 1 } ^ { \mathbf { k } } \sum _ { j = 1 } ^ { n } ( \mathbf { y } _ { i j } - \mathbf { \overline { { y } } _ { i } } + \mathbf { \overline { { y } } } _ { i } - \mathbf { \overline { { y } } } _ { j } ) ^ { 2 } = \displaystyle \sum _ { i = 1 } ^ { \mathbf { k } } \sum _ { j = 1 } ^ { n } [ ( \mathbf { y } _ { i j } - \mathbf { \overline { { y } } } _ { i } ) ^ { 2 } - 2 \Big ( \mathbf { y } _ { i j } - \mathbf { \overline { { y } } } _ { i } \Big ) \cdot ( \mathbf { \overline { { y } } } _ { i } - \mathbf { \overline { { y } } } _ { j } \Big ) + ( \mathbf { \overline { { y } } } _ { i } - \mathbf { \overline { { y } } } _ { j } ) ^ { 2 } ] } \\ & { \displaystyle \bullet = \sum _ { i = 1 } ^ { \mathbf { k } } \sum _ { j = 1 } ^ { n } ( \mathbf { y } _ { i j } - \mathbf { \overline { { y } } _ { i } } ) ^ { 2 } - 2 \sum _ { i = 1 } ^ { \mathbf { k } } ( \mathbf { \overline { { y } } } _ { i } - \mathbf { \overline { { y } } } _ { j } ) \cdot \sum _ { j = 1 } ^ { n } ( \mathbf { y } _ { i j } - \mathbf { \overline { { y } } } _ { i } ) + \displaystyle \mathbf { n } \cdot \sum _ { i = 1 } ^ { \mathbf { k } } ( \mathbf { \overline { { y } } } _ { i } - \mathbf { \overline { { y } } } _ { j } ) ^ { 2 } } \\ & { \displaystyle \quad \textnormal { i = 1 } j = 1 } \end{array}
$$

ycomo:

$$
\sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left( { \mathrm { y } } _ { \mathrm { i j } } - { \mathrm { \overline { { y } } } } _ { \mathrm { i } } \right) = 0
$$

se verifica la relación anterior:

Se acostumbra a denotar:

a) Suma de Cuadrados Total, SST:

$$
\mathrm { { S S T } = \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n } \left( y _ { i j } - \overline { { y } } _ { . } \right) ^ { 2 } }
$$

b) Suma de Cuadrados de Error, SSE:

$$
{ \mathrm { S S E } } = { \mathrm { k } } \cdot ( { \mathrm { n } } - 1 ) \cdot { \widehat { \mathrm { \sigma } } } { \mathrm { w } } ^ { 2 } = \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } \sum _ { \mathrm { j } = 1 } ^ { \mathrm { n } } \left( { \mathrm { y } } _ { \mathrm { i j } } - { \overline { { \mathrm { y } } } } _ { \mathrm { i } } ^ { 2 } \right) ^ { 2 }
$$

c) Suma de Cuadrados de Tratamiento $\mathrm { S S ( T r ) }$ :

$$
{ \mathrm { S S } } ( { \mathrm { T r } } ) = ( { \bf k } - 1 ) { \cdot } { \widehat { \sigma } } _ { \mathrm { ~ H ~ } } ^ { 2 } = { \mathrm { n } } { \cdot } \sum _ { \bf i = 1 } ^ { \bf k } { \bf \Gamma } \left( { \overline { { y _ { \bf i } } } } - { \overline { { y } } } _ { \mathrm { . } } ^ { 2 } \right) ^ { 2 }
$$

Luego, $\mathrm { F }$ se puede escribir así:

<html><body><table><tr><td rowspan="3">F =</td><td>SS(Tr)</td></tr><tr><td>k-1</td></tr><tr><td>SSE</td></tr><tr><td colspan="2">k·(n-1)</td></tr></table></body></html>

Los resultados obtenidos son mostrados en la siguiente tabla:

<html><body><table><tr><td>Fuentesde Variacion</td><td>Gradosde Libertad</td><td>Suma de Cuadrados</td><td>MediaCuadrada</td><td>F</td></tr><tr><td>Tratamientos</td><td>k-1</td><td>SS(Tr)</td><td>MS(Tr)=SS(Tr)/(k-1)</td><td>MS(Tr)/MSE</td></tr><tr><td>Error</td><td>k.(n-1)</td><td>SSE</td><td>MSE=SSE/k.(n-1)</td><td></td></tr><tr><td>Total</td><td>n.k-1</td><td>SST</td><td></td><td></td></tr></table></body></html>

Ejemplo: A fin de utilizar el Análisis de Varianza para un criterio de clasificación, suponer el siguiente esquema de mediciones de cuatro laboratorios de un parámetro determinado (revestimiento de estaño de 12 discos) cuyos resultados son:

<html><body><table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Total</td></tr><tr><td>Lab.A</td><td>.25</td><td>27</td><td>.22</td><td>.30</td><td>.27</td><td></td><td>28.3224.31.26</td><td></td><td></td><td></td><td>.21</td><td>.28</td><td>3.21</td></tr><tr><td>Lab.B</td><td>.18</td><td>.28</td><td>.21</td><td>.23</td><td>.25</td><td></td><td>.20.27.19.24.22</td><td></td><td></td><td></td><td>.29</td><td>.16</td><td>2.72</td></tr><tr><td>Lab.C</td><td>.19</td><td>25</td><td>27</td><td>.24</td><td>.18</td><td></td><td>26.28.24.25.20</td><td></td><td></td><td></td><td>.21</td><td>.19</td><td>2.76</td></tr><tr><td>Lab.D</td><td>.23</td><td>.30</td><td>.28</td><td>.28</td><td>.24</td><td></td><td>34.20.18.24.28</td><td></td><td></td><td></td><td>.22</td><td>.21</td><td>3.00</td></tr><tr><td>Total</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>11.69</td></tr></table></body></html>

del que se quiere probar que las medias obtenidas por cada uno de ellos es significativamente igual (Hipótesis Nula) con $\scriptstyle \alpha = 0 . 0 I$ . Construir una Tabla de análisis de varianza.

1. Hipótesis nula: Las medias de las mediciones son iguales Hipótesis alternativa: No lo son 2. Nivel de significancia: $\mathtt { q } = 0 . 0 1$ $\alpha : = 0 . 0 1$

3. Criterio se acepta la Ho si F < 4.261 k 4 := número de tratamientos n 12 := tamaño de la muestra ν1 k 1 := - = 3 grados de libertad del numerador $\nu 2 : = \mathrm { k } { \cdot } ( \mathrm { n } - 1 ) = 4 4$ grados de libertad del denominador $\mathrm { F 0 5 : = \ q F ( 1 - \alpha , } \nu 1 , \nu 2 ) = 4 . 2 6 1$ F crítico

t 0 0.01 := , .. 5


4. Cálculos:

Para facilitar cálculos, se utilizan las fórmulas:

$$
\mathrm { S S T } = \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } \sum _ { \mathrm { j } = 1 } ^ { \mathrm { n } } \left( \mathrm { y _ { i j } } \right) ^ { 2 } - \mathrm { C } \qquad \mathrm { S S ( T r ) } = \frac { 1 } { \mathrm { n } } . \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } { \mathrm { T _ { i } } } ^ { 2 } - \mathrm { C }
$$

# Demostración:

Para Suma de Cuadrados total

$$
\begin{array} { r l } & { \mathrm { s s T } = \displaystyle \sum _ { \mathbf { i } = 1 } ^ { \mathbf { k } } \sum _ { \mathbf { j } = 1 } ^ { \mathbf { n } } \left( \mathbf { y } _ { \bar { \mathbf { j } } } - \overline { { \mathbf { y } } } \right) ^ { 2 } = \displaystyle \sum _ { \mathbf { i } = 1 } ^ { \mathbf { k } } \sum _ { j = 1 } ^ { \mathbf { n } } \left[ \left( \mathbf { y } _ { \bar { \mathbf { j } } } \right) ^ { 2 } - 2 \cdot \mathbf { y } _ { \bar { \mathbf { j } } } \cdot \overline { { \mathbf { y } } } _ { \mathbf { \cdot } } + \left( \overline { { \mathbf { y } } } _ { \mathbf { \cdot } } \right) ^ { 2 } \right] } \\ & { \quad = \displaystyle \sum _ { \mathbf { i } = 1 } ^ { \mathbf { k } } \sum _ { \mathbf { j } = 1 } ^ { \mathbf { n } } \left( \mathbf { y } _ { \bar { \mathbf { j } } } \right) ^ { 2 } - 2 \cdot \overline { { \mathbf { y } } } _ { \mathbf { \cdot } } \left( \mathbf { k } \cdot \mathbf { n } \right) \cdot \frac { 1 } { \left( \mathbf { k } \cdot \mathbf { n } \right) } \cdot \displaystyle \sum _ { \mathbf { i } = 1 } ^ { \mathbf { k } } \sum _ { \mathbf { j } = 1 } ^ { \mathbf { n } } \mathbf { y } _ { \bar { \mathbf { j } } } + \mathbf { k } \cdot \mathbf { n } \cdot \left( \overline { { \mathbf { y } } } \right) ^ { 2 } } \\ & { \quad = \displaystyle \sum _ { \mathbf { i } = 1 } ^ { \mathbf { k } } \sum _ { \mathbf { j } = 1 } ^ { \mathbf { n } } \left( \mathbf { y } _ { \bar { \mathbf { j } } } \right) ^ { 2 } - \mathbf { k } \cdot \mathbf { n } \cdot \left( \overline { { \mathbf { y } } } \right) ^ { 2 } } \end{array}
$$

$$
\mathbf { C = k \cdot n \cdot } \left( \overline { { \mathbf { y } } } \right) ^ { 2 } \mathbf { \equiv } \left( \mathbf { k \cdot n } \right) . \frac { \left( \sum _ { \mathbf { i } = 1 } ^ { \mathbf { k } } \sum _ { \mathbf { j } = 1 } ^ { \mathbf { n } } \mathbf { \sigma } _ { \mathbf { j } \mathbf { j } } ^ { \mathbf { y } } \right) ^ { 2 } } { \left( \mathbf { k \cdot n } \right) ^ { 2 } } \mathbf { \equiv } \frac { 1 } { \mathbf { k \cdot n } } . \left( \sum _ { \mathbf { i } = 1 } ^ { \mathbf { k } } \sum _ { \mathbf { j } = 1 } ^ { \mathbf { n } } \mathbf { \sigma } _ { \mathbf { j } \mathbf { j } } ^ { \mathbf { y } } \right) ^ { 2 }
$$

Para Suma de Cuadrados de Tratamientos:

$$
{ \begin{array} { r l } & { { \mathrm { S S } } ( { \mathrm { T r } } ) = { \mathrm { n } } \cdot { \displaystyle \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } } \left( { \overline { { \mathbf { y } _ { \mathrm { i } } } } } - { \overline { { \mathbf { y } } } } \right) ^ { 2 } } = { \mathrm { n } } \cdot { \left[ \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } \right]} \left( { \overline { { \mathbf { y } _ { \mathrm { i } } } } } \right) ^ { 2 } - 2 { \cdot } { \overline { { \mathbf { y } } } } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } { \overline { { \mathbf { y } _ { \mathrm { i } } } } } + { \mathbf { k } } \cdot \left( { \overline { { \mathbf { y } } } } \right) ^ { 2 }  }  \\ & { { \mathrm { S S } } ( { \mathrm { T r } } ) = { \frac { 1 } { \mathrm { n } } } \cdot { \displaystyle \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } } \left( \sum _ { \mathrm { j } = 1 } ^ { \mathrm { n } } \mathbf { y } _ { \mathrm { i j } } \right) ^ { 2 } - { \mathrm { c } } = { \frac { 1 } { \mathrm { n } } } \cdot { \displaystyle \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } } \left( { \mathrm { T } } _ { \mathrm { i } } \right) ^ { 2 } - { \mathrm { c } } } \end{array} 
$$

donde C (llamado Término de Corrección) y Ti es:

$$
\mathrm { { T _ { i } = \sum _ { j = 1 } ^ { n } \ y _ { i j } } }
$$

Para obtener los datos del problema, se leen de un archivo externo.

$$
\mathbf { i } : = 1 \ldots \mathbf { j } : = 1 \ldots \mathbf { n }
$$

$$
\mathrm { { C : = \frac { 1 } { k \cdot n } \cdot \left( \sum _ { i \ : = 1 } ^ { k } \sum _ { j \ : = 1 } ^ { n } \mathrm { { y } _ { i , j } } \right) ^ { 2 } = : } }
$$

$$
\mathrm { T _ { i } : = \sum _ { j = 1 } ^ { n } \mathcal { I } _ { i , j } }
$$

$$
\ S S \mathrm { T : = \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n } \left( y _ { i , j } \right) ^ { 2 } - C = : }
$$

$$
\mathrm { { _ { - } ^ { 5 } } T r : = \frac { 1 } { \pi } . \sum _ { i = 1 } ^ { k } \left( T _ { i j } \right) ^ { 2 } - C = \bullet }
$$

Suma de cuadrados total

Suma de cuadrados de tratamientos

Suma de cuadrados de error

$$
\mathrm { M S \ _ T r : = \frac { S S \_ T r } { k - 1 } = \bullet }
$$

$$
\mathrm { M S E } : = { \frac { \mathrm { S S E } } { \mathrm { k } { \cdot } ( \mathrm { n } - 1 ) } } = \mathsf { \ " }
$$

$$
\frac { 4 3 } { 1 5 } = 2 . 8 6 7
$$

<html><body><table><tr><td rowspan="2">F:=</td><td>0.0043</td><td>2.87</td></tr><tr><td>0.0015</td><td></td></tr></table></body></html>

La tabla queda

Estadístico

<html><body><table><tr><td>Fuentes Variacion</td><td>deGrados Libertad</td><td>deSuma Cuadrados</td><td>deMedia Cuadrada</td><td>F</td></tr><tr><td>Laboratorios</td><td>3</td><td>0.0130</td><td>0.0043</td><td>2.87</td></tr><tr><td>Error</td><td>44</td><td>0.0679</td><td>0.0015</td><td></td></tr><tr><td>Total</td><td>47</td><td>0.0809</td><td></td><td></td></tr></table></body></html>

t F05 , , F

$\mathrm { F 0 } 5 = 4 . 2 6 1 $

5. Decisión: Ya que F (2.87) NO excede a $\underline { { \mathbf { F _ { 0 . 0 5 } } } } \underline { { = 4 . 2 6 1 } }$ se acepta la Hipótesis Nula, luego los laboratorios SI están logrando resultados consistentes.

X READPRN "c:\datos\anova.txt" := ( )

$$
\begin{array} { r l } { \mathbf { A } : = } & { \lfloor \mathrm { S S T r } \gets \mathrm { c o l s ( \mathcal { X } ) } \cdot \displaystyle \sum _ { \mathrm { i = 1 } } ^ { \mathrm { r o w s ( X ) } } [ [ \mathrm { m e a n } \Big [ \Big ( _ { X } \mathrm { T } \Big ) ^ {  \hat { \nu }  } ] - \mathrm { m e a n ( X ) } \Big ] ^ { 2 } ] } \\ & { \lfloor \mathrm { S S T } \gets [ \displaystyle \sum _ { \mathrm { i = 1 } } ^ { \mathrm { r o w s ( X ) } } \sum _ { \mathrm { j = 1 } } ^ { \mathrm { c o l s ( X ) } } [ \Big ( \mathrm { X } _ { \mathrm { i , j } } - \mathrm { m e a n ( X ) } \Big ) ^ { 2 } ] ] } \end{array}
$$

A =

<html><body><table><tr><td>Fuentes Variacion</td><td>deGrados Libertad</td><td>deSuma de Cuadrados</td><td>Media Cuadrada</td><td>F</td></tr><tr><td>Laboratorios</td><td>3</td><td>0.0130</td><td>0.0043</td><td>2.87</td></tr><tr><td>Error</td><td>44</td><td>0.0679</td><td>0.0015</td><td></td></tr><tr><td>Total</td><td>47</td><td>0.0809</td><td></td><td></td></tr></table></body></html>

Para estimar los parámetros $\mathsf { 1 } , \mathsf { d } _ { 1 } , \mathsf { d } _ { 2 } , \mathsf { d } _ { 3 }$ y ${ \alpha } _ { 4 }$ se puede emplear mínimos cuadrados minimizando:

$$
\sum _ { \mathrm { i } \mathop { = } 1 } ^ { \mathrm { k } } \sum _ { \mathrm { j } \mathop { = } 1 } ^ { \mathrm { n } } \left( { \mathrm { y } } _ { \mathrm { i } , \mathrm { j } } - \mu - { \alpha } _ { \mathrm { i } } \right) ^ { 2 }
$$

con respecto a $\mu$ y a las ${ \bf { \alpha } } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } }$ , sujetas a la restricción

$$
\sum _ { \mathrm { ~ i ~ } = 1 } ^ { \mathrm { ~ k ~ } } \alpha _ { \mathrm { { i } } } = 0
$$

Derivando la penúltima expresión respecto de $\mu$ e igualando a cero:

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n } - 2 \cdot \big ( y _ { 1 } - \mu - \alpha _ { i } \big ) = 0 } } \\ { { \displaystyle \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n } \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n } \mu - \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n } \mu _ { i } = 0 } } \\ { { \displaystyle \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n } \sum _ { y _ { i } = k } ^ { n } - \sum _ { i = 1 } ^ { n } \mu - 0 } } \\ { { \displaystyle \operatorname * { l i } = \sum _ { n \neq 1 } ^ { 1 } \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n } y _ { i } = \overline { { y } } , } } \end{array}
$$

para un i dado:

$$
\begin{array} { l } { { \displaystyle \sum _ { \bf j = 1 } ^ { \bf n } - 2 \cdot \left( y _ { \bf i j } - \cdot \mathbf { \sigma } \mathbf { \boldsymbol { \mu } } - \alpha _ { \bf i } \right) = 0 \qquad \ \sum _ { \bf j = 1 } ^ { \bf n } \ \alpha _ { \bf i } = \sum _ { \bf j = 1 } ^ { \bf n } \mathrm { y _ { \bf i j } - \sum _ { \bf j = 1 } ^ { \bf n } \ \boldsymbol { \mu } } } } \\  { \displaystyle \mathrm { n . { \alpha } \cdot { \alpha } _ { \bf i } = \sum _ { \bf j = 1 } ^ { \bf n } \ { y _ { \bf i j } - \bf n \cdot { \sigma } } } } \end{array}
$$

Ejemplo: Estimar los parámetros del modelo con un criterio de clasificación para los revestimientos de estaño del ejemplo anterior.

$$
\mu : = { \frac { 1 } { \mathrm { n } \cdot \mathrm { k } } } \cdot \sum _ { \mathrm { ~ i ~ } = 1 } ^ { \mathrm { k } } \sum _ { \mathrm { ~ j ~ } = 1 } ^ { \mathrm { n } } { \mathrm { ~ y } _ { \mathrm { i , j } } } = \mathsf { \pm }
$$

$$
\alpha _ { \overset { . } { 1 } } : = \frac { et { } { ' } \sum _ { \mathfrak { p } } \binom { \mathfrak { p } } { \mathfrak { p } } ^ { \zeta _ { \mathfrak { p } } } } { \mathfrak { n } } - \mu
$$

$$
\sum \mathbb { \alpha } = \mathbf { \eta }
$$

# TAMAÑOS MUESTRALES DISTINTOS

El Análisis de Varianza descripto, se aplica a criterios de clasificación en que cada muestra tiene el mismo número de observaciones.

Si no es así, y los tamaños muestrales $\operatorname { s o n n } _ { 1 } , \operatorname { n } _ { 2 } , . . . , \operatorname { n } _ { \mathrm { k } } \operatorname { s e }$ tiene que sustituir $\mathbf { N } = \pmb { \Sigma }$ ni por n.k en todo lo anterior, quedando el siguiente esquema de partida:

<html><body><table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Medias</td></tr><tr><td>Muestra 1</td><td>y11</td><td>y12</td><td></td><td>yij</td><td></td><td>1n1</td><td></td></tr><tr><td>Muestra 2</td><td>y21</td><td>y22</td><td></td><td>y2j</td><td>·</td><td>y2n2</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Muestra i</td><td>y</td><td>y2</td><td></td><td></td><td>…</td><td>Vini</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Muestra k</td><td>yk1</td><td>yk2</td><td></td><td></td><td></td><td>yknk</td><td>yk</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html>

Se obtiene la varianza dentro de la muestra:

$$
{ \mathrm { s _ { i } } } ^ { 2 } = { \frac { 1 } { \mathrm { n _ { i } } - 1 } } \cdot \sum _ { \mathrm { j ~ } = 1 } ^ { \mathrm { n _ { i } } } { \bigl ( } \mathrm { y _ { i j } } - { \overline { { \mathrm { y _ { i } } } } } { \bigr ) } ^ { 2 }
$$

y

$$
{ \widehat { \sigma } } _ { \mathbb { W } } ^ { 2 } = { \frac { 1 } { \operatorname { k } } } \cdot \sum _ { \mathrm { i \ m } } ^ { \operatorname { k } } { s _ { \mathrm { i \ m } } ^ { \operatorname { \ell } } } ^ { 2 } = \sum _ { \mathrm { i \ m } } ^ { \operatorname { k } } \sum _ { \mathrm { j \ } = 1 } ^ { \operatorname { n } _ { \mathrm { i } } } { \frac { \left( \mathrm { y _ { i j } } - { \overline { { y _ { i } } } } \right) ^ { 2 } } { \operatorname { k } \cdot \left( \mathrm { n } _ { \mathrm { i } } - 1 \right) } }
$$

La varianza de las $\mathbf { k }$ medias muestrales es:

$$
\begin{array} { r l } & { \widehat { \mathbf { s } } \frac { 2 } { \mathbf { x } } = \displaystyle \sum _ { \mathrm { i } = 1 } ^ { \mathbf { k } } \frac { \binom { - } { \mathbf { y } _ { \mathrm { i } } - \mathbf { y } _ { \mathrm { . } } } ^ { 2 } } { \mathbf { k } - 1 } } \\ & { \widehat { \mathbf { \Phi } } _ { \widehat { \mathbf { U } } } ^ { \mathrm { ~ ~ } } \frac { 1 } { \mathbf { y } } = \displaystyle \sum _ { \mathrm { i } = 1 } ^ { \mathbf { k } } \frac { \binom { - } { \mathbf { y } _ { \mathrm { i } } - \mathbf { y } _ { \mathrm { . } } } ^ { 2 } } { \mathbf { k } - 1 } } \end{array}
$$

y

con lo cual se determina:

La varianza muestral de las $_ \mathrm { N }$ observaciones está dada por:

$$
s ^ { 2 } = \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n _ { i } } \ \frac { \left( y _ { i j } - \overline { { y } } _ { \cdot } \right) ^ { 2 } } { \mathrm { N } - 1 }
$$

Se puede demostrar que:

$$
\sum _ { \mathrm { ~ i ~ } = 1 } ^ { \mathrm { ~ k ~ } } \sum _ { \mathrm { ~ j ~ } = 1 } ^ { \mathrm { ~ n _ { i } ~ } } \left( \mathrm { y _ { i j } - \mathrm { ~ \overline { { y } } _ { \cdot } } } \right) ^ { 2 } = \sum _ { \mathrm { ~ i ~ } = 1 } ^ { \mathrm { ~ k ~ } } \sum _ { \mathrm { ~ j ~ } = 1 } ^ { \mathrm { ~ n _ { i } ~ } } \left( \mathrm { y _ { i j } - \mathrm { ~ \overline { { y } } _ { i } } } \right) ^ { 2 } + \sum _ { \mathrm { ~ i ~ } = 1 } ^ { \mathrm { ~ k ~ } } \mathrm { ~ n _ { i } ~ } \cdot \left( \mathrm { \overline { { y _ { i } } } - \mathrm { ~ \overline { { y } } _ { \cdot } } } \right) ^ { 2 }
$$

SST = SSE + SS(Tr)

Con:

$$
\mathrm { S S T } = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { k } } \sum _ { \mathrm { j = 1 } } ^ { \mathrm { n _ { i } } } \left( \mathrm { y _ { i j } } \right) ^ { 2 } - \mathrm { C } \qquad \mathrm { S S ( T r ) = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { k } } \frac { \partial \left( T _ { i } \right) ^ { 2 } } { \partial \mathrm { n _ { i } } } - \mathrm { C } }
$$

siendo:

$$
\begin{array}{c} \mathrm { C = { \frac { 1 } { N } } { \cdot } \left( \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { n _ { i } } y _ { i j } \right) ^ { 2 } } \mathrm { T _ { i } = \left( \sum _ { i = 1 } ^ { k } \ y _ { i j } \right) }  \end{array}
$$

Problema: El contenido de aflatoxina, en partes por millón, de algunas muestras de crema de maní se prueba y se consiguen los siguientes resultados:

<html><body><table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Total</td></tr><tr><td>Marca A</td><td>0.5</td><td>0.0</td><td>3.2</td><td>1.4</td><td>0.0</td><td>1.0</td><td>8.6</td><td>2.9</td><td>17.6</td></tr><tr><td>Marca B</td><td>4.7</td><td>6.2</td><td>0.0</td><td>10.52.1</td><td></td><td>0.8</td><td></td><td></td><td>24.3</td></tr><tr><td>Total</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>41.9</td></tr></table></body></html>

a) Emplear Análisis de Varianza para probar si las dos marcas difieren en contenido de aflatoxina, con un nivel de significancia $\scriptstyle { a = 0 . 0 5 }$ . b) Probar la misma hipótesis usando la prueba t-bimuestral.

1. Hipótesis nula: las dos marcas difieren en contenido de aflatoxina Hipótesis alternativa: No difieren

2. Nivel de significancia: α $= 0 . 0 5$ $\alpha : = 0 . 0 5$

3. Criterio se acepta la Ho si F $< 2 . 8 1 6$

$$
\mathrm { y l } : = \left( 0 . 5 0 3 . 2 1 . 4 0 1 . 0 8 . 6 2 . 9 \right) ^ { \mathrm { T } }
$$

$$
\mathrm {  ~ n _ 1 ~ } : = \mathrm {  ~ \ l e n g t h ( y 1 ) ~ } \mathrm {  ~ \qquad n _ 2 ~ } : = \mathrm {  ~ \ l e n g t h ( y 2 ) ~ } \mathrm {  ~ \underset { \scriptstyle \wedge \ n } { \longrightarrow } ~ } + \mathrm {  ~ n _ 1 ~ } + \mathrm {  ~ n _ 2 ~ } = 1 4 \mathrm {  ~ \qquad ~ } \mathrm {  ~ \biggr ~ k _ { \wedge \ n } ^ { \ k } = ~ } 2
$$

$$
\underbrace { \nu 2 } _ { M m } : = \nu - \nu 1 = 1 2
$$


$$
\operatorname { \underset { \mathbf { \dot { \mathbf { M } } } } { \mathrm { T } } } : = \sum _ { \mathrm { ~ j ~ = ~ 1 ~ } } ^ { \mathfrak { n } _ { 1 } } \mathfrak { y } \mathbb { 1 } _ { \mathrm { j } } \qquad \quad \mathbb { T } _ { 2 } : = \sum _ { \mathrm { ~ j ~ = ~ 1 ~ } } ^ { \mathfrak { n } _ { 2 } } \mathfrak { y } \mathbb { 2 } _ { \mathrm { j } }
$$

$$
\underset { \mathbf { \dot { N } } \mathbf { \dot { w } } } { \underbrace { \boldsymbol { \mathbb { C } } } } = \frac { 1 } { \mathrm { N } } \mathbf { \cdot } \left( \left[ \sum _ { \mathrm { j } = 1 } ^ { \mathrm { n _ { 1 } } } \mathrm {  \ y l } _ { \mathrm { j } } + \sum _ { \mathrm { j } = 1 } ^ { \mathrm { n _ { 2 } } } \mathrm {  \ y } \boldsymbol { 2 } _ { \mathrm { j } } \right) \right) ^ { 2 } = 1 2 5 . 4 0 1
$$

$$
\mathrm { S S T : = \sum _ { j = 1 } ^ { n _ { l } } \left( ^ { y l } j \right) ^ { 2 } + \sum _ { j   \ = 1 } ^ { n _ { 2 } } \left( ^ { y 2 } j \right) ^ { 2 } - C = 1 4 6 . 2 4 9 }
$$

$$
{ \mathrm { S S } } _ { - } \mathrm { T r } : = \sum _ { \mathrm { i } = 1 } ^ { \mathrm { k } } \ \frac { \left( \mathrm { T } _ { \mathrm { i } } \right) ^ { 2 } } { \mathrm { n } _ { \mathrm { i } } } - \mathbf { C } = 1 1 . 7 3 4
$$

$$
\mathrm { M S \_ T r } : = { \frac { \mathrm { S S \_ T r } } { \nu 1 } } = 1 1 . 7 3 4
$$

$$
{ \mathrm { S S E } } : = { \mathrm { S S T } } - { \mathrm { S S } } \_ { \mathrm { T r } } = 1 3 4 . 5 1 5
$$

$$
\mathrm { M S E } : = { \frac { \mathrm { S S E } } { \nu 2 } } = 1 1 . 2 1
$$


<html><body><table><tr><td>Fuentesde Variacion</td><td>Grados Libertad</td><td>deSuma Cuadrados</td><td>deMedia Cuadrada</td><td>F</td></tr><tr><td>Tratamientos</td><td>1</td><td>11.74</td><td>11.74</td><td>1.05</td></tr><tr><td>Error</td><td>12</td><td>134.51</td><td>11.21</td><td></td></tr><tr><td>Total</td><td>13</td><td>146.25</td><td></td><td></td></tr></table></body></html>

Dado que $1 . 0 5 < 4 . 7 5$ (valor de F, de Tablas, con $\mathrm { \alpha } { = } 0 . 0 5$ , $\mathbf { \nabla } \boldsymbol { \mathrm { v } } 1 = 1$ y $\scriptstyle { \mathrm { v } } 2 = 1 2$ ) se Acepta la Hipótesis Nula, luego dos marcas NO difieren en el contenido de aflatoxina.

b)   
1. Hipótesis nula: las dos marcas difieren en contenido de aflatoxina Hipótesis alternativa: No difieren   
2. Nivel de significancia: $\mathtt { q } = 0 . 0 5$ $\underset { N } { \underbrace { \alpha : = } } ~ 0 . 0 5$

ν n 1 n 2:= + - 2 = 12 grados de libertad $\displaystyle { \mathfrak { t } } 0 2 5 : = { \mathfrak { q } } { \mathfrak { t } } { \left( 1 - { \frac { \alpha } { 2 } } , \nu \right) } = 2 . 1 7 9$

3. Criterio se acepta la Ho si 2.179 < t < 2.816

$$
\mathbf { w } : = - 3 , - 2 . 9 9 . . 3
$$


El estadístico para esta prueba es:

$$
\mathbf { t } = { \frac { \left[ \left( { \overline { { \mathbf { x } _ { 1 } } } } - { \overline { { \mathbf { x } _ { 2 } } } } \right) - \delta \right] } { \sqrt { \left( \mathbf { n } _ { 1 } - 1 \right) \cdot \left( \mathbf { s } _ { 1 } \right) ^ { 2 } + \left( \mathbf { n } _ { 2 } - 1 \right) \cdot \left( \mathbf { s } _ { 2 } \right) ^ { 2 } } } } \cdot { \sqrt { \frac { \mathbf { n } _ { 1 } \cdot \mathbf { n } _ { 2 } \cdot \left( \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } - 2 \right) } { \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } } } }
$$

$$
\mathbf { t } : = { \frac { \operatorname* { m e a n } ( \mathbf { y } \mathbf { 1 } ) - \operatorname* { m e a n } ( \mathbf { y } \mathbf { 2 } ) - 0 } { \sqrt { { \left( \mathbf { n } _ { 1 } - \mathbf { 1 } \right) } \cdot { \cfrac { \mathbf { n } _ { 1 } } { \mathbf { n } _ { 1 } } } \cdot \mathbf { v a r } ( \mathbf { y } \mathbf { 1 } ) + { \left( \mathbf { n } _ { 2 } - \mathbf { 1 } \right) } \cdot { \cfrac { \mathbf { n } _ { 2 } } { \mathbf { n } _ { 2 } - 1 } } \cdot \mathbf { v a r } ( \mathbf { y } \mathbf { 2 } ) } } }  \cdot { \sqrt { \frac { \mathbf { n } _ { 1 } \cdot \mathbf { n } _ { 2 } \cdot \left( \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } - \mathbf { 2 } \right) } { \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } } } }  = - 1 . 0 2 3
$$


$\mathbf { t } = - 1 . 0 2 3$

5. Decisión: Se aprecia que $\operatorname { t } \left( - 1 . 0 2 3 \right) >$ -t025 por lo tanto se Acepta la Hipótesis Nula de que las dos marcas NO difieren en el contenido de aflatoxina.

Se supondrá que el experimentador tiene a su disposición mediciones relativas a a tratamientos distribuidos en b bloques.

Se considerará el caso en que hay exactamente una observación de cada tratamiento en cada bloque (para el caso anterior, cada laboratorio probaría un disco de cada tira). Si yij denota la observación relativa al i-esimo tratamiento y al j-ésimo bloque,

es la media de las b observaciones para el i-ésimo tratamiento es la media de las a observaciones para el j-ésimo bloque es la gran media de las a.b observaciones se emplea el siguiente esquema en esta clase de clasificación con dos criterios:

<html><body><table><tr><td></td><td></td><td>BB</td><td></td><td>B</td><td></td><td>Bb</td><td>Medias</td></tr><tr><td>Tratamiento 1</td><td>y1</td><td>y12</td><td></td><td>yii</td><td></td><td>y1b</td><td></td></tr><tr><td>Tratamiento2</td><td>y21</td><td>y22</td><td></td><td>yi</td><td>…</td><td>y2b</td><td>y2</td></tr><tr><td></td><td>…</td><td>…</td><td></td><td></td><td>…</td><td></td><td></td></tr><tr><td>Tratamiento i</td><td>yi</td><td>yi2</td><td></td><td>yi</td><td>…</td><td>Vib</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tratamiento k</td><td>ya1</td><td>ya2</td><td></td><td>Yai</td><td>…</td><td>Yab</td><td>yk</td></tr><tr><td>Medias</td><td>，</td><td></td><td></td><td></td><td></td><td>y</td><td></td></tr></table></body></html>

Al esquema se lo llama aleatorio, siempre que los tratamientos sean asignados al azar dentro de cada bloque.

Cuando se usa un punto en lugar de un subíndice, esto significa que la media se obtiene sumando sobre él.

El modelo que se supondrá para el análisis con una observación por “celda” está dado por:

$$
\mathrm { y _ { i j } = \mu + \alpha _ { i } + \beta _ { j } + \varepsilon _ { i j } }
$$

aquí $\mu$ es la gran media, ${ \bf q _ { i } }$ es el efecto de i-ésimo tratamiento, $\beta _ { \mathrm { i } }$ el efecto del j-ésimo bloque y los  $\ddot { \bf l }$ son valores de variables aleatorias independientes normalmente distribuidas que tienen media cero y varianza común $\sigma ^ { 2 }$ .   
Se restringen los parámetros imponiendo las condiciones que:

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { a } } \underset { } { \alpha } _ { \mathrm { i } } = 0 \qquad \sum _ { \mathrm { j = 1 } } ^ { \mathrm { b } } \underset { } { \beta } _ { \mathrm { j } } = 0
$$

En el análisis de clasificación con dos criterios, cada tratamiento es representado una vez dentro de cada bloque, el objetivo principal consiste en probar la significancia de las diferencias entre las medias o sea, probar la Hipótesis Nula:

$$
\mathfrak { a } _ { 1 } = \mathfrak { a } _ { 2 } = \mathfrak { . . . } = \mathfrak { a } _ { \mathrm { a } } = 0 .
$$

Más aún, quizás convenga probar si la división en bloques ha sido eficaz, esto es probar que la Hipótesis Nula: $\beta _ { 1 } = \beta _ { 2 } = . . . = \beta _ { \nu } = 0$ puede rechazarse o no.

En cualquier caso, la Hipótesis alterna establece que al menos uno de los efectos no es cero.

Como en el análisis con un criterio, se fundará la prueba de significancia mediante comparaciones de $\sigma ^ { 2 }$ (una basada en la variación entre tratamientos, la otra basada en la variación entre bloques y la última que mide el error experimental ).

Nótese que sólo el último es una estimación de $\sigma ^ { 2 }$ cuando cualquiera (o ambas) las Hipótesis Nulas no son válidas.

Las sumas de cuadrados requeridas están dadas por el siguiente teorema:

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { a } } \sum _ { \mathrm { j = 1 } } ^ { \mathrm { b } } { \binom { \mathrm { y } _ { \mathrm { i j } } - \mathrm { \overline { { y } } } _ { \mathrm { . . . } } ^ { - } } { \mathrm { i = 1 } } } ^ { 2 } = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { a } } \sum _ { \mathrm { j = 1 } } ^ { \mathrm { b } } { \binom { \mathrm { y } _ { \mathrm { i j } } - \mathrm { \overline { { y } } } _ { \mathrm { i } } - \mathrm { \overline { { y } } } _ { \mathrm { . . } } ^ { - } + \mathrm { \overline { { y } } } _ { \mathrm { . . } } ^ { - } } { \mathrm { i = 1 } } } ^ { 2 } + \ . . .
$$

$$
\mathbf { S S T } = \mathbf { S S E } + \mathbf { S S } ( \mathbf { T r } ) + \mathbf { S S } \underline { { \mathbf { \delta B l } } }
$$

En la práctica se usan las siguientes fórmulas:

$$
\begin{array} { l l } { { \displaystyle { \mathrm { S S T } } = \sum _ { \mathrm { i } = 1 } ^ { \mathrm { a } } \sum _ { \mathrm { j } = 1 } ^ { \mathrm { b } } \left( \mathrm { y } _ { \mathrm { i } } \right) ^ { 2 } - \mathrm { C } } } & { { \displaystyle { \mathrm { S S } } ( \mathrm { T r } ) = \sum _ { \mathrm { b } } ^ { 1 } \sum _ { \mathrm { i } = 1 } ^ { \mathrm { a } } \left( \mathrm { T } _ { \mathrm { i . } } \right) ^ { 2 } - \mathrm { C } } } \\ { { \displaystyle { \mathrm { S S T } } ( \mathrm { B l } ) = \frac { 1 } { \mathrm { a } } \cdot \sum _ { \mathrm { j } = 1 } ^ { \mathrm { b } } \mathrm { T . j } ^ { 2 } - \mathrm { C } } } & { { \displaystyle { \mathrm { C } } = \frac { 1 } { \mathrm { a . b } } \mathrm { T . } ^ { 2 } } } \end{array}
$$

Donde:

C es el término de corrección $\mathrm { T _ { i } }$ es la suma de las b observaciones para el i-ésimo tratamiento $\mathrm { T } _ { \mathrm { + } }$ es la suma de las a observaciones para el j-ésimo bloque T.. es la suma de todas las observaciones

Empleando esta sumas de cuadrados, se puede rechazar la Hipótesis Nula de que las ${ \bf { \alpha } } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } } \mathrm { ~  ~ \alpha ~ } _ { \bf { \alpha } }$ son todas nulas, con un nivel de significancia $\alpha$ si:

$$
\mathrm { F \_ T r } = \frac { \mathrm { M S \_ T r } } { \mathrm { M S E } } = \frac { \frac { \mathrm { S S \_ T r } } { \mathrm { a - 1 } } } { \frac { \mathrm { S S E } } { \left( \mathrm { a - 1 } \right) \cdot \left( \mathrm { b - 1 } \right) } }
$$

excede $\mathrm { F _ { a } }$ con (a-1) y (a-1).(b-1) grados de libertad.

Se puede rechazar la Hipótesis Nula de que todas las $\beta _ { \mathrm { i } }$ son todas nulas, con un nivel de significancia $\alpha$ si:

$$
\mathrm { F _ { \mathrm { - } } B l = \frac { M S \mathrm { \^ B l } } { M S E } = \frac { \frac { S S \mathrm { \^ { } _ { - } B l } } { b - 1 } } { \frac { S S E } { ( a - 1 ) \cdot ( b - 1 ) } } }
$$

excede $\operatorname { F } _ { \mathfrak { a } } \mathtt { c o n } ( \mathfrak { b } - 1 )$ y (a-1).(b-1) grados de libertad.

Nótese que las medias de los cuadrados MS_Tr, MS_Bl y MSE se definen otra vez como las correspondientes sumas de cuadrados divididas entre sus grados de libertad. La siguiente tabla resume todo el procedimiento:

<html><body><table><tr><td>Fuentesde Variacion</td><td>Grados deSumade Libertad</td><td>Cuadrados</td><td>MediaCuadrada</td><td>F</td></tr><tr><td>Tratamientos</td><td>a-1</td><td>SS(Tr)</td><td>MS(Tr)=SS(Tr)/(a-1)</td><td>Fx=MS(Tr）/MSE</td></tr><tr><td>Bloques</td><td>b-1</td><td>SS(BI)</td><td>MS(B1)=SS(B1)/(b-1)</td><td>FBl=MS(B1)/MSE</td></tr><tr><td>Error</td><td>(a-1).(b-1)</td><td>SSE</td><td>MSE=SSE/(a-1).(b-1)</td><td></td></tr><tr><td>Total</td><td>a.b-1</td><td>SST</td><td></td><td></td></tr></table></body></html>

Ejemplo: Se diseñó un experimento para estudiar el rendimiento de cuatro detergentes diferentes. Las siguientes lecturas de “blancura” se obtuvieron con un equipo especialmente diseñado para $^ { l 2 }$ cargas de lavado , distribuidas en tres modelos de lavadoras:

<html><body><table><tr><td></td><td>Lavadora1</td><td>Lavadora2</td><td>Lavadora3</td><td>Totales</td></tr><tr><td>Detergente A</td><td>45</td><td>43</td><td>51</td><td>139</td></tr><tr><td>DetergenteB</td><td>47</td><td>46</td><td>52</td><td>145</td></tr><tr><td>Detergente C</td><td>48</td><td>50</td><td>55</td><td>153</td></tr><tr><td>Detergente D</td><td>42</td><td>37</td><td>49</td><td>128</td></tr><tr><td>Totales</td><td>182</td><td>176</td><td>207</td><td>565</td></tr></table></body></html>

Considerando los detergentes como tratamientos y las lavadoras como bloques, obtener la Tabla de Análisis de Varianza y probar, con un nivel de significación 0.01, si existen diferencias entre los detergentes y/o entre las lavadoras.

1 Hipótesis Nula: $\alpha _ { 1 } = \alpha _ { 2 } = \alpha _ { 3 } = \alpha _ { 4 } = 0 , \beta _ { 1 } = \beta _ { 2 } = \beta _ { 3 } = 0$ Hipótesis Alternativa: no todas las $\alpha$ y tampoco las $\beta$ iguales a 0. 2 - Nivel de significancia: $\alpha { = } 0 . 0 1$ .

$$
\ g _ { \dot { w } } = 0 . 0 1
$$

$$
\mathbf { y } : = \left( \begin{array} { l l l l } { 4 5 } & { 4 3 } & { 5 1 } & { 1 3 9 } \\ { 4 7 } & { 4 6 } & { 5 2 } & { 1 4 5 } \\ { 4 8 } & { 5 0 } & { 5 5 } & { 1 5 3 } \\ { 4 2 } & { 3 7 } & { 4 9 } & { 1 2 8 } \\ { 1 8 2 } & { 1 7 6 } & { 2 0 7 } & { 5 6 5 } \end{array} \right) \qquad \mathrm { a : = r o w s ( y ) - 1 = 4 }
$$

3- Criterio: Se rechaza Ho si $\mathrm { F } > $ (este valor corresponde a $\mathrm { F _ { 0 . 0 1 } }$ con $\mathrm { v } 1 = 3 \mathrm { ~ y ~ } \mathrm { v } 2 = 6 )$

O si $\mathrm { F } { > } 1 0 . 9$ (este valor corresponde a $\mathrm { F } _ { 0 . 0 1 } \mathrm { c o n v } 1 = 2$ y $\mathsf { v } 2 = 6$ ) ν1 := a 1 - = 3 $\underbrace { \nu 2 \ldots } _ { \boldsymbol { \mathsf { M M } } } : = \boldsymbol { \mathsf { b } } - 1 = 2 \qquad \underbrace { \nu \mathopen { : } = \boldsymbol { \mathsf { a } } \cdot \boldsymbol { \mathsf { b } } - 1 } _ { \boldsymbol { \mathsf { M } } }$ ν3 := ν ν- 1 - ν2 = 6 $\left| \mathrm { F T r 0 1 } : = \mathrm { q F } ( 1 - \alpha , \nu 1 , \nu 3 ) = 9 . 7 8 \right|$ F crítico para tratamiento $\mathrm { \ F B l { 0 1 : = } \ q F ( 1 \mathrm { \ - } \alpha } { \mathrm { \alpha } } { \mathrm { , } \nu } 2 { \mathrm { , } \nu } 3 ) \mathrm { \ = } 1 0 . 9 2 5 \ \mathrm { \ ] }$ F crítico para bloques

4 Cálculos:

$\begin{array} { r l } & { \mathrm { i : = 0 . a - 1 } \qquad \mathrm { j : = 0 . b - 1 } \qquad \mathsf { i n d i c e s } } \\ & { \mathrm { T \_ p u n t o \_ i : = ( y ) } ^ { \left. _ { \mathsf { b + 1 } } \right. } \qquad \mathrm { T \_ p u n t o \_ i } ^ { \mathrm { T } } = ( 1 3 9 \quad 1 4 5 \quad 1 5 3 \quad 1 2 8 \quad 5 6 5 ) } \\ & { \mathrm { T \_ p u n t o \_ p u n t o \ : = \left( y \right) } ^ { \left. _ { \mathsf { a + 1 } } \right. } \qquad \mathrm { T \_ j \_ p u n t o } ^ { \mathrm { T } } = ( 1 8 2 \quad 1 7 6 \quad 2 0 7 \quad 5 6 5 ) } \end{array}$   
$\mathrm { T \_ p u n t o \_ p u n t o : = y _ { a + 1 , b + 1 } = 5 6 5 }$   
${ \underset { \mathbf { \theta } } { \underbrace { \mathbb { C } } : = } } { \frac { \mathrm { { T } } { \_ { \mathbf { \theta } } \mathrm { p u n t o } } { \_ { \mathbf { \theta } } \mathrm { p u n t o } } ^ { 2 } } { \mathrm { a } { \cdot } \mathrm { b } } } = 2 6 6 0 2 . 0 8 3$   
$\underset { \mathrm { i } = 1 } { \overset { \mathrm { S S T } } { \mathop { : } } = \sum } \sum _ { \mathrm { i } } ^ { \mathrm { a } } \sum _ { \mathrm { j } = 1 } ^ { \mathrm { b } } \left( \mathrm { y } _ { \mathrm { i } , \mathrm { j } } \right) ^ { 2 } - \mathrm { C } = 2 6 4 . 9 1 7$   
S $\underset { \mathrm { \tiny ~ i = 1 } } { \mathrm {  ~ \scriptstyle ~ S ~ } } \mathrm {  ~ \scriptstyle ~ T r : } = \frac { 1 } { { \mathrm {  ~ b ~ } } } \cdot \sum _ { \mathrm { \tiny ~ i = 1 } } ^ { \mathrm { \tiny ~ a ~ } } \left( \mathrm { \mathrm { T \_ ~ p u n t o \_ i } } _ { \mathrm { i } } \right) ^ { 2 } - \mathrm { \bf C } = 1 1 0 . 9 1 7$   
S $\displaystyle \mathsf { S \_ B l } : = \frac { 1 } { \mathrm { a } } \cdot \sum _ { \mathrm { j } = 1 } ^ { \mathrm { b } } \left( \mathrm { T \_ j \_ p u n t o _ { j } } \right) ^ { 2 } - \mathrm { C } = 1 3 5 . 1 6 7$

SSE := SST SS_Tr - - SS_Bl = 18.833

La Tabla queda:

<html><body><table><tr><td>Fuentesde Variacion</td><td>Grados deSuma Libertad</td><td>CuadradosCuadrada</td><td>deMedia</td><td>F</td></tr><tr><td>Detergentes</td><td>3</td><td>111</td><td>37.0</td><td>11.6</td></tr><tr><td>Lavadoras</td><td>2</td><td>135</td><td>67.5</td><td>21.1</td></tr><tr><td>Error</td><td>6</td><td>19</td><td>3.2</td><td></td></tr><tr><td>Total</td><td>11</td><td>265</td><td></td><td></td></tr></table></body></html>

t := 0 0.01 , .. 12

t FTr01 , , 11.6   
t FBl01 , , 21.1

5- Decisión: Dado que $1 1 . 6 > 9 . 7 8$ (crítico) se Rechaza la primera Hipótesis Nula, por lo tanto hay diferencia significativa entre la eficacia de los detergentes, y dado que $2 1 . 1 > 1 0 . 9 $ (crítico) también hay diferencia significativa entre la eficacia de las lavadoras.

# COMPARACIONES MÚLTIPLES

Con las pruebas F empleadas se demostraba si las diferencias entre varias medias eran significativas, pero no informaban si una media en particula r (o medias) difieren en forma significativa de otra media considerada (o grupo de medias). En el caso de los pesos de los recubrimientos puede ser importante que los laboratorios difieran unos de los otros.

Si un experimentador tiene ante sí k medias, parece razonable probar entre todos los pares posibles, esto es efectuar $\mathrm { k } ( \mathrm { k } { - } 1 ) / 2$ pruebas t bimuestrales.

Esto no es eficiente. Para ello se utilizan Pruebas de Comparaciones Múltiples, y entre ellas la Prueba del Rango Múltiple de Duncan.

Las suposiciones básicas son, en esencia, las del análisis de la varianza en una dimensión para tamaños muestrales iguales.

La prueba compara el Rango de Mínima Significancia, $\mathbf { R _ { p } } ,$ dado por:

$$
\mathrm { R _ { p } = s _ { \overline { { x } } } \cdot r _ { p } }
$$

S- es una estimación de:

$$
\sigma _ { _ { \mathrm { X } } } ^ { - } = \frac { \sigma } { \sqrt { \mathrm { n } } }
$$

y puede calcularse como:

$$
\mathrm { _ { \Delta x } ^ { s - } } = \sqrt { \frac { \mathrm { M S E } } { \mathrm { ~ n ~ } } }
$$

donde MSE es la media de los cuadrados de error en el Análisis de Varianza. El valor de $\mathrm { { r _ { p } } }$ depende del valor deseado de significancia y del número de grados de libertad correspondiente a la MSE, que se obtienen de tablas existentes en la bibliografía (Miller y Freund, “Estadística para Ingenieros”, tablas 12a, para $\mathrm { \alpha } { = } 0 . 0 5$ y 12b, para $\mathrm { \alpha { \stackrel { \textstyle } { - } } 0 1 }$ , con p=2,3,…,10 y para varios grados de libertad entre 1 y 120). http://www.um.edu.ar/math/estadis/tablas/duncan.htm

# Ejemplo: Con respecto a los datos de los pesos de los recubrimientos de estaño, aplicar la prueba del Rango Múltiple de Duncan para probar cuáles medias de los laboratorios difieren de las otras empleando un nivel de significancia de 0.05.

<html><body><table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Prom.</td></tr><tr><td>Lab.A</td><td>.25</td><td>.27</td><td>.22</td><td>.30</td><td>.27</td><td></td><td></td><td></td><td>28.32.24.31.26</td><td></td><td>.21</td><td>.28</td><td>0.268</td></tr><tr><td>Lab.B</td><td>.18</td><td>.28</td><td>.21</td><td>.23</td><td>.25</td><td></td><td>20.27.19</td><td></td><td>.24.22</td><td></td><td>.29</td><td>.16</td><td>0.227</td></tr><tr><td>Lab. C</td><td>.19</td><td>.25</td><td>.27</td><td>.24</td><td>.18</td><td></td><td>.26.28.24.25.20</td><td></td><td></td><td></td><td>.21</td><td>.19</td><td>0.230</td></tr><tr><td>Lab.D</td><td>.23</td><td>.30</td><td>.28</td><td>.28</td><td>.24</td><td>.34.20.18.24.28</td><td></td><td></td><td></td><td></td><td>.22</td><td>.21</td><td>0.250</td></tr></table></body></html>

Para ello se ordenan, en forma creciente, las cuatro medias muestrales:

<html><body><table><tr><td>Laboratorio</td><td>B</td><td>C</td><td>D</td><td>A</td></tr><tr><td>Media</td><td></td><td></td><td>0.2270.2300.250</td><td>0.268</td></tr></table></body></html>

Luego, se hace el siguiente cálculo considerando el valor MSE de la Tabla de Análisis de la Varianza.

$$
\mathrm { s } _ { _ { \overline { { X } } } } = { \sqrt { \frac { 0 . 0 0 1 5 } { 1 2 } } } = 0 . 0 1 1
$$

siendo el número de grados de libertad $\mathbf { v } = \mathbf { k } ( \mathbf { n - 1 } ) = 4 4 .$ . Por interpolación, en la Tabla 12-a, se obtienen los valores de rp:

<html><body><table><tr><td colspan="10">df p-&gt; 2 3 4 5 6 7 8 9</td></tr><tr><td colspan="10"></td></tr><tr><td>363738</td><td>2.868</td><td>3.015</td><td>3.111</td><td>3.180</td><td>3.232</td><td>3.274</td><td>3.307</td><td>3.335</td></tr><tr><td></td><td>2.865</td><td>3.013</td><td>3.109</td><td>3.178</td><td>3.230</td><td>3.272</td><td>3.305</td><td>3.333</td></tr><tr><td></td><td>2.863</td><td>3.010</td><td>3.106</td><td>3.175</td><td>3.228</td><td>3.270</td><td>3.303</td><td>3.331</td></tr><tr><td>39</td><td>2.861</td><td>3.008</td><td>3.104</td><td>3.173</td><td>3.226</td><td>3.268</td><td>3.301</td><td>3.330</td></tr><tr><td>40</td><td>2.858</td><td>3.005</td><td>3.102</td><td>3.171</td><td>3.224</td><td>3.266</td><td>3.300</td><td>3.328</td></tr><tr><td>48</td><td>2.843</td><td>2.991</td><td>3.087</td><td>3.157</td><td>3.211</td><td>3.253</td><td>3.288</td><td>3.318</td></tr><tr><td>60</td><td>2.829</td><td>2.976</td><td>3.0/3</td><td>3.143</td><td>3.198</td><td>3.241</td><td>3.277</td><td>3.307</td></tr></table></body></html>

2.858 2.843-   
Para p = 2 2.843  + = 2.851 2   
Para p= 3 $2 . 9 9 1 + { \frac { 3 . 0 0 5 - 2 . 9 9 1 } { 2 } } = 2 . 9 9 8$   
Para p= 4 $3 . 0 8 7 + { \frac { 3 . 1 0 2 - 3 . 0 8 7 } { 2 } } = 3 . 0 9 5$

<html><body><table><tr><td>p</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Ip</td><td>2.85</td><td>3.00</td><td>3.09</td></tr></table></body></html>

multiplicando rp por =0.011

<html><body><table><tr><td>P</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Rp</td><td>0.031</td><td>0.033</td><td>0.034</td></tr></table></body></html>

3.160 0.273  = 0.863

El rango de las cuatro medias es $0 . 2 6 8 - 0 . 2 2 7 = 0 . 0 4 1$ , que excede a $\mathbf { R 4 } = \mathbf { 0 . 0 3 4 }$ , que es el rango significativo mínimo.

Esto era de esperar, porque la prueba F indicó que las diferencias entre las cuatro medias eran significativas con ${ \bf q } = { \bf 0 . 0 5 }$ .   
Para probar que hay diferencias significativas entre tres medias adyacentes, se obtienen los rangos de $0 . 0 3 8 \mathrm { y } 0 . 0 2 3$ respectivamente para 0.230, 0.250, 0.268 y 0.227, 0.230, 0.250.   
Puesto que el primero de estos valores sobrepasa a $\mathrm { R } _ { 3 } { \bf = } { \bf 0 . 0 3 } 3$ , las diferencias   
correspondientes no son significativas.   
Por último en el caso de parejas adyacentes de medias, ningún par adyacente tiene rango mayor que el rango significativo mínimo $\mathbf { R } _ { 2 } = \mathbf { 0 . 0 3 1 }$ .

Esto se resume:


donde se ha dibujado una línea bajo cualquier conjunto de medias adyacentes para las cuales el rango es menor que un valor correspondiente de $\mathrm { R } _ { \mathrm { p } }$ , esto es, bajo cualquier conjunto de medias adyacentes, para las cuales las diferencias no son significativas.

Se concluye así que el Laboratorio A obtiene los pesos medios de recubrimiento más alto que los Laboratorios B y C.

# OTROS DISEÑOS EXPERIMENTALES

Para el diseño de Cuadro Latino, se supone que es necesario comparar tres tratamientos A, B y C en presencia de otras dos fuentes de variabilidad. Por ejemplo, los tres tratamientos pueden ser tres métodos de soldadura para conductores eléctricos y las dos fuentes de variabilidad pueden ser:

1) Diferentes operarios   
2) La utilización de diferentes fundentes para soldar.

Si se consideran tres operarios y tres fundentes, el experimento puede disponerse así:

<html><body><table><tr><td></td><td></td><td>Fundente1Fundente2</td><td>Fundente3</td></tr><tr><td>Operador1</td><td>A</td><td>B</td><td>C</td></tr><tr><td>Operador2</td><td>C</td><td>A</td><td>B</td></tr><tr><td>Operador3</td><td>B</td><td>C</td><td>A</td></tr></table></body></html>

Aquí cada método de soldadura se aplica sólo una vez por cada operario junto con cada fundente.

Un arreglo experimental como el descripto de denomina Cuadro Latino.

Un Cuadro Latino n x n es una arreglo cuadrado de n letras distintas, las cuales aparecen sólo una vez en cada renglón y en cada columna.

Nótese que en un experimento en Cuadro Latino de n tratamientos es necesario incluir $\mathrm { n } ^ { 2 }$ observaciones, n por cada tratamiento.   
Un experimento en Cuadro Latino sin repetición da solo (n-1).(n-2) grados de libertad para estimar el error experimental. De modo que tales experimentos son efectuados en contadas ocasiones sin repetición cuando n es pequeño.

Si existe un total de r repeticiones, el análisis de los datos presupone el siguiente modelo, donde $\mathbf { y _ { i j ( k ) l } }$ es la observación en el i-ésimo renglón, en la j-ésima columna, de la l-ésima repetición y el subíndice $\mathrm { k \Omega }$ indica el k-ésimo tratamiento:

$$
| \mathrm { y } _ { \mathrm { i j } ( \mathbf { k } ) 1 } | = | \mathrm { \mathsf { k } } + \mathrm { \boldsymbol { \alpha } } _ { \mathrm { { i } } } + \mathrm { \boldsymbol { \beta } } _ { \mathrm { { j } } } + \mathrm { \boldsymbol { \gamma } } _ { \mathrm { { k } } } + \mathrm { \boldsymbol { \rho } } _ { \mathrm { { l } } } + \varepsilon _ { \mathrm { { i j } } ( \mathbf { k } ) } \} \qquad \mathrm { p a r a ~ i , j , k = 1 , 2 , . . . , n ~ y } | = 1 , 2 , . . . , \mathrm { r }
$$

con las restricciones:

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \mathrm {  ~ { ~ \alpha ~ } ~ } _ { \mathrm { { i } } } = 0 \qquad \sum _ { \mathrm { j } = 1 } ^ { \mathrm { n } } \mathrm {  ~ { ~ \beta ~ } ~ } _ { \mathrm { i } } = 0 \qquad \sum _ { \mathrm { k } = 1 } ^ { \mathrm { n } } \mathrm {  ~ { ~ \gamma ~ } ~ } _ { \mathrm { i } } = 0 \qquad \sum _ { \mathrm { l } = 1 } ^ { \mathrm { r } } \mathrm {  ~ { ~ \rho ~ } ~ } _ { \mathrm { i } } = 0
$$

donde:

$\mu$ es la gran media   
${ \bf { \alpha } } _ { \bf { \alpha } } \alpha _ { \bf { { i } } }$ es el efecto de la i-ésima fila o renglón   
$\beta _ { \mathrm { j } }$ es el efecto de la j-ésima columna   
$\gamma _ { \mathbf { k } }$ es el efecto del k-ésimo tratamiento   
$\rho _ { \mathsf { I } }$ es el efecto de la l-ésima repetición   
ij(k)l variable aleatoria independiente normal con $\mu { = } 0$ y varianza común $\sigma ^ { 2 }$ . Nótese que por los “efectos de los renglones” y los “efectos de las columnas” se entienden los efectos de las dos variables extrañas y que se incluyen los “efectos de la repetición” como una tercera variable extraña.   
$\mathrm { k \Omega }$ está entre paréntesis ya que para un diseño de Cuadro Latino dado, k es   
automáticamente determinada cuando i y j se conocen.   
La hipótesis principal a probar es la Hipótesis Nula $\gamma _ { \bf k } = 0$ , para toda k, es decir la Hipótesis Nula de que no existe diferencia en la eficacia de n tratamientos.   
También se puede probar si $\mathrm { \bf q _ { i } } = 0$ , para todo i y $\beta _ { \mathbf { j } } { = } 0$ , para todo j con el fin de   
comprobar si las dos variables extrañas tienen algún efecto sobre el fenómeno que se está considerando.   
Mas aún, se puede probar es la Hipótesis Nula $\rho _ { \mathbf { l } } { = } 0$ , para toda l, contra la alternativa que no todas las $\rho _ { \mathsf { I } }$ son iguales a cero, y esta prueba del efecto de las repeticiones puede ser importante si las partes del experimento , que representan los Cuadros Latinos individuales, fueron realizados en distintos días, a diferentes temperaturas, etc..

Las fórmula a aplicar son:

$$
\mathsf { C } = \frac { 1 } { { \mathrm { r } } { \cdot } { \mathrm { n } } ^ { 2 } } { \cdot } \mathrm { T } \ldots ^ { 2 }
$$

Donde:

T total de las r.n observaciones en todos los i-esimos renglones total de las r.n observaciones en todas las j-ésimas columnas T1 total de las $\mathrm { n } ^ { 2 }$ observaciones en todos las1-ésimasrepeticiones T（k） total de las r.n observaciones relativas a los j-esimos tratamientos T.. es el gran total de las $\mathrm { r } . \mathrm { n } ^ { 2 }$ observaciones

Lo que lleva al siguiente cuadro de análisis:

<html><body><table><tr><td>Fuentede Variacion</td><td>Gradosde libertad</td><td>Suma de cuadrados</td><td>CuadradosMedios</td><td>F</td></tr><tr><td>Tratamientos</td><td>n-1</td><td>SS(Tr)</td><td>MS(Tr)=SS(Tr)/(n-1)</td><td>MS(Tr)/MSE</td></tr><tr><td>Renglon</td><td>n-1</td><td>SSR</td><td>MSR=SSR/(n-1)</td><td>MSR/MSE</td></tr><tr><td>Columna</td><td>n-1</td><td>SSC</td><td>MSC=SSC/(n-1)</td><td>MSC/MSE</td></tr><tr><td>Repeticion</td><td>r-1</td><td>SS(Rep)</td><td>MS(Rep)=SS(Rep)/(r-1)</td><td>MS(Rep)/MSE</td></tr><tr><td>EIror</td><td>(n-1)(r.n+r-3）</td><td>SSE</td><td>MSE=SSE/[(n-1).（r.n+r-3）</td><td></td></tr><tr><td>Total</td><td>r.n2-1</td><td>SST</td><td></td><td></td></tr></table></body></html>

# Ejemplo: Suponer que se efectúan repeticiones del experimento de soldadura empleando el siguiente arreglo:

Repeticion I Fundentes   

<html><body><table><tr><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td>Operador1</td><td>A</td><td>B</td><td>C</td></tr><tr><td>Operador2</td><td>C</td><td>A</td><td>B</td></tr><tr><td>Operador 3</td><td>B</td><td>C</td><td>A</td></tr></table></body></html>

RepeticionⅡ Fundentes   

<html><body><table><tr><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td>Operador1</td><td>C</td><td>B</td><td>A</td></tr><tr><td>Operador2</td><td>A</td><td>C</td><td>B</td></tr><tr><td>Operador3</td><td>B</td><td>A</td><td>C</td></tr></table></body></html>

Los resultados, que señalan el número de kilogramos fuerza de tensión requeridos para separar los puntos soldados, fueron como se indica a continuación:

RepeticionI Fundentes   

<html><body><table><tr><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td>Operador1</td><td>14.0</td><td>16.5</td><td>11.0</td></tr><tr><td>Operador2</td><td>9.5</td><td>17.0</td><td>15.0</td></tr><tr><td>Operador3</td><td>11.0</td><td>12.0</td><td>13.5</td></tr></table></body></html>

RepeticionⅡ Fundentes   

<html><body><table><tr><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td>Operador1</td><td>10.0</td><td>16.5</td><td>13.0</td></tr><tr><td>Operador 2</td><td>12.0</td><td>12.0</td><td>14.0</td></tr><tr><td>Operador3</td><td>13.5</td><td>18.0</td><td>11.5</td></tr></table></body></html>

Analizar el experimento como un Cuadro Latino y probar con un nivel de significación de 0.01 si existen diferencias en los métodos, en los operadores, los fundentes o las repeticiones.

1 - Hipótesis Nula: $\alpha _ { 1 } = \alpha _ { 2 } = \alpha _ { 3 } = 0 ; \beta _ { 1 } = \beta _ { 2 } = \beta _ { 3 } = 0 ; \gamma _ { 1 } = \gamma _ { 2 } = \gamma _ { 3 } = 0 ;$ $\rho _ { 1 } = \rho _ { 2 } = 0$

Hipótesis Alternativa: no todas las $\alpha , \beta , \gamma , \rho$ iguales a 0.

2 - Nivel de significancia: $\alpha { = } 0 . 0 1$ . α := 0.01

3 - Criterio: Para tratamientos, renglones y columnas se rechaza Ho si $\mathrm { F } { > } 7 . 5 6$ (este valor corresponde a $\mathrm { F _ { 0 . 0 1 } c o n v _ { 1 } } = 2 \mathrm { y } \mathrm { \ v _ { 2 } } = 1 0 )$

Para repeticiones se rechaza Ho si $\mathrm { F } > $ (este valor corresponde a $\mathrm { F } _ { 0 . 0 1 } \mathrm { c o n v } _ { 1 } = 1$ y $\begin{array} { r } { v _ { 2 } = 1 0 \ } \end{array}$ )

$$
\nu \mathrm { R } : = { \mathfrak { n } } - 1 \qquad \nu \mathrm { C } : = \nu \mathrm { R } \qquad \nu \mathrm { T } : = \nu \mathrm { R } \qquad \nu \mathrm { r } : = { \mathfrak { r } } - 1
$$

$$
V : = \mathrm { n } ^ { 2 } \cdot \mathrm { r } - 1 = 1 7 \qquad \quad \nu \mathrm { E } : = \nu - \nu \mathrm { R } - \nu \mathrm { C } - \nu \mathrm { T } - \nu \mathrm { r } = 1 0
$$

$$
{ \big | } { \mathrm { F R 0 1 : } } = { \mathrm { q F } } ( 1 - \alpha , \nu \mathrm { R } , \nu \mathrm { E } ) = 7 . 5 5 9 { \big | } \qquad { \mathrm { F R 0 1 } } = { \mathrm { F C 0 1 } } = { \mathrm { F T 0 1 } }
$$

t 0 0.01:= , .. 12


4 Cálculos:

T_1_punto_punto $\therefore 1 4 + 1 6 . 5 + 1 1 + 1 0 + 1 6 . 5 + 1 3 = 8 1$

T_2_punto_punto $: = 9 . 5 + 1 7 + 1 5 + 1 2 + 1 2 + 1 4 = 7 9 . 5$   
T_3_punto_punto $: = 1 1 + 1 2 + 1 3 . 5 + 1 3 . 5 + 1 8 + 1 1 . 5 = 7 9 . 5$   
T_punto_1_punto $: = 1 4 + 9 . 5 + 1 1 + 1 0 + 1 2 + 1 3 . 5 = 7 0$   
T_punto_2_punto $: = 1 6 . 5 + 1 7 + 1 2 + 1 6 . 5 + 1 2 + 1 8 = 9 2$   
T_punto_3_punto $: = 1 1 + 1 5 + 1 3 . 5 + 1 3 + 1 4 + 1 1 . 5 = 7 8$   
$\mathrm { T A } : = 1 4 + 1 7 + 1 3 . 5 + 1 2 + 1 8 + 1 3 = 8 7 . 5$   
$\mathrm { T B } : = 1 1 + 1 6 . 5 + 1 5 + 1 6 . 5 + 1 3 . 5 + 1 4 = 8 6 . 5$   
$\mathrm { T C } : = 9 . 5 + 1 2 + 1 1 + 1 0 + 1 2 + 1 1 . 5 = 6 6$   
T_punto_punto $\begin{array} { r } { 1 : = 1 4 + 1 6 . 5 + 1 1 + 9 . 5 + 1 7 + 1 5 + 1 1 + 1 2 + 1 3 . 5 = 1 1 9 . 5 } \end{array}$   
T_punto_punto_2 10 16.5 := + + 13 + 12 + 12 + 14 + 13.5 + 18 + 11.5 = 120.5   
T_punto_punto_punto $: = \mathrm { T } \phantom { \frac { A } { A } }$ _punto_punto_ $\mathrm { \Omega } 1 + \mathrm { T } \mathrm { \Omega }$ _punto_punto $2 = 2 4 0$   
$\begin{array} { r l } { \mathrm { T \_ c u a d r a d o : } = 1 4 ^ { 2 } + 1 6 . 5 ^ { 2 } + 1 1 ^ { 2 } + 9 . 5 ^ { 2 } + 1 7 ^ { 2 } + 1 5 ^ { 2 } + 1 1 ^ { 2 } + 1 2 ^ { 2 } + 1 3 . 5 ^ { 2 } \ldots } & { = 3 3 0 4 . 5 } \\ { + 1 0 ^ { 2 } + 1 6 . 5 ^ { 2 } + 1 3 ^ { 2 } + 1 2 ^ { 2 } + 1 2 ^ { 2 } + 1 4 ^ { 2 } + 1 3 . 5 ^ { 2 } + 1 8 ^ { 2 } + 1 1 . 5 ^ { 2 } } \end{array}$   
$\underset { \mathrm { { \left. \infty \right.}  } } { \mathbb { C } } : = \frac { \mathrm { { T } } \mathrm { { \_ p u n t o } } \mathrm { { p u n t o } } \mathrm { { p u n t o } } 2 } { \mathrm { { n } } ^ { 2 } \cdot \mathrm { { r } } } = 3 2 0 0$   
SST := T_cuadrado C - = 104.5   
$\begin{array} { r l } & { \mathrm { S S T r } : = \frac { \left( \mathrm { T A } ^ { 2 } + \mathrm { T B } ^ { 2 } + \mathrm { T C } ^ { 2 } \right) } { \mathrm { n \cdot r } } - \mathrm { C } = 4 9 . 0 8 3 } \\ & { \mathrm { S S R } : = \frac { \left( \mathrm { T } _ { - 1 } \mathrm { J } \mathrm { u n l o } _ { - } \mathrm { p u n l o } ^ { 2 } + \mathrm { T } _ { - 2 } \mathrm { p u n l o } _ { - } \mathrm { p u n l o } ^ { 2 } + \mathrm { T } _ { - 3 } \mathrm { p u n l o } _ { - } \mathrm { p u n l o } ^ { 2 } \right) } { \mathrm { n \cdot r } } - \mathrm { C } = 0 . 2 5 } \\ & { \mathrm { S S C } : = \frac { \left( \mathrm { T } _ { \mathrm { p u n l o } \_ \mathrm { 1 \cdot p u n l o } ^ { 2 } } + \mathrm { T } _ { \mathrm { p u n l o } \_ \mathrm { 2 \cdot p u n l o } ^ { 2 } } + \mathrm { T } _ { \mathrm { - p u n l o } \_ { - } \mathrm { 3 \cdot p u n l o } ^ { 2 } } \right) } { \mathrm { n \cdot r } } - \mathrm { C } = 4 1 . 3 3 3 } \\ & { \mathrm { S S r } : = \frac { \left( \mathrm { T } _ { \mathrm { p u n l o } \_ \mathrm { p u n l o } _ { - } } \mathrm { 1 } ^ { 2 } + \mathrm { T } _ { \mathrm { p u n l o } \_ \mathrm { p u n l o } _ { - } 2 } ^ { 2 } \right) } { \mathrm { n \cdot r } ^ { 2 } } - \mathrm { C } = 0 . 0 5 6 } \end{array}$   
SSE := SST SSR - - SSC - SSTr - SSr = 13.778   
La Tabla queda:

<html><body><table><tr><td>Fuentesde Variacion</td><td>Gradosde Libertad</td><td>Suma de Cuadrados</td><td>Media Cuadrada</td><td>F</td></tr><tr><td>Tratamientos (Metodos)</td><td>2</td><td>49.1</td><td>24.6</td><td>17.6</td></tr><tr><td>Renglones (Operadores)</td><td>2</td><td>0.2</td><td>0.1</td><td>0.1</td></tr><tr><td>Columnas (Fundentes)</td><td>2</td><td>41.3</td><td>20.6</td><td>14.7</td></tr><tr><td>Repeticiones</td><td>1</td><td>0.1</td><td>0.1</td><td>0.1</td></tr><tr><td>Error</td><td>10</td><td>13.8</td><td>1.4</td><td></td></tr><tr><td>Total</td><td>17</td><td>104.5</td><td></td><td></td></tr></table></body></html>

FT 17.6 := FR 0.1:= FC 14.7 := Fr 0.1 :=

t 0 0.01 := , .. 20

t Fr01, , Fr

5 - Decisión: En lo que respecta a tratamientos (métodos) y a columnas (fundentes) dado que $\mathrm { F } = 1 7 . 6$ (línea verde) y 14.7 (línea negra) sobrepasan a 7.56 se rechazan las Hipótesis Nulas correspondientes.   
Para renglones (operarios) dado que $\mathsf { F } = 0 . 1$ (línea cyan) no excede a 7.56, no se rechaza Ho.   
En cuanto a las repeticiones dado que $\mathsf { F } = 0 . 1$ no excede 10.0 no se rechaza Ho.

En otras palabras, se concluye que hay diferencias en los métodos y en los fundentes, pero no en los operadore s ni en las repeticiones, en cuanto a afectación de la resistencia mecánica de la soldadura.

Si se quiere hacer la prueba del Rango Múltiple de Duncan con $\alpha = 0 . 0 1$ , se calculan los promedios de los tratamientos y se ordenan

$$
{ \frac { \mathrm { T A } } { 6 } } = 1 4 . 5 8 3 \qquad { \frac { \mathrm { T B } } { 6 } } = 1 4 . 4 1 7 \qquad { \frac { \mathrm { T C } } { 6 } } = 1 1
$$

<html><body><table><tr><td></td><td>MetodoC</td><td>MetodoB</td><td>Metodo A</td></tr><tr><td>Media</td><td>11.0</td><td>14.4</td><td>14.6</td></tr></table></body></html>

MSE := 1.4 $\mathrm { { s \_ x \_ m e d i a : = \sqrt { \frac { M S E } { 3 } } } = 0 . 6 8 3 \qquad }  &  \chi \backslash = 1 0$

α=0.01

Valores Criticos q'(p，df;

<html><body><table><tr><td>df p-&gt; 2 3 4</td></tr><tr><td>1 90.02490.02490.024 2 14.036 14.03614.036 34 8.260 8.321 8.321</td></tr><tr><td>5678 5.702 5.893 5.989 5.243 5.439 5.549 4.949 5.145 5.260</td></tr><tr><td>4.745 4.939 5.056 A506 A 707 4.906</td></tr><tr><td>10 4.482 4.671 4.789 11 4.392 4.579 4.697</td></tr></table></body></html>

<html><body><table><tr><td>p</td><td>2</td><td>3</td></tr><tr><td>Ip</td><td>4.482</td><td>4.671</td></tr></table></body></html>

Multiplicando $\boldsymbol { \mathsf { r } } _ { \mathsf { p } }$ por s:x_media:

<html><body><table><tr><td>P</td><td>2</td><td>3</td></tr><tr><td>Rp</td><td>3.061</td><td>3.19</td></tr></table></body></html>

El rango de las tres medias es $1 4 . 6 - 1 1 = 3 . 6$ , que excede a $\mathrm { R } 3 \mathrm { = } 3 . 1 9$ , que es el rango significativo mínimo.

Esto era de esperar, porque la prueba F indicó que las diferencias entre las tres medias eran significativas con $\mathrm { { q } = 0 . 0 1 }$ .

Para probar que hay diferencias significativas entre dos medias adyacentes, se obtienen los rangos de $0 . 2 \mathrm { y } 3 . 4$ respectivamente . Puesto que el primero de estos valores NO sobrepasa a ${ \bf R } 2 = 3 . 0 6 { \bf 1 }$ , las diferencias correspondientes no son significativas.


En consecuencia, se concluye que el Método C produce uniones con soldaduras significativamente más débiles que los Métodos A y B.

La eliminación de tres fuentes extrañas de variabilidad puede lograrse mediante el diseño de Cuadro Grecolatino. En un diseño consistente en un arreglo cuadrado de n letras latinas y n letras griegas; más exactamente, cada letra latina aparece sólo una vez al lado de cada letra griega:

<html><body><table><tr><td>Aa</td><td>Bβ</td><td>CY</td><td>D8</td></tr><tr><td>B8</td><td>AY</td><td>Dβ</td><td>Ca</td></tr><tr><td>cβ</td><td>Dα</td><td>A8</td><td>BY</td></tr><tr><td>DY</td><td>C8</td><td>Bα</td><td>Aβ</td></tr></table></body></html>

También se los llama “Cuadros Grecolatinos Ortogonales”. Como ejemplo, suponer el caso de las soldaduras, la temperatura es otra fuente de variabilidad. Si tres temperaturas de soldado, denotadas $\cdot$ , $\cdot$ y $\gamma$ se utilizan junto con los tres métodos, los tres operadores (renglones) y tres fundentes (columnas), la repetición de un experimento apropiado de Cuadro Grecolatino puede establecerse así:

<html><body><table><tr><td></td><td>Fundente1</td><td></td><td>Fundente2Fundente3</td></tr><tr><td>Operador 1</td><td>Aα</td><td>Bβ</td><td>CY</td></tr><tr><td>Operador 2</td><td>CY</td><td>Aβ</td><td>Bα</td></tr><tr><td>Operador3</td><td>Bβ</td><td>Ca</td><td>AY</td></tr></table></body></html>

Así pues, el Método A sería utilizado por el Operador 1, usando fundente 1, a la temperatura $\alpha$ , por el Operador 2, usando fundente 2, a la temperatura $\beta$ y por el Operador 3, usando fundente 3, a la temperatura $\gamma$ . En un Cuadro Grecolatino, cada variable (representada por renglones, columnas, letras latinas o letras griegas) está “distribuida equitativamente” respecto a las otras variables.