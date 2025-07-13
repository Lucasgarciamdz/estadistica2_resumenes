CONCEPTOS BÁSICOS DE LA ESTADÍSTICA

# INTRODUCCION

Se reproducira un exprimento aleatorio en el que se arrojara 1000 veces una moneda, y se guardara el resultado en un vector X.

$\mathrm { \Delta n : = ~ 1 0 0 0 }$ T. de la muestra $\mathrm { i } : = 0 \ldots \mathrm { n - 1 }$ Indice para el vector X

$$
\mathrm { X _ { i } } \mathrm { : = r o u n d ( r n d ( 1 ) ) }
$$

Ahora se realizara un conteo de cuanto 1's y $\boldsymbol { 0 } ^ { \prime } \boldsymbol { \mathsf { s } }$ hay en el vector

$$
{ \mathrm { n } } 1 : = \sum { \mathrm { X } } = 5 0 2
$$

Si se suman todos los elementos del vector se obtiene la cantidad de 1's que hay en el, dado que los 0's no suman al resultado.

${ \tt n } 0 : = { \tt n } - { \tt n } 1 = 4 9 8$ El complemento de n1 es el numero de 0's

Ahora se puede obtener la frecuencia relativa con la que aparecen cada uno de los resultados

$$
\mathrm { n r } 1 : = \frac { \mathrm { n l } } { \mathrm { n } } = 0 . 5 0 2
$$

$$
\mathrm { n r } 0 : = \frac { \mathrm { n 0 } } { \mathrm { n } } = 0 . 4 9 8
$$

Por ultimo podemos graficar la funcion de densidad de probabilidad en base a la muestra

![](images/d6ef9d65e1f1dac13f46e9af544d40d5527474afe8033a22c637274612b56795.jpg)

Ejemplo sacado del libro Miller & Freund

Supongamos que de una muestra de tamano n se calcula la media muestral, xm. Es natural pensar que si tomamos otra muestra la media de esa muestra seria distinta a la media de la primera. Estas diferencias entre muestras se atribuyen normalmente al azar, lo cual plantea dudas en cuanto a su distribucion.

Para encarar esto de manera experimental, supongamos que tomamos una muestra de tamano $\mathsf { n } = 1 0$ de una poblacion que sigue una distribucion uniforme discreta.

$$
f ( x ) = { \left\{ \begin{array} { l l } { \displaystyle { \frac { 1 } { 1 0 } } } & { \quad { \mathrm { p a r a ~ } } x = 0 , 1 , 2 , \ldots , 9 } \\ { 0 } & { \quad { \mathrm { d e ~ o t r a ~ f o r m a } } } \end{array} \right. }
$$

n := 10 i 0 n 1:= .. -

muestra $: =$ floor rnd 10 ( ) ( )

<html><body><table><tr><td rowspan="2">T muestra</td><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>8</td><td>3</td><td>6</td><td>2</td><td>1</td><td>2</td><td>0</td><td>9</td><td>6</td><td>4</td></tr></table></body></html>

Ahora calculamos la media muestrala del vector obtenido

$$
\mathrm { \ x m \_ m u e s t r a : = \ m e a n ( m u e s t r a ) = 4 . 1 }
$$

Como dijimos, es natural pensar que si tomamos varias muestras es probable que estas difieran en valor entre si. Por lo que se a continuacion se toman 50 muestras de tamano 10 cada una y se calcula un vector de XM que posee las medias muestrales de cada de ellas.

$$
\begin{array} { r l } & { \underset { \mathbf { \dot { W } } } { \mathbf { N } } : = \ : 5 0 0 \qquad \mathbf { \dot { j } } : = 0 \ldots \mathbf { N } - 1 } \\ & { } \\ & { \mathbf { M _ { \dot { j } , \dot { i } } } : = \ : \mathrm { f l o o r } ( \mathrm { r n d } ( 1 0 ) ) } \end{array}
$$

Ahora se calcula el vector de medias muestrales

$$
\mathrm { { X M } _ { j } : = \ m e a n \Big [ \Big ( M ^ { T } \Big ) ^ { \big < j } \Big ] }
$$

<html><body><table><tr><td rowspan="2">XMT=</td><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>5.7</td><td>4.4</td><td>4.6</td><td>3.5</td><td>6.1</td><td>4.4</td><td>3.5</td><td>4.1</td><td>4.3</td><td>…</td></tr></table></body></html>

Para el vector x los extremos son:

$$
\mathrm { i n f } : = \mathrm { m i n } ( \mathrm { X M } ) = 1 . 6
$$

$$
\operatorname* { s u p } : = \operatorname* { m a x } ( \mathrm { X M } ) = 7 . 2
$$

Si se desea un Vector de Intervalos (I) de 5 subintervalos:

$$
\mathbf { k } : = 0 \ldots \mathrm { n s }
$$

$$
\Delta : = { \frac { \mathrm { s u p - i n f } } { \mathrm { n s } } }
$$

Luego el valor de I será:

$$
\begin{array} { l } { { \mathrm { I } _ { \mathrm { k } } : = \mathrm { i n f } + \mathrm { k } { \cdot } \Delta } } \\ { { \mathrm { I } ^ { \mathrm { T } } = ( 1 . 6 2 . 7 2 3 . 8 4 4 . 9 6 6 . 0 8 7 . 2 ) } } \end{array}
$$

En este punto, se deberá hacer un "conteo" de cuàntos elementos del vector x caen en los subintervalos $\mathsf { m } { + } \Delta$ , $\mathsf { m } { + } 2 \Delta$ , $\ m { + } 3 \Delta$ , etc. Esta operación se puede hacer automáticamente con la instrucción:

$$
\begin{array} { r l } & { \mathrel { \mathop { \mathrm { H } } : } \mathrel { = } \mathrm { h i s t } ( \mathrm { I } , \mathrm { X M } ) } \\ & { \mathrel { } } \\ & { \mathrel { \mathop { \mathrm { H } } } ^ { \mathrm { T } } = ( 1 3 ~ 1 0 3 ~ 2 1 7 ~ 1 4 6 ~ 2 0 ) } \end{array}
$$

Para hacer normalizadas estas frecuencias absolutas, se deben dividir por el tamaño de la muestra (N)

$$
{ \sf h } : = \frac { { \sf H } } { { \sf N } }
$$

$$
{ \boldsymbol { \mathrm { h } } } ^ { \mathrm { T } } = ( 0 . 0 2 6 \ \ \ 0 . 2 0 6 \ \ \ 0 . 4 3 4 \ 0 . 2 9 2 \ \ 0 . 0 4 )
$$

A partir de este punto se puede construir el histograma correspondiente:

![](images/cf29b405d4a69de2f7a4ff4d30e9fdcfd8b3689062651f951b61833567ad21e9.jpg)

Segun la teoria, la media y la desviacion estandar de la distribcion uniforme se calculan como:

$$
\mu : = \frac { 1 } { 1 0 } \cdot \sum _ { \mathbf { k } = 0 } ^ { 9 } \mathbf { \Omega } ( \mathbf { k } ) = 4 . 5 \sigma : \sigma : \sigma : \sqrt { \frac { 1 } { 1 0 } \cdot \sum _ { \mathbf { k } = 0 } ^ { 9 } \left[ \left( \mathbf { k } - \mu \right) ^ { 2 } \right] } = 2 . 8 7 2 \cdot
$$

Y del vector de medias obtenemos los siguientes resultados:

$$
\mathrm { 4 _ { X M } : = \ m e a n ( X M ) = 4 . 5 3 6 \qquad } \qquad \sigma _ { \mathrm { X M } } : = \mathrm { s t d e v ( X M ) = 0 . 9 0 8 }
$$

Vemos que $\mu _ { \mathrm { x } \mathrm { m } } \mathsf { e s }$ un buen estimador de la media poblacional, mientras que podemos notar la siguiente relacion entre la desviacion estandar poblacional σ con la d. e. $\sigma _ { \mathsf { X M } }$

$$
\frac { \sigma } { \sqrt { \mathrm { n } } } = 0 . 9 0 8
$$

Que ademas, cuando el tamano de la muestra n (n minuscula) es considerablemente grande respecto al tamano total de la poblacion N (n mayuscula), se debe incluir un factor de correccion por finitud de la poblacion.

$$
\mathrm { F } = { \frac { \mathrm { N } - \mathrm { n } } { \mathrm { N } - 1 } }
$$

Si embargo, como en el ejemplo se muestrea de una poblacion en la que se supone infinita o bien finita con reposicion, este factor no se incluye en la misma. Por ultimo, marcar que cuando el tamano de la muestra es menor al $5 \%$ del tamano poblacional el factor tiende a 1, por lo que su aporte es despreciable.

# FORMULAS PARA $\mu _ { \mathsf { X M } } \Upsilon \sigma _ { \mathsf { X M } }$

Sea una poblacion con media $\mu \gamma$ varianza $\mathfrak { O } ^ { 2 }$ , que sigue una distribucion X. Si se toma una muestra de tamano n y se calcula la media muestral de la misma se obtiene un valor de la variable aleatoria XM (X barra) que posee tambien media $\mu$ al igual que X.

Para empezar, podemos mostrar que XM es una variable aleatoria. Considerando que una muestra de n elementos consiste de un vector con n observaciones de la variable aleatoria X, o bien, como es mas util verlo, consiste de n observaciones simples (individuales) de n variables aleatorias independientes entre si, que siguen la distribucion de la variable aleatoria X. Vector de observaciones:

$( \mathsf { x } _ { 1 } , \mathsf { x } _ { 2 } , \ldots , \mathsf { x } _ { \mathsf { n } } )$ que corresponden a n observaciones de la v.a. X

Vector de variables aleatorias:

$( { \sf X } _ { 1 } , { \sf X } _ { 2 } , \dots , { \sf X } _ { \sf n } )$ ) siendo $\mathsf { X } _ { \mathrm { i } }$ una v.a. independiente que sigue una distribucion como la

de X

Con lo que podemos ver que cada $\mathsf { X } _ { \mathrm { i } }$ tendra media $\mu \ y \sigma ^ { 2 }$ igual que X. Por lo tanto, cada vez que calculemos la media muestral, obtendremos lo siguiente:

$$
\mathrm { x m } = { \frac { \mathrm { x } _ { 1 } + \mathrm { x } _ { 2 } + \mathrm { . . . } + \mathrm { x } _ { \mathrm { n } } } { \mathrm { n } } }
$$

$$
\mathrm { { X M } = \frac { X _ { 1 } + X _ { 2 } + \ldots + X _ { n } } { n } = \frac { 1 } { \bar { n } } . \sum _ { i = 1 } ^ { n } \mathrm { { X _ { i } } } }
$$

Ahora si calculamos la esperanza matematica de la variable aleatoria XM:

$$
\operatorname { E } ( \operatorname { X M } ) = \operatorname { E } \left( { \frac { \mathrm { X } _ { 1 } + \mathrm { X } _ { 2 } + \ldots + \mathrm { X } _ { \mathrm { n } } } { \mathrm { n } } } \right) = \operatorname { E } \left( { \frac { \mathrm { X } _ { 1 } } { \mathrm { n } } } \right) + \operatorname { E } \left( { \frac { \mathrm { X } _ { 2 } } { \mathrm { n } } } \right) + \ldots + \operatorname { E } \left( { \frac { \mathrm { X } _ { \mathrm { n } } } { \mathrm { n } } } \right)
$$

Recordando la propiedad:

$$
\mathrm { E } ( \mathrm { a } { \cdot } \mathrm { X } ) = \mathrm { a } { \cdot } \mathrm { E } ( \mathrm { X } )
$$

Se obtiene que:

$$
\mathrm { E ( X M ) } = { \frac { \mathrm { E { \big ( } X _ { 1 } { \big ) } } } { \mathrm { n } } } + { \frac { \mathrm { E { \big ( } X _ { 2 } { \big ) } } } { \mathrm { n } } } + \ldots + { \frac { \mathrm { E { \big ( } X _ { n } { \big ) } } } { \mathrm { n } } }
$$

Ademas se sabe que cada $\mathsf { X } _ { \mathsf { i } }$ sigue una distribucion como la de X, por lo tanto la esperanza de Xi sera igual a $\mu$

$$
\mathrm { E ( X M ) } = { \frac { \mathrm { E { \big ( } X _ { 1 } { \big ) } } } { \mathrm { n } } } + { \frac { \mathrm { E { \big ( } X _ { 2 } { \big ) } } } { \mathrm { n } } } + \ldots + { \frac { \mathrm { E { \big ( } X _ { n } { \big ) } } } { \mathrm { n } } } = { \frac { \mu } { \mathrm { n } } } + { \frac { \mu } { \mathrm { n } } } + \ldots + { \frac { \mu } { \mathrm { n } } }
$$

Con lo que obtenemos:

$$
\mu _ { \mathrm { X M } } = \mathrm { E } ( \mathrm { X M } ) = \mu
$$

La media de la distribucion de medias es igual a la media poblacional

Asi mismo, bajo las condiciones anteriores tenemos que ${ \sigma _ { \mathsf { X M } } } ^ { 2 }$ :

$$
\sigma _ { \mathrm { X M } } { } ^ { 2 } = \mathrm { v a r } ( \mathrm { X M } ) = \mathrm { v a r } \left( { \frac { \mathrm { X } _ { 1 } + \mathrm { X } _ { 2 } + \ldots + \mathrm { X } _ { \mathrm { n } } } { \mathrm { n } } } \right) = \mathrm { v a r } { } \left( { \frac { \mathrm { X } _ { 1 } } { \mathrm { n } } } \right) + \mathrm { v a r } { } \left( { \frac { \mathrm { X } _ { 2 } } { \mathrm { n } } } \right) + \ldots + \mathrm { v a r } { } \left( { \frac { \mathrm { X } _ { \mathrm { n } } } { \mathrm { n } } } \right)
$$

Recordando la propiedad:

$$
\operatorname { v a r } ( \mathbf { a } { \cdot } \mathbf { X } ) = \mathbf { a } ^ { 2 } { \cdot } \operatorname { v a r } ( \mathbf { X } )
$$

Se obtiene

que:

$$
\mathrm { { \sigma _ { X M } } ^ { 2 } = \mathrm { { v a r } ( X M ) = \frac { \ v a r \left( X _ { 1 } \right) } { n ^ { 2 } } + \frac { \ v a r \left( X _ { 2 } \right) } { n ^ { 2 } } + \ldots + \frac { \ v a r \left( X _ { n } \right) } { n ^ { 2 } } } }
$$

Ademas se sabe que cada $\mathsf { X } _ { \mathsf { i } }$ sigue una distribucion como la de X, por lo tanto la varianza de Xi sera igual a $\sigma ^ { 2 }$

$$
\sigma _ { \mathrm { X M } } ^ { \mathrm { ~ 2 ~ } } = \mathrm { v a r ( X M ) } = { \frac { \mathrm { v a r { \bigl ( } X _ { 1 } { \bigr ) } } } { \mathrm { n } ^ { \mathrm { ~ 2 ~ } } } } + { \frac { \mathrm { v a r { \bigl ( } X _ { 2 } { \bigr ) } } } { \mathrm { n } ^ { \mathrm { ~ 2 ~ } } } } + \ldots + { \frac { \mathrm { v a r { \bigl ( } X _ { n } { \bigr ) } } } { \mathrm { n } ^ { \mathrm { ~ 2 ~ } } } } = { \frac { \sigma ^ { 2 } } { \mathrm { n } } } + { \frac { \sigma ^ { 2 } } { \mathrm { n } } } + \ldots + { \frac { \sigma ^ { 2 } } { \mathrm { n } } }
$$

Con lo que obtenemos:

$$
{ \sigma _ { \mathrm { X M } } } ^ { 2 } = \mathrm { v a r } ( \mathrm { X M } ) = \frac { \sigma ^ { 2 } } { \mathrm { n } }
$$

La varianza de la distribucion de medias para poblaciones INFINITAS es igual a la varianza poblacional entre n

CENTRAL Enunciado:

Si XM es la media de una muestra aleatoria de tamano n tomada de una poblacion con media $\mu \gamma$ desviacion estandar σ, entonces:

$$
Z = { \frac { \mathrm { X M - \mu } } { \frac { \sigma } { \sqrt { \mu } } } }
$$

es una variable aleatoria, cuya funcion de distribucion tiende a una distribucion normal estandar cuando n tiende a ∞   
En la practica, el teorema ofrece una buena aproximacion cuando n $\mathtt { 1 } > = 3 0$ , es decir, no es necesaria una muestra de tamano excesivamente grande.   
Ademas, si la muestra proviene de una poblacion con distribucion normal, XM es normal sin importar el tamano de la muestra.   
En la practica dificilmente se conoce de antemano la desviacion estandar de una poblacion, sin embargo, para un tamano de muestra suficientemente grande es razonable sustituir a σ (d. e. poblacional) por s (d. e. muestral).   
Es decir, si la media proviene de una población grande $\bf { n } > 3 0$ , aún suponiendo que no se conozca la varianza de la misma) es posible definir una variable aleatoria llamada media estandarizada cuyos valores están dados por:

Como se ha mencionado anteriormente, cuando el tamano de la muestra es mayor a 30 no hay problema en sustituir a σ con s, sin embargo cuando no se conoce σ y la muestra es menor a 30, se debe recurrir a otro tipo de distribucion, a una t-Student, para lo cual primero se debe cumplir el requisito de que la muestra provenga de una poblacion normal. Cuando la muestra proviene de una poblacion normal, con σ desconocida y el tamano es menor a 30 es posible definir un estadistico como el siguiente:

Que se distribuye como una t-Student con parametro $v = n - 1$ (nu), conocidos como grados de libertad.

$\mathbf { x } : = - 4 , - 3 . 9 9 \ldots 4$

![](images/f2632cccb96734a223efbf789287141e7a2b6873de3f7eb25936adad6aa31a59.jpg)

# TEOREMA DE

CHEVYSHEV

Por ultimo punto a cubrir, cuando: - La distribucion no puede suponerse normal - El tamano de la muestra es inferior a 30

Es posible recurrir al teorema de chevyshev el cual nos permite obtener una expresion para intonol)d) oonfionz) ro la media.   
generar un Enunciado:

La proporción de las medias en un conjunto de datos que se sitúa dentro de las k desviaciones estándar de la media no es menor de $1 . 1 / 1 \times ^ { 2 }$ , siendo $\mathsf { k } \geq 1$

$$
\mathrm { P } \big ( \big | \mathrm { x m - \mu } \big | \leq \mathrm { k } { \cdot } \sigma _ { \mathrm { x m } } \big ) \leq 1 - \frac { 1 } { \mathrm { k } ^ { 2 } }
$$

Graficamente:

![](images/727a18a09ece11a26d26794b850d703b70637af10fb0c1654aa8bdf02e3754f5.jpg)

A partir de aquí se puede verificar que por definición de la varianza

$$
{ \sigma } ^ { 2 } = \int _ { - \infty } ^ { \infty } { \mathrm { f } ( \mathbf { x } ) \cdot \left( \mathbf { x } - \mu \right) ^ { 2 } \mathrm { d } \mathbf { x } }
$$

que se puede subdividir en tres términos

$$
{ \boldsymbol { \sigma } } ^ { 2 } = \int _ { - \infty } ^ { | \mathbf { u } - \mathbf { k } \cdot \boldsymbol { \sigma } } \mathbf { f } ( \mathbf { x } ) \cdot \left( \mathbf { x } - \mathbf { \boldsymbol { \mu } } \right) ^ { 2 } \mathrm { d } \mathbf { x } + \int _ { | \mathbf { u } - \mathbf { k } \cdot \boldsymbol { \sigma } } ^ { | \mathbf { u } + \mathbf { k } \cdot \boldsymbol { \sigma } } \mathbf { f } ( \mathbf { x } ) \cdot \left( \mathbf { x } - \mathbf { \boldsymbol { \mu } } \right) ^ { 2 } \mathrm { d } \mathbf { x } + \int _ { | \mathbf { u } + \mathbf { k } \cdot \boldsymbol { \sigma } } ^ { \infty } \mathbf { f } ( \mathbf { x } ) \cdot \left( \mathbf { x } - \mathbf { \boldsymbol { \mu } } \right) ^ { 2 } \mathrm { d } \mathbf { x }
$$

y también que

$$
\displaystyle \boldsymbol { \sigma } ^ { 2 } \geq \int _ { - \infty } ^ { | \mathsf { k } - \mathsf { k } \cdot \boldsymbol { \sigma } } \mathbf { f } ( \mathbf { x } ) \cdot \left( \mathbf { x } - \boldsymbol { \mu } \right) ^ { 2 } \mathrm { d } \mathbf { x } + \int _ { | \mathsf { k } + \mathbf { k } \cdot \boldsymbol { \sigma } } ^ { \infty } \mathbf { f } ( \mathbf { x } ) \cdot \left( \mathbf { x } - \boldsymbol { \mu } \right) ^ { 2 } \mathrm { d } \mathbf { x }
$$

DISTRIBUCILas regiones $\mathsf { R } _ { 1 } \cup \mathsf { R } _ { 3 } ( \mathsf { R } _ { 1 }$ “unión” $\mathsf { R } _ { 3 } )$

VARIANZverifican:

$$
| \mathbf { x } - \mathbf { \boldsymbol { \mu } } | \geq \mathbf { k } { \cdot } \sigma \qquad \mathbf { y } \qquad \left( \mathbf { x } - \mathbf { \boldsymbol { \mu } } \right) ^ { 2 } \geq \mathbf { \boldsymbol { \mu } } ^ { 2 } { \cdot } \sigma ^ { 2 }
$$

Luego

$$
\sigma ^ { 2 } \geq \operatorname { k } ^ { 2 } \cdot \sigma ^ { 2 } \cdot \left( \int _ { - \infty } ^ { | t - \operatorname { k } \cdot \sigma } { \mathrm { ~ f ( x ) ~ d x + ~ } } \int _ { | t + \operatorname { k } \cdot \sigma } ^ { \infty } { \mathrm { ~ f ( x ) ~ d x } } \right)
$$

$$
{ \frac { 1 } { { \bf k } ^ { 2 } } } \geq \int _ { - \infty } ^ { { \bf \mu } \mu - { \bf k } \cdot \sigma } { \bf f } ( { \bf x } ) \mathrm { d } { \bf x } + \int _ { { \bf \mu } \mu + { \bf k } \cdot \sigma } ^ { \infty } { \bf f } ( { \bf x } ) \mathrm { d } { \bf x }
$$

$$
\int _ { - \infty } ^ { \mu - \ k \cdot \sigma } \mathbf { f } ( \kappa ) \mathrm { d } \mathbf { x } + \int _ { \mu + \ k \cdot \sigma } ^ { \infty } \mathbf { f } ( \ x ) \mathrm { d } \mathbf { x } = \mathrm { P } ( \left| \kappa - \mu \right| \geq \ k \cdot \sigma )
$$

O también

$$
\operatorname { P } ( \left| \mathbf { x } - \mathbf { \mu } \right| \leq \mathbf { k } { \cdot } \sigma ) \leq 1 - \frac { 1 } { \mathbf { k } ^ { 2 } }
$$

Aplicandolo al muestreo de medias se obtiene:

$$
\mathrm { P } \big ( \big | \mathrm { x m - \mu } \big | \leq \mathrm { k } { \cdot } \sigma _ { \mathrm { x m } } \big ) \leq 1 - \frac { 1 } { \mathrm { k } ^ { 2 } }
$$

Decimos que la probabilidad de que una media muestral difiera de la media poblacional (verdadera) en menos "k" veces la d. e. muestral es menor a 1 menos 1 sobre $\mathsf { k } ^ { 2 }$ Es decir, si quiero generar un intervalo de confianza del $1 0 0 ^ { \star } ( 1 { - } \mathsf { a } ) \%$

![](images/efaee0998de029d96463d6ae757bf2e7a2090d4c8d65d4a4e62498e6e2a32da9.jpg)

![](images/de9e6549d9cf59866e58a03359dd1f5531b0e653ad6ca0ab7c54a3f7536d77ed.jpg)

Ejemplo: Para una muestra de tamaño $\mathbf { n } { = } \mathbf { 1 5 }$ tubos de TV, la vida útil media de operación es $\scriptstyle \mathbf { x m } = 8 9 0 0$ hs con una desviación estándar de $\mathtt { s } = 5 0 0$ hs. Construir un intervalo de confianza $9 0 \%$ para la media de la población si en este caso la vida útil media de operación de todos los tubos no puede suponerse normalmente distribuida.

$$
\begin{array} { l c r } { { 1 - \displaystyle \frac { 1 } { { \bf \sigma } } = 0 . 9 } } & { { ~ \displaystyle { \bf k } : = \sqrt { \frac { 1 } { ( 1 - 0 . 9 ) } } = 3 . 1 6 2 } } \\ { { \displaystyle \underset { \mathrm { M } } { \mathrm {  ~ \scriptstyle ~ \chi ~ } } = 1 5 ~ } } & { { ~ \displaystyle \mathrm { x m } : = 8 9 0 0 ~ } } & { { \displaystyle \underset { \displaystyle \mathrm { N } } { \mathrm {  ~ \scriptstyle ~ \chi ~ } } : = ~ 5 0 0 } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle \mathrm { x m - k \cdot } { \frac { \mathrm { s } } { \sqrt { n } } } = 8 . 4 9 2 \times ~ { 1 0 } ^ { 3 } } } \\ { { } } \\ { { \displaystyle \mathrm { x m + k \cdot } { \frac { \mathrm { s } } { \sqrt { n } } } = 9 . 3 0 8 \times ~ { 1 0 } ^ { 3 } } } \end{array}
$$

$$
8 . 4 9 2 \times { 1 0 } ^ { 3 } < up . 4 < 9 . 3 0 8 \times { 1 0 } ^ { 3 }
$$

Todo lo desarrollado previamente, con el TLC, la t-Student y el teorema de Chevyshev se puede resumir en el siguiente cuadro.

<html><body><table><tr><td>Poblacion</td><td>Tamano de la muestra</td><td>conocida</td><td>desconocida</td></tr><tr><td rowspan="2">Normalmente Distribuida</td><td>Grande (n≥ 30)</td><td>xm±Zα.Oxm</td><td>xm± Zα.Sxm</td></tr><tr><td>Chica(n&lt;30）</td><td>xm± Zq.Oxm</td><td>xm±ta. $xm</td></tr><tr><td rowspan="2">No Normalmente Distribuida</td><td>Grande (n ≥ 30)</td><td>xm± Zα.Oxm</td><td>xm±ZqSxm</td></tr><tr><td>Chica(n&lt;30）</td><td>donde 1-1/k² se define por medio define por medio del del Teorema deTeorema de Chebyshev xm±k.0xm</td><td>donde 1-1/k2 se Chebyshev xm±k.$xm</td></tr></table></body></html>

A continuacion se realizara una verificacion experimental sobre como es la distribucion de la varianza.

Primero, se sabe que la varinza no puede ser negativa, por lo tanto una distribucion normal no puede ajustarse a ella.

Tomando 50 muestras de tamano 10 de una poblacion normal $\begin{array} { r } { \underset { \ r { \mathsf { M } } } { \boldsymbol { \mathsf { n } } } : = 1 0 \quad \underset { \ r { \mathsf { N } } } { \boldsymbol { \mathsf { N } } } : = 1 0 0 0 \quad \quad \_ { \ r { \mathsf { J } } } : = 0 \ldots \mathrm { N } - 1 \qquad \quad \quad \quad \mathrm { M } : = 0 } \end{array}$

$$
\underset { \mathbf { \hat { M } } \mathbf { \hat { y } } } { \mathbf { M } } : = \operatorname { r n o r m } ( \mathrm { n } , 0 , 1 )
$$

Si calculamos la varianza para cada uno de los vectores de muestras:

$$
\mathrm { \Delta V A R _ { j } : = \ v a r ( M _ { j } ) { \cdot } \frac { n } { n - 1 } }
$$

Para el vector x los extremos son:

$$
{ \underset { \mathrm { A W W } } { \mathrm { i n f } } } \mathbf { \cdot } = \mathbf { \mathrm { m i n } } ( \mathrm { V A R } ) = 0 . 1 0 7 \qquad \quad { \underset { \mathrm { A W W } } { \mathrm { s u p } } } \mathbf { \cdot } = \mathbf { \mathrm { m a x } } ( \mathrm { V A R } ) = 3 . 1 9 4
$$

Si se desea un Vector de Intervalos (I) de 5 subintervalos:

ns := 10 número de $\operatorname* { k } _ { N \ i } \colon = 0 \dots \mathrm { n s }$ subintervalos   
$\frac { \Delta } { m } = \frac { \frac { s u p - i n f } { n s } } { n s }$ Incremento

Luego el valor de I será:

<html><body><table><tr><td rowspan="2">T</td><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>0</td><td>0.107</td><td>0.415</td><td>0.724</td><td>1.033</td><td>1.341</td><td>1.65</td><td>1.959</td><td>2.268</td><td></td></tr></table></body></html>

En este punto, se deberá hacer un "conteo" de cuàntos elementos del vector x caen en los subintervalos $\mathsf { m } { + } \Delta$ , $\mathsf { m } { + } 2 \Delta$ , $\mathsf { m } { + } 3 \Delta ,$ etc. Esta operación se puede hacer automáticamente con la instrucción:

$\operatorname { H } _ { \mathsf { M } } : = \mathrm { h i s t } ( \mathrm { I } , \mathrm { V A R } )$

<html><body><table><tr><td rowspan="3">HT=</td><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td>70</td><td>253</td><td>304</td><td>174</td><td>105</td><td>46</td><td>34</td><td>7</td><td>6</td><td>1</td></tr></table></body></html>

Para hacer normalizadas estas frecuencias absolutas, se deben dividir por el tamaño de la muestra (N)

$$
\operatorname* { h } _ { M } : = \frac { H } { N }
$$

<html><body><table><tr><td rowspan="3">hT=</td><td></td><td>0</td><td>１</td><td>2</td><td>3</td><td>4</td><td>５</td><td>6</td><td>7</td></tr><tr><td></td><td>0.07</td><td>0.253</td><td>0.304</td><td>0.174</td><td>0.105</td><td>0.046</td><td>0.034</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html>

A partir de este punto se puede construir el histograma correspondiente:

![](images/0d08353dc2f50c124ad0a79c967153dfd7352a0150c1585328e79beaff1f2933.jpg)

Vemos que sigue una distribucion conocida como Chi cuadrado $( X ^ { 2 } )$ con parametro $v = \mathsf { n } - 1$ grados de libertad.

Esto desemboca en el siguiente teorema.

Enunciado:

Si ${ \mathbb S } ^ { 2 }$ es la varianza de una muestra aleatoria de tamano n proveniente de una poblacion normal con varianza $\mathfrak { O } ^ { 2 }$ , entonces:

$$
{ \boldsymbol { \chi } } ^ { 2 } = { \frac { ( \mathbf { n } - 1 ) \cdot \mathbf { S } ^ { 2 } } { \sigma ^ { 2 } } } = { \frac { \displaystyle \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left( { \mathrm { X } } _ { \mathrm { i } } - { \mathrm { X M } } \right) ^ { 2 } } { \sigma ^ { 2 } } }
$$

es una variable aleatoria que tiene una distribucion chi cuadrada con parametro $v = n - 1$

Un problema que se relaciona mucho con encontrar la distribucion de la varianza es el de encontrar la distribucion de la razon (cociente) entre dos varianzas de dos muestras aleatorias independientes. Este problema es recurrente ya que, como se ve mas adelante, en ocasiones es necsario para determinar el tipo de prueba a realizar si las varianzas de dos poblaciones son iguales o no.

Para esto se utiliza el siguiente teorema.

Enunciado:

Si $\mathsf { S } _ { 1 } { } ^ { 2 } \mathsf { y } \mathsf { S } _ { 2 } { } ^ { 2 }$ son las varianzas de las muestras aleatorias independientes de tamano $\mathsf { n } _ { 1 } \mathsf { y n } _ { 2 }$ respectivamente, tomadas de dos poblaciones normales con la misma varianza, entonces:

$$
\mathrm { F } = { \frac { \left( \mathrm { S } _ { 1 } \right) ^ { 2 } } { \left( \mathrm { S } _ { 2 } \right) ^ { 2 } } }
$$

es una variable aleatoria que se distribuye como una F con parametros $\mathsf { v } _ { 1 } = \mathsf { n } _ { 1 } - 1 \mathsf { y } \mathsf { v } _ { 2 } = \mathsf { n } _ { 2 } .$ - 1 grados de libertad.

t 0 0.001:= , .. 10

#

![](images/0ae3dc385cb9dd76fa2e25dbc772501aae121f343d17c3e854a95a0972edbb47.jpg)

# ESTIMACION PUNTUAL

Se trata de la eleccion de un estadistico, que es un solo valor (numero) calculado a partir de datos muestrales. Para este estadistico se tiene cierta esperanza o seguridad de que se encuentra relativamente "cercano" al valor real del parametro que se esta estimando.

En este contexto, se introduce la caracteristica de que un estimador sea insesgado, lo cual puede expresarse como que la esperanza de ese estimador $\boldsymbol { \Theta } _ { \mathrm { e s t } }$ sea igual al parametro que se desea estimar.

$$
\mathrm { E } \big ( \theta _ { \mathrm { e s t } } \big ) = \theta
$$

Si analizamos a los estimadores de la media poblacional: - Media - Mediana

Vemos que ambos son estimadores insesgados de la media poblacional $\mu$ , sin embargo existe un criterio que permite determinar cual de los dos es un estimador mas eficiente. Se dice que θ1est es un estimador insesgado mas eficiente del parametro θ que ${ \theta } 2 _ { \mathrm { e s t } }$ si:

1. Ambos son estimadores insesgados   
2. La varianza de ${ \boldsymbol { \Theta } } 1 _ { \mathsf { e s t } }$ es menor que la de ${ \theta } 2 _ { \mathrm { e s t } }$

Cuando realizamos este tipo de estimaciones, es sabido de antemano que las probabilidades de acertar exactamente al parametro $\mu \mathsf { s o n }$ practicamente inexistentes. Por lo tanto, es deseable acompanar a esta estimacion con un error maximo de estimacion.

El error se representa como $\mathsf { E } = \mathsf { x m } - \mu$ . Dada una muestra grande $( > = 3 0 )$ ), una varianza conocida y suponiendo la normalidad de la poblacion, se puede afirmar con probabilidad ( 1 - α ) que se satisface la siguiente desigualdad.

$$
- z _ { \frac { \alpha } { 2 } } \leq \frac { \mathrm { X M - \mu } } { \sigma } \leq z _ { \frac { \alpha } { 2 } }
$$

o bien que

$$
\frac { \left| \operatorname { X M } - \mu \right| } { \frac { \sigma } { \sqrt { \eta } } } \leq \mu \frac { \alpha } { 2 }
$$

de donde se despeja $| \mathsf { X M - } | ,$

$\mathrm { E } = \left| \mathrm { X M } - \mu \right| = \mu _ { \alpha } \cdot \frac { \sigma } { \sqrt { \bar { \mu } } }$ Error maximo de estimacion

Donde $z _ { \alpha / 2 }$ es una abscisa que deja a su derecha un area bajo la curva normal igual a ${ \tt o } / 2$ .

![](images/ef5d6e094ee0e9727549ad5776b1ccedf58df557320f1cf8d21c22a76866973f.jpg)

Tambien se puede conocer el error maximo de estrimacion cuando la muestra es menor a 30, posee una varianza desconocida y proviene de una poblacion normal. Para esto usamos el estadistico t que se distribuye como una t-Student y despejamos de igual forma.

$$
\frac { - \mathfrak { t } _ { \alpha } } { 2 } ^ { \leq \frac { \mathrm { X M } - \mu } { \alpha } \leq \mathfrak { t } _ { \alpha } } \frac { \alpha } { 2 }
$$

o bien que

$$
\frac { \left| \mathbf { X } \mathbf { M } - \mathbf { \mu } \right| } { \frac { \mathrm { s } } { \sqrt { \mathrm { n } } } } \leq t _ { \frac { \alpha } { 2 } }
$$

de donde se despeja $\mathsf { X M - } \mu \mid$

E XM = - μ t = s α √r n Error maximo de estimacion 2

# ESTIMACION POR INTERVALO DE CONFIANZA

Dado que, hablando de forma rigurosa, no existe la probabilidad en el punto y ademas en la practica no se espera que las estimaciones puntuales coincidan con las cantidades que se pretende estimar, a veces es preferible generar o presentar los datos en forma de estimaciones por intervalo

Un intervalo de confianza es un intervalo construido en base a la media muestral, con el cual puede especificarse una probabilidad de que el intervalo contenga al valor del parametro $\mu$ (media poblacional)

El grado de confianza asociado a un intervalo de confianza indica el porcentaje de los intervalos que inlcuiran el parametro estimado

![](images/9b6da5f6c9478439a3b1210982ccd0506f43e7ba3f64543f3e6b02a6dde2bff2.jpg)

Para comenzar, como en la seccion anterior, se supone una muestra grande $( n > = 3 0$ ) con varianza poblacional conocida. Haciendo referncia a la desigualdad

$$
- z _ { \frac { \alpha } { 2 } } \leq \frac { \mathrm { X M - \mu } } { \sigma } \leq z _ { \frac { \alpha } { 2 } }
$$

Operando algebraicamente, podemos despejar a la media poblacional $\mu$

$$
- z _ { \alpha } \cdot { \frac { \sigma } { \sqrt { \mathrm { n } } } } \leq \mathrm { X M } - \mu \leq \mathrm { z } _ { \alpha } \cdot { \frac { \sigma } { \sqrt { \mathrm { n } } } }
$$

$$
- z _ { \frac { \alpha } { 2 } } \cdot \frac { \sigma } { \sqrt { \eta } } - \mathrm { X M } \leq - \mu \leq \tau _ { \frac { \alpha } { 2 } } \cdot \frac { \sigma } { \sqrt { \eta } } - \mathrm { X M }
$$

$$
\frac  z _ { \alpha } \cdot \frac { \sigma } { \sigma } + \mathrm { X M } \geq \mu \geq - z _ { \alpha } \cdot \frac { \sigma } { \sqrt { \ n } } + \mathrm { X M }
$$

Ordenando los miembros y reemplazando a la variable aleatoria XM por su valor observado en la muestra.

$$
\tan - z  _ { \frac { \alpha } { 2 } } \cdot \frac { \sigma } { \sqrt { \mathsf { n } } } \leq \mu \leq \kappa \mathsf { m } + \mathsf { z } _ { \alpha } \cdot \frac { \sigma } { \sqrt { \mathsf { n } } }
$$

Que nos dice que la media poblacional $\mu$ se encuentra entre los dos miembros "externos" de la desigualdad, con un $( 1 - \mathsf { a } ) 1 0 0 \%$ de probabilidad. Lo cual podemos expresar en forma de intervalo.

A su vez si se desconoce la varianza, pero la muestra es grande se puede reemplazar a σ por s que es la desviacion estandar muestral. Quedando

Por ultimo de igual forma es posible, determinar un intervalo de confianza cuando la muestra es chica, se desconoce la varianza pero proviene de una poblacion normal.

s s Intervalo de confianza para xm t α  n -   xm t , + α  n μ de muestra chica, σ 2 2 desconocida y poblacion normal

En relacion al error maximo de estimacion, se puede decir que dar una estimacion puntual de la forma:

Es una forma similar de presentar un intervalo de confianza, ya que

$$
\mathrm { l i m i t e \_ i n f e r i o r = x m - E \quad \mit { y } } \quad \mathrm { l i m i t e \_ s u p e r i o r = x m + E }
$$

Es decir, se pueden obtener los limites de confianza del intervalo partiendo del error maximo de estimacion.

UNIDAD II PRUEBAS DE HIPOTESIS

# INTRODUCCION

Existen muchos problemas en los que, en lugar de estimar el valor de un parametro, es necsario decidir si un enunciado respecto a un parametro es verdadero o falso. Como por ejemplo: La vida media (μ) de la baterias de litio que se usan en un dispositivo es de

La desviacion estandar (σ) en el peso de bolsas de cemento es menor que

La proporcion (p) de usuarios de Linux es mayor a ...

Es decir, ponemos a prueba una hipotesis acerca de un parametro.

Agregar algun problema o algun ejemplo para complementar...

El proceso de decision podria conducir a resultado erroneos, dado el componente aleatorio que se encuentra dentro del problema, es decir, puede que "esa muestra en especifico" me lleve a tomar conclusiones erroneas. Sin embargo, es posible respaldar nuestra decision con un cierto nivel de significacion asociado a la prueba.

# SIMULACION

Una fabrica de luces RGB afirma que los diodos leds utilizados tienen en promedio (μ) una vida util de 10000 horas. Sin embargo, se reciben constantes quejas por parte de los clientes de que la vida util es menor a lo que la fabrica asegura.

Para esto se toma una muestra de 40 diodos y se los pone a prueba. Se sabe por experiencia que $\mathtt { \sigma } = 5 0 0$ horas. Se establece que si la media obtenida es menor a 49800 horas, se deberan realizar inspecciones y posteriores mejoras en el proceso de fabricacion de los diodos.

$\begin{array} { r l } & { \mathrm { n : ~ } = 4 0 } \\ & { \begin{array} { r l } & { \mathrm { M : = ~ } 1 0 0 0 0 0 } \\ & { \mathrm { i : = ~ } 0 . \mathrm { N - 1 } } \\ & { \sigma : = 5 0 0 } \\ & { \mathrm { | t : = ~ } 5 0 0 0 0 } \end{array} } \\ & { \begin{array} { r l } & { \mathrm { | t \leq ~ } 5 0 0 0 0 } \\ & { \mathrm { x _ { c r i t i c i e : } = 4 9 8 0 0 } } \\ & { \mathrm { | t _ { i } : = \mathrm { ~ m e a n } ( m o r m ( n , ~ , ~ , } \sigma ) ) } \end{array} } \\ & { \begin{array} { r l } & { \mathrm { ~ A _ { i } : = ~ i f \big ( M _ i < ~ x _ { c r i t i c 0 } , ~ 1 , } 0 \big ) } \end{array} } \end{array}$ Simula tomar 100000 muestras de tamano 40 Tamano de la muestra Desviacion estandar poblacional Media poblacional Valor critico para aceptacion o rechazo de la hipotesis Arreglo de 100000 medias de muestras de tamano 40 Vector cuyos elementos son asignados en base a si la media de la i-esima muestra es mayor o menor que el valor critico. $\ 1 =$ menor ; $0 =$ mayor   
$\alpha : = \frac { \sum \mathrm { A } } { \mathrm { N } } = 5 . 6 6 \times 1 0 ^ { - 3 }$ Frecuencia relativa de muestras cuya media fue menor a 49800   
α% := α100 = 0.566 En porcentaje $( \% )$

Esto me dice que de 100000 muestras que fueron simuladas, solo el ${ \sim } 0 . 6 \%$ de ellas poseen una media inferior a 48900. Por lo tanto si se obtuviese una media muestral inferior a 49800 horas se debe sospechar que la media verdadera es inferior a la supuesta de 50000 horas, dado que la probabilidad de obtener dicha media muestral es baja, aunque es posible.

La forma teorica de calcular estas probabilidades sin necesidad de tomar 100000 muestras es la siguiente:

Dado el caso de los leds, se sabe que la media muestral se aproxima a una distribucion normal conforme n aumenta, y que para $n > = 3 0$ , ya se obtiene una buena aproximacion de la misma. Por lo tanto, es posible calcular la probabilidad de que la media muestral sea menor a 49800.

$\mathbf { x } : = 4 8 5 0 0 , 4 8 5 0 1 \ldots 5 0 5 0 0$

![](images/479b08ef84b44cf47ec826206ff863f54495f973e9a6c1651535e89d3500f884.jpg)

$$
{ \underset { - \infty } { \underbrace { \boldsymbol { \alpha } \cdot \mathrm { i } } } } = \int _ { - \infty } ^ { \mathrm { x } _ { \mathrm { c r i t i c o } } } \mathrm { d n o r m } \Bigg ( \mathrm { t } , \mathrm { \textmu } , { \frac { \boldsymbol { \sigma } } { \sqrt { n } } } \Bigg ) \mathrm { d t } = 5 . 7 6 2 8 6 \times ~ 1 0 ^ { - 3 } ~ \mathrm { \qquad } { \underset { \mathrm { A W M a t } } { \underbrace { 8 \boldsymbol { \omega } _ { \mathrm { G } } } : = } } \alpha \cdot 1 0 0 = 0 . 5 7 6 2 9
$$

Por otro lado, que pasaria si la media no fuese $\mu = 5 0 0 0 0$ , sino que en realidad es de 49700, cual seria la probabilidad de aceptar la hipotesis de que la media es de 50000 horas.

![](images/3fe2b728d64df953a6900f6eb7aa333a34a0d2c138db7fad1988ead35385630c.jpg)

$$
\beta : = \int _ { \mathrm { \tiny ~ x _ { c r i t i c o } } } ^ { \infty } \mathrm { d n o r m } \Bigg ( \mathrm { t } , 4 9 7 0 0 , \frac { \sigma } { \sqrt { \mathrm { n } } } \Bigg ) \mathrm { d t } = 0 . 1 0 2 9 9 \qquad \beta _ { \% } : = \mathrm { \tiny ~ \beta \cdot 1 0 0 = 1 0 . 2 9 8 9 4 }
$$

Con esto se han descripto de forma practica los dos tipos de errores presentes a la hora de tomar una decision utilizando las llamadas pruebas de hipotesis.

En el siguiente grafico vemos ambas curvas, con ambos errores graficados.

![](images/e19a8c31e0f2b89441a4465036889c8567944a0c7a507af7f07a38dcb29af6f1.jpg)

En la siguiente imagen se muestra con mas detalles, las areas y errores que le corresponden a cada una, ademas de su significado.

![](images/98e8b82b152baa3ead2d6b27c4bd40a2a3a74d002227a96be188467f7f20fa84.jpg)

En el siguiente cuadro se resumen, todos los posibles casos que se pueden dar:

<html><body><table><tr><td rowspan="3">H es verdadera H es falsa</td><td>Aceptar H</td><td>Rechazar H</td></tr><tr><td>Decision correcta</td><td>Error tipo I</td></tr><tr><td>Error tipo II</td><td>Decision correcta</td></tr></table></body></html>

Como vemos, el error tipo I se comete cuando se rechaza H siendo esta verdadera, y la probabilidad de cometerlo es justamente el α que calculamos previamente.

Mientras tanto, el error tipo II se comete cuando se acepta H siendo esta falsa, la probabilidad de cometerlo es lo que previamente denominamos $\beta$ .

A menudo, las hipotesis se formulan para probarse como un solo valor para un parametro (dentro de lo posible). Por lo general, eso requiere que se haga una hipotesis opuesta a lo que se espera probar.

Para probar que la media de rendimiento de un CPU A es mayor que la de un CPU B se formula la hipotesis de que ambos rendimientos medios son iguales.

Para probar que la proporcion de usuarios de sistemas UNIX es mayor en un pais A que otro pais B se formula la hipotesis de que las proporcion en ambos paises es igual. Para probar que la variacion en el llenado de recipientes es menor en la maquina A que en la maquina B se formula una hipotesis en la que ambas varianzas son iguales.

Como en principio se hace la hipotesis de que "NO existe diferencia" entre los parametros, a estas hipotesis se las conoce como hipotesis nula y se las denota como ${ \sf H } _ { 0 }$ .

Para desarrollar los procedimientos para las pruebas de hipotesis se utilizara el ejemplo de la vida media de los diodos leds usados en la construcction de luces RGB.

1. Formular una hipotesis nula y una alternativa adecuada que se aceptara en caso de rechazar la hipotesis nula.   
2. Establecer la probabilidad de error tipo I (α), es decir, la significancia de la prueba. Ademas, de ser posible o necesario se pueden especificar las probabilidades de error tipo II (β), para alternativas particulares.   
3. Con base en la distribucion muestral de un estadistico adecuado, se construye un criterio para poner a prueba la hipotesis nula contra la alternativa dada.   
4. A partir de los datos, calcular el valor del estadistico sobre el cual se debe basar la decision.   
5. Decidir si hay que rechazar la hipotesis nula o fallar al rechazarla.

En el ejemplo:

1. Formular una hipotesis nula y una alternativa adecuada que se aceptara en caso de rechazar la hipotesis nula.

$$
\begin{array} { r } { \mathsf { H } _ { 0 } : \mu = } \\ { \mathsf { \Pi } _ { \mathsf { P } } \rho _ { 1 } \ L _ { 0 } \ L _ { \Psi } \alpha } \end{array}
$$

En este caso, el interes de la prueba de hipotesis es el de comprobar si la media es igual a 50000 horas o si es menor que 50000 horas, por lo tanto es una prueba unilateral de cola izquierda. Otro caso podria darse si la fabrica quisiera comprobar si la media es igual a 50000 horas o si es distinta $( ! = )$ de 50000, lo cual la convertiria en una prueba bilateral.

2. Establecer la probabilidad de error tipo I (α), es decir, la significancia de la

# prueba. Ademas, de ser posible o necesario se pueden especificar las probabilidades de error tipo II (β), para alternativas particulares.

Las probabilidades de cometer un error del Tipo I se encuentran "estandarizadas", y los valores convencionales para este son de $\mathtt { d } = 0 . 0 5 \circ \mathtt { d } = 0 . 0 1$

3. Con base en la distribucion muestral de un estadistico adecuado, se construye un criterio para poner a prueba la hipotesis nula contra la alternativa dada. Dado que se sabe que la distribucion muestral de la media se aproxima a una normal conforme aumenta n, y que para $n > = 3 0$ la distribucion normal ofrece una buena aproximacion. Es posible construir un criterio utilizando:

Para $\mathtt { q } = 0 . 0 1$ , la abscisa debera ser:

$$
\mathrm { x m } _ { 0 0 1 } : = \mathrm { q n o r m } \left( 0 . 0 1 , \mu , { \frac { \sigma } { \sqrt { \mathrm { n } } } } \right) = 4 . 9 8 1 6 1 \times 1 0 ^ { 4 }
$$

Para $\mathtt { q } = 0 . 0 5$ , la abscisa debera ser:

$$
\mathrm { x m } _ { 0 0 5 } : = \mathrm { q n o r m } \left( 0 . 0 5 , \mu , { \frac { \sigma } { \sqrt { \mathrm { n } } } } \right) = 4 . 9 8 7 \times 1 0 ^ { 4 }
$$

4. A partir de los datos, calcular el valor del estadistico sobre el cual se debe basar la decision.

A partir de este punto, se simula una muestra para poder finalizar el desarrollo de los pasos.

$$
\mathrm { x m } : = \mathrm { M } _ { 0 } = 4 . 9 9 5 3 8 \times 1 0 ^ { 4 }
$$

# 5. Decidir si hay que rechazar la hipotesis nula o fallar al rechazarla.

Dado que $\mathsf { x m } > \mathsf { x m } _ { \mathsf { c r i t i c o } } \mathsf { s }$ e falla en rechazar la hipotesis nula. Es decir, la vida media $\mu$ de los diodos led es significativamente igual a 50000 horas.

En el ejemplo, no se ha realizado la estandarizacion del valor critico ni del estadistico, esto es posible gracias a que nos encontramos utilizando un software capaz de calcular en forma directa valores y areas de una curva normal en base a parametros especificados en la llamada a la funcion. Sin embargo, dado el caso de que no se dispongan de estas herramientas, es posible trabajar con valores estandarizados del estadistico, para luego poder utilizar valores criticos tabulados en tablas de la distribucion normal estandar.

<html><body><table><tr><td>Poblacion</td><td>Tamafiodelamuestra</td><td>aconocida</td><td>desconocida</td></tr><tr><td rowspan="2">Normalmente Distribuida</td><td>Grande (n≥ 30)</td><td>xm±Zα.Oxm</td><td>xm±Za.Sxm</td></tr><tr><td>Chica(n&lt;30）</td><td>xm±Zα.Oxm</td><td>xm±tα.sxm</td></tr><tr><td rowspan="2">NoNormalmente Distribuida</td><td>Grande (n≥ 30)</td><td>xm±Zq.Oxm</td><td>xm±Zα.Sxm</td></tr><tr><td>Chica(n&lt;30）</td><td>donde 1-1/k2 se del Teorema de Chebyshev xm±k.0xm</td><td>donde 1-1/k se define por medio define por medio del Teorema de Chebyshev xm±k.sxm</td></tr></table></body></html>

<html><body><table><tr><td>xm - μ z =</td><td>xm - μ Z =</td><td>t</td><td> xm - μ</td></tr><tr><td>q</td><td>s</td><td>n-1</td><td>S</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>√n</td><td>Jn</td><td></td><td></td></tr></table></body></html>

<html><body><table><tr><td colspan="11">Tabla 3 Funcion de distribucion normal estandar</td></tr><tr><td colspan="8">F（z） F(2)=π d</td><td colspan="3">=0</td></tr><tr><td>Z</td><td>0.00</td><td>0.01</td><td>0.02</td><td>0.03</td><td>0.04</td><td>0.05</td><td>0.06</td><td>0.07</td><td>0.08</td><td>0.09</td></tr><tr><td>-5.0 -4.0</td><td colspan="8">0.0000003 0.00003</td><td></td><td></td><td></td></tr><tr><td>-3.5</td><td>0.0002</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-3.4</td><td>0.0003</td><td>0.0003</td><td>0.0003</td><td>0.0003</td><td>0.0003</td><td>0.0003</td><td>0.0003</td><td>0.00030.0003</td><td></td><td>0.0002</td></tr><tr><td>-3.3</td><td>0.0005</td><td>0.0005</td><td>0.0005</td><td>0.0004</td><td>0.0004</td><td>0.0004</td><td>0.0004</td><td>0.0004</td><td>0.0006</td><td>0.0003</td></tr><tr><td>-3.2</td><td>0.0007</td><td>0.0007</td><td>0.0006</td><td>0.0006</td><td>0.0006</td><td>0.0006</td><td>0.0006</td><td>0.0005</td><td>0.0005</td><td>0.0005</td></tr><tr><td>-3.1</td><td>0.0010</td><td>0.0009</td><td>0.0009</td><td>0.0009</td><td>0.0008</td><td>0.0008</td><td>0.0008</td><td>0.0008</td><td>0.0007</td><td>0.0007</td></tr><tr><td>-3.0</td><td>0.0013</td><td>0.0013</td><td>0.0013</td><td>0.0012</td><td>0.0012</td><td>0.0011</td><td>0.0011</td><td>0.0011</td><td>0.0010</td><td>0.0010</td></tr><tr><td>-2.9</td><td>0.0019</td><td>0.0018</td><td>0.0018</td><td>0.0017</td><td>0.0016</td><td>0.0016</td><td>0.0015</td><td>0.0015</td><td>0.0014</td><td>0.0014</td></tr><tr><td>-2.8</td><td>0.0026</td><td>0.0025</td><td>0.0024</td><td>0.0023</td><td>0.0023</td><td>0.0022</td><td>0.0021</td><td>0.0021</td><td>0.0020</td><td>0.0019</td></tr><tr><td>-2.7</td><td>0.0035</td><td>0.0034</td><td>0.0033</td><td>0.0032</td><td>0.0031</td><td>0.0030</td><td>0.0029</td><td>0.0028</td><td>0.0027</td><td>0.0026</td></tr><tr><td>-2.6</td><td>0.0047</td><td>0.0045</td><td>0.0044</td><td>0.0043</td><td>0.0041</td><td>0.0040</td><td>0.0039</td><td>0.0038</td><td>0.0037</td><td>0.0036</td></tr><tr><td>-2.5</td><td>0.0062</td><td>0.0060</td><td>0.0059</td><td>0.0057</td><td>0.0055</td><td>0.0054</td><td>0.0052</td><td>0.0051</td><td>0.0049</td><td>0.0048</td></tr><tr><td>-2.4</td><td>0.0082</td><td>0.0080</td><td>0.0078</td><td>0.0075</td><td>0.0073</td><td>0.0071</td><td>0.0069</td><td>0.0068</td><td>0.0066</td><td>0.0064</td></tr><tr><td>-2.3</td><td>0.0107</td><td>0.0104</td><td>0.0102</td><td>0.0099</td><td>0.0096</td><td>0.0094</td><td>0.0091</td><td>0.0089</td><td>0.0087</td><td>0.0084</td></tr><tr><td>-2.2</td><td>0.0139</td><td>0.0136</td><td>0.0132</td><td>0.0129</td><td>0.0125</td><td>0.0122</td><td>0.0119</td><td>0.0116</td><td>0.0113</td><td>0.0110</td></tr><tr><td>-2.1 -2.0</td><td>0.0179</td><td>0.0174</td><td>0.0170</td><td>0.0166</td><td>0.0162</td><td>0.0158</td><td>0.0154</td><td>0.0150</td><td>0.0146</td><td>0.0143</td></tr><tr><td></td><td>0.0228</td><td>0.0222</td><td>0.0217</td><td>0.0212</td><td>0.0207</td><td>0.0202</td><td>0.0197</td><td>0.0192</td><td>0.0188</td><td>0.0183</td></tr><tr><td>-1.9 -1.8</td><td>0.0287</td><td>0.0281</td><td>0.0274</td><td>0.0268</td><td>0.0262</td><td>0.0256</td><td>0.0250</td><td>0.0244</td><td>0.0239</td><td>0.0233</td></tr><tr><td></td><td>0.0359</td><td>0.0351</td><td>0.0344</td><td>0.0336</td><td>0.0329</td><td>0.0322</td><td>0.0314</td><td>0.0307</td><td>0.0301</td><td>0.0294</td></tr><tr><td>-1.7</td><td>0.0446</td><td>0.0436</td><td>0.0427</td><td>0.0418</td><td>0.0409</td><td>0.0401</td><td>0.0392</td><td>0.0384</td><td>0.0375</td><td>0.0367</td></tr><tr><td>-1.6</td><td>0.0548</td><td>0.0537</td><td>0.0526</td><td>0.0516</td><td>0.0505</td><td>0.0495</td><td>0.0485</td><td>0.0475</td><td>0.0465</td><td>0.0455</td></tr><tr><td>-1.5</td><td>0.0668</td><td>0.0655</td><td>0.0643</td><td>0.0630</td><td>0.0618</td><td>0.0606</td><td></td><td>0.0594 0.0582</td><td>0.0571</td><td>0.0559</td></tr></table></body></html>

<html><body><table><tr><td colspan="10">Tabla4Valoresdetα</td></tr><tr><td colspan="8"></td><td>0</td><td>α ta</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>α=0.10 α=0.05 α=0.025α=0.01 α=0.00833 α=0.00625 α=0.005</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="9">12345 6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>V</td></tr><tr><td>3.078</td><td>6.314</td><td>12.706</td><td>31.821</td><td>38.204</td><td>50.923</td><td></td><td>63.657</td><td>1</td></tr><tr><td>1.886</td><td>2.920</td><td>4.303</td><td>6.965</td><td>7.650</td><td>8.860</td><td></td><td>9.925</td><td></td></tr><tr><td>1.638</td><td>2.353</td><td>3.182</td><td>4.541</td><td>4.857 3.961</td><td></td><td>5.392 4.315</td><td>5.841</td><td>234</td></tr><tr><td>1.533</td><td>2.132 2.015</td><td>2.776 2.571</td><td>3.747 3.365</td><td>3.534</td><td></td><td>3.810</td><td>4.604 4.032</td><td>5</td></tr><tr><td>1.476</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.440</td><td>1.943</td><td>2.447 2.365</td><td>3.143 2.998</td><td>3.288 3.128</td><td></td><td>3.521</td><td>3.707</td><td>6</td></tr><tr><td>1.415</td><td>1.895 1.860</td><td>2.306</td><td>2.896</td><td>3.016</td><td></td><td>3.335 3.206</td><td>3.499 3.355</td><td></td></tr><tr><td>1.397 1.383</td><td>1.833</td><td>2.262</td><td>2.821</td><td>2.934</td><td></td><td>3.111</td><td>3.250</td><td>789</td></tr><tr><td>789 10</td><td>1.372</td><td>1.812</td><td>2.228</td><td>2.764</td><td>2.870</td><td>3.038</td><td>3.169</td><td></td><td>10</td></tr></table></body></html>

La ventaja de trabajar con valores normalizados es que los valores criticos se pueden reutilizar para distintos problemas. En el ejemplo anterior queda:

$$
\begin{array} { l } { { z _ { 0 0 1 } : = \mathrm { q n o r m } ( 0 . 0 1 , 0 , 1 ) = - 2 . 3 2 6 3 5 } } \\ { { \ } } \\ { { z _ { 0 0 5 } : = \mathrm { q n o r m } ( 0 . 0 5 , 0 , 1 ) = - 1 . 6 4 4 8 5 } } \end{array}
$$

Y normalizando el valor de xm:

$$
\mathsf { z } : = \frac { \mathrm { x m } - \mu } { \sigma } = - 0 . 5 8 4 2 3
$$

Lo que nos deja con la misma conclusion. A continuacion se muestran graficas normalizada y absoluta del problema.

$\mathrm { y } : = - 4 , - 3 . 9 9 \dots 4$

![](images/04f9875f5e8e5de923cf4ab9471c6f1cccb7c520ad961c3da280c84af9fa1df2.jpg)

![](images/f4d9c093ecbde79c7f8780fce509641e27b99ce8d05744eb8aa624bcdeed8b8b.jpg)

# CURVAS DE OPERACION

Hasta el momento no se ha puesto mayor interes en el error tipo II. En el ejemplo de los diodos led se eligio un valor arbitrario de $\mu = 4 9 7 0 0$ horas, sin embargo podria resultar interesante ver que sucede con $\beta$ conforme varian los distintos valores de $\mu .$ .

Para esta prueba, se definira una funcion $\beta ( \updownarrow )$ la cual tomara como argumento, distintos valores para la media verdadera $\mu$ .

t 49500 49525 := , .. 50500

$$
\beta _ { \mathrm { i z q } } ( \mathrm { t } ) : = 1 - \mathrm { p n o r m } \bigg ( \mathrm { x } _ { \mathrm { c r i t i c o } } , \mathrm { t } , \frac { \sigma } { \sqrt { \mathrm { n } } } \bigg )
$$

$$
\mathbf { x } _ { \mathrm { c r i t i c o } } = 4 . 9 8 \times 1 0 ^ { 4 } \qquad \mathbf { n } = 4 0 \qquad \qquad \sigma = 5 0 0
$$

![](images/5eb1a6649b918d8ae32dcea321d746a9964a6dc3250db120d3230533158e3fad.jpg)

A pesar de que no es el caso del ejemplo, si la prueba fuese de cola derecha, la curva se veria como la siguiente:

$$
\beta _ { \mathrm { d e r } } ( \mathrm { t } ) : = \mathrm { p n o r m } \Bigg ( \mathrm { x } _ { \mathrm { c r i t i c o } } , \mathrm { t } , \frac { \sigma } { \sqrt { \mathrm { n } } } \Bigg )
$$

$$
\mathrm { x } _ { \mathrm { c r i t i c o } } = 4 . 9 8 \times 1 0 ^ { 4 } \qquad \mathrm { n } = 4 0 \qquad \qquad \sigma = 5 0 0
$$

![](images/96d364c2afe92f0881ec239d0e5bd14a662767966e1313d2f6d4e04d322e0271.jpg)

Por ultimo la prueba bilateral posee una curva diferente a las antes vistas, donde alcanza su valor maximo cuando $\mu 1 = \mu 0$ , el cual es $\beta = 1 - \alpha$

![](images/23e360202ebd62be467e8b4b3bb26c5d2ecbfc9de4b5ed04cc2d4c39c601ab9a.jpg)

# COMPARACIONES DE DOS TRATAMIENTOS

Existen muchos casos donde no solo se desea comparar un parametro contra un valor esperado o deseable, sino que es necesario comparar dos parametros de dos poblaciones entre si, por ejemplo:

La media de consumo de energia electrica por parte de dos maquinas...

La varianza en el llenado de recipientes por parte de una maquina A contra una maquina B...   
La proporcion de usuarios de INTEL en Argentina contra la proporcion de usuarios en EEUU...

COMPARACION DE DOS MUESTRAS INDEPENDIENTES GRANDES

Sean $\mathsf X _ { 1 } , \mathsf X _ { 2 } , . . . , \mathsf X _ { \mathsf n 1 } \mathsf e \mathsf { Y } _ { 1 } , \mathsf Y _ { 2 } , . . . , \mathsf Y _ { \mathsf n 2 }$ muestras aleatorias independientes entre si provenientes de dos poblaciones, con parametros $\mu _ { 1 } , \sigma _ { 1 } \gamma \mu _ { 2 } , \sigma _ { 2 }$ respectivamente Se sabe que:

$$
\mathrm { { E } ( X M ) = \mu _ { 1 } \qquad \ v a r { ( X M ) } = \frac { \left( \sigma _ { 1 } \right) ^ { 2 } } { \mu _ { 1 } } }
$$

$$
\mathrm { E ( Y M ) } = \mu _ { 2 } \qquad \mathrm { v a r ( Y M ) } = \frac { \left( \sigma _ { 2 } \right) ^ { 2 } } { \mathrm { n } _ { 2 } }
$$

Dado que son combinaciones lineales y las muestras son independientes entre si, es posible afirmar lo siguiente:

$$
\mathrm { E } ( \mathrm { X M } - \mathrm { Y M } ) = \mu _ { 1 } - \mu _ { 2 }
$$

$$
\mathrm { v a r } ( \mathrm { X M } - \mathrm { Y M } ) = \frac { { \left( \sigma _ { 1 } \right) } ^ { 2 } } { \mathrm { n _ { 1 } } } + \frac { { \left( \sigma _ { 2 } \right) } ^ { 2 } } { \mathrm { n _ { 2 } } }
$$

Entonces cuando n1 y n2 son grandes, por el TCL, la diferencia entre XM e YM es aproximadamente normal y el estadistico

$$
\mathrm { \Lambda _ { z } = \frac { ( X M - Y M ) - \delta } { \sqrt { \frac { \left( \sigma _ { 1 } \right) ^ { 2 } } { \mathrm { \Lambda _ { 1 } } } + \frac { \left( \sigma _ { 2 } \right) ^ { 2 } } { \mathrm { \Lambda _ { 2 } } } } } }
$$

tiene una distribucion aproximadamente normal estandar, ademas, cuando n1 y n2 son lo suficientemente grandes, la muestra representa relativamente bien a la poblacion, por lo que es valido sustituir las varianzas poblacionales con las varianzas muestrales

$$
\mathrm { \Lambda _ { z } = \frac { ( X M - Y M ) - \delta } { \sqrt { \frac { \left( s _ { 1 } \right) ^ { 2 } } { n _ { 1 } } } + \frac { \left( s _ { 2 } \right) ^ { 2 } } { n _ { 2 } } } }
$$

# Agregar alguna prueba de hipotesis para dos muestras grandes

Cuando n1, n2 o ambos son chicos y las varianzas poblacionales son desconocidas es posible utilizar el estadistico t, siempre que sea posible suponer que ambdas poblaciones son normales con varianzas iguales $\sigma _ { 1 } = \sigma _ { 2 } = \sigma$

$$
\mathrm { \bf t } = \frac { \left( \mathrm { X M } - \mathrm { Y M } \right) - \delta } { \sigma _ { \mathrm { e s t } ^ { * } } \sqrt { \frac { 1 } { \mathrm { n } _ { 1 } } + \mathrm { \frac { 1 } { \mathrm { n } _ { 2 } } } } }
$$

donde t es una variable aleatoria que se distribuye como una t-Student de $\mathsf { v } = \mathsf { n } _ { 1 } +$ $\mathsf { n } _ { 2 } - 2$ grados de libertad y $\sigma _ { \mathrm { e s t } }$ es la desviacion estandar estimada que se calcula al combinar la suma de las desviaciones al cuadrado de las respectivas medias muestrales.

$$
\sigma _ { \mathrm { e s t } } ^ { \mathrm { \scriptsize { \sim } } 2 } = { \frac { \displaystyle \sum _ { \mathrm { i } = 1 } ^ { \mathrm { \scriptsize { n } } _ { 1 } } { \bigl ( \mathrm { x } _ { \mathrm { i } } - \mathrm { x m } \bigr ) } ^ { 2 } + \sum _ { \mathrm { i } = 1 } ^ { \mathrm { \scriptsize { n } } _ { 2 } } { \bigl ( \mathrm { y } _ { \mathrm { i } } - \mathrm { y m } \bigr ) } ^ { 2 } } { \displaystyle \mathrm { n } _ { 1 } + \mathrm { n } _ { 2 } - 2 } } = { \frac { \bigl ( \mathrm { n } _ { 1 } - 1 \bigr ) \bigl ( \mathrm { s } _ { 1 } \bigr ) ^ { 2 } + \bigl ( \mathrm { n } _ { 2 } - 1 \bigr ) \bigl ( \mathrm { s } _ { 2 } \bigr ) ^ { 2 } } { \mathrm { n } _ { 1 } + \mathrm { n } _ { 2 } - 2 } }
$$

Sustituyendo en la expresion del estadistico t:

$$
\mathbf { t } = { \frac { \left( \mathbf { X } \mathbf { M } - \mathbf { Y } \mathbf { M } \right) - { \boldsymbol { \delta } } } { \sigma _ { \mathrm { e s t } } \cdot { \sqrt { { \frac { 1 } { \mathbf { n } _ { 1 } } } + { \frac { 1 } { \mathbf { n } _ { 2 } } } } } } } = { \frac { \left( \mathbf { X } \mathbf { M } - \mathbf { Y } \mathbf { M } \right) - { \boldsymbol { \delta } } } { \sqrt { \left( \mathbf { n } _ { 1 } - 1 \right) \cdot \left( \mathbf { s } _ { 1 } \right) ^ { 2 } + \left( \mathbf { n } _ { 2 } - 1 \right) \cdot \left( \mathbf { s } _ { 2 } \right) ^ { 2 } } } } \cdot { \sqrt { \frac { \mathbf { n } _ { 1 } \cdot \mathbf { \tilde { n } } _ { 2 } \cdot \left( \mathbf { \tilde { n } } _ { 1 } + \mathbf { n } _ { 2 } - 2 \right) } { \mathbf { n } _ { 1 } + \mathbf { \tilde { n } } _ { 2 } } } }
$$

con parametro $\mathsf { v } = \mathsf { n } \mathsf { 1 } + \mathsf { n } 2 - 2$ grados de libertad

# Agregar algun ejemplo para prueba t bimuestral

Algo que se debe cuidar a la hora de aplicar la prueba, es que las variables sean independientes entre si. El ejemplo mas claro de variables que no son independientes es cuando los datos son de "antes y despues". En ese caso es posible aplicar una comparacion que se basa en diferencias pareadas, conocida como prueba t pareada.

Primero se considera una variable aleatoria como la siguiente:

$$
\mathrm { D } = \mathrm { X } - \mathrm { Y }
$$

Donde D es la diferencia entre la variable aleatoria pareadas X e Y. Las pruebas de hipotesis ${ \mu } _ { \mathsf { D } } = 0$ se basan en:

$$
\frac { \mathrm { { D M } - \mu _ { \mathrm { { D } } } } } { \mathrm { { s _ { \mathrm { { D } } } } } }
$$

Donde DM y $\mathsf { S } _ { \mathsf { D } }$ son la media y la desviacion estandar de las diferencias, respectivamente.

Agregar ejemplo de prueba t pareada

UNIDAD III VARIANZA Y PROPORCIONES

UNIDAD III

# ESTIMACION DE VARIANZAS

Asi como en unidades anteriores, el interes se enfoco en la estimacion y pruebas de significacion relativas a medias, existen situaciones donde el parametro de interes sea σ.

Estimador insesgado de $\sigma ^ { 2 }$

Aunque la varianza muestral es un estimador insesgado de $\sigma ^ { 2 }$ , no se sigue que la desviacion estandar muestral sea un estimador insesgado de $\sigma$ , de hecho no lo es. Sin embargo, para muestras grande, el sesgo es despreciable, por lo que es comun usarlo en la practica.

Ademas de s, es comun estimar la desviacion estandar muestral en terminos del rango muestral R.

$$
\mathrm { R = \ m a x ( m u e s t r a ) - \ m i n ( m u e s t r a ) }
$$

Dada una muestra aleatoria de tamano n de una poblacion normal, puede demostrarse que la distribucion muestral del rango tiene media ${ \sf d } _ { 2 }$ .σ y la desviacion estandar ${ \mathsf d } _ { 3 }$ .σ

# SIMULACION

$$
\begin{array} { l l } { { \displaystyle \mathsf { N } _ { \mathsf { N } ^ { \star } } = 1 0 0 0 0 } } & { { \mathrm { i : = 0 . N - 1 } } } \\ { { \displaystyle \mathsf { n } : = 1 0 } } & { { \mathrm { j : = 0 . n - 1 } } } \\ { { \displaystyle { \mathsf { \mu } } } } & { { } } \\ { { \displaystyle { \mathsf { \mu } } : = 0 } } & { { \sigma : = 1 } } \\ { { \displaystyle { \mathsf { M } _ { \mathsf { i } } : = \mathrm { r n o r m } ( { \bf n } , { \bf \mu } , { \bf \sigma } ) } } } & { { } } \\ { { \displaystyle { \mathsf { R } _ { \mathsf { i } } : = \mathrm { m a x } \big ( { \bf M } _ { \mathsf { i } } \big ) - \mathrm { m i n } \Big ( { \bf M } _ { \mathsf { i } } \Big ) } } } & { { } } \end{array}
$$

Para el vector x los extremos son:

$$
\mathrm { i n f : = m i n ( R ) } = 0 . 7
$$

$$
\operatorname* { s u p } : = \operatorname* { m a x } ( \mathrm { R } ) = 6 . 6 8 8
$$

Si se desea un Vector de Intervalos (I) de 5 subintervalos:

$$
\mathbf { k } : = 0 \ldots \mathrm { n s }
$$

$$
\Delta : = { \frac { \mathrm { s u p - i n f } } { \mathrm { n s } } }
$$

Luego el valor de I será:

$$
\mathrm { I } _ { \mathrm { k } } \langle = \mathrm { i n f } + \mathrm { k } \cdot \Delta
$$

En este punto, se deberá hacer un "conteo" de cuàntos elementos del vector x caen en los subintervalos $\mathsf { m } { + } \Delta$ , $\mathsf { m } { + } 2 \Delta$ , $\ m { + } 3 \Delta$ , etc. Esta operación se puede hacer automáticamente con la instrucción:

$$
\operatorname* { H } _ { M } \langle = \mathrm { h i s t } ( \operatorname { I } , \operatorname { R } )
$$

Para hacer normalizadas estas frecuencias absolutas, se deben dividir por el tamaño de la muestra (N)

$$
\mathbf { h } : = \frac { \mathbf { H } } { \mathbf { N } }
$$

A partir de este punto se puede construir el histograma correspondiente:

h口

![](images/7ab6fdeac92cac0f597de48598164dc61fbde055c8fb9f278560f6690d6bff83.jpg)

Basandonos en la siguiente tabla podemos obtener los valores de d2 y d3 para hallar los parametros de la distribucion muestral del rango.

<html><body><table><tr><td>n</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>d</td><td>1.128</td><td>1.693</td><td>2.059</td><td>2.326</td><td>2.534</td><td>2.704</td><td>2.847</td><td>2.970</td><td>3.078</td></tr><tr><td>d</td><td>0.853</td><td>0.888</td><td>0.880</td><td>0.864</td><td>0.848</td><td>0.833</td><td>0.820</td><td>0.808</td><td>0.797</td></tr></table></body></html>

Dada una muestra de $\mathsf { n } = 1 0$ :

Por lo tanto:

$$
\begin{array} { r } { \mu _ { \mathrm { R } } : = { \mathrm { d } } _ { 2 } { \cdot } \sigma = 3 . 0 7 8 } \\ { \sigma _ { \mathrm { R } } : = { \mathrm { d } } _ { 3 } { \cdot } \sigma = 0 . 7 9 7 } \end{array}
$$

Comprobando con la simulacion:

$$
\begin{array} { r } { \mathrm { m e a n } ( \mathrm { R } ) = 3 . 0 7 5 } \\ { \mathrm { s t d e v } ( \mathrm { R } ) = 0 . 8 0 1 } \end{array}
$$

Por consiguiente, $\mathsf { R } / \mathsf { d } _ { 2 }$ es un estimador insesgado de $\sigma$ , sin embargo conforme la muestra crece en tamano, s se vuelve un estimador mas eficiente. Se usa principalmente en control de calidad donde los tamanos de muestra, no son muy grandes y la facilidad de calculo es una preocupacion fundamental.

# Agregar ejemplo rango muestral

En varias aplicaciones practicas, las estimaciones de σ o $\sigma ^ { 2 }$ se basan en la desviacion estandar muestral o varianza muestral. Para muestras aleatorias provenientes de poblaciones normales, es posible utilizar el siguiente teorema:

$$
\scriptstyle { \frac { ( \ n - 1 ) \cdot { \mathrm { S } } ^ { 2 } } { \sigma ^ { 2 } } }
$$

Es una variable aleatoria que se distribuye como una $\mathsf { X } ^ { 2 }$ de n - 1 grados de libertad. Entonces ${ \tt X } _ { \tt d } ^ { 2 }$ siendo la abscisa que deja un area de α hacia su izquierda, es posible afirmar con una probabilidad de 1 - α que:

$$
{ \Big ( } \chi ^ { 2 } { \Big ) } _ { \frac { \alpha } { 2 } } < { \frac { ( { \mathrm { n } } - 1 ) \cdot { \mathrm { S } } ^ { 2 } } { { \sigma } ^ { 2 } } } < { \Big ( } \chi ^ { 2 } { \Big ) } _ { 1 - { \frac { \alpha } { 2 } } }
$$

Luego, operando algebraicamente:

( ) S n 1  2  2 ( ) Sn 1 2    
χ 2   α  σ χ 2   α Intervalo de confianza para $\sigma ^ { 2 }$ 2 2

x 0 0.001   30

# Distribucion Chi-Cuadrada

![](images/789e4a2dc25f87192bd8b962945bf5508910dc65e4488910c3b129d75169fd18.jpg)  
Agregar ejemplo intervalo de confianza para desviacion estandar

Cuando el tamano de la muestra es suficientemente grande, la distribucion muestral de la desviacion estandar puede aproximarse a una normal con media σ y desviacion estandar $\sigma / ( 2 \mathsf { n } ) ^ { 1 / 2 }$

$$
\mathrm { g l } : = 5 0 \qquad \mathrm { x } : = 0 , 0 . 0 1 \dots 1 0 0
$$

![](images/08f9bcfe0f8a7a5a20cf8cd2341f6032264bc5fea36e22c8d89bc7a626109ad8.jpg)

# SIMULACION

$$
\begin{array} { r l } & { \begin{array} { r l } & { \mathrm { N } _ { \mathrm { i } } : = 1 0 0 0 0 } \\ & { \mathrm { ~ i } : = 0 \ldots \mathrm { N } - 1 } \end{array} } \\ & { \begin{array} { r l } & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \end{array} } \\ &  \begin{array} { r l } & { \mathrm { \begin{array} { r l } & { \mathrm { ~ i } : = 0 \ldots \mathrm { ~ s t } - 1 } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \end{array} } \\ & { \begin{array} { r l } & { \mathrm { \begin{array} { r l } & { \mathrm { ~ i } ~ } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } } \end{array} } } \end{array} } \end{array} \end{array}
$$

Para el vector x los extremos son:

$$
\operatorname* { i n f } _ { N M W } = \operatorname* { m i n } ( \mathrm { D V } ) = 0 . 6 0 3
$$

$$
\underset { \ r { M } \ r { M } \ r { M } } { \operatorname* { s u p } } : = \mathrm { m a x } ( \mathrm { D V } ) = 1 . 4 5 8
$$

Si se desea un Vector de Intervalos (I) de 5 subintervalos:

ns  10 número de $\mathbf { k } : = 0 \ldots \mathrm { n s }$ subintervalos   
$\frac { \Delta } { m } = \frac { \frac { s u p - i n f } { n s } } { n s }$ Incremento

Luego el valor de I será:

$$
\mathrm { I } _ { \mathrm { k } } : = \mathrm { i n f } + \mathrm { k } \cdot \Delta
$$

En este punto, se deberá hacer un "conteo" de cuàntos elementos del vector x caen en los subintervalos $\mathsf { m } { + } \Delta$ , $\mathsf { m } { + } 2 \Delta$ , $\ m { + } 3 \Delta$ , etc. Esta operación se puede hacer automáticamente con la instrucción:

$$
\operatorname* { H } _ { M \mathcal { N } } : = \mathrm { h i s t } ( \mathrm { I } , \mathrm { D V } )
$$

Para hacer normalizadas estas frecuencias absolutas, se deben dividir por el tamaño de la muestra (N)

$$
\tan : = \frac { H } { N }
$$

A partir de este punto se puede construir el histograma correspondiente:

![](images/d8b63d46c0fc5d27926e001ced9297074f8b580b5adc2067b6797dfc190d28c2.jpg)

Comprobando la simulacion contra los valores teoricos:

$$
\mathrm { m e a n } ( \mathrm { D V } ) = 0 . 9 9 5
$$

$$
\sigma = 1
$$

$$
{ \sqrt { \frac { \mathrm { n } } { \mathrm { n - 1 } } } } \cdot \operatorname { s t d e v } ( { \mathrm { D V } } ) = 0 . 1 0 1 \qquad { \frac { \mathrm { \sigma } } { \sqrt { 2 \cdot \mathrm { n } } } } = 0 . 1
$$

Con esto se concluye que es posible utilizar una distribucion normal para estimar la desviacion estandar cuando el tamano de la muestra es grande, en la practica, mayor a 30.

s  σ z = σ Estadistico z que posee una distribucion normal 2 n estandar

Esto plantea un intervalo de confianza, a partir de la siguiente desigualdad:

$$
\frac { - z } { 2 } ^ { < } \frac { \frac { \textrm { s - } \sigma } { \sigma } < z } { \sqrt { 2 \cdot n } } \frac { \frac { \alpha } { 2 } } { }
$$

Operando algerabricamente

$$
\frac { - z } { 2 } < \frac { ( \mathbf { s } - \sigma ) \cdot \sqrt { 2 \cdot \mathbf { n } } } { \sigma } < z \frac { \mathbf { \sigma } } { 2 }
$$

$$
\frac { \frac { - z } { \alpha } } { \sqrt { 2 \cdot { \mathfrak { n } } } } < \frac { ( \mathrm { s } - \sigma ) } { \sigma } < \frac { \frac { z } { 2 } } { \sqrt { 2 \cdot { \mathfrak { n } } } }
$$

$$
\frac { \frac { \alpha } { 2 } } { \sqrt { 2 \cdot { \mathfrak { n } } } } < \frac { \mathrm { s } } { \sigma } - 1 < \frac { \mathrm { z } } { \sqrt { 2 \cdot { \mathfrak { n } } } }
$$

$$
{ \frac { \frac { - z } { \alpha } } { \sqrt { 2 \cdot { \mathrm { n } } } } } + 1 < { \frac { \mathrm { s } } { \sigma } } < { \frac { \mathrm { z } } { \sqrt { 2 \cdot { \mathrm { n } } } } } + 1
$$

$$
\frac { 1 } { \frac { - z } { \frac { \alpha } { 2 } } } > \frac { \sigma } { \mathrm { s } } > \frac { 1 } { \frac { \alpha } { 2 } }
$$

Obteniendo una expresion para un intervalo de confianza del $1 0 0 ^ { \star } ( 1 - \mathsf { a } ) \%$ para σ en muestras de tamano mayor o igual a 30.

# HIPOTESIS CONCERNIENTES A UNA VARIANZA

Aqui se considera el problema de probar la hipotesis nula ${ \sf H } _ { 0 }$ de que la varianza poblacional es igual a una constante especificada contra una alternativa (uni o bilateral), es decir:

$$
\mathsf { H } _ { 0 } : \sigma ^ { 2 } = \sigma _ { 0 } { } ^ { 2 }
$$

contra las alternativas detalladas en el siguiente cuadro:

<html><body><table><tr><td colspan="2">Regiones criticas para probar g² σ² (poblacion normal)</td></tr><tr><td>Hipótesis alternativa</td><td>Rechazar la hipótesis nula si:</td></tr><tr><td>g²&lt;</td><td>x²&lt;x²-a</td></tr><tr><td>g²&gt;</td><td>x²&gt;x</td></tr><tr><td>g²+0</td><td>x²&lt;x²-a/2 obien x² &gt; x/2</td></tr></table></body></html>

Pruebas de este estilo son importantes siempre que se desee comprobar la uniformidad de un producto o una operacion.

![](images/ef18e114acd047afb212bdc48cd1afd59d34fff0d74172192256fba76c66ef47.jpg)

Agregar ejemplo para prueba de hipotesis de varianza

# Precauciones a tener en cuenta:

En contraste con los procedimientos para realizar inferencias sobre la media poblacional $\mu$ , la validez de los procedimientos desarrollados depende FUERTEMENTE de la suposicion de normalidad de la poblacion. Se dice que dichos procedimientos no son robustos para efectuar inferencias sobre $\sigma ^ { 2 }$ cuando existen desviaciones de la normalidad.

# ESTIMACION DE PROPORCIONES

Muchos problemas a menudo tienen que ver con proporciones y porcentajes. En el muestreo de aceptacion, uno se preocupa por la cantidad de defectuoso en un lote. Otro ejemplo podria ser el porcentaje de individuos de una poblacion que no comen carne, que podria ser de interes para cadenas de comida rapida, en la toma de decision sobre incluir o no una opcion libre de carne. La informacion que usualmente se encuentra disponible para la estimacion de una proporcion es el numero de veces, X, que ocurre un evento (considerado como "exito") en n ensayos, ocasiones u observaciones independientes entre si. El estimador puntual de la proporcion poblacional p es la proporcion muestral X/n.

Para n ensayos que satisfacen la distribucion binomial: 1. Solo hay dos posibles resultados para cada ensayo (exito o fracaso) 2. La probabilidad de exito es la misma para cada ensayo 3. Los resultados de los diferentes ensayos son independientes entre si

Se sabe que:

$$
\begin{array} { c } { \mathsf { \Pi } \displaystyle \mu = \mathsf { n } \cdot \mathsf { p } } \\ { \displaystyle \sigma = \sqrt { \mathsf { n } \cdot \mathsf { p } \cdot ( 1 - \mathsf { p } ) } } \end{array}
$$

# SIMULACION

$$
\displaystyle { \underset { \ r { \ r { \ r { \ r { \ r { \ r { \ r } } } } } } { \boldsymbol { \mu } } : \ r { \ r { \ b { \mu } } } } { \boldsymbol { \mu } } } = 2 0 \qquad \quad \mathrm { ~ \ r ~ { ~ p ~ : = ~ 0 . 6 5 ~ } ~ }
$$

$$
{ \mathrm { P } } : = { \mathrm { r b i n o m } } ( { \mathrm { N } } , { \mathrm { n } } , { \mathrm { p } } )
$$

Contrastando valores teoricos con los obtenidos en la simulacion

$$
\mathrm { m e a n } ( \mathrm { P } ) = 1 2 . 9 8 8
$$

$$
\mathsf { n } \cdot \mathsf { p } = 1 3
$$

$$
\mathrm { s t d e v } ( \mathsf { P } ) = 2 . 1 5 1
$$

$$
{ \sqrt { \mathbf { n } { \cdot } \mathbf { p } { \cdot } ( 1 - \mathbf { p } ) } } = 2 { . } 1 3 3
$$

$\mathsf { S i } \mu \mathsf { y } \sigma$ son la media y desviacion estandar del numero de exitos, entonces, dividiendolos entre n se obtiene la media y la desviacion estandar de la proporcion de exitos, es decir:

$$
{ \frac { \mu } { \mu } } = { \frac { \mathrm { n } \cdot \mathrm { p } } { \mathrm { n } } } = \mathrm { p }
$$

$$
{ \frac { \sigma } { \mathrm { n } } } = { \frac { { \sqrt { \mathrm { n } \cdot { \mathrm { p } } \cdot ( 1 - { \mathrm { p } } ) } } } { \mathrm { n } } } = { \sqrt { \frac { { \mathrm { n } } \cdot { \mathrm { p } } \cdot ( 1 - { \mathrm { p } } ) } { \mathrm { n } ^ { 2 } } } } = { \sqrt { \frac { { \mathrm { p } } \cdot ( 1 - { \mathrm { p } } ) } { \mathrm { n } } } }
$$

Lo cual nos indica que la proporcion muestral es un estimador insesgado del parametro binomial p.

A la hora de construir intervalos de confianza para el parametro p aparecen varios obstaculos. El primero, debido a que tanto x como x/n son variables discretas, es practicamente imposible determinar un intervalo para el cual el grado de confianza sea exactamente $1 0 0 ^ { \star } ( 1 - \mathsf { a } ) \%$ . Segundo, es necesario conocer p para hallar σ/n.

Para construir un intervalo de confianza para p, con $( 1 - \mathsf { a } ) 1 0 0 \%$ de confianza, primero, es necesario determinar las abscisas $\mathsf { x } 0 \mathsf { y } \times 1$ que dejan un area de ${ \tt q } / 2$ hacia izquierda y derecha respectivamente.

Por ejemplo:

k 0 25  

$$
\mathbf { \alpha } \mathbf { \alpha } \mathbf { : } = 0 . 0 5
$$

Distribucion binomial con $\mathbf { n } = 2 5 \mathbf { y } \mathbf { p } = 0 . 3$

![](images/64c4c12bbb1cf078e467ee9bc6ce752af7d7d647635699e62406d1316ec2a87d.jpg)

$$
\mathbf { x } 0 : = \mathrm { p b i n o m } ( 2 , 2 5 , 0 . 3 ) = 8 . 9 6 1 \times 1 0 ^ { - 3 } \qquad \mathbf { x } 1 : = 1 - \mathrm { p b i n o m } ( 1 2 , 2 5 , 0 . 3 ) = 0 . 0 1 7
$$

Es posible asegurar con $( 1 - \mathsf { a } ) 1 0 0 \%$ de confianza que

$$
\begin{array} { l } { { \tt x 0 ( p ) < x < } } \\ { { \tt x 1 ( p ) } } \end{array}
$$

Planteando estos limites para diferentes valores de p es posbile plantear un grafico que permita traducir esta desigualdad en un intervalo de confianza para p, dado un valor observado de la variable aleatoria x.

$$
\underset { \ r { \infty } } { \underline { { \mathrm { n } } } } : = 2 5 \qquad \underset { \ r { \infty } } { \underline { { \mathrm { N } } } } : = 2 0 \qquad \mathrm { i } : = 0 \dots \mathrm { N } - 1
$$

$$
\lambda _ { \dot { \bf k } } : = \frac { \mathrm { i } } { \mathrm {  ~ N ~ } } \qquad \underset { \mathrm { { A w w } } } { \mathrm { x 0 } } \mathrm { ( p ) } : = \mathrm { q b i n o m } \biggl ( \frac { \alpha } { 2 } , { \bf n } , { \bf p } \biggr ) - 1 \qquad \underset { \mathrm { { A w } } } { \mathrm { x l } } \mathrm { ( p ) } : = \mathrm { q b i n o m } \biggl ( 1 - \frac { \alpha } { 2 } , { \bf n } , { \bf p } \biggr )
$$

<html><body><table><tr><td rowspan="2">T p</td><td></td><td>０</td><td>１</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>0</td><td>0.05</td><td>0.1</td><td>0.15</td><td>0.2</td><td>0.25</td><td>0.3</td><td>0.35</td><td>0.4</td><td></td></tr></table></body></html>

t 0 0.01    1

![](images/67fc1b51341a0ed0d7dd2c3977fed61f282479f8fcdf0e684b8b7f4c2cbe2804.jpg)

Aumentando el N se obtiene una trama mas fina de puntos, lo que suaviza las curvas. Si tomamos un tamano de n mas grande las curvas se acercan una a la otra, lo cual brinda un intervalo con menor amplitud.

Esto se ha estandarizado y se muestran a continuacion graficas con multiples curvas para ${ \mathfrak { a } } =$ $0 . 0 5 \ y \mathfrak { a } = 0 . 0 1$ con distintos valores de n.

![](images/645853bdb701397cdbdf216d4584098d6a38050ef5c692f0ab04796c1e0c313f.jpg)

Cuando n es sufientemente grande, se construyen intervalos de confianza aproximados para p al usar la aproximacion normal a la distribucion binomial.

$$
\begin{array} { l l } { \underset { \mathsf { M } } { \mathrm { n } } : = 1 0 0 } & { \quad \mathrm { p } : = 0 . 5 } \\ { \begin{array} { l } { \mathrm { k } : = 0 \dots \mathrm { n } } \\ { \mathrm { I } _ { \mathrm { k } } : = \mathrm { k } } \end{array} } \end{array}
$$

![](images/71250be1de6595a6d0bfae4ac63b1e82401ad0e350e92469d8cbac76661bf16e.jpg)

Como regla practica para que la distribucion binomial se acerque a la normal basta con que $\mathsf { n } ^ { \star } \mathsf { p }$ $\mathsf { y n } ^ { \star } ( 1 - \mathsf { p } )$ sean ambos mayores que 5.

Con esto decimos que cuando n es suficientemente grande, podemos aproximar a la distribucion binomial con una curva normal con parametros

$$
\underset { \mathbf { \hat { w } } ^ { \prime } } { \underbrace { \mathbf { u } } } : = \mathbf { n } \cdot \mathbf { p } \qquad \underset { \mathbf { \hat { w } } ^ { \prime } } { \underbrace { \mathbf { \sigma } } } = \sqrt { \mathbf { n } \cdot \mathbf { p } \cdot ( 1 - \mathbf { p } ) }
$$

Dejando al valor normalizado o estadistico z como:

$$
\mathrm { \mathrm { ~ z = \frac { \partial X - \mu } { \partial \sigma } = \frac { X - n \cdot p } { \sqrt { n \cdot p \cdot ( 1 - p ) } } } }
$$

Partiendo de las mismas bases que para otros intervalos de confianza, decimos que el estadistico utilizado se encuentra entre dos limites de confianza, con un $1 0 0 ^ { \star } ( 1 - \mathsf { a } ) \%$ de confianza.

$$
\frac { - z } { 2 } < z < z _ { \alpha }
$$

$$
- z _ { \frac { \alpha } { 2 } } < \frac { X - \mathtt { n } \cdot \mathtt { p } } { \sqrt { \mathtt { n } \cdot \mathtt { p } \cdot ( 1 - \mathtt { p } ) } } < \mathtt { z } _ { \frac { \alpha } { 2 } }
$$

Despejar p no es tarea facil, por lo que se recurre a la aproximacion del mismo en el denominador con el fin de simplificar el despeje.

$$
\frac { - z } { 2 } ^ { < } \frac { X - \mathbf { n } \cdot \mathbf { p } } { \sqrt { \mathbf { n } \cdot \frac { \mathbf { x } } { \mathbf { n } } \cdot \left( 1 - \frac { \mathbf { x } } { \mathbf { n } } \right) } } < z \frac { \mathbf { \Phi } _ { \alpha } } { 2 }
$$

Operando algebraicamente

Intervalo de confianza para p de muestra grande

Hacer un ejemplo combinando ambos metodos, grafico y con estadistico z

La magnitud del error absoluto cometido, cuando usamos x/n como estimador de o, viene dado por

Sustituyendo a p por su estimacion, se obtiene a su vez una estimacion de E

La expresion del error permite encontrar una formula para determinar el tamano de la muestra requerida para lograr cierto grado de precision.

α 2E  Determinacion del tamano de la n p 1 p  ( )  =  muestra

Sin embargo, esta expresion requiere conocimiento previo de p, ya sea por experimentos o muestras anteriores. Esto no siempre es posible, pero se puede usar el hecho de que a lo sumo el producto ${ \mathsf p } ^ { \star } ( 1 - { \mathsf p } )$ es $1 / 4$ .

Demostracio n:

$$
{ \frac { \mathrm { d } } { \mathrm { d } \mathrm { p } } } [ \mathrm { p } { \cdot } ( 1 - \mathrm { p } ) ] = 1 - 2 { \cdot } \mathrm { p }
$$

Hallando el maximo de la funcion

$$
\begin{array} { r } { 1 - 2 { \cdot } { \mathfrak { p } } = 0 } \\ { { \mathfrak { p } } = { \frac { 1 } { 2 } } } \end{array}
$$

Por lo tanto, el producto ${ \mathsf p } ^ { \star } ( 1 - { \mathsf p } )$ es maximo e igual a $1 / 4$ cuando ${ \mathsf p } = 1 / 2$ , que es el caso en el que mayor tamano de muestra voy a necesitar.

De esto obtenemos una expresion que a costa de ser conservadores por no conocer p de antemano, resulta en un mayor tamano muestral.

Determinacion de tamano de muestra (p desconocido)

Por ultimo, cuando p es un valor proximo a cero (alta confiabilidad) y este es la probabilidad de fracaso, se usan intervalos de confiana para p chico y n grande.

$$
{ \mathfrak { p } } < { \frac { 1 } { 2 \cdot \mathrm { n } } } \cdot \left( { \mathfrak { x } } ^ { 2 } \right) _ { \alpha }
$$

Con $\textsf { X } _ { \mathtt { q } }$ con una distribucion chi-cuadarado de $2 ^ { \star } ( \mathsf { x } + 1 )$ grados de libertad

# HIPOTESIS RELATIVA A UNA PROPORCION

Muchos de los metodos empleados en la inspeccion de una uestra, controles de calidad y verificaciones se basan en realizar pruebas de hipotesis sobre un valor determinado para una proporcion (o porcentaje), ya sea, propocion de piezas defectuosas, cantidad de individuos con alguna caracteristicas particular, etc.

A continuacion vemos una prueba en la que se utiliza la aproximacion normal de la curva binomial, es decir, la muestra debe ser suficientemente grande, lo que se traduce en:

$$
\mathtt { n { \cdot p } } \wedge \mathtt { n { \cdot } } ( 1 - \mathtt { p } ) > 5
$$

El estadistico utilizado es:

$\mathrm { \displaystyle z = { \frac { X - n \cdot p } { \sqrt { n \cdot p \cdot ( 1 - p ) } } } }$ Estadistico de prueba de muestra grande relativo a p

Las regiones criticas utilizadas son:

<html><body><table><tr><td>Regiones criticas para probar p = po (muestra grande)</td><td></td></tr><tr><td>Hipótesis alternativa</td><td>Rechazar hipótesis nula si:</td></tr><tr><td>p&lt;po</td><td>Z &lt;-zα</td></tr><tr><td>p &gt; po</td><td>Z &gt; zα</td></tr><tr><td>p ≠pO</td><td>Z &lt; -zα/2</td></tr><tr><td></td><td> Z&gt; zα/2</td></tr></table></body></html>

A menudo surge la necesidad de comprobar si la proporcion entre distintas poblaciones es igual para cada una de ellas. Ya sea la proporcion de defectuosos en distintas fabricas del mismo producto, la proporcion de posibles votantes de un partido politico en distintos departamentos, etc. En todos estos casos se estamos interesados en probar la hipotesis nula ${ \sf H } _ { 0 }$ en la cual dos o mas poblaciones binomiales comparten el mismo parametro p.

$$
{ \mathfrak { p } } _ { 1 } = { \mathfrak { p } } _ { 2 } = \ l _ { \cdots } = { \mathfrak { p } } _ { \mathrm { k } } = { \mathfrak { p } }
$$

En oposicion se encuentra la hipotesis alternativa ${ \mathsf { H } } _ { 1 }$ , en la cual, al menos una proporcion $\mathsf { p } _ { \mathsf { i } }$ difiere significativamente del resto, es decir, no todas las proporciones son iguales.

Como se menciona para el caso de una sola muestra, cuando el tamano de la muestra es suficientemente grande

$$
[ \mathtt { n } { \cdot } \mathtt { p } \wedge \mathtt { n } { \cdot } ( 1 - \mathtt { p } ) ] > 5
$$

La distribucion mustral de

$$
\mathrm { \mathrm { z _ { i } = \frac { \partial \mathrm { X _ { i } - \mathrm { n _ { i } \cdot \mathrm { p _ { i } } } } } { \sqrt { \mathrm { n _ { i } \cdot \mathrm { p _ { i } } \cdot \left( 1 - \mathrm { p _ { i } } \right) } } } } }
$$

es aproximadamente normal estandar.

Tambien se usara el hecho de que el cuadrado de una variable aleatoria con distribucion normal estandar (como Z ) es una variable aleatoria con distribucion chi-cuadrada con 1 grado

de libertad. Por ultimo, la sumatoria de k variables aleatorias con distribucion chi-cuadrado de 1 grado de libertad es otra variable aleatoria con distribucion chi-cuadrado con k grados de libertad.

Entonces

$$
\chi ^ { 2 } = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { k } } \ { \frac { \left( \mathrm { \vec { x } _ { i } - \vec { n } _ { i } \cdot \vec { p } _ { i } } \right) ^ { 2 } } { \mathrm { \vec { n } _ { i } \cdot \vec { p } _ { i } \cdot \left( 1 - \vec { p } _ { i } \right) } } }
$$

es una variable aleatoria con distribucion aproximadamente normal con k grados de libertad.

En la practica, se sustituyen los $\mathsf { p } _ { \mathsf { i } }$ dado que la hipotesis nula supone que son iguales, usando un estimado calculado a partir de las k muestras

$$
\mathrm { p } _ { \mathrm { e s t } } \mathbf { = } { \frac { \mathbf { x } _ { 1 } + \mathbf { x } _ { 2 } + \ldots + \mathbf { x } _ { \mathrm { k } } } { \mathrm { n } _ { 1 } + \mathbf { n } _ { 2 } + \ldots + \mathbf { n } _ { \mathrm { k } } } }
$$

Para esta prueba de hipotesis, el interes es el de rechazar ${ \sf H } _ { 0 }$ si la suma de las diferencias entre $\mathsf { x } _ { \mathrm { i } } \mathsf { y } \mathsf { n } _ { \mathrm { i } } ^ { \star } \mathsf { p } _ { \mathsf { e s t } }$ son grande, lo cual nos conduce a una prueba de hipotesis unilateral de cola derecha en la que rechazamos ${ \sf H } _ { 0 } \thinspace { \sf s i } \thinspace { \sf x } ^ { 2 } > { \sf X } _ { \mathrm { ~ \sf ~ d } } ^ { 2 } ,$ siendo $\mathsf { X } _ { \mathrm { ~ \mathsf ~ { ~ a ~ } ~ } } ^ { 2 }$ una variable aleatoria con distribucion chi-cuadrada con k - 1 grados de libertad (la perdida de un g.l. es debido al uso de $\mathsf { p } _ { \mathsf { e s t } } )$ .

$$
\chi ^ { 2 } = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { k } } \ \frac { \left( \mathrm { x _ { \mathrm { i } } - \mathrm { n _ { \mathrm { i } } } \cdot \mathrm { p _ { \mathrm { e s t } } } } \right) ^ { 2 } } { \mathrm { n _ { \mathrm { i } } \cdot \mathrm { p _ { \mathrm { e s t } } } } \cdot \left( 1 - \mathrm { p _ { \mathrm { e s t } } } \right) }
$$

En la practica, es posible calcular el estadistico de prueba de otra forma alternativa disponiendo los datos de la siguiente forma:

<html><body><table><tr><td></td><td>Muestra 1</td><td>Muestra 2</td><td></td><td>Muestra k</td><td>Total</td></tr><tr><td>Exitos</td><td>X1</td><td>12</td><td></td><td>xk</td><td>x</td></tr><tr><td>Fracasos</td><td>n1-x1</td><td>n2 - x2</td><td></td><td>nk-xk</td><td>n-x</td></tr><tr><td>Total</td><td>m</td><td>12</td><td></td><td>nk</td><td>n</td></tr></table></body></html>

Donde cada celda es lo que se conoce como frecuencia observada

Luego, se cualculan la frecuencias esperadas y se distribuyen de forma tabular/matricial al igual que las frecuencias observadas.

$$
\mathbf { e } _ { 1 , { \bf j } } ^ { \mathrm { } } = \frac { \mathbf { n } _ { \mathrm { j } } ^ { \cdot \cdot \mathrm { x } } } { \mathrm { n } } = \mathbf { n } _ { \mathrm { j } } ^ { \cdot \cdot \mathrm { p } } \mathrm { e s t } \qquad \mathbf { e } _ { 2 , { \bf j } } ^ { \mathrm { } } = \frac { \mathbf { n } _ { \mathrm { j } } ^ { \cdot } ( \mathrm { n - x } ) } { \mathrm { n } } = \mathbf { n } _ { \mathrm { j } } ^ { \cdot } \Big ( 1 - \mathrm { p } _ { \mathrm { e s t } } \Big )
$$

Vemos que cada frecuencia esperada se puede obtener al multiplicar el total de la fila (x o n - x) por el total de la columna n y dividirlo por el gran total n

De esta forma es posible calcular el estadistico $\mathsf { X } ^ { 2 }$ de forma alternativa con la siguiente expresion

$$
\chi ^ { 2 } = \sum _ { \mathrm { i = 1 ~ j = 1 } } ^ { 2 } \frac { \left( { \bf { \sigma } } _ { \mathrm { i , j } } ^ { 2 } - { \bf { \sigma } } _ { \mathrm { i , j } } ^ { 2 } \right) ^ { 2 } } { \bf { \sigma } } _ { \mathrm { { \bf { \vec { i } } , j } } }
$$

La formula no presenta gran ventaja cuando hablamos de una poblacion con dos resultados (dicotomica), sin embargo, el beneficio de la expresion alternativa es que permite extender facilmente al caso donde el ensayo posea mas de dos resultados.

Agregar ejemplo prueba de hipotesis varias proporciones

# TABLAS DE CONTINGENCIA O RXC

Estas tablas se ajustan a los casos donde la clasificacion es de doble entrada con r filas y c columnas. Estas tablas pueden aparecer en problemas como:

Clasificacion de posicion politica respecto de un partido segun nivel de ingresos

Extraida de 3 poblaciones (ingresos altos, medios y bajos), clasificados segun su posicion - Homogeneidad   

<html><body><table><tr><td></td><td>Afavor</td><td>En contra</td><td>Indiferente</td><td>Indeciso</td></tr><tr><td>Altos</td><td>56</td><td>25</td><td>15</td><td>10</td></tr><tr><td>Medios</td><td>40</td><td>60</td><td>23</td><td>5</td></tr><tr><td>Bajos</td><td>22</td><td>45</td><td>10</td><td>2</td></tr></table></body></html>

Clasificacion de rendimiento con respecto al promedio de vehiculos segun su gama   
xtraida de una sola poblacion, clasificados segun su rendimiento y gama - Independencia   

<html><body><table><tr><td></td><td>Excelente</td><td>Superior</td><td>Promedio</td><td>Deficiente</td></tr><tr><td>Lujo</td><td>10</td><td>8</td><td>5</td><td>13</td></tr><tr><td>Alta</td><td>1</td><td>18</td><td>25</td><td>8</td></tr><tr><td>Media</td><td>0</td><td>10</td><td>4</td><td>24</td></tr><tr><td>Entrada</td><td>7</td><td>26</td><td>24</td><td>24</td></tr></table></body></html>

Para el analisis, primero es necesario calcular las frecuencias esperadas de forma similar a como se realizo en el caso de poblaciones dicotomicas.

Donde la frecuencia esperada de la i-esima fila y j-esima columna se calcula como el total de la i-esima fila x_total por el total de la j-esima columna $\mathsf { n } _ { \mathsf { j } }$ , dividido por el gran total n.

Como se menciono anteriormente, el estadistico de prueba es:

$$
\chi ^ { 2 } = \sum _ { \mathrm { i = 1 ~ j = 1 } } ^ { \mathrm { r } } \sum _ { \mathrm { { \scriptsize ~ i = 1 ~ } } } ^ { \mathrm { c } } \frac { { \left( { { \bf { \sigma } } _ { { \mathrm { i , j } } } - { \bf { \sigma } } _ { { \mathrm { i , j } } } } \right) ^ { 2 } } } { { { \bf { \sigma } } _ { { \mathrm { i , j } } } } }
$$

Donde en lugar de "i" ir hasta 2, ahora llega hasta r filas que posea la tabla. Y la variable aleatoria se distribuye como una $\mathsf { X } ^ { 2 } \mathsf { d e } ( \mathsf { r } - 1 ) ( \mathsf { c } - 1 )$ grados de libertad.

Se rechazara $H _ { 0 } \mathsf { s i } \mathsf { x } ^ { 2 } > \mathsf { X } _ { \mathrm { ~ a ~ } } ^ { 2 }$ para $\mathsf { v } = ( \mathsf { r } - 1 ) ( \mathsf { c } - 1 )$ g.d.l.

Agregar ejemplo con la ultima tabla de ejemplo (lujo, alta, media, entrada)

# BONDAD DE AJUSTE

Hasta ahora se han desarrollado pruebas de hipotesis en las que la poblacion o su distribucion de probabilidad es conocida (normal, binomial, etc.), sin embargo, existe otro tipo de prueba en el que no conocemos la distribucion de la poblacion subyacente y deseamos probar la hipotesis de que alguna distribucion en particular seria un modelo satisfactorio para esa poblacion. Por ejemplo, dada una muestra de alguna poblacion:

Se desea probar si es normal...

Se desea probar si es Poisson...

Se desea probar si es exponencial...

Si bien siempre es posible graficar de alguna forma conveniente los datos para ver algun patron en su distribucion de probabilidades, el ojo es subjetivo, por lo que es bueno introducir un metodo cientifico que nos indique "que tan bien se ajusta a una distribucion en concreto", el cual es conocido como bondad de ajuste.

La prueba requiere de una muestra aleatoria de tamano n de la poblacion cuya distribucion se desea comprobar, luego, se ordenan las frecuencias observadas en forma de histograma ubicandolas en k intervalos de clase. Luego se calculan las probabilidades teoricas de la distribucion propuesta para cada intervalo de clase y se calculan las frecuencias absolutas esperadas para cada intervalo. El estadistico de prueba a utilizar es:

χ 2 k o i e i    e= Estadistico de prueba $\mathsf { X } ^ { 2 }$ para probar bondad de ajuste

La distribucion muestral de este estadistico es aproximadamente chi-cuadrada con grados de libertad $v = k - m - 1$

A continuacion un ejemplo para ilustrar el procedimiento:

El numero de defectos en circuitos impresos se supone con distribucion Poisson. Una muestra aleatoria de 60 placas fue recolectada y se tabularon los defectos como sigue:

n  60

<html><body><table><tr><td>Number of Defects</td><td>Observed Frequency</td></tr><tr><td>0</td><td>32</td></tr><tr><td>1</td><td>15</td></tr><tr><td>2</td><td>9</td></tr><tr><td>3</td><td>4</td></tr></table></body></html>

Para comenzar, vemos que el parametro $\lambda$ propio de la distribucion Poisson no es un dato disponible, por lo que debemos inferirlo de la muestra.

$$
\lambda : = \frac { 0 \cdot 3 2 + 1 5 \cdot 1 + 2 \cdot 9 + 3 \cdot 4 } { \mathrm { n } } = 0 . 7 5
$$

A continuacion, calculamos las probabilidades teoricas para cada intervalo de clase.

$$
\mathrm { i } : = 0 \dots 2
$$

$$
\begin{array} { l } { \displaystyle \mathrm { E } _ { \mathrm { i } } : = \mathrm { d } { \mathsf { p o i s } } ( \mathrm { i } , \lambda ) } \\ { \displaystyle \mathrm { E } _ { 3 } : = 1 - \sum _ { \mathrm { i } } \mathrm { E } _ { \mathrm { i } } } \end{array}
$$

$$
\operatorname { E } ^ { \mathrm { T } } = ( 0 . 4 7 2 \ \ \ 0 . 3 5 4 \ \ 0 . 1 3 3 \ \ 0 . 0 4 1 )
$$

Calculamos las frecuencias absolutas esperadas.

$$
\left( \mathbf { n } { \cdot } \mathbf { E } \right) ^ { \mathsf { T } } = ( 2 8 . 3 4 2 \ \ \ 2 1 . 2 5 6 \ \ \ 7 . 9 7 1 \ \ 2 . 4 3 )
$$

<html><body><table><tr><td>Number of Defects</td><td>Probability</td><td>Expected Frequency</td></tr><tr><td>0</td><td>0.472</td><td>28.32</td></tr><tr><td>1</td><td>0.354</td><td>21.24</td></tr><tr><td>2</td><td>0.133</td><td>7.98</td></tr><tr><td>3 (or more)</td><td>0.041</td><td>2.46</td></tr></table></body></html>

Dado que hay valores menores a 5, se los combina con la clase adyacente.

<html><body><table><tr><td>Number of Defects</td><td>Observed Frequency</td><td>Expected Frequency</td></tr><tr><td>0</td><td>32</td><td>28.32</td></tr><tr><td>1</td><td>15</td><td>21.24</td></tr><tr><td>2 (or more)</td><td>13</td><td>10.44</td></tr></table></body></html>

Por ultimo aplicamos el procedimiento normal de una prueba de hipotesis.

1. Planteo de hipotesis

H0 : La variable de interes se ajusta a una distribucion Poisson.   
H1 : La variable NO se ajusta a una distribucion Poisson.

2. Nivel de significacion de la prueba

$$
\underset { N } { \underbrace { \mathrm { \alpha } } } \overset { \cdot = } { \down } 0 . 0 5
$$

3. Criterio

$\begin{array} { l l } { \underset { \ r { \mathrm { \tiny ~  ~ } } } { \mathrm { m } } : = 1 } & { \mathsf { N u m e r o d } } \\ { \underset { \ r { \mathrm { \tiny ~ k } } : = } { \ r { \mathrm { \tiny ~ \wedge ~ } } } 3 } & { \mathsf { l n t e r v a l o s } } \\ { \nu : = \mathrm { k } - \mathrm { m } - 1 = 1 } \\ { \mathrm { \ x ~ { \mathrm { \tiny ~ \cdot ~ } } } } \\ { \chi _ { \mathrm { \tiny ~  ~ } } : = \mathrm { q c h i s q } ( 1 - \alpha , \nu ) = 3 . 8 4 1 } \end{array}$ e parametros estimados despues de modificacion

# 4. Calculos

$$
\chi : = \frac { \left( 3 2 - 2 8 . 3 2 \right) ^ { 2 } } { 2 8 . 3 2 } + \frac { \left( 1 5 - 2 1 . 2 4 \right) ^ { 2 } } { 2 1 . 2 4 } + \frac { \left( 1 3 - 1 0 . 4 4 \right) ^ { 2 } } { 1 0 . 4 4 } = 2 . 9 3 9
$$

# 5. Conclusion

Dado que $\tt X { < } \tt X _ { \tt d }$ , se falla al rechazar la hipotesis nula de que la distribucion de los defectos en los circuitos impresos es Poisson, con un nivel de significacion 0.05.

# UNIDAD IV PRUEBAS NO PARAMETRICAS

# UNIDAD IV

# INTRODUCCION

La mayoria de los metodos de inferencia vistos se basan en suposiciones o requisitos con respecto a las poblaciones o tamanos de las muestras. Sin embargo, se da en ocasiones que el tamano de la muestra o el supuesto de normalidad no se cumplen o no pueden ser asegurados.

Esto no quita que los metodos que suponen normalidad son los mas eficientes. Por ejemplo, la media aritmetica es un estimador mas eficiente que la mediana para estimar la media poblacional.

# SIMULACION

$$
\mathrm { X M _ { i } : = m e a n \Big ( X _ { i } \Big ) }
$$

$$
\mathrm { X M E D I A N _ { i } } { : = } \ \mathrm { m e d i a n } \big ( \mathrm { X _ { i } } \big )
$$

$$
\frac { \sigma } { \mu } = 0 . 0 1
$$

$$
\frac { \sigma } { n } { \cdot } 1 . 5 7 = 0 . 0 1 6
$$

Si la media aritmetica representa una eficiencia del $100 \%$ entonces, se puede deducir:

$$
{ \frac { \operatorname { v a r } ( \mathrm { X M } ) } { \operatorname { v a r } ( \mathrm { X M E D I A N } ) } } \cdot 1 0 0 = 6 4 . 5 3 5
$$

La eficiencia de la mediana como estimador de la media es de aproximadamente el $64 \%$ .

Asi mismo, tambien se podria ver el caso del rango como estimador de la desviacion estandar, cuya eficiencia disminuye conforme aumenta el tamano de la muestra.

# Ventajas de las pruebas no parametricas:

1. Simples de usar y entender   
2. No requieren suposiciones excluyentes de su uso   
3. Se puede usar con variables cualitativas.

# Desventajas de las pruebas no parametricas:

1. Pueden no hacer uso de la totalidad de la informacion   
2. Son menos eficientes que las pruebas parametricas (por eso se usan cuando son necesarias).   
3. Tienen mayor probabilidad de "aceptar" (no rechazar) una hipotesis nula falsa. (β)

# PRUEBA DEL SIGNO

Alternativa no parametrica a: T-Unimuestral para muestras pareadas (antes-despues) y correspondientes pruebas para muestras grandes.

Se aplica cuando se muestrea de una poblacion simetrica, de modo que la probabilidad de obtener valores tanto mayores como menores es del $50 \%$ , es decir, 1/2.

Nota: En ocasiones, en lugar de usar la media, dado que es dificil verificar la simetria, se usa la mediana poblacional.

# Procedimiento:

1. Se plantean las hipotesis

$$
\mathsf { H } 0 : \mu = \mu _ { 0 } \qquad \mathsf { o b i e n } \qquad \mathsf { H } 0 : \mu _ { - } \mathsf { m e d i a n } = \mu _ { 0 - } \mathsf { m e d i a n }
$$

contra alguna H1 adecuada.

2. Se establece el nivel de significacion (α)

3. Se establece el criterio. Siendo la cantidad de $" + "$ la cantidad de exitos en n ensayos binomiales, se calcula la probabilidad de esa cantidad de exitos.

4. Se reemplaza cada valor de la muestra por un "+" o "-", segun sea mayor o menor que $\mu _ { 0 }$ , respectivamente. En caso de que un valor sea igual a $\mu _ { 0 }$ se ignora.

5. Se comparan α contra la probabilidad y se elabora la conclusion

# Ejemplo:

# Un psicologo afirma que que el numero de delincuelntes reincidentes disminuiria si los delincuentes por primera vez completan un curso de rehabilitacion. Selecciona de forma aleatoria 10 prisiones y registra el numero de reincidentes durante 24 meses.

<html><body><table><tr><td>Prisi6n</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Antes</td><td>21</td><td>34</td><td>9</td><td>45</td><td>30</td><td>54</td><td>37</td><td>36</td><td>33</td><td>40</td></tr><tr><td>Después</td><td>19</td><td>22</td><td>16</td><td>31</td><td>21</td><td>30</td><td>22</td><td>18</td><td>17</td><td>21</td></tr></table></body></html>

1 - Hipotesis

H0: El numero de reincidentes es igual H1: El numero es menor

2 - Significancia

$$
\mathbf { \alpha } \mathbf { \alpha } \mathbf { : } = 0 . 0 5
$$

3 - Estadistico + + - + + + + + + + $\displaystyle \begin{array} { c } { { \mathrm { \Delta x : = 9 } } } \\ { { \displaystyle \operatorname* { n } _ { \mathrm { \Delta w } } : = 1 0 } } \end{array}$

4 - Calculo

![](images/991b6c95ff105309140f5f588b345a5979e6cbe78e30c265a850a9fe5950eb1b.jpg)

n $\sum \mathrm { \ d b i n o m ( k , n , 0 . 5 ) } = 0 . 0 5 5$ Vemos que el valor critico estaria muy cercano a 8 8k 

# 5. Conclusion

Dado que $\mathsf { P } = 0 . 0 1 1 < \mathsf { a } = 0 . 0 5$ se rechaza H0. Por lo tanto existe evidencia significativa de que el curso tiene efecto en la reincidencia de los presos.

# PRUEBA DE SUMA DE RANGOS

Dentro de las pruebas de sumas de rango existen dos tipos de ellas. La prueba U o de Wilcoxon y la prueba H o de Kruskall-Wallis

# WILCOXON

A modo de ejemplificar el metodo se realiza el siguiente ejemplo.

Se realizo un examen de aptitud a dos grupos de mecanicos en dos talleres, se desea saber si las medias de puntaje son significativamente iguales $( a = 0 . 0 5 )$ . No se conoce la distribucion estadistica de ninguna de las dos poblaciones.

Muestra 1:

5.5890 5.6750 6.4830 7.0620 6.4040 6.6690 7.5390 7.2190 7.4050   
5.8440 5.8950 5.8970 6.5930

Muestra 2:

7.4280 6.525 6.3040 10.0500 6.7140 5.7200 7.7590 6.6070 5.7960   
5.9630 6.9810

1 - Hipotesis H0: Las medias son iguales H1: Las medias son distintas

2 - Significacion

3 - Criterio $z _ { 0 0 9 5 } : = \mathrm { q n o r m } \left( 1 - \frac { \alpha } { 2 } , 0 , 1 \right) = 1 . 9 6$

4 - Calculos

Primero se consideran a los datos como si fueran una sola muestra y se los ordena de forma creciente.

x  ( 5.589 5.675 6.483 7.062 6.404 6.669 7.539 7.219 7.405 5.844 5.895 5.897 6.5 y 7.428 6.525 6.304 10.050 6.714 5.720 7.759 6.607 5.796 5.963 6.981  ( )

A augment x y ( )  T Concateno vectores B sort A  ( )

<html><body><table><tr><td>0</td><td>5.589</td><td>5.5890 1</td><td>1</td></tr><tr><td>1</td><td>5.675</td><td>5.6750 1 2 3</td><td></td></tr><tr><td>2</td><td>5.72</td><td>5.7200 2 5.7960 2</td><td>4</td></tr><tr><td>3</td><td>5.796</td><td>5.8440 11</td><td>56</td></tr><tr><td>4</td><td>5.844</td><td>5.8970 1</td><td>7</td></tr><tr><td>5</td><td>5.895</td><td>5.9630 22</td><td>89</td></tr><tr><td>6</td><td>5.897</td><td>6.4040 1</td><td>10</td></tr><tr><td>B= 7</td><td></td><td>6.4830 1</td><td>11</td></tr><tr><td></td><td>5.963</td><td>6.5250 2</td><td>12</td></tr><tr><td>8</td><td>6.304</td><td>6.5930 12</td><td>14</td></tr><tr><td>9</td><td>6.404</td><td>6.6690 1</td><td>15</td></tr><tr><td>10</td><td>6.483</td><td>6.7140 2 6.9810 2</td><td>16 17</td></tr><tr><td>11</td><td>6.525</td><td></td><td></td></tr><tr><td></td><td></td><td>7.0620 11</td><td>1819</td></tr><tr><td>12</td><td>6.593</td><td>7.4050 1</td><td>20</td></tr><tr><td>13</td><td>6.607</td><td>7.4290 21</td><td>2122</td></tr><tr><td>14</td><td>6.669</td><td>7.7590 2</td><td>23</td></tr><tr><td></td><td></td><td>10.0500 2</td><td>24</td></tr><tr><td>15</td><td></td><td></td><td></td></tr></table></body></html>

Luego, se asignan rangos a los valores como se ve en la figura. En el caso de que existan dos, tres o mas valores iguales, a cada uno de esos valores se les asigna el mismo numero de rango, que se calcula como la sumatoria de los rangos involucrados dividiva por la cantidad de valores iguales.

Ejemplo:

Se repiten el 5to, 6to, 7mo y 8vo valor. A cada uno se le asignara el rango:

$$
{ \frac { 5 + 6 + 7 + 8 } { 4 } } = 6 . 5
$$

La hipotesis nula que se quiere probar es que ambas muestra provienen de poblaciones identicas, lo cual es razon para indicar que las medias de sus rangos debe ser mas o menos iguales.

En este metodo lo que se comparan son la suma de los rangos asignados, en nuestro ejemplo:

$$
\begin{array} { l l } { { \mathrm { R } _ { 1 } = 1 + 2 + 5 + \ldots } } & { { \qquad \mathrm { R } _ { _ 2 } = 3 + 4 + 8 + \ldots } } \\ { { } } & { { } } \\ { { \mathrm { R } _ { 1 } : = 1 4 9 } } & { { \qquad \mathrm { R } _ { 2 } : = 1 5 3 } } \end{array}
$$

Lo que queda ahora es ver si esta diferencia en la suma de los rangos es significativa. Para esto se definen dos estadisticos:

$$
\mathrm { U } _ { 2 } : = \mathrm { n } _ { 1 } \cdot \mathrm { n } _ { 2 } + { \frac { \mathrm { n } _ { 2 } \cdot \left( \mathrm { n } _ { 2 } + 1 \right) } { 2 } } - \mathrm { R } _ { 2 } = 5 6
$$

Nos quedamos con el menor, osea, U1. Puede comprobarse que la media y la desviacion estandar del estadistico U son:

$$
\mathsf { \Pi } \mathsf { \Pi } \mathsf { \mu } _ { \mathrm { U } 1 } : = \frac { \mathrm { \mathbf { n } } _ { 1 } \cdot \mathrm { \mathbf { n } } _ { 2 } } { 2 } = 7 1 . 5 \qquad \sigma _ { \mathrm { U } 1 } : = \sqrt { \frac { \mathrm { \mathbf { n } } _ { 1 } \cdot \mathrm { \mathbf { n } } _ { 2 } \cdot \left( \mathrm { \mathbf { n } } _ { 1 } + \mathrm { \mathbf { n } } _ { 2 } + 1 \right) } { 1 2 } } = 1 7 . 2 6
$$

Puesto que estudios numericos demuestran que la distribucion muestral de U puede aproximarse a una distribucion normal, cuando ambos tamanos de muestra son mayores que 8.

$$
\cup _ { 1 } \sim \mathsf { N o r m a l } ( \mathsf { \Pi } \mu _ { \mathsf { U } 1 } , \sigma _ { \mathsf { U } 1 } ) \mathsf { c u a n d o n } _ { 1 } \mathsf { y } \mathsf { n } _ { 2 } \mathsf { s o n m a y o r e s a } \mathsf { \delta }
$$

Por lo que podemos basar la prueba en el estadistico

$$
\mathrm { z : = \frac { U _ { 1 } - \mu _ { U 1 } } { \sigma _ { U 1 } } = 0 . 7 8 2 }
$$

Estadisitco de prueba U para muestra mayor a 8

Que tiene aproximadamente distribucion normal estandar

$$
\mathfrak { t } : = - 3 , - 2 . 9 9 9 \ldots 3
$$

![](images/2bb78e9ae58185a279df8c85ebdb1cdc9c8a4c7800ff588a92ee012c90f58fff.jpg)

En nuestro caso, se falla en rechazar H0, dado que $- z _ { 0 0 9 5 } < z < z _ { 0 0 9 5 }$ . Se concluye que no existe diferencia entre las medias de puntajes en el examen de mecanicos de ambos talleres.

Hay que destacar que:   
Cuando probamos la H0 contra H1: $\mu 1 > \mu 2$ se rechaza $\mathsf { H O }$ si $z < z _ { \alpha }$ dado que a valores   
pequenos de U1 corresponden grandes valores de R1

Dado que como R1 resta en la formula a mayor R1, menor U1

Cuando probamos la H0 contra H1: $\mu 1 < \mu 2$ se rechaza $\mathsf { H O }$ se $z > z _ { \mathrm { q } }$ dado que a valores grandes de U1 corresponden pequenos valores de R1.

Dado que como R1 resta en la formula a menor R1, mayor U1

# KRUSKAL-WALLIS

Alternativa no parametrica a: Analisis de varianza de un factor

Es una generalizacion de la prueba U o de Wilcoxon. Permite probar la H0 de que k muestras aleatorias independientes provienen de poblaciones identicas.

H0 : Las k muestras provienen de poblaciones identicas

Como en la prueba U, todas las observaciones se clasifican como si fueran una sola muestra.

A continuacion de define el estadistico de la prueba:

$$
\mathrm { { H } = \frac { 1 2 } { n \cdot ( n + 1 ) } { \cdot } \sum _ { i = 1 } ^ { k } \frac { \binom { k } { i } ^ { 2 } } { n _ { i } } - 3 { \cdot } ( n + 1 ) }
$$

Estadistico de prueba H

Donde:

n es la sumatoria de todos los tamano muestrales k es el numero de muestras o tratamientos $\mathsf { R } _ { \mathrm { i } }$ es el rango de la i-esima muestra $\mathsf { n } _ { \mathsf { i } }$ es el tamano de la i-esima muestra

Cuando $\mathsf { n } _ { \mathrm { i } } > 5$ para cada una de las k muestras y la H0 es verdadera, la distribucion muestral de H es aproximadamente una chi-cuadrada de k - 1 g.d.l. A modo de ilustrar el metodo se realiza el siguiente ejemplo.

Se encontro que ejercicio puede ayudar a aliviar la depresion. Para esto se reunio un grupo de personas y se verifico que esten igualmente deprimidas para empezar. Luego se asigno a cada una al azar a uno de tres grupos. El 1er grupo no hizo ningun tipo de ejercicio, el 2do realizo 20 minutos de trote por dia y el 3ro realizo 60 minutos de trote por dia. Luego de 1 mes, se le pidio a cada uno que marque en una escala (Likert) del 1 (totalmente miserable) al 100 (Feliz) que tan deprimido se sentia

# Rating de la escala de depresión

<html><body><table><tr><td></td><td>Sin ejercicio</td><td>Trote de 20 min.</td><td>Trote de 60 min</td></tr><tr><td></td><td>23</td><td>22</td><td>59</td></tr><tr><td></td><td>26</td><td>27</td><td>66</td></tr><tr><td></td><td>51</td><td>39</td><td>38</td></tr><tr><td></td><td>49</td><td>29</td><td>49</td></tr><tr><td></td><td>58</td><td>46</td><td>56</td></tr><tr><td></td><td>37</td><td>48</td><td>60</td></tr><tr><td></td><td>29</td><td>49</td><td>56</td></tr><tr><td></td><td>44</td><td>65</td><td>62</td></tr><tr><td>Media:</td><td>39.63</td><td>40.63</td><td> 55.75</td></tr><tr><td>(SD):</td><td>(12.85)</td><td>(14.23)</td><td>(8.73)</td></tr></table></body></html>

1 - Hipotesis

$\mathsf { H O }$ : Las medias (3) son iguales H1: Al menos una de ellas difiere significativamente

2 - Significacion α  0.05

3 - Criterio k 3  k es el numero de muestras ${ \mathrm { c h i } } _ { 0 0 9 5 } : = { \mathrm { q c h i s q } } ( 1 - \mathbf { \alpha } , \mathbf { k } - 1 ) = 5 . 9 9 1$

4 - Calculos

Datos ordenadosde menora mayor:

$$
\mathrm { R A } : = 2 + 3 + 5 . 5 + 7 + 1 0 + 1 4 + 1 6 + 1 9 = 7 6 . 5
$$

$$
\mathrm { R B } : = 1 + 4 + 5 . 5 + 9 + 1 1 + 1 2 + 1 4 + 2 3 = 7 9 . 5
$$

$$
\mathrm { R C } : = 8 + 1 4 + 1 7 + 1 8 + 2 0 + 2 1 + 2 2 + 2 4 = 1 4 4
$$

$$
\begin{array} { r l r l r l } & { \underset {  0 } { \mathrm { R } } : = 7 6 . 5 } & & { \mathrm { R } _ { 1 } : = 7 9 . 5 } & & { \mathrm { R } _ { 2 } : = 1 4 4 } \\ & { \underset {  0 } { \mathrm { R } } : = 8 } & & { \mathrm { n } _ { 1 } : = 8 } & & { \mathrm { n } _ { 2 } : = 8 } \end{array}
$$

$$
\underset { \mathbf { j } } { \mathbf { N } } { : = } \sum _ { \mathbf { j } = 0 } ^ { 2 } \ \underset { \mathbf { j } } { \mathbf { n } } = 2 4
$$

$$
\underset { \mathbf { \hat { \rho } } } { \mathbf { H } } : = \frac { 1 2 } { \mathbf { N } \cdot ( \mathbf { N } + \mathbf { 1 } ) } . \sum _ { \mathrm { i } = 0 } ^ { \mathbf { k } - 1 } \frac { \binom { \mathbf { R _ { i } } } { \mathbf { i } } ^ { 2 } } { \mathbf { n _ { i } } } - 3 { \cdot } ( \mathbf { N } + \mathbf { 1 } ) = 7 . 2 7 1
$$

t 0 0.001   10

![](images/d44aea99b3318fa746a588844f3d50c062583096240bf0dc85ac36cc72f33e13.jpg)  
t chi0095 H

Se rechaza H0, dado que $\mathsf { H } = 7 . 2 7 1 > \mathsf { X } _ { 0 0 9 5 } = 5 . 9 9 1$ . Por lo que existe evidencia significativa de que al menos una difiere, es decir, que el tipo ejercicio fisico tiene efecto en el alivio de la depresion.

# PRUEBA DE ALEATORIEDAD

A menudo es necesario poder probar si una muestra puede considerarse como aleatoria. Una de esas tecnicas se basa en el orden en el que se obtuvieron los valores de esa muestra, en otras palabras, se basa en el numero de corridas o rachas que arrojan los resultados muestrales.

Racha: Sucesion de simbolos identicos contenidos entre diferentes simbolos (o ninguno)

Por ejemplo, en el stream anterior vemos que hay 13 corridas.

$$
\mathrm { ~ u ~ } { : = } \ 1 3
$$

Este numero de corridas puede servir para determinar el "grado de aleatoriedad". De forma intuitiva, si hubieran pocas corridas como 2 (15 L's seguidas y 15 O's seguidas) o muchas como 30 (1 L y 1 O, alternadas), habriamos de sospechar que existe un patron o tendencia y la secuencia no es aleatoria.

Nota: La sospecha surgio del orden de aparicion, no del numero de apariciones de L y O

Si un stream de simbolos contiene $\mathsf { n } _ { 1 }$ simbolos de un tipo (L, en nuestro ejemplo) y ${ \mathsf n } _ { 2 }$ simbolos del otro tipo (O), siempre que ambas cantidades sean mayores o iguales a 10, la distribucion del numero de corridas u, puede aproximarse con una distribucion normal, con los siguientes parametros:

$$
\mu _ { \mathrm { u } } = \frac { \boldsymbol { 2 } \cdot \mathrm { n } _ { 1 } \cdot \mathrm { n } _ { 2 } } { \mathrm { n } _ { 1 } + \mathrm { n } _ { 2 } } + 1
$$

$$
\sigma _ { \mathrm { u } } = \sqrt { \frac { 2 \cdot \mathrm { n } _ { 1 } \cdot \mathrm { n } _ { 2 } \cdot \left( 2 \cdot \mathrm { n } _ { 1 } \cdot \mathrm { n } _ { 2 } - \mathrm { n } _ { 1 } - \mathrm { n } _ { 2 } \right) } { \left( \mathrm { n } _ { 1 } + \mathrm { n } _ { 2 } \right) ^ { 2 } \cdot \left( \mathrm { n } _ { 1 } + \mathrm { n } _ { 2 } - 1 \right) } }
$$

En nuestro ejemplo:

$$
\begin{array} { r } { \mathrm { n } _ { 2 } \cdot = 1 0 \quad \mathsf { C a n t . d e O ^ { \circ } s } } \end{array}
$$

$$
\mu _ { \mathrm { u } } : = { \frac { 2 { \cdot } \mathrm { n } _ { 1 } { \cdot } \mathrm { n } _ { 2 } } { \mathrm { n } _ { 1 } + \mathrm { n } _ { 2 } } } + 1 = 1 4 . 3 3 3
$$

$$
\sigma _ { \mathrm { { u } } } : = { \sqrt { \frac { 2 \cdot \mathrm { n } _ { 1 } \cdot \mathrm { n } _ { 2 } \cdot \left( { 2 \cdot \mathrm { n } _ { 1 } \cdot \mathrm { n } _ { 2 } - \mathrm { n } _ { 1 } - \mathrm { n } _ { 2 } } \right) } { \left( \mathrm { n } _ { 1 } + \mathrm { n } _ { 2 } \right) ^ { 2 } \cdot \left( \mathrm { n } _ { 1 } + \mathrm { n } _ { 2 } - 1 \right) } } } = 2 . 3 8 1
$$

Como la variable aleatoria se distribuye aproximadamente normal, podemos basar nuestra prueba en el siguiente estadistico:

$$
\underset { \mathrm { ^ { M } } } { \underbrace { z } } : = \frac { \mathrm { u } - \mu _ { \mathrm { u } } } { \sigma _ { \mathrm { u } } } = - 0 . 5 6
$$

Si quisieramos probar con una significacion $\mathtt { q } = 0 . 0 5$ :

$$
z _ { \alpha } : = \mathrm { q n o r m } \left( 1 - \frac { 0 . 0 5 } { 2 } , 0 , 1 \right) = 1 . 9 6
$$

La prueba es de dos colas, ya que probamos si el numero de corridas es "muy alto o muy bajo"

t 4  3.99  4

![](images/8b92a387166efdb8b34f79620c8b463f0d2e3725e88a0355474301decb19b3ff.jpg)

Dado que $- z _ { \alpha / 2 } < z = - 0 . 5 6 < z _ { \alpha / 2 }$ . Se falla en rechazar H0, por lo que existe aleatoriedad en la secuencia de L's y O's.

La prueba de rachas tambien puede usarse para comprobar la aleatoriedad de muestras que contienen valores numericos, al asignar simbolos (diferentes) a los valores que se encuentran por encima (a, por ejemplo) y por debajo (b, por ejemplo) de la mediana muestral.

Esta practica es comun en las pruebas de control de calidad. A continuacion se enuncia un caso en el que se podria aplicar.

Un ingeniero está preocupado por la posibilidad de que demasiados cambios se cometen en la coniguración de un torno automático. Dados los siguientes diámetros medios (en pulgadas) de 40 ejes sucesivos que giran en el torno

0.261 0.258 0.249 0.251 0.247 0.256 0.250 0.247 0.255 0.243   
0.252 0.250 0.253 0.247 0.251 0.243 0.258 0.251 0.245 0.250   
0.248 0.252 0.254 0.250 0.247 0.253 0.251 0.246 0.249 0.252   
0.247 0.250 0.253 0.247 0.249 0.253 0.246 0.251 0.249 0.253

En este caso la mediana es de 0.250. Se generaria una stream de simbolos a's y b's segun los valores se encuentren por encima o por debajo de dicha mediana (en caso de igualdad se saltea ese valor). Luego el procedimiento es como el desarrollado en el anterior ejemplo.

# PRUEBA DE KOLMOGOROV-SMIRNOV

Se utiliza para analizar diferencias entre distribuciones acumuladas. La prueba para una sola muestra se encarga de comparar valores observados contra valores esperados o teoricos de una distribucion c ontinua en particular, por lo tanto es una prueba de bondad de ajuste. La prueba de Kolmogorov-Smirnov para una muestra, es generalmente mas eficiente que la prueba chi-cuadrada cuando el tamano de la muestra es pequeno.

La prueba se basa en la diferencia absoluta maxima D entre los valores de la distribucion acumulada observada (para la muestra de tamano n) y una distribucion acumulada teorica. Para decidir si esta diferencia absoluta maxima es razonable, con un respecto a un nivel de significacion α asociado a la prueba, se buscan los valores criticos de D en la siguiente tabla.

<html><body><table><tr><td rowspan="2">TAMANO DE LA MUESTRA (N)</td><td colspan="5"> NIVEL DE SIGNIFICANCIA PARA D = MAX [ Fg(X) - Sn(X)]</td></tr><tr><td>.20</td><td>.15</td><td>.10</td><td>.05</td><td>.01</td></tr><tr><td>1</td><td>.900</td><td>.925</td><td>.950</td><td>.975</td><td>.995</td></tr><tr><td>2</td><td>.684</td><td>.726</td><td>.776</td><td>.842</td><td>.929</td></tr><tr><td>③</td><td>.565</td><td>.597</td><td>.642</td><td>.708</td><td>.828</td></tr><tr><td>4</td><td>.494</td><td>.525</td><td>.564</td><td>.624</td><td>.733</td></tr><tr><td>5</td><td>.446</td><td>.474</td><td>.510</td><td>.565</td><td>.669</td></tr><tr><td></td><td>.410</td><td>.436</td><td>.470</td><td>.521</td><td>.618</td></tr><tr><td>7</td><td>.381</td><td>.405</td><td>.438</td><td>.486</td><td>.577</td></tr><tr><td>8</td><td>.358</td><td>.381</td><td>.411</td><td>.457</td><td>.543</td></tr><tr><td>9</td><td>.339</td><td>.360</td><td>.388</td><td>.432</td><td>.514</td></tr><tr><td>10</td><td>.322</td><td>.342</td><td>.368</td><td>.410</td><td>.490</td></tr><tr><td>11</td><td>.307</td><td>.326</td><td>.352</td><td>.391</td><td>.468</td></tr><tr><td>12</td><td>.205</td><td>.313</td><td>.338</td><td>.375</td><td>.450</td></tr><tr><td>13</td><td>.284</td><td>.302</td><td>.325</td><td>.361</td><td>.433</td></tr><tr><td>14</td><td>.274</td><td>.292</td><td>.314</td><td>.349</td><td>.418</td></tr><tr><td>15</td><td>.266</td><td>.283</td><td>.304</td><td>.338</td><td>.404</td></tr><tr><td>16</td><td>.258</td><td>.274</td><td>.295</td><td>.328</td><td>.392</td></tr><tr><td>17</td><td>.250</td><td>.266</td><td>.286</td><td>.318</td><td>.381</td></tr><tr><td>18</td><td>.244</td><td>.259</td><td>.278</td><td>.309</td><td>.371</td></tr><tr><td>19</td><td>.237</td><td>.252</td><td>.272</td><td>.301</td><td>.363</td></tr><tr><td>20</td><td>.231</td><td>.246</td><td>.264</td><td>.294</td><td>.356</td></tr><tr><td>25</td><td>.210</td><td>.220</td><td>.240</td><td>.270</td><td>.320</td></tr><tr><td>30</td><td>.190</td><td>.200</td><td>.220</td><td>.240</td><td>.290</td></tr><tr><td>35</td><td>.180</td><td>.190</td><td>.210</td><td>.230</td><td>.270</td></tr><tr><td>MAS DE 35</td><td>1.07 N</td><td>1.14</td><td>1.22 N</td><td>1.36 N</td><td>1.63 N</td></tr></table></body></html>

A continuacion el siguiente ejemplo ilustra la prueba.

Se desea comprobar que el punto de ebullicion de un compuesto de silicio (en grados Celsius) proviene de una poblacion normal con $\mu = 1 6 0$ grados Celsius y $\sigma = 1 0$ grados Celsius.

166 141 136 154 170 162 155 146 183 157 148 132 160 175 150

1- Hipotesis

H0 : $\mathrm { F ( x ) } = \int _ { - \infty } ^ { \mathrm { x } } \mathrm { d n o r m ( t , 1 6 0 , 1 0 ) d t }$ H1 : Los puntos de ebullcion del compuesto de silicio no siguen una distribucion normal

2- Nivel de significacion

3- Criterio Ingresando en la tabla con α y el tamano muestral $\mathrm { D } _ { \alpha } \mathrm { : = } 0 . 3 3 8$ Diferencia absoluta maxima admisible

4- Calculos

Construimos ambas distribuciones acumuladas (observada y esperada)

$\mathbf { n } : = 1 5 \qquad \quad \mathbf { i } : = 0 \ldots \mathbf { n } - 1$   
${ \operatorname k } _ { \mathord { \cdot } \mathord { : } \mathrm { = } } 0 _ { \mathord { \cdot } \mathrm { . } \mathrm { n } }$   
raw 166 141 136 154 170 162 155 146 183 157 148 132 160 175 150 ( ) T

$\mathrm { I _ { k } : = \operatorname* { m i n } ( r a w ) + \frac { \ m a x ( r a w ) - \ m i n ( r a w ) } { n } \cdot k }$ Intervalos del histograma

$$
\operatorname { H } _ { \mathsf { W } } : = { \frac { \operatorname { h i s t } ( \operatorname { I } , \operatorname { s o r t } ( \operatorname { r a w } ) ) } { \operatorname { r o w s } ( \operatorname { r a w } ) } }
$$

Histograma normalizado

Oi  H  j Funcion acumuladade valores empiricos $\mathrm { E _ { i } } { : = \ p n o r m \Big ( I _ { i } , 1 6 0 , 1 0 \Big ) }$ Funcion acumuladade valores teoricos 0j  t 120 120.1   190

![](images/680be6a0b4f1e6ee2a097fccef8efe69120d68d4d503f328baf5d25619b9cf6a.jpg)

# Calculamos el vector de diferencias absolutas entre Observados y Teoricos

$$
\mathrm { d _ { i } } \mathrm { : = \left| { O _ { i } } - { E _ { i } } \right| }
$$

Estadistico D para prueba de D max d  ( ) 0.31  Kolmogorov-Smirnov

<html><body><table><tr><td rowspan="15"></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td>0</td><td></td><td>0</td><td></td><td></td></tr><tr><td>0</td><td>0.067</td><td>0</td><td>2.555:10-3</td><td>0</td><td>0.064</td></tr><tr><td>1 2</td><td>0.133 0.2</td><td>1 2</td><td>6.947-10-3</td><td>1</td><td>0.126</td></tr><tr><td>3</td><td>0.2</td><td>3</td><td>0.017 0.038</td><td>2 3</td><td>0.183 0.162</td></tr><tr><td></td><td>0.333</td><td>4</td><td>0.075</td><td>4</td><td>0.258</td></tr><tr><td>4 5</td><td>0.4</td><td>E=</td><td>0.136</td><td>5</td><td>0.264</td></tr><tr><td>6</td><td>0.533</td><td>5 6</td><td>0.224</td><td></td><td>0.31</td></tr><tr><td>0= 7</td><td>0.6</td><td>7</td><td>0.337</td><td>6</td><td>0.263</td></tr><tr><td>8</td><td>0.733</td><td>8</td><td>0.468</td><td>7 8</td><td>0.265</td></tr><tr><td>9</td><td>0.733</td><td>9</td><td>0.603</td><td>9</td><td>0.131</td></tr><tr><td>10</td><td>0.8</td><td>10</td><td>0.726</td><td></td><td>0.074</td></tr><tr><td>11</td><td>0.867</td><td>11</td><td>0.826</td><td>10 11</td><td>0.04</td></tr><tr><td>12</td><td>0.933</td><td>12</td><td>0.9</td><td>12</td><td>0.034</td></tr><tr><td>13</td><td>0.933</td><td>13</td><td>0.947</td><td>13</td><td>0.014</td></tr><tr><td>14</td><td>1</td><td>14</td><td>0.975</td><td>14</td><td>0.025</td></tr></table></body></html>

# 5- Conclusion

Dado que $\mathsf { D } = 0 . 3 1 < \mathsf { D } _ { \mathtt { d } } = 0 . 3 3 8$ , se falla en rechazar la $\mathsf { H O }$ . Por lo tanto, la distribucion de los puntos de ebullicion del compuesto de silicio se ajustan satisfactoriamente a la distribucion normal N $| ( { \mu } = 1 6 0 , \sigma = 1 0 )$

UNIDAD V AJUSTE DE CURVAS

# UNIDAD V

# INTRODUCCION

Uno de los principales objetivos de muchas invesitgaciones estadisticas es el de realizar predicciones, basadas en algun metodo cientifico, preferentemente. Por ejemplo:

Predecir la performance de un procesador en determinada tarea dado su numero de nucleos y frecuencia de operacion...

Predecir el numero de individuos de una poblacion pasado un cierto tiempo...

Predecir el numero de kilometros para desgastar un neumatico en funcion de su grosor y composicion...

Por lo general este tipo de problemas que buscan realizar predicciones se basan en valores conocidos de variables dependientes e independientes. Segun la complejidad del modelo, se pueden incluir una o varias variables independientes, que es lo que conocemos como regresion simple o multiple.

En otras ocasiones el objetivo de analisis, previo a poder predecir el valor de alguna variables, sera el de determinar si existe alguna asociacion o correlacion entre las variables cuantitativas a estudiar.

# METODO DE LOS MINIMOS CUADRADOS

Para desarrollar como modelizar una relacion entre variables, primero se recurre al caso mas sencillo de regresion, el cual modela el comportamiento de una variable explicada o de respuesta y, en funcion de otra x, llamada independiente, explicativa o predictora. Ademas, se limita al caso donde la relacion que existe entre la variables es de tipo lineal.

Partiendo de una muestra de n pares ordenados $( \mathsf { x } _ { \mathrm { i } } , \mathsf { y } _ { \mathrm { i } } ) \mathsf { c o n i } = 1 , . . . , \mathsf { r }$ . Los cuales pueden ser dispuestos en un diagrama de dispersion como el siguiente.

$$
\begin{array} { l l } { { \mathtt { n } : = 2 0 \qquad } } & { { \mathtt { i } : = 0 \ldots \mathtt { n } - 1 } } \\ { { \alpha : = 3 \qquad } } & { { \beta : = 2 } } \end{array}
$$

$$
\mathrm { x _ { i } : = 0 . 5 { \cdot } i \qquad \quad \mathrm { y _ { i } : = \alpha + \beta \beta \cdot \mathrm { x _ { i } + \ r n o r m ( 1 , 0 , 1 ) } _ { 0 } } }
$$

![](images/778c07c8f048d77a65945cbe6bc9338092d0b1be7dce855b2d6a15cc10b1a6b0.jpg)

Con estas condiciones, el problema se remite a encontrar la ecuacion de la recta $a + \beta x$ que mejor se ajuste al conjunto de datos. Tradicionalmente se recurre al metodo de los minimos cuadrados, que elige como recta de regresion aquella que minimiza las alturas verticales de los valores observados $\mathsf { y } _ { \mathrm { i } }$ a la recta.

Por empezar, vemos que (en general), todos los yi van a diferir de la recta de regresion (por ahora desconocida) $\tt { q } + \beta \tt { x }$ en algun $\mathfrak { E } _ { \mathrm { i } }$ . Con esto, decimos que ε es una variable aleatoria.

$$
\mathrm { y _ { i } = \alpha + \beta _ { i } \mathrm { x _ { i } + \varepsilon _ { i } } }
$$

El valor de ε para la i-esima observacion dependera de:

· Errores de medicion · Influencia de otras variables despreciadas

![](images/09512d3481a72be2a3820ef712dc66d5593b4d10c3abac30ff1d916c7968773b.jpg)  
Recta de regresion con errores entre prediccion y observacion

A continuacion, es razonable pensar que al determinar a y b, se quiere minimizar todos los $\mathfrak { E } _ { \mathrm { i } }$ de forma simultanea. Por lo tanto, con este fin, se opta por minimizar la sumatoria de todos ellos.

$$
\sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \ \varepsilon _ { \mathrm { i } }
$$

Sin embargo, un forma tan "directa" no es aconsejable, dado que los errores son positivos y negativos (dado que hay puntos por arriba y por debajo de la recta), por lo tanto se compensarian entre si, lo cual deriva en una respuesta inadecuada. Con esto, una estrategia seria eliminar el signo del error, lo cual se puede lograr elevando al cuadrado (valor absoluto tambien lo permite) cada uno de los errores $\mathfrak { E } _ { \mathrm { i } }$ .

$$
\sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } { \left( \varepsilon _ { \mathrm { i } } \right) } ^ { 2 }
$$

Se sabe que:

$$
\varepsilon _ { \mathrm { i } } = \mathrm { y } _ { \mathrm { i } } - \left( \mathrm { a } + \mathrm { b } { \cdot } \mathrm { x } _ { \mathrm { i } } \right)
$$

Los errores son las distancias verticales de los puntos respecto a la recta

Reemplazando en la sumatoria:

$$
\sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left( \varepsilon _ { \mathrm { i } } \right) ^ { 2 } = \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \mathrm { y } _ { \mathrm { i } } - \left( \mathrm { a } + \mathrm { b } { \cdot } \mathrm { x } _ { \mathrm { i } } \right) \right] ^ { 2 }
$$

Con esto, decimos que lo que se busca minimizar es la suma de las distancias verticales desde los puntos hacia la recta, este es el metodo conocido como Minimos Cuadrados. Ahora, si pensamos a esta sumatoria como una funcion, la condicion para que exista un minimo es que las derivadas parciales de sus variables (en este caso a y b) se anulen.

$$
{ \frac { \mathrm { d } } { \mathrm { d } { \mathrm { a } } } } \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \mathrm { y } _ { \mathrm { i } } - \left( \mathrm { a } + \mathrm { b } { \cdot } \mathrm { x } _ { \mathrm { i } } \right) \right] ^ { 2 } = 2 { \cdot } \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \left( \mathrm { y } _ { \mathrm { i } } - \mathrm { a } - \mathrm { b } { \cdot } \mathrm { x } _ { \mathrm { i } } \right) { \cdot } ( - 1 ) \right] = 0
$$

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left( \mathrm { y } _ { \mathrm { i } } - \mathrm { a } - \mathrm { b } { \cdot } \mathrm { x } _ { \mathrm { i } } \right) = 0
$$

Distribuyendo la sumatoria a cada uno de los terminos:

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } { \mathrm {  ~ \scriptstyle { y } _ { \mathrm { i } } - \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } { \mathrm {  ~ \scriptstyle { a - \sum _ { i = 1 } ^ { \mathrm { n } } ~ } } } } } \left( { \mathrm {  ~ \not { b \cdot } { \mathrm { x } _ { \mathrm { i } } } } } \right) = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } { \mathrm {  ~ \scriptstyle { y } _ { \mathrm { i } } - a \cdot { \mathrm { n - b } } \mathrm {  ~ \scriptstyle { \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } ~ } } } } { \mathrm {  ~ \scriptstyle { x } _ { \mathrm { i } } = 0 ~ } }
$$

Dejando las incognitas de un lado:

$$
\sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } { \mathrm { y } _ { \mathrm { i } } } = \mathrm { a } \cdot \mathrm { n } + \mathrm { b } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } { \mathrm { ? } }
$$

Siguiendo un procedimiento similar para la derivada parcial de b:

$$
\frac { \mathrm { d } } { \mathrm { d } \mathrm { b } } \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left[ \mathrm { y } _ { \mathrm { i } } - \left( \mathrm { a + b } \cdot \mathrm { x } _ { \mathrm { i } } \right) \right] ^ { 2 } = 2 \cdot \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left[ \left( \mathrm { y } _ { \mathrm { i } } - \mathrm { a } - \mathrm { b } \cdot \mathrm { x } _ { \mathrm { i } } \right) \cdot \left( - \mathrm { x } _ { \mathrm { i } } \right) \right] = 0
$$

$$
\sum _ { i = 1 } ^ { n } \ \left( \mathrm { y _ { i } { \cdot } x _ { i } } \right) = \mathrm { a } { \cdot } \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \mathrm { x _ { i } } + \mathrm { b } { \cdot } \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left( \mathrm { x _ { i } } \right) ^ { 2 }
$$

De esta forma se obtiene un sistema de ecuaciones de $^ { 2 \times 2 }$ , el cual recibe el nombre especial de Sistema de Ecuaciones Normales. Y resolviendo este sistema, hallaremos los valores de a y b que minimizan la sumatoria de cuadrados, y por lo tanto hallaremos la recta que mejor se ajusta al conjunto de datos, desde el punto de vista de los minimos cuadrados

$$
\left[ \begin{array} { l l l } & { \displaystyle \sum _ { \mathrm { ~ i ~ = ~ 1 ~ } } ^ { \mathrm { ~ n ~ } } \mathrm { ~ x _ { i } ~ } } \\ & { \displaystyle \sum _ { \mathrm { ~ i ~ = ~ 1 ~ } } ^ { \mathrm { ~ n ~ } } \mathrm { ~ x _ { i } ~ } } \\ & { \displaystyle \sum _ { \mathrm { ~ i ~ = ~ 1 ~ } } ^ { \mathrm { ~ n ~ } } \mathrm { ~ x _ { i } ~ } \sum _ { \mathrm { ~ i ~ = ~ 1 ~ } } ^ { \mathrm { ~ n ~ } } \left( \mathrm { x _ { i } } \right) ^ { 2 } } \end{array} \right] \left( \begin{array} { l } { \displaystyle { \mathrm { a } } } \\ { \displaystyle { \mathrm { b } } } \\ { \displaystyle { \mathrm { b } } } \end{array} \right) = \left[ \begin{array} { l } { \displaystyle { \mathrm { ~ n ~ } } } \\ { \displaystyle { \sum _ { \mathrm { ~ i ~ = ~ 1 ~ } } ^ { \mathrm { ~ n ~ } } \mathrm { y _ { i } ~ } } } \\ { \displaystyle { \mathrm { ~ i ~ = ~ 1 ~ } } } \\ { \displaystyle { \mathrm { ~ n ~ } } } \\ { \displaystyle { \sum _ { \mathrm { ~ i ~ = ~ 1 ~ } } ^ { \mathrm { ~ n ~ } } \left( \mathrm { y _ { i } } \cdot \mathrm { x _ { i } } \right) } } \end{array} \right]
$$

Sistema de Ecuaciones Normales - Forma matricial

Algo que se debe destacar, es que la recta es la que mejor se ajusta al conjunto de datos dado, en consecuencia, puede no ser (y generalmente no lo es) la que mejor se ajuste a la poblacion. Viendo en el ejemplo del comienzo:

$$
\mathbf { \Sigma } _ { \times \times } ^ { \mathbf { S } } : = \left[ \begin{array} { l } { \mathbf { n } \cdot \sum _ { \mathbf { i } = 0 } ^ { \mathbf { n } - 1 } \mathbf { \Sigma } _ { \mathbf { i } } } \\ { \mathbf { \Sigma } _ { \mathbf { i } = 0 } ^ { \mathbf { n } } } \end{array} \right] ^ { - 1 } \left[ \begin{array} { l } { \mathbf { n } - 1 } \\ { \displaystyle \sum _ { \mathbf { i } = 0 } ^ { \mathbf { n } - 1 } \mathbf { \Sigma } _ { \mathbf { j } _ { \mathbf { i } } } } \\ { \displaystyle \sum _ { \mathbf { i } = 0 } ^ { \mathbf { n } - 1 } \left( \mathbf { \Sigma } _ { \mathbf { i } } \cdot \mathbf { N } _ { \mathbf { i } } \right) } \\ { \displaystyle \sum _ { \mathbf { i } = 0 } ^ { \mathbf { n } - 1 } \left( \mathbf { \Sigma } _ { \mathbf { i } } \cdot \mathbf { N } _ { \mathbf { i } } \right) } \end{array} \right] = \left( \begin{array} { l } { 2 . 7 7 2 } \\ { 2 . 0 5 7 } \end{array} \right)
$$

$$
{ \begin{array} { r l r l } & { \mathbf { a } : = \mathbf { S } _ { 0 } = 2 . 7 7 2 } & & { \qquad \mathbf { b } : = \mathbf { S } _ { 1 } = 2 . 0 5 7 } \\ & { } & & { } \\ & { { \mathrm { i n t e r c e p t } } ( \mathbf { x } , \mathbf { y } ) = 2 . 7 7 2 } & & { \qquad { \mathrm { s l o p e } } ( \mathbf { x } , \mathbf { y } ) = 2 . 0 5 7 } \\ & { } & & { } \\ & { \qquad \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { = } 3 } & & { \qquad \mathbf { \beta } \mathbf { = } 2 } \end{array} }
$$

![](images/d8612e7f0dd74335617f53ab6e74dd065a28c8f7a48aef6b278062b783382f7a.jpg)

Nota: Aca vemos como lo que obtenemos despues de la estimacion no son los parametros originales α y β sino unos valores que los estiman, que son a y b. Para otra muestra se obtendra otra estimacion de α y β.

# INFERENCIAS BASADAS EN MINIMOS CUADRADOS

El metodo de los minimos cuadrados desarrollado anteriormente ( caso lineal) se usa para modelar la relacion lineal que existe entre la variable explicativa x y una variable aleatoria Y. En lo siguiente se supondra que la regresion es lineal y que para los n pares ordenados, cada una de la $\mathsf { Y } _ { \mathrm { i } }$ son variables aleatorias independientes entre si, que estan distribuidas normalmente con media ${ \tt G } + \beta$ x y varianza comun $\sigma ^ { 2 }$ . Entonces, de aca deriva que la i-esima observacion de la variable aleatoria Y, osea, $\mathsf { Y } _ { \mathrm { i } }$ puede describirse como:

$$
\mathrm { Y _ { i } } = \alpha + \beta { \cdot } \mathrm { x _ { i } } + \varepsilon _ { \mathrm { i } }
$$

Donde decimos que $\mathfrak { E } _ { \mathrm { i } }$ son variables aleatorias independientes, con distribucion normal, media $\mu _ { \varepsilon } = 0$ y varianza $\sigma _ { \varepsilon } ^ { 2 } = \sigma ^ { 2 }$

![](images/0ddb26564db7875a9a032d23cd8c6f41930eb9af1c461e74d905c7ce2fff39e2.jpg)

Diagrama que muestra la distribucion normal de cada Yi alrededor de una media $\alpha + \beta x _ { p }$ una varianza

A continuacion, resulta util a futuro el establecer ciertos valores "resumen" o notaciones especiales que resultan convenientes en ciertos calculos:

$$
\mathrm { S _ { _ { X X } } = n { \cdot } \sum _ { i = 1 } ^ { n } \binom { x _ { i } } { i } ^ { 2 } - \left( \sum _ { i = 1 } ^ { n } \mathrm { x _ { i } } \right) ^ { 2 } = n { \cdot } \binom { s } { x } ^ { 2 } { \cdot } ( n - 1 ) }
$$

$$
\mathrm { \bf S _ { y y } = n \cdot \sum _ { i = 1 } ^ { n } \Delta \left( y _ { i } \right) ^ { 2 } - \left( \sum _ { i = 1 } ^ { n } y _ { i } \right) ^ { 2 } = n \cdot \left( s _ { y } \right) ^ { 2 } \cdot ( n - 1 ) \quad }
$$

$$
\mathrm { \bf S _ { \mathrm { _ { x y } } } = \mathrm { n \cdot \sum _ { i = 1 } ^ { n } \partial \left( \mathrm { x _ { i } \cdot \mathrm { y _ { i } } } \right) - \sum _ { i = 1 } ^ { n } \partial \mathrm { \bf \Sigma _ { i } \cdot \sum _ { i = 1 } ^ { n } \mathrm { y _ { i } = \mathrm { n \cdot \mathrm { s _ { _ { x y } \cdot ( n - 1 ) } } } } } } }
$$

Por empezar, el calculo de los coeficientes a y b queda:

$$
\begin{array} { r } { \mathbf { b } = \frac { \mathbf { S } } { \mathbf { S } } \qquad \mathbf { a } = \mathbf { m e a n } ( \mathbf { y } ) - \mathbf { m e a n } ( \mathbf { x } ) \cdot \mathbf { b } } \end{array}
$$

Es conveniente resaltar la estrecha relacion que existe entre $\mathsf { S } _ { \mathsf { x } } \mathsf { y } \mathsf { S } _ { \mathsf { y } }$ con las respectivas varianzas muestrales de cada una $\mathsf { s } _ { \mathsf { x } } \mathsf { y } \mathsf { s } _ { \mathsf { y } }$

Entrando en la parte de estimacion, la varianza comun $\sigma ^ { 2 }$ , mencionada anteriormente, puede calcularse en termino de las desviaciones verticales de los puntos dato o muestrales desde la linea de prediccion. Siendo la i-esima desviacion:

$$
\mathsf { y } _ { \mathrm { i } } - \mathbf { a } - \mathbf { b } { \cdot } \mathbf { x } _ { \mathrm { i } }
$$

Calculando la suma de las desviaciones y dividiendo por n - 2, se obtiene:

$$
\mathrm { \left( s _ { e } \right) ^ { 2 } = \frac { 1 } { n - 2 } { \cdot } \sum _ { i = 1 } ^ { n } \ \left( y _ { i } - a - b { \cdot } x _ { i } \right) ^ { 2 } }
$$

Donde ${ \mathfrak { s } } _ { \mathfrak { e } }$ se conoce como Error Estandar de Estimacion. Tambien, $\ S _ { \theta } { } ^ { 2 } ( \mathsf { n } - 2 )$ es conocida como Suma de cuadrados Residual o Suma de cuadrados de Error. Usando las expresiones equivalentes obtenemos la siguiente expresion:

$$
\mathrm { \left( s _ { e } \right) ^ { 2 } = \frac { s _ { x x } { \cdot S _ { y y } - \left( s _ { x y } \right) ^ { 2 } } } { \ n \cdot ( n - 2 ) \cdot S _ { x x } } }
$$

Estimacion de $\mathfrak { O } ^ { 2 }$

El divisor n - 2 se utiliza para que el estimador resultante de $\sigma ^ { 2 }$ sea insesgado.

En base a los supuestos realizados (normalidad, varianzas comunes, etc.), se pueden probar los siguientes teoremas:

Estadisticos para inferencias acerca de α y β

Donde ambas t son variables aleatorias que tienen distribucion t-Student con n - 2 grados de libertad.

Comenzando con las inferencias, gracias al estadistico del teorema anterior, podemos plantear los siguiente intervalos de confianza para los parametros α y β:

$$
\mathbf { a } - \mathbf { t } _ { \frac { \mathbf { \alpha } } { 2 } } \mathbf { \alpha } _ { \mathbf { e } } \cdot \mathbf { s } _ { \mathbf { e } } \cdot { \sqrt { \frac { 1 } { \mathfrak { n } } + \frac { \mathrm { m e a n } \left( \mathbf { x } \right) ^ { 2 } } { \mathbf { S } _ { \mathbf { x x } } } } } < \mathbf { \alpha } \propto \mathbf { a } + \mathbf { t } _ { \frac { \mathbf { \alpha } } { 2 } } \mathbf { \alpha } _ { \mathbf { e } } \cdot \mathbf { s } _ { \mathbf { e } } \cdot { \sqrt { \frac { 1 } { \mathfrak { n } } + \frac { \mathrm { m e a n } \left( \mathbf { x } \right) ^ { 2 } } { \mathbf { S } _ { \mathbf { x x } } } } }
$$

$$
\mathbf { b } - \mathbf { t } _ { \underline { { \alpha } } } \cdot \mathbf { s } _ { \mathrm { e } } \cdot \frac { 1 } { \sqrt { \mathrm { S } _ { \mathrm { x x } } } } < \beta < \mathbf { b } + \mathbf { t } _ { \underline { { \alpha } } } \cdot \mathbf { s } _ { \mathrm { e } } \cdot \frac { 1 } { \sqrt { \mathrm { S } _ { \mathrm { x x } } } }
$$

Siguiendo con el ejemplo del comienzo:

$$
\begin{array} { l } { \displaystyle \underset { \mathrm { \tiny { W } } } { \mathrm { \tiny { \alpha } } } : = 0 . 0 5 \qquad \nu : = { \mathrm { \tiny { ~ n ~ - ~ } } } 2 = 1 8 \qquad \displaystyle \mathrm { \tiny { t _ { \alpha } : = ~ } } { \mathrm { \tiny { q r } } } \left( 1 - \frac { \alpha } { 2 } , { \nu } \right) = 2 . 1 0 1 } \\ { \displaystyle \mathrm { \tiny { s _ { e } } } : = \frac { 1 } { { \mathrm { \tiny { ~ n ~ - ~ } } } 2 } \cdot \sum _ { \mathrm { \tiny { i = ~ } } 0 } ^ { { \mathrm { \tiny { n - 1 } } } } \left( \mathrm { y _ { i } } ^ { \mathrm { \tiny { ~ - ~ a ~ - ~ b } \cdot } } \mathrm { x _ { i } } \right) ^ { 2 } = 0 . 8 5 8 } \end{array}
$$

$$
{ \mathrm { E } } _ { \alpha } { : = } \mathrm { t } _ { \alpha } { \cdot } \mathrm { s } _ { \mathrm { e } } \cdot \sqrt { \frac { 1 } { \alpha } + \frac { \mathrm { m e a n } ( \alpha ) ^ { 2 } } { \mathrm { S } _ { \mathrm { x x } } } } = 0 . 4 3
$$

$$
\mathrm { E _ { \beta } : = t _ { \alpha } { \cdot } s _ { e } { \cdot } } \frac { 1 } { \sqrt { \mathrm { S _ { x x } } } } = 0 . 0 3 1
$$

$\begin{array} { l l } { \mathbf { a } - \mathbf { E } _ { \mathbf { \Phi } } = 2 . 3 4 2 } & { \qquad \mathbf { a } + \mathrm { E } _ { \mathbf { \Phi } } = 3 . 2 0 2 } \\ { \mathbf { b } - \mathrm { E } _ { \mathbf { \Phi } } = 2 . 0 2 5 } & { \qquad \mathbf { b } + \mathrm { E } _ { \mathbf { \Phi } } = 2 . 0 8 8 } \end{array}$ Intervalo para Intervalo para α $\beta$

Siguiendo con la parte inferencial, tenemos las pruebas de hipotesis donde las relacionadas con $\beta$ son de fundamental importancia, ya que este parametro indica el cambio promedio de la variable y con respecto a un incremento unitario de la variable x. Ya que si $\beta = 0$ , la linea de regresion es horizontal, y por tanto, la media de las y no depende linealmente de $\mathsf { x } .$

A modo de ejemplo, probamos la hipotesis nula $\mathsf { H 0 }$ , de que $\beta = 0$ contra la alternativa de que sea $\beta ! = 0$ , con una significacion de $\mathtt { q } = 0 . 0 5$ .

1- Hipotesis $\begin{array} { c } { { \mathsf { H } 0 : \beta = 0 } } \\ { { \mathsf { H } 1 : \beta : = 0 } } \end{array}$

2- Significacion

$$
\underset { N } { \underbrace { \mathrm { a } } } _ { i } \mathrm { = } \ 0 . 0 5
$$

3- Criterio

$$
\begin{array} { l } { \displaystyle \underset { \ r { \mathsf { M } } } { \nu } : = \mathsf { n } - 2 = 1 8 } \\ { \displaystyle } \\ { \displaystyle \mathfrak { t } _ { 0 0 2 5 } : = \mathfrak { q t } \Bigg ( 1 - \frac { \alpha } { 2 } , \nu \Bigg ) = 2 . 1 0 1 } \end{array}
$$

4- Calculos

$$
\mathrm { \Delta t = \frac { b - \beta } { s _ { e } } \cdot \sqrt { s _ { \mathrm { x x } } } }
$$

Por hipotesis $\beta = 0$ , entonces:

$$
\mathrm { \Delta t : = \frac { b - 0 } { s _ { e } } \cdot \sqrt { S _ { x x } } = 1 3 8 . 2 0 7 }
$$

w 4:= - , -3.99.. 4

![](images/8aa1653492c39d8765d19cf4810c4ea536ef8cc8f5cd70163faf0de8fa3ba4d1.jpg)

5- Conclusion

Dado que $\mathfrak { t } = 1 2 9 . 4 9 3 > \mathfrak { t } _ { 0 0 2 5 } = 2 . 1 0 1$ , se rechaza $\mathsf { H O }$ de que $\beta = 0$ . Por lo tanto, se dice que $\beta$ es significativamente distinto de 0.

A continuacion, se plantea el problema de estimar ${ \mathsf { a } } + { \mathsf { \beta } } \mathbf { \mathsf { x } }$ , es decir, la media $\mu _ { \gamma }$ de la distribucion de y para un x determinado.

Si x se matinene fijo, es decir, $\mathsf { x } = \mathsf { x } _ { 0 }$ . El problema se reduce a estimar $\mathsf { a } + \mathsf { \beta } \mathsf { x } _ { 0 }$ , para lo cual, seria razonable usar las estimaciones a y b de α y $\beta$ , obtenidas por minimos cuadrados. Puede verificarse que este estimador es insesgado con varianza:

$$
\sigma ^ { 2 } . \left[ \frac { 1 } { \mathrm { ~ n ~ } } + \mathrm { n } . \frac { \left( \mathrm { x } _ { 0 } - \mathrm { m e a n ( x ) } \right) ^ { 2 } } { \mathrm { S } _ { \mathrm { x x } } } \right]
$$

y que los limites de confianza del $( 1 - \mathsf { a } ) 1 0 0 \%$ para $\mathsf { q } + \mathsf { \beta } \mathsf { x } _ { 0 }$ estan dados por la siguiente expresion:

$$
\mathbf { a } + \mathbf { b } \cdot \mathbf { x } _ { 0 } \mathbf { ) } - \mathbf { t } _ { \underline { { \alpha } } } \cdot \mathbf { s } _ { \mathrm { c } } \cdot \left[ \frac { 1 } { \mathrm { n } } + \frac { \mathbf { n } \cdot \left( \mathbf { x } _ { 0 } - \mathrm { m e a n } ( \mathbf { x } ) \right) ^ { 2 } } { \mathbf { S } _ { \mathbf { x } \mathbf { x } } } < \mathbf { \alpha } \propto \mathbf { \beta } \cdot \mathbf { x } _ { 0 } < \left( \mathbf { a } + \mathbf { b } \cdot \mathbf { x } _ { 0 } \right) + \mathbf { t } _ { \underline { { \alpha } } } \cdot \mathbf { s } _ { \mathrm { c } } \cdot \left[ \frac { 1 } { \mathrm { n } } + \frac { \mathbf { n } \cdot \left( \mathbf { x } _ { 0 } - \mathrm { m e a n } ( \mathbf { x } ) \right) ^ { 2 } } { \mathbf { S } _ { \mathbf { x } \mathbf { x } } } \right] \right] .
$$

"En otras palabras, la banda por la que puede pasar la recta de prediccion."

De mayor importancia, es la prediccion de una valor futuro de y cuando $\mathsf { x } = \mathsf { x } _ { 0 }$ donde $\mathsf { x } _ { 0 }$ se encuentra dentro del rango de experimentacion.

A continuacion se describe el metodo para obtener un intervalo en el cual puede esperarse que "caiga" una futura observacion de y con una probabilidad (o confianza) determinada.

Si se conociera α y $\beta$ se podria usar el hecho de que Y es una variable aleatoria que sigue una distribucion normal con media $\mathsf { q } + \mathsf { \beta } \mathsf { x }$ y varianza $\sigma ^ { 2 }$ (o que ε sigue una distribucion normal con media 0 y varianza $\mathfrak { O } ^ { 2 }$ ).

Sin embargo, se desconocen los parametros α y $\beta$ por lo que es razonable usar sus estimaciones, para considerar la cantidad $\mathsf { Y } - a - \mathsf { b x } _ { 0 }$ , donde Y, a y b son variables

aleatorias y a la teoria resultante conduce a los limites de prediccion para un valor futuro que se observe de Y, para $\mathbf { x } = \mathbf { x } _ { 0 }$ .

$$
( a + b x _ { 0 } ) \pm t _ { \alpha / 2 } \cdot s _ { e } \sqrt { 1 + \frac { 1 } { n } + \frac { ( x _ { 0 } - \overline { { x } } ) ^ { 2 } } { S _ { x x } } }
$$

donde el numero de grados de libertad para tα/2 esn-2.

# REGRESION CURVILINEA

Hasta ahora se abordo el caso lineal, sin mebargo, para ampliar el modelo se considerara el caso en el que la curva de regresion NO es lineal, pero mediante transformaciones matematicas se puede conseguir aplicar los mismo metodos que para el caso lineal. Con esto decimos que si "enderezamos" los datos, podemos conseguir un modelo lineal si los ejes estan escalados adecuadamente.

# Caso exponencial:

$$
\mathbf { y } = \mathbf { \alpha } _ { \alpha \cdot \beta } ^ { \mathbf { X } }
$$

Tomando logaritmo a ambos miembros:

$$
\mathrm { l o g ( y ) = l o g ( \alpha \alpha ) + x { \cdot } l o g ( \beta ) }
$$

Con lo cual ahora se pueden obtener por el mismo metodo (caso lineal) log(α) y log(β), para luego obtener α y $\beta$ respectivamente, aplicando el metodo de los minimos cuadrados a los n pares $( \mathbf { \lambda x } _ { \mathrm { i } } , \mathsf { l o o } ( \mathsf { y } _ { \mathrm { i } } )$ ).

$$
\mathbf { x } : = { \left( \mathrm { 1 } \ \mathrm { 2 } \ \mathrm { 5 } \ \mathrm { 1 0 } \ \mathrm { 2 0 } \ \mathrm { 3 0 } \ \mathrm { 4 0 } \ \mathrm { 5 0 } \right) } ^ { \mathrm { T } } \quad \mathbf { y } : = \left( 9 8 . 2 \ 9 1 . 7 \ 8 1 . 3 \ 6 4 . 0 \ 3 6 . 4 \ 3 2 . 6 \ 1 7 . 1 \ 1 1 . 3 \right) ^ { \mathrm { T } }
$$

![](images/e190fa9d188c770d9b60bb710c9c27b41f32c68ec3142e495a68f87337c129ec.jpg)

$$
\begin{array} { r } { \mathrm { y m o d } : = \mathrm { l o g } ( \mathrm { y } ) \qquad \underset { \mathbb { A } \times \mathrm { w } } { \mathrm { a } } : = 1 0 ^ { \mathrm { i n t e r c e p t } ( \mathrm { x } , \mathrm { y m o d } ) } = 9 9 . 9 4 1 \qquad \underset { \mathbb { M } \times \mathrm { w } } { \mathrm { b } } : = 1 0 ^ { \mathrm { s l o p e } ( \mathrm { x } , \mathrm { y m o d } ) } = 0 . 9 5 8 \mathrm { a m } ^ { - \mathrm { p t r a m } } , } \end{array}
$$

w 0 0.1 := , .. 50

![](images/30a2339d784e355f73595a8872745ae74c12206a9ef6aa16952d4ea18b6dff66.jpg)

# Caso potencial:

$$
\mathrm { y } = \mathrm { \alpha } \mathrm { \alpha } \mathrm { \cdot } \mathrm { x } ^ { \beta }
$$

Tomando logaritmo a ambos miembros:

$$
\mathrm { l o g ( y ) } = \mathrm { l o g ( \alpha ) } + \mathrm { l o g ( \alpha ) } \cdot \beta
$$

En este caso, si dispusieramos los datos sobre un papel doble logaritmico (ambos ejes en escala logaritmica), conseguiriamos una forma de recta.

Al aplicar el metodo a los pares modificados $[ \log ( x _ { \mathrm { i } } ) , \log ( y _ { \mathrm { i } } )$ ), obtenemos las estimaciones de log(α) y β, de los cuales podemos conocer α y $\beta$ respectivamente.

![](images/7e0e2515e3fd42afc8f881391ae57c6b56de6c8fea4d4627791db053ea9cd0e7.jpg)

$$
\underset {  } { \underline { { \mathrm { a } } } } : = 1 0 ^ { \mathrm { i n t e r c e p t ( x m o d , y m o d ) } } = 6 . 7 4 3
$$

$$
\mathsf { \Pi } _ { \mathsf { m } } ^ { \mathsf { b } } : = \mathsf { s l o p e } ( \mathrm { x m o d } , \mathrm { y m o d } ) = 2 . 3 3 8
$$

w 0 0.01 := , .. 7

![](images/c8871ea754e76c0c77465efc926b647e3db79ce4125cb028b436d084f8b85c6e.jpg)

# Caso reciproco:

$$
\mathrm { y = \frac { 1 } { \alpha + \beta { \cdot } x } }
$$

Tomando logaritmo a ambos miembros:

$$
{ \frac { 1 } { \mathrm { y } } } = \alpha + { \beta \cdot \mathrm { x } }
$$

Al aplicar el metodo a los pares modificados $( x _ { i } , 1 I y _ { i } )$ , obtenemos las estimaciones de α y $\pmb { \beta }$ , directamente.

![](images/bb4efd3905c0920f4213861ee32206e9216bc7d130f13e2264f3e3c75344f158.jpg)

w 0 0.01 := , .. 7

![](images/a17c8840fa69f5b68992f633d1fdfaf95333d3220d6c33d740aea2751cb64fdc.jpg)

# AJUSTE DE UN POLINOMIO

En numerosos casos, ya sea por razonamiento teorico, resultados exprimentales, o bien porque no hay indicio acerca de la forma funcional de la regresion, a menudo se supone que la relacion al menos "se comporta bien", en la medida que tiene una expansion en Serie de Taylor, y que los primeros terminos de esa expansion seran los mas representativos. Con esto, llegamos a que los datos se ajustan a una regresion polinomial, es decir, que los valores de y en funcion de x vienen dados de la forma:

$$
\mathrm {  ~ y = \beta _ { 0 } + \beta _ { 1 } \mathrm {  ~ \cdot x + \beta _ { 2 } \mathrm {  ~ \cdot x ^ { 2 } + \ldots + \beta _ { p } \mathrm {  ~ \cdot x ^ { p } = \sum _ { i = 0 } ^ { p } ~ \left( \beta _ { i } \cdot \mathrm { x ^ { i } } \right) } } } }
$$

Donde los primero que debemos hacer es determinar que grado de polinomio sera el que vamos a ajustar, lo cual lo podemos hacer mediante observacion ("a ojo") o con un metodo mas riguroso, desarrollado a continuacion.

Dado un conjunto de n pares ordenados $( { \sf x _ { i } } , { \sf y _ { i } } )$ , la expresion de la suma de cuadrados de error queda.

![](images/af9be944361f5add304abf82fdad57eb4ebec4da2f3211cbccbeab796d09e735.jpg)  
Distancias verticales desde la curva polinomial hasta los puntos $y _ { j }$

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left[ \mathrm { y _ { i } - \left( \beta _ { 0 } + \beta _ { 1 } \cdot x + \beta _ { 2 } \cdot x ^ { 2 } + \hdots + \beta _ { p } \cdot x ^ { p } \right) } \right] ^ { 2 }
$$

De igual forma, se diferencia con respecto a cada uno de los $\beta _ { \mathrm { i } }$ , se igualan estas derivadas parciales a cero y se reemplazan a los $\beta _ { \mathrm { i } }$ por sus estimaciones $\mathsf { b } _ { \mathsf { i } }$ .

$$
\frac { \mathrm { d } } { \mathrm { d } \beta _ { 0 } } { \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \mathrm { y _ { i } - \left[ \mathrm { b _ { 0 } + b _ { \mathrm { 1 } } \cdot x _ { i } + b _ { \mathrm { 2 } } \cdot \left( x _ { i } \right) ^ { 2 } + \hdots + b _ { \mathrm { p } } \cdot \left( x _ { i } \right) ^ { p }   ^ { 2 } = 0 } } }\right]\right]
$$

$$
\frac { \mathrm { d } } { \mathrm { d } \beta _ { 1 } } { \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } { \left[ \mathrm { y } _ { \mathrm { i } } { - } \left[ \mathrm { b } _ { 0 } + \mathrm { b } _ { 1 } { \cdot } \mathrm { x } _ { \mathrm { i } } + \mathrm { b } _ { 2 } { \cdot } \left( \mathrm { x } _ { \mathrm { i } } \right) ^ { 2 } + \hdots + \mathrm { b } _ { \mathrm { p } } { \cdot } \left( \mathrm { x } _ { \mathrm { i } } \right) ^ { \mathrm { p } } \right] \right] } ^ { 2 } } = 0
$$

$$
\frac { \mathrm { d } } { \mathrm { d } \beta } \sum _ { \mathrm { p _ { i } = 1 } } ^ { \mathrm { n } } \left[ \mathrm { y _ { i } - \left[ b _ { 0 } + b _ { \mathrm { 1 } } \cdot x _ { i } + b _ { \mathrm { 2 } } \cdot \left( x _ { i } \right) ^ { 2 } + \hdots + b _ { \mathrm { p } } \cdot \left( x _ { i } \right) ^ { p } \right] \right] ^ { 2 } = 0 }
$$

Acontinuacion se muestra la p-esima derivada y su despeje:

$$
\sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \Big [ 2 \Big [ \mathrm { y _ { i } } - \Big [ \mathrm { b _ { 0 } } + \mathrm { b _ { \mathrm { 1 } } } \cdot \mathrm { x _ { i } } + \mathrm { b _ { \mathrm { 2 } } } \cdot \Big ( \mathrm { x _ { i } } \Big ) ^ { 2 } + \dots + \mathrm { b _ { \mathrm { p } } } \cdot \Big ( \mathrm { x _ { i } } \Big ) ^ { \mathrm { p } } \Big ] \Big ] \cdot \Big [ - \big ( \mathrm { x _ { i } } \big ) ^ { \mathrm { p } } \Big ] \Big ] = 0
$$

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } [ \bigg [ \mathrm { y _ { i } } - \bigg [ \mathrm { b _ { 0 } } + \mathrm { b _ { 1 } } \mathrm { \cdot x _ { i } } + \mathrm { b _ { 2 } } \mathrm { \cdot \Big ( x _ { i } } \bigg ) ^ { 2 } + \ldots + \mathrm { b _ { p } } \mathrm { \cdot \Big ( x _ { i } } \Big ) ^ { p } \bigg ] \bigg [ \mathrm { \cdot \Big [ \mathrm { \cdot \big [ \mathrm { x _ { i } } \mathrm { \cdot } \Big ] ^ { p } } \bigg ] \bigg ] = 0 }
$$

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left[ \mathrm { y _ { i } \cdot ( x _ { i } ) ^ { p } } - \left[ \mathrm { \mathbf { b } _ { 0 } \cdot \left( x _ { i } \right) ^ { p } } + \mathrm { \mathbf { b } _ { \omega _ { i } \cdot } } \left( \mathrm { \mathbf { x } _ { i } } \right) ^ { p + 1 } + \mathrm { \mathbf { b } _ { 2 } \cdot \left( x _ { i } \right) ^ { p + 2 } } + \ldots + \mathrm { \mathbf { b } _ { \omega _ { i } \cdot } } \left( \mathrm { \mathbf { x } _ { i } } \right) ^ { p + p } \right] \right] = 0
$$

$$
\sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \mathrm { y } _ { \mathrm { i } } \cdot \left( \mathrm { x } _ { \mathrm { i } } \right) ^ { \mathrm { p } } \right] = \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \mathrm { b } _ { 0 } \cdot \left( \mathrm { x } _ { \mathrm { i } } \right) ^ { \mathrm { p } } \right] + \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \mathrm { b } _ { \mathrm { i } } \cdot \left( \mathrm { x } _ { \mathrm { i } } \right) ^ { \mathrm { p } + 1 } \right] + \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \mathrm { b } _ { 2 } \cdot \left( \mathrm { x } _ { \mathrm { i } } \right) ^ { \mathrm { p } + 2 } \right] + \ldots + \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \mathrm { b } _ { \mathrm { p } } \cdot \left( \mathrm { x } _ { \mathrm { i } } \right) ^ { \mathrm { p } + \mathrm { p } } \right]
$$

Donde los coeficientes $\mathsf { b } _ { 0 } , \mathsf { b } _ { 1 } , . . . , \mathsf { b } _ { \mathsf { p } }$ son las incognitas del sistema.

$$
\left[ \begin{array} { c c c c c } { { \bf \sigma } } & { { \displaystyle \sum _ { i } } } & { { \bf \sigma } } & { { \bf \sigma } } & { { \displaystyle \sum _ { i } } \left( { \bf x } _ { \mathrm { i } } \right) ^ { \mathrm { p } } } \\ { { \bf \sigma } } & { { \bf \sigma } _ { \mathrm { i } } } & { { \bf \sigma } } & { { \bf \sigma } } \\ { { \displaystyle \sum _ { i } } } & { { \bf \sigma } } & { { \displaystyle \sum _ { i } } \left( { \bf x } _ { \mathrm { i } } \right) ^ { 2 } } & { { \bf \sigma } } & { { \displaystyle \sum _ { i } } \left( { \bf x } _ { \mathrm { i } } \right) ^ { \mathrm { p } + 1 } \left( \left[ \begin{array} { c } { { \bf b } _ { 0 } } \\ { { \bf b } _ { 1 } } \\ { { \bf b } _ { 2 } } \\ { { \bf \sigma } } \end{array} \right] + \left[ \begin{array} { c } { { \bf \sigma } } { { \bf \sigma } } \\ { { \bf \sigma } } \end{array} \right] \right. }  \\ { { \bf \sigma } } & { { \bf \sigma } } & { { \displaystyle \dots } } & { { \bf \sigma } } \\ { { \bf \sigma } } & { { \bf \sigma } } & { { \displaystyle \sum _ { i } } \left( { \bf x } _ { \mathrm { i } } \right) ^ { \mathrm { p } + 1 } } & { { \bf \sigma } } & { { \displaystyle \sum _ { i } } \left( { \bf x } _ { \mathrm { i } } \right) ^ { 2 \mathrm { p } } } \\ { { \bf \sigma } } & { { \bf \sigma } } & { { \displaystyle \sum _ { i } } \left( { \bf x } _ { \mathrm { i } } \right) ^ { \mathrm { p } } } & { { \bf \sigma } } & { { \displaystyle \sum _ { i } } \left( { \bf x } _ { \mathrm { i } } \right) ^ { \mathrm { p } + 1 } } \end{array} \right] \left[ \begin{array} { c } { { \bf \sigma } } \\ { { \bf b } _ { 0 } } \\ { { \bf b } _ { 1 } } \\ { { \bf \sigma } } \end{array} \right] = \left[ \begin{array} { c } { { \bf \sigma } \sum _ { i } { \bf y } _ { i } { \bf \sigma } } \\ { { \bf \sigma } } \\ { { \bf \sigma } \sum _ { i } \left( { \bf y } _ { i } \cdot { \bf x } _ { i } \right) } \\ { { \bf \sigma } } \end{array} \right]
$$

En la practica, puede ser dificil determinar el grado del polinomio que se ajusta a un conjunto de datos. Siempre es posible interpolar, es decir, hallar un polinomio de grado $n - 1$ que pase por los n puntos. Sin embargo el objetivo es encontrar un polinomio de grado minimo que describa adecuadamente los datos, ya que los sistemas tienen inercia, los datos error, etc. y que el polinomio pase por todos los puntos puede no ser lo mas deseable.

# METODO DE LA VARIANZA RESIDUAL

Cuando ajustamos un polinomio, se suele comenazar ajustando los datos a una recta, es decir, hacemos una regresion lineal, luego calculamos la varianza residual. Esta ultima se utiliza como media de la bondad de ajuste, cuanto menor sea la varianza residual menores seran los residuos o errores (εi).

# Siendo:

$\mathsf { y } _ { \mathsf { e s t } }$ la estimacion dada por el polinomio en x i   
n la cantidad de pares ordenados   
Grados de libertad la cantidad de puntos menos la cantidad de coeficientes estimados, es decir, n - ${ \mathsf { p } } + 1 { \mathsf { \Omega } } )$ .

Este proceso se reitera con polinomio de grados superiores, es decir, ajustes cuadraticos, cubicos, cuarticos, etc. Hasta que se produzca el salto decreciente mas significativo.

A continuacion, se realiza un ejemplo para mostrar el metodo:

$$
{ \begin{array} { l } { \mathbf { x } : = ( 0 . 5 \ 1 . 5 \ 2 . 5 \ 5 . 5 \ 6 . 5 \ 9 . 5 \ 1 0 . 5 \ 1 2 . 5 \ 1 4 . 5 \ 1 5 . 5 ) ^ { \mathrm { T } } } \\ { \mathbf { y } : = ( 3 \ 7 \ 1 2 . 5 \ 1 4 . 5 \ 1 6 \ 1 4 . 5 \ 1 6 \ 1 6 \ 2 1 \ 2 3 ) ^ { \mathrm { T } } } \\ { \mathbf { n } : = \mathrm { l e n g t h } ( \mathbf { x } ) = 1 0 \ \qquad \quad \mathbf { i } : = 0 . \mathbf { n } - 1 } \end{array} }
$$

Para comenzar, se intentara un ajuste lineal.

$$
\underset { \mathbf { \dot { \mathbf { M } } } } { \mathbf { \dot { b } } } : = \left[ \begin{array} { c c } { \mathbf { n } } & { \sum _ { \mathbf { \dot { i } } } \mathbf { x _ { \dot { i } } } } \\ { \mathbf { \dot { \mathbf { N } } } } & { \mathbf { \dot { \mathbf { \xi } } } } \\ { \sum _ { \mathbf { \dot { i } } } \mathbf { x _ { \dot { i } } } } & { \sum _ { \mathbf { \dot { i } } } \left( \mathbf { \dot { x } _ { \dot { i } } } \right) ^ { 2 } } \\ { \mathbf { \dot { i } } } & { \mathbf { \dot { \mathbf { \xi } } } } \end{array} \right] ^ { - 1 } \left[ \begin{array} { c } { \sum _ { \mathbf { \dot { i } } } \mathbf { y _ { \dot { i } } } } \\ { \sum _ { \mathbf { \dot { i } } } \left( \mathbf { y _ { \dot { i } } } \cdot \mathbf { x _ { \dot { i } } } \right) } \\ { \sum _ { \mathbf { \dot { i } } } \left( \mathbf { y _ { \dot { i } } } \cdot \mathbf { x _ { \dot { i } } } \right) } \\ { \mathbf { \dot { i } } } \end{array} \right] = \left( \begin{array} { c } { 6 . 5 7 8 } \\ { 0 . 9 8 4 } \end{array} \right)
$$

$$
\sum _ { \mathbf { k } = 0 } ^ { \mathrm { n - 1 } } \left[ \mathrm { y _ { i } } - \sum _ { \mathbf { k } = 0 } ^ { \mathrm { p } } \left[ \mathbf { b _ { k } } { \cdot } \left( \mathbf { x _ { i } } \right) ^ { \mathbf { k } } \right] \right] ^ { 2 }
$$

t := 0 0.1 , .. 20

![](images/6d32a4318a66deaf12191bc63e61aafc7670a4f034bc8ba19d759ca0166dd980.jpg)  
Diagrama de dispersion con polinomio de regresion

Se continua con un ajuste cuadratico.

$$
{ \tt R } _ { \sf \sf } ^ { : = 2 }
$$

$$
\mathbf { b } : = \left[ \begin{array} { c c c c } { \mathbf { n } } & { \sum _ { \overset { \mathbf { x } _ { \overset { \mathbf { x } } { _ { 1 } } } } } } & { \sum _ { \overset { \mathbf { x } _ { \overset { \mathbf { x } } { _ { 1 } } } } } ( \mathbf { x } _ { \overset { \mathbf { x } _ { \overset { \mathbf { ) } } } } { \mathbf { i } } } ^ { 2 } } \end{array} \right] ^ { - 1 } \left[ \begin{array} { c c c c } { \sum _ { \overset { \mathbf { y } _ { \overset { \mathbf { y } } } { _ { 1 } } } } } & \\ & { \vdots } & \\ &  \sum _ { \overset { \mathbf { x } _ { \overset { \mathbf { x } } { _ { 1 } } } } } \end{array} \right] = \left( \begin{array} { c c c c } { 5 . 3 9 9 } & \\ { 1 . 5 } & \\ & { \vdots } & \\ & & { \ddots } & \\ & { \vdots } & \end{array} \right)
$$

$$
\sum _ { \mathbf { k } = 0 } ^ { \mathrm { n - 1 } } \left[ \mathbf { y _ { i } } - \sum _ { \mathbf { k } = 0 } ^ { \mathrm { p } } \left[ \mathbf { b _ { k } } \mathbf { \cdot } \left( \mathbf { x _ { i } } \right) ^ { \mathbf { k } } \right] ^ { 2 } \right] ^ { 2 }
$$

t 0 0.1 := , .. 20

![](images/c46f2c6b5725d25358a0572dc9a7284d85f043c2860694dfb7959bfeb9c5a911.jpg)  
Diagrama de dispersion con polinomio de regresion

p := 3

$$
\sum _ { \mathrm { { v a r } } \ { \mathrm { ~ r e s } } _ { 3 } } ^ { \mathrm { { n - 1 } } } \left[ \mathrm { { y } } _ { \mathrm { { i } } } - \sum _ { \mathrm { { k } } = 0 } ^ { 3 } \left[ \mathrm { { b } } _ { \mathrm { { k } } } { \cdot } \left( { \mathrm { x } } _ { \mathrm { { i } } } \right) ^ { \mathrm { { k } } } \right] \right] ^ { 2 }
$$

t 0 0.1 := , .. 20

![](images/d90025b9dd59475cbe54e86f7d588df70120db04b9ddcc3358bfdb2d29770752.jpg)  
Diagrama de dispersion con polinomio de regresion

Se hace uso de la funcion regress incluida de Mathcad para continuar la regresion hasta el grado 4.

$$
\begin{array} { l } { \mathbf { j } : = 1 \ldots \mathbf { n } - 1 } \\ { \textstyle \operatorname { \mathcal { R } } _ { \mathbf { j } } : = \mathbf { j } } \\ { \operatorname { c o e f } _ { \mathbf { j } } : = \operatorname { r e g r e s s } \left( \mathbf { x } , \mathbf { y } , \mathbf { p } _ { \mathbf { j } } \right) } \end{array}
$$

$$
\mathbf { b } : = { \left[ \begin{array} { l } { \left( \mathrm { c o e f } _ { \mathbf { g r a d o } } \right) _ { 3 } } \\ { \left( \mathrm { c o e f } _ { \mathbf { g r a d o } } \right) _ { 4 } } \\ { \left( \mathrm { c o e f } _ { \mathbf { g r a d o } } \right) _ { 5 } } \\ { \left( \mathrm { c o e f } _ { \mathbf { g r a d o } } \right) _ { 6 } } \\ { \left( \mathrm { c o e f } _ { \mathbf { g r a d o } } \right) _ { 7 } } \end{array} \right] } .
$$

$$
\mathrm { v a r \_ r s ^ { T } } = ( 0 \ \cdot \ 7 . 2 0 7 \ \cdot \ 7 . 5 8 1 . 0 2 1 \ 0 . 9 9 2 )
$$

Viendo el vector var_res podemos observar que el mayor salto se produce cuando "se pasa" del ajuste cuadratico al cubico, con lo cual, el mejor estimador lo constituye el ajuste cubico.

temp coef 9:=   
$\boldsymbol { \mathrm { b } } : = \left( \mathrm { \sf t e m p } _ { 3 } \mathrm { \sf ~ t e m p } _ { 4 } \mathrm { \sf ~ t e m p } _ { 5 } \mathrm { \sf ~ t e m p } _ { 6 } \mathrm { \sf ~ t e m p } _ { 7 } \mathrm { \sf ~ t e m p } _ { 8 } \mathrm { \sf ~ t e m p } _ { 9 } \mathrm { \sf ~ t e m p } _ { 1 0 } \mathrm { \sf ~ t e m p } _ { 1 1 } \mathrm { \sf ~ t e m p } _ { 1 2 } \right) ^ { \mathrm { T } }$ $\sum _ { \mathrm { i } = 0 } ^ { \mathrm { n - 1 } } [ \mathrm { y } _ { \mathrm { i } } - \sum _ { \mathrm { k } = 0 } ^ { 9 } [ ( \mathbf { b } ) _ { \mathrm { k } } \mathbf { \cdot } ( \mathbf { x } _ { \mathrm { i } } ) ^ { \mathrm { k } } ] ^ { 2 } = 0$

Suma de cuadrados de error para un el polinomio de grado 9

t 0 0.1:= , .. 16

![](images/6c267aaaf62e7c2b328b1bab0a7565b48e789ecece2bf1581e942adedd8fe4e2.jpg)

# REGRESION MULTIPLE

Antes de extender los metodos de regresion anteriores a problemas con mas de una variable independiente, vale la pena aclarar que los metodos de regresion con los cuales obtenemos curvas que describen conjuntos de datos, no solo se usan para realizar predicciones, sino que tambien para problemas de optimizacion, donde, al encontrar un maximo o un minimo de la curva producida por el metodo de los minimos cuadrados, hallamos que valor de la variable independiente maximiza o minimiza a la variable dependiente.

A los metodos estadisticos de prediccion y optimizacion con frecuencia se los conoce con el nombre de Analisis de Superficie de Respuesta.

En la regresion multiple, manejamos datos que constan de n (r+1)-tuplas, es decir, $( \mathsf { x } _ { 1 \mathrm { i } } , \mathsf { x } _ { 2 \mathrm { i } } , \ldots , \mathsf { x } _ { \hat { \mathsf { n } } } , \mathsf { y } _ { \mathrm { i } } )$ , es decir, n tuplas de datos. Donde xi son variables predictoras, e yi son valores de variables aleatorias.

Como se menciono al comienzo de este apunte, algunos problemas donde aparecen este tipo de regresiones son:

Predecir la performance de un procesador en determinada tarea dado su numero de nucleos y frecuencia de operacion...

Predecir el numero de kilometros para desgastar un neumatico en funcion de su grosor y composicion...

"Problemas donde tengo 2 o mas variables que predicen a otra"

Para el desarrollo de la regresion multiple, se aborda el caso donde la regresion es de tipo lineal, con 2 variables predictoras, de modo que se puedan graficar en la tridimension. Cuando decimos que el caso es lineal, decimos que la funcion se expresa en la forma de:

$$
\mathrm { y } = \boldsymbol { \beta } _ { 0 } + \boldsymbol { \beta } _ { 1 } { \cdot } \mathrm { x } _ { 1 } + \boldsymbol { \beta } _ { 2 } { \cdot } \mathrm { x } _ { 2 } + \ldots + \boldsymbol { \beta } _ { \mathrm { r } ^ { \cdot } \mathrm { x } _ { \mathrm { r } } }
$$

y como nos limitamos al caso donde solo hay dos variables independientes:

$$
\mathrm { y } = \boldsymbol { \beta } _ { 0 } + \boldsymbol { \beta } _ { 1 } { \cdot } \mathrm { x } _ { 1 } + \boldsymbol { \beta } _ { 2 } { \cdot } \mathrm { x } _ { 2 }
$$

De esta forma, ${ \sf r } = 2 . { \sf Y }$ al graficar las ternas $( \mathsf { x } _ { 1 } , \mathsf { x } _ { 2 } , \mathsf { y } _ { \mathrm { i } } )$ en el espacio, vemos lo siguiente:

![](images/ddbc2c14a8dbc8511cb4809f58b34393d35c231331c94a71b910c03c818fef6b.jpg)

Al aplicar el metodo de los minimos cuadrados para obtener los coeficientes $\beta _ { 0 } , \beta _ { 1 } \gamma \beta _ { 2 }$ que minimizen la suma de cuadrados de error, obtenemos lo siguiente.

$$
\sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \mathrm { y } _ { \mathrm { i } } - \left( \beta _ { 0 } + \beta _ { 1 } { \cdot } \mathrm { x } _ { 1 } + \beta _ { 2 } { \cdot } \mathrm { x } _ { 2 } \right) \right] ^ { 2 }
$$

Suma de cuadrados de error para regresion multiple con r $^ { \circ } = 2$

$$
\begin{array} { l } { \displaystyle \frac { \mathrm { d } } { \mathrm { d } \boldsymbol { \beta } _ { 0 } } \sum _ { \mathbf { i } = 1 } ^ { n } \Big [ \mathbf { y } _ { \mathrm { i } } - \Big ( \boldsymbol { \beta } _ { 0 } + \boldsymbol { \beta } _ { 1 } \cdot \mathbf { x } _ { 1 } + \boldsymbol { \beta } _ { 2 } \cdot \mathbf { x } _ { 2 } \Big ) \Big ] ^ { 2 } = 0 } \\ { \displaystyle \frac { \mathrm { d } } { \mathrm { d } \boldsymbol { \beta } _ { 1 } } \sum _ { \mathbf { i } = 1 } ^ { n } \Big [ \mathbf { y } _ { \mathrm { i } } - \Big ( \boldsymbol { \beta } _ { 0 } + \boldsymbol { \beta } _ { 1 } \cdot \mathbf { x } _ { 1 } + \boldsymbol { \beta } _ { 2 } \cdot \mathbf { x } _ { 2 } \Big ) \Big ] ^ { 2 } = 0 } \\ { \displaystyle \frac { \mathrm { d } } { \mathrm { d } \boldsymbol { \beta } _ { 2 } } \sum _ { \mathbf { i } = 1 } ^ { n } \Big [ \mathbf { y } _ { \mathrm { i } } - \Big ( \boldsymbol { \beta } _ { 0 } + \boldsymbol { \beta } _ { 1 } \cdot \mathbf { x } _ { 1 } + \boldsymbol { \beta } _ { 2 } \cdot \mathbf { x } _ { 2 } \Big ) \Big ] ^ { 2 } = 0 } \end{array}
$$

Derivadas parciales con respecto a $\beta _ { j }$ igualadas a cero

Si llevamos a cabo el mismo proceso que con los demas casos de regresion, obtenemos las siguientes ecuaciones normales.

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \mathrm {  ~ \ y _ { \mathrm { i } } = \mathrm { b } _ { 0 } \cdot \mathrm { n } + \mathrm { b } _ { 1 } \cdot \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \mathrm {  ~ \ x _ { 1 i } + \mathrm { b } _ { 2 } \cdot \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \mathrm {  ~ \ x _ { 2 i } ~ } } }
$$

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } { \left( \mathrm { y } _ { \mathrm { i } } \mathrm { x } _ { 1 \mathrm { i } } \right) } = \mathrm { b } _ { 0 } ; \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } { \mathrm {  ~ \scriptstyle { \ x } _ { 1 \mathrm { i } } + \mathrm { b } _ { 1 } } \mathrm {  ~ \scriptstyle { \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } { \left( \mathrm { x } _ { 1 \mathrm { i } } \right) } ^ { 2 } + \mathrm { b } _ { 2 } \mathrm {  ~ \scriptstyle { \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } { \left( \mathrm { x } _ { 1 \mathrm { i } } \cdot \mathrm { x } _ { 2 \mathrm { i } } \right) } } } } } } 
$$

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } { \left( \mathrm { y } _ { \mathrm { i } } \mathrm { \cdot } \mathrm { x } _ { 2 \mathrm { i } } \right) } = \mathrm { b } _ { 0 } { \cdot } \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } { \mathrm {  \ x } _ { 2 \mathrm { i } } } + \mathrm { b } _ { \mathrm { l } } { \cdot } \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } { \left( \mathrm { x } _ { 1 \mathrm { i } } \mathrm { \cdot } \mathrm { x } _ { 2 \mathrm { i } } \right) } + \mathrm { b } _ { 2 } { \cdot } \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } { \left( \mathrm { x } _ { 2 \mathrm { i } } \right) } ^ { 2 }
$$

$$
\left[ \begin{array} { l l l l } { { \bf n } } & { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } { \bf x } _ { \mathrm { l i } } } & { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } { \bf x } _ { 2 \mathrm { i } } } \\ { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } { \bf x } _ { \mathrm { l i } } } & { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } \left( { \bf x } _ { 1 1 } { \bf x } _ { 2 \mathrm { i } } \right) } \\ { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } { \bf x } _ { \mathrm { l i } } } & { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } \left( { \bf x } _ { 1 1 } \right) ^ { 2 } } & { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } \left( { \bf x } _ { 1 1 } { \bf x } _ { 2 \mathrm { i } } \right) } \\ { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } { \bf x } _ { 2 \mathrm { i } } } & { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } \left( { \bf x } _ { 1 1 } { \bf x } _ { 2 \mathrm { i } } \right) } & { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } \left( { \bf x } _ { 2 \mathrm { i } } \right) ^ { 2 } } \end{array} \right] \left( \begin{array} { l } { { \bf b } _ { 0 } } \\ { { \bf b } _ { 1 } } \\ { { \bf b } _ { 2 } } \\ { { \bf b } _ { 2 } } \end{array} \right) = \left[ \begin{array} { l } { { \displaystyle \sum _ { \bf i = 1 } ^ { \bf n } { \bf y } _ { \mathrm { i } } } } \\ { { \bf { \bar { i } } } _ { 1 } { \bf { \bar { \Phi } } } } \\ { { \bf { \bar { i } } } _ { 1 } { \bf { \bar { \Phi } } } } \\ { { \bf { \bar { i } } } _ { 1 } { \bf { \bar { \Phi } } } } \\ { { \bf { \bar { i } } } _ { 1 } { \bf { \bar { \Phi } } } } \end{array} \right]
$$

Donde $\mathsf { b } _ { 0 } , \mathsf { b } _ { 1 } \mathsf { y } \mathsf { b } _ { 2 }$ son estimaciones en base a la muestra de n tuplas, de los parametros $\mathsf { \pmb { \beta } } _ { 0 } , \mathsf { \pmb { \beta } } _ { 1 } \mathsf { \pmb { \gamma } } \mathsf { \pmb { \beta } } _ { 2 }$ .

# COEFICIENTE DE CORRELACION SIMPLE DE PEARSON (MODELO RECTILINEO)

El coeficiente de correlacion es una medida de asociacion entre dos variables y se simboliza con la letra r.

El coeficiente va desde -1 a 1, pasando por cero.

$$
- 1 \leq \mathbf { r } \leq 1
$$

Cuando ${ \sf r } = 0$ , indica ausencia de correlacion.

Cuando $\mathsf { r } = - 1$ , indica una correlacion inversamente proporcional.

![](images/cbfa123d573805b23f30468e12174a0333c7250d24c755759d224571ce50f719.jpg)

Cuando $\mathsf r = \mathsf { 1 }$ , indica una correlacion directamente proporcional proporcional.

![](images/ada3fed073f80d684f8e2d5933fb883a03fa98c4d1e03250a54cf376ec7a6a68.jpg)

El coeficiente de correlacion permite predecir si entre dos variables existe o no una relacion o dependencia matematica.

A continuacion, se muestran ejemplos donde vemos correlaciones, positivas y negativas.

En el siguiente grafico de dispersion vemos que existe una correlacion, entre la potencia del motor (CV) y su consumo en litros cada 100km.   
En este caso, si calculamos el coeficiente de correlacion veriamos que ${ \sf r } = 0 . 8 7$ , lo cual indica que existe una relacion directamente proporcional entre la potencia y el consumo de un vehiculo.

![](images/fcc4c02c988cc17779a3df41fc43661e2010fa28e1530a08d49250a37c206a36.jpg)

A continuacion, un ejemplo simulado para realizar un calculo sobre r.

n := 100 i 0 n 1 := .. -

$$
\mathrm { x _ { i } } : = \mathrm { i } + \mathrm { r n o r m } ( 1 , 0 , 1 0 ) _ { 0 }
$$

$$
\mathrm { y _ { i } } \mathrm { : = 1 0 + 2 { \cdot } x _ { i } } + \mathrm { r n o r m } ( 1 , 0 , 2 0 ) _ { 0 }
$$

t 50 := - , -49.. 150

![](images/0e69887caf52dfc749b43fa3b39cda1f747cd4c7c42b891f4bf58cdbf10f901f.jpg)  
$\mathrm { r } : = \mathrm { c o r r } ( \mathrm { x } , \mathrm { y } ) = 0 . 9 4 9$ Funcion built-in de mathcad

Vemos que el coeficiente de correlacion indica un valor proximo a 1, es decir, existe una relacion directamente proporcional entre la variable x e y.

Realizamos lo mismo, para una relacion inversamente proporcional

$$
\begin{array} { c } { \mathrm { x _ { i } : = i + r n o r m ( 1 , 0 , 2 0 ) _ { 0 } } } \\ { \mathrm { y _ { i } : = 1 0 0 - 2 { \cdot } x _ { i } + r n o r m ( 1 , 0 , 5 0 ) _ { 0 } } } \end{array}
$$

t 50 := - , -49.. 150

![](images/b150b1e676ab1db1d85ee6000700a96cd9bdf09b310468032ae7f37c548519e3.jpg)  
r := corr x y ( ) 0.822 , = - Funcion built-in de mathcad

En este caso vemos que el coeficiente es negativo, con lo cual, confirmamos lo que queriamos modelar, que era una relacion inversamente proporcional entre la variables x e y.

Para poder interpretar este coeficiente, Colton, propuso los siguientes lineamientos generales:

Valores entre $\tt 0 9 0 . 2 5$ implica que no existe correlacion Valores entre $\pmb { 0 . 2 5 \ y 0 . 5 0 }$ implica una correlacion baja a moderada · Valores entre $\pmb { 0 . 5 0 y 0 . 7 5 }$ implica una relacion moderada a buena Valores entre 0.75 o mayores implica una correlacion muy buena a excelente

Los rangos son extrapolables a valores negativos.

Se debe tener precacucion de que ambas variables varien juntas permanentemente. Por ejemplo, si correlacionamos edad vs. altura, ambas creceran juntas hasta cierto punto, donde la altura dejara de aumentar.

El coeficiente de correlacion lineal, mide la fortaleza de de una relacion lineal, por lo que valores de este cercanos a cero, implican que la asociacion lineal entre las variables es debil. Sin embargo, el conjunto de datos aun puede poseer una asociacion fuerte para otros tipos de curvas.

n := 100 i 0 n 1 := .. -

$$
\begin{array} { l } { \displaystyle \mathrm { x } _ { \mathrm { i } } : = \mathrm { i } - \frac { \mathrm { n } } { 2 } + \mathrm { r n o r m } ( 1 , 0 , 1 ) _ { 0 } } \\ { \displaystyle \mathrm { y } _ { \mathrm { i } } : = \left( \mathrm { x } _ { \mathrm { i } } \right) ^ { 2 } + \mathrm { r n o r m } ( 1 , 0 , 5 0 ) _ { 0 } } \end{array}
$$

t 50 := - , -49.. 50

![](images/8fa9551f4f662235ab77524a6c9d559e0a412f25ff51203ded2f73e4db06b34e.jpg)

Para calcular el coeficiente de correlacion se considera el caso en el que las dos variables son aleatorias. Dada una muestra de n pares $( x _ { \mathrm { i } } , y _ { \mathrm { i } } )$ :

$$
\left( \mathsf { x } 1 , \mathsf { y } 1 \right) , \left( \mathsf { x } 2 , \mathsf { y } 2 \right) , . . . , \left( \mathsf { x } \mathsf { n } , \mathsf { y } \mathsf { n } \right)
$$

proveniente de una poblacion normal bidimensional ( X , Y ), se puede determinar:

$$
\operatorname { m e a n } ( \mathbf { x } ) = { \frac { 1 } { \mathrm { n } } } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } { \mathrm {  ~ { \vec { x } } _ { i } ~ } } \qquad \operatorname { s . } _ { \mathrm { x } } ^ { 2 } = { \frac { 1 } { \mathrm { n } - 1 } } \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left( \mathrm { x } _ { \mathrm { i } } - \operatorname { m e a n } ( \mathbf { x } ) \right) ^ { 2 }
$$

Media y varianza muestral de la variable aleatoria X

$$
\mathrm { { m e a n } ( y ) = \frac { 1 } { n } { \cdot } \sum _ { i = 1 } ^ { n } y _ { i } }
$$

$$
{ s _ { \mathrm { y } } } ^ { 2 } = { \frac { 1 } { \mathrm { n } - 1 } } { \cdot } \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left( \mathrm { y } _ { \mathrm { i } } - \mathrm { m e a n ( y ) } \right) ^ { 2 }
$$

Se define como covarianza:

$$
{ \mathrm { s _ { x y } } } ^ { 2 } = { \frac { 1 } { \mathrm { n } - 1 } } . \sum _ { \mathrm { i } \mathrm { = 1 } } ^ { \mathrm { n } } \left[ \left( { \mathrm { x } } _ { \mathrm { { i } } } - { \mathrm { m e a n } } ( \mathrm { x } ) \right) \left( \mathrm { y } _ { \mathrm { { i } } } - { \mathrm { m e a n } } ( \mathrm { y } ) \right) \right]
$$

Con esto, el coeficiente de correlacion es

O en terminos de los valores resumen $\mathsf { S } _ { \mathsf { x } } , \mathsf { S } _ { \mathsf { y } } \mathsf { y } \mathsf { S } _ { \mathsf { x } \mathsf { y } }$

Sxy Formula alternativa para el calculo r Sxx Syy  de r

Recordemos que:

$$
\mathrm { S _ { _ { X X } } = n { \cdot } \sum _ { i = 1 } ^ { n } \binom { x _ { i } } { i } ^ { 2 } - \left( \sum _ { i = 1 } ^ { n } \mathrm { x _ { i } } \right) ^ { 2 } = n { \cdot } \binom { s } { x } ^ { 2 } { \cdot } ( n - 1 ) }
$$

$$
\mathrm { S _ { y y } = n { \cdot } \sum _ { i = 1 } ^ { n } \left( y _ { i } \right) ^ { 2 } - \left( \sum _ { i = 1 } ^ { n } y _ { i } \right) ^ { 2 } = n { \cdot } \binom { s } { y } ^ { 2 } { \cdot } ( n - 1 ) }
$$

$$
\mathrm { S _ { _ { X y } } = n { \cdot } \sum _ { i = 1 } ^ { n } \ \left( \mathrm { x } _ { i } { \cdot } \mathrm { y } _ { i } \right) - \sum _ { i = 1 } ^ { n } \mathrm { x } _ { i } { \cdot } \sum _ { i = 1 } ^ { n } \mathrm { y } _ { i } = n { \cdot } \mathrm { s } _ { _ { X y } } { \cdot } ( n - 1 ) }  
$$

$$
{ \frac { \mathbf { n \cdot s } _ { \mathbf { x y } } \cdot ( \mathbf { n } - 1 ) } { \sqrt { \mathbf { n } \cdot { \Big ( } \mathbf { s } _ { \mathbf { x } } { \Big ) } ^ { 2 } \cdot ( \mathbf { n } - 1 ) } \cdot { \sqrt { \mathbf { n } \cdot { \Big ( } \mathbf { s } _ { \mathbf { y } } { \Big ) } ^ { 2 } \cdot ( \mathbf { n } - 1 ) } } } } = { \frac { \mathbf { n \cdot s } _ { \mathbf { x y } } \cdot ( \mathbf { n } - 1 ) } { \sqrt { \mathbf { n } \cdot { \Big ( } \mathbf { s } _ { \mathbf { y } } { \Big ) } ^ { 2 } \cdot { \Big ( } \mathbf { s } _ { \mathbf { x } } { \Big ) } ^ { 2 } \cdot ( \mathbf { n } - 1 ) ^ { 2 } } } } = { \frac { \mathbf { n \cdot s } _ { \mathbf { x y } } \cdot ( \mathbf { n } - 1 ) } { \mathbf { n } \cdot ( \mathbf { n } - 1 ) \cdot \mathbf { s } _ { \mathbf { x } } \cdot \mathbf { s } _ { \mathbf { y } } } }
$$

$$
\mathrm { { r } = \frac { S _ { x y } } { \sqrt { S _ { x x } \cdot S _ { y y } } } = \frac { s _ { x y } } { s _ { x } \cdot s _ { y } } }
$$

Dado que $\mathsf { s } _ { \mathsf { x } } \mathsf { y s } _ { \mathsf { y } }$ son ambos mayores que 0, el signo de r viene dado por el signo de $\mathsf { s } _ { \mathsf { x y } }$ el cual puede ser positivo o negativo.

Generando una simulacion de una muestra de $\mathsf { n } = 1 0 0$ pares ordenados $( { \sf x } _ { \mathrm { i } } , { \sf y } _ { \mathrm { i } } )$

$$
\begin{array} { r } { \underset { \mathbf { m } } { \boldsymbol { \mathrm { n } } } : = 1 0 0 \qquad \quad \mathrm { ~ i ~ } : = 0 \ldots \boldsymbol { \mathrm { n } } - 1 } \end{array}
$$

$$
\begin{array} { r l } { - 1 } & { } \\ & { \mathrm { ~  ~ \gamma ~ } _ { \mathrm { { X } } _ { \mathrm { { i } } } } : = \mathrm { { i } } + \mathrm { { r n o r m } } ( 1 , 0 , 1 0 ) _ { 0 } } \\ & { } \\ & { \mathrm { ~  ~ \gamma ~ } _ { \mathrm { { y } } _ { \mathrm { { i } } } } : = 1 0 + 2 \cdot \mathrm { { x } } _ { \mathrm { { i } } } + \mathrm { { r n o r m } } ( 1 , 0 , 2 0 ) _ { 0 } } \end{array}
$$

t 50 := - , -49.. 150

![](images/bb43dddfddb0c14247fc0d1a73871a707581ddc1455ff1edda5f445dc805e361.jpg)

$$
\underset { \mathrm { i } = 0 } { \overset { \mathrm { n - 1 } } { \sum } } \left( \mathrm { x _ { i } } \right) ^ { 2 } - \left( \sum _ { \mathrm { i } = 0 } ^ { \mathrm { n - 1 } } \mathrm { x _ { i } } \right) ^ { 2 } = 1 . 0 5 1 \times 1 0 ^ { 7 }
$$

$$
\mathrm { S _ { y y } : = n \cdot \sum _ { i = 0 } ^ { n - 1 } \left( y _ { i } \right) ^ { 2 } - \left( \sum _ { i = 0 } ^ { n - 1 } y _ { i } \right) ^ { 2 } = 4 . 7 0 5 \times 1 0 ^ { 7 } }
$$

$$
{ \underset { \mathbf { i } = \mathbf { 0 } } { \overset { \mathrm { n - 1 } } { \sum } } } \left( \mathbf { x } _ { \mathrm { i } } \mathbf { \cdot y } _ { \mathrm { i } } \right) - \sum _ { \mathrm { i } = \mathbf { 0 } } ^ { \mathrm { n - 1 } } \mathbf { \Phi } _ { \mathrm { i } } \mathbf { \cdot } \sum _ { \mathrm { i } = \mathbf { 0 } } ^ { \mathrm { n - 1 } } \mathbf { \Psi } _ { \mathrm { i } } = 2 . 1 2 7 \times ~ { 1 0 } ^ { 7 } \mathbf { \Phi } \quad \quad { \mathrm { c v a r } } ( \mathbf { x } , \mathbf { y } ) = 2 . 1 2 7 \times ~ { 1 0 } ^ { 3 }
$$

![](images/ebd264f8b3aa1a037a70484189ce38d345191164dac4f3863a94bd795355de54.jpg)

# COEFICIENTE DE CORRELACION DE LA POBLACION

Hasta aca hemos usado una muestra de n pares ordenados $( { \sf x _ { i } } , { \sf y _ { i } } )$

$$
\left( \mathsf { x } 1 , \mathsf { y } 1 \right) , \left( \mathsf { x } 2 , \mathsf { y } 2 \right) , . . . , \left( \mathsf { x } \mathsf { n } , \mathsf { y } \mathsf { n } \right)
$$

extraidos de una poblacion XY.

Dadas las variables aleatorias X e Y, sus respectivas medias poblacionales

$$
\mu _ { \mathrm { X } } = \mathrm { E ( X ) ~ \mu _ { \mathrm { Y } } = \mathrm { E ( Y ) } }
$$

sus varianzas poblacionales

$$
\begin{array} { r } { \sigma _ { \mathrm { X } } ^ { \mathrm { \Delta } 2 } = \mathrm { E } \bigg [ \Big ( \mathrm { X } - \mu _ { \mathrm { X } } \Big ) ^ { 2 } \bigg ] \qquad \quad \sigma _ { \mathrm { Y } } ^ { \mathrm { \Delta } 2 } = \mathrm { E } \bigg [ \Big ( \mathrm { Y } - \mu _ { \mathrm { Y } } \Big ) ^ { 2 } \bigg ] } \end{array}
$$

la cantidad

$$
{ \sigma _ { \mathrm { X Y } } } ^ { 2 } = \mathrm { E } \big [ \big ( \mathrm { X } - \mu _ { \mathrm { X } } \big ) \cdot \big ( \mathrm { Y } - \mu _ { \mathrm { Y } } \big ) \big ]
$$

se denomina covarianza poblacional de las variables X e Y. Entonces el cociente

$$
\rho = \frac { \sigma _ { \mathrm { X Y } } } { \sigma _ { \mathrm { X } } \cdot \sigma _ { \mathrm { Y } } }
$$

es lo que denominamos como coeficiente de correlacion poblacional de X e Y.

Si ${ \pmb \rho } = { \pmb 0 }$ , entonces X e Y no estan correlacionadas (linealmente), tambien si X e Y son independientes entre si $\sigma _ { \mathrm { x v } } = 0 \textrm { y } \rho = 0$ .

# Teorema:

"Si las variables aletorias X e Y son independientes, entonces no estan correlacionadas. Lo reciproco no es cierto (No estar correlacionadas no implica independecia)."

Ejemplo:

Suponer que X es una variable aleatoria que toma los valores -1, 0 y 1, cada uno de ellos con una probabilidad de ${ \mathsf p } = 1 / 3$ . Entonces ${ \mu _ { \mathsf { X } } } = 0$ . Sea $\mathsf { Y } = \mathsf { X } ^ { 2 }$ , entonces:

$$
\sigma _ { \mathrm { X Y } } ^ { \mathrm { ~ \tiny ~ 2 ~ } } = \mathrm { E } ( \mathrm { X Y } ) - \mathrm { E } ( \mathrm { X } ) { \cdot } \mathrm { E } ( \mathrm { Y } ) = \mathrm { E } \big ( \mathrm { X } ^ { 3 } \big ) - 0 { \cdot } \mathrm { E } ( \mathrm { Y } ) = 0
$$

$$
{ \sigma _ { \mathrm { X Y } } } ^ { 2 } = { ( - 1 ) } ^ { 3 } { \cdot } { \frac { 1 } { 3 } } + { ( 0 ) } ^ { 3 } { \cdot } { \frac { 1 } { 3 } } + { ( 1 ) } ^ { 3 } { \cdot } { \frac { 1 } { 3 } } = 0
$$

$$
{ \sigma _ { \mathrm { X Y } } } ^ { 2 } = 0
$$

Por lo tanto $\rho = 0$ , por lo que no existe correlacion (lineal) entre X e Y, sin embargo, existe dependencia funcional entre X e Y.

La variacion total de una variable aleatoria Y se define como

$$
\mathrm { { V T } = \sum _ { i = 1 } ^ { n } \Big ( y _ { i } - m e a n ( y ) \Big ) ^ { 2 } }
$$

Definicion de variacion total

Suma de los cuadrados de las desviaciones de los valores observados de y con respecto a su media

Partiendo de la siguiente igualdad:

$$
\mathrm { y _ { i } - m e a n ( y ) = \left( y _ { i } - y _ { e s t } \right) + \left( y _ { e s t } - m e a n ( y ) \right) }
$$

Elevando ambos miembros al cuadrado y tomando sumatoria

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left( \mathrm { y _ { i } - m e a n ( y ) } \right) ^ { 2 } = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left[ \left( \mathrm { y _ { i } - y _ { e s t } } \right) + \left( \mathrm { y _ { e s t } - m e a n ( y ) } \right) \right] ^ { 2 }
$$

Desarrollando el cuadrado de un binomio en le segundo miembro

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \ \left( \mathrm { y _ { i } - \mathrm { y _ { e s t } } } \right) ^ { 2 } + \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \ \left( \mathrm { y _ { e s t } - m e a n ( y ) } \right) ^ { 2 } + 2 \cdot \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left[ \left( \mathrm { y _ { i } - \mathrm { y _ { e s t } } } \right) \cdot \left( \mathrm { y _ { e s t } - m e a n ( y ) } \right) \right]
$$

Se sabe que $\mathsf { y } _ { \mathsf { e s t } }$ (en algun xi) es igual a a $^ +$ bxi entonces:

$$
2 \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \left( \mathrm { y _ { i } - y _ { \mathrm { e s t } } } \right) \cdot \left( \mathrm { y _ { \mathrm { e s t } } - m e a n ( y ) } \right) \right] = 2 \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \left( \mathrm { y _ { i } - a - b \cdot x _ { i } } \right) \cdot \left( \mathrm { y _ { \mathrm { e s t } } - m e a n ( y ) } \right) \right]
$$

Como, supuestamente, $y _ { i } - a - b x _ { i }$ son numeros pequenos (minimos), se puede suponer que $y _ { \mathrm { i } } - a - b x _ { \mathrm { i } } = 0$ . Con lo cual, podemos decir

$$
2 \cdot \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \left[ \left( \mathrm { y } _ { \mathrm { i } } - \mathrm { a } - \mathrm { b } { \cdot } \mathrm { x } _ { \mathrm { i } } \right) \cdot \left( \mathrm { y } _ { \mathrm { e s t } } - \mathrm { m e a n ( y ) } \right) \right] = 0
$$

Lo que nos deja en la expresion original

$$
\sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left( \mathrm { y _ { i } - m e a n ( y ) } \right) ^ { 2 } = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left( \mathrm { y _ { i } - y _ { e s t } } \right) ^ { 2 } + \sum _ { \mathrm { i = 1 } } ^ { \mathrm { n } } \left( \mathrm { y _ { e s t } - m e a n ( y ) } \right) ^ { 2 }
$$

Del lado izquierdo, en el primer miembro, tenemos lo que definimos como variacion total. Mientras tanto, en el segundo miembro, en el primer termino, encontramos lo que denominaremos como variacion no explicada, y esto es asi porque esta variacion tiene un componente aleatorio (yi). Por ultimo, en el segundo termino del segundo miembro, encontramos lo que llamamos variacion explicada, por lo que existe un patron definido.

La razon entre la variacion explicada y la variacion total, es lo que denominamos como Coeficiente de Determinacion, $\mathsf { r } ^ { 2 }$ .

$$
\mathrm { r } ^ { 2 } = { \frac { \mathrm { V E } } { \mathrm { V T } } }
$$

Cuando VE $= 0$ , es decir, la variacion total es toda no explicada.

Cuando VE $= \mathsf { V } \mathsf { T }$ , la razon da 1 $( \mathsf { V E N T } = 1 $ ), es decir, la variacion total es toda explicada, este seria el caso en el que el modelo sea "perfecto", en otras palabras, que los datos esten perfectamente alineados.

Los demas casos van entre 0 y 1.

# Ejemplo:

Los siguientes son los números de minutos que tardan 10 mecánicos en ensamblar una pieza de maquinaria en la mañana, $\mathsf { \pmb X } ,$ , y en la tarde, y.

![](images/c75d664fe511ac92e0698682b44d2034ad5236fec53469c8742776cfa9c2066b.jpg)

$$
\mathbf { b } : = \mathrm { s l o p e } ( \mathbf { x } , \mathbf { y } ) = 1 . 0 1 2
$$

$$
\mathrm { V T } : = \sum _ { \mathrm { i } = 0 } ^ { \mathrm { n } - 1 } \left( \mathrm { y } _ { \mathrm { i } } - \mathrm { m e a n } ( \mathrm { y } ) \right) ^ { 2 } = 1 1 5 . 5 7 6
$$

$$
\mathrm { V E } : = \sum _ { \mathrm { i } = 0 } ^ { \mathrm { n - 1 } } \left( \mathrm { a } + \mathrm { b } { \cdot } \mathrm { x } _ { \mathrm { i } } - \mathrm { m e a n } ( \mathrm { y } ) \right) ^ { 2 } = 6 1 . 8 8
$$

Esto nos dice que el $5 3 . 5 \%$ de la variacion entre los tiempos de la tarde responden a las diferencias correspondientes entre los tiempos matutinos.

Siempre que un valor se fundamenta en una muestra aleatoria de una poblacion normal bivariada

![](images/b18b48d8ea4083df47644184a35d0065a525ca62e37707ac7dcae8bbd4209d98.jpg)

$$
\frac { 1 } { \tau \sigma _ { 1 } \sigma _ { 2 } \sqrt { 1 - \rho ^ { 2 } } } \exp \{ - \frac { 1 } { 2 \sigma _ { 1 } ^ { 2 } \sigma _ { 2 } ^ { 2 } ( 1 - \rho ^ { 2 } ) } ( \sigma _ { 2 } ^ { 2 } ( x - \mu _ { 1 } ) ^ { 2 } + \sigma _ { 1 } ^ { 2 } ( y - \mu _ { 2 } ) ^ { 2 } - 2 \sigma _ { 1 } \sigma _ { 2 } \rho ( x - \mu _ { 1 } ) ( y - \mu _ { 2 } ) ) \}
$$

se puede practicar una prueba de significacion ( $\rho = \rho _ { 0 }$ ) o construir un intervalo de confianza para ρ, en base a la trasformacion de Fischer, que se muestra a continuacion

$$
Z = { \frac { 1 } { 2 } } { \cdot } \ln \left( { \frac { 1 + { \bf r } } { 1 - { \bf r } } } \right)
$$

Z es un estadistico con distribucion normal con media y varianza dadas por las siguientes expresiones

$$
\mathsf { \Pi } _ { \mathsf { L } _ { \mathsf { Z } } } = \frac { 1 } { 2 } \cdot \ln \left( \frac { 1 + \mathsf { \Pi } _ { \mathsf { \Lambda } } \mathsf { \Lambda } _ { \mathsf { L } } } { 1 - \mathsf { \Pi } _ { \mathsf { \Lambda } } } \right) \qquad \mathsf { \Gamma } _ { \mathsf { Z } _ { \mathsf { Z } } } ^ { 2 } = \frac { 1 } { \mathsf { \Pi } _ { \mathsf { \Lambda } } - 3 }
$$

Normalizando el estadistico Z se obtiene la siguiente expresion

$$
\mathbf { \sigma } _ { \mathbf { z } } = { \frac { Z - \mu _ { Z } } { \sigma _ { \mathrm { Z } } } } = \left( { \frac { 1 } { 2 } } . \ln \left( { \frac { 1 + \tau } { 1 - \tau } } \right) - { \frac { 1 } { 2 } } . \ln \left( { \frac { 1 + \rho } { 1 - \rho } } \right) \right) \cdot { \sqrt { \mu - 3 } }
$$

$\mathrm { ~ z = \frac { \sqrt { n - 3 } } { 2 } { \cdot } l n } \biggl [ \frac { ( 1 + \mathrm { r } ) { \cdot } ( 1 - \mathrm { p } ) } { ( 1 - \mathrm { r } ) { \cdot } ( 1 + \mathrm { p } ) } \biggr ]$ Estadistico de prueba z

# PRUEBA DE HIPOTESIS RELATIVA ρ

En particular cuando se prueba que $\rho = 0$ , es decir, no hay correlacion, el estadistico queda

$$
z = { \frac { \sqrt { \mathrm { n } - 3 } } { 2 } } \cdot \ln \left[ { \frac { ( 1 + \mathrm { r } ) } { ( 1 - \mathrm { r } ) } } \right]
$$

Con respecto al ejemplo anterior, donde se tenía $\mathsf { n } = 1 0 \mathsf { y } \mathsf { r } = 0 . 7 3 2$ , pruebe la hipótesis nula $\rho = 0$ contra la hipótesis nula $\rho \neq 0$ , con nivel de signiicancia de 0.05.

$\operatorname* { n } _ { \ M } : = 1 0 \qquad \operatorname* { r } _ { \ M } : = 0 . 7 3 2$ 1- Hipotesis $\begin{array} { r } { \mathsf { H 0 } : \mathsf { \rho = 0 } } \\ { \mathsf { H } 1 : \mathsf { \rho \neq 0 } } \end{array}$

2- Significacion

$$
\underset { N } { \underbrace { \mathrm { a } } } \mathrm { ; = } \ 0 . 0 5
$$

3- Criterio

$$
\mathsf { z } _ { \mathrm { c r i t i c o } } : = \mathrm { q n o r m } \left( 1 - \frac { \alpha } { 2 } , 0 , 1 \right) = 1 . 9 6
$$

4- Calculos

$$
\mathsf { z } : = \frac { \sqrt { \mathsf { n } - 3 } } { 2 } { \cdot } \mathsf { l n } \Bigg [ \frac { ( 1 + \mathsf { r } ) } { ( 1 - \mathsf { r } ) } \Bigg ] = 2 . 4 6 9
$$

t 4:= - , -3.99.. 4

![](images/5de23b2f0b4566124db73f18f9cb27eaef849c62e7741feafec673ab90953e36.jpg)

# 5- Conclusion

Dado que $z _ { \mathrm { c } \mathrm { r } \mathrm { i } \mathrm { t i c o } } = 1 . 9 6 < z = 2 . 4 7$ , se rechaza H0. Por lo tanto, el coeficiente de correlacion ρ es significativamente distinto de 0. Entonces, existe relacion entre el tiempo de ensamblaje que ocupa en la manana y en la tarde

# INTERVALO DE CONFIANZA PARA ρ

Si se quiere construir un intervalo de confianza para ρ se debe comenzar por construir uno para $\mu _ { z }$

$$
\displaystyle { \frac { - z } { \frac { \alpha } { 2 } } } < \frac { Z - \mu _ { Z } } { \sigma _ { Z } } < \mu _ { \frac { \alpha } { 2 } }
$$

$$
\begin{array} { c } { { - z _ { \alpha } \cdot \sigma _ { Z } < Z - \mu _ { Z } < z _ { \alpha } \cdot \sigma _ { Z } } } \\ { { \frac { \alpha } { 2 } } } \end{array}
$$

$$
\begin{array} { r } { { - z _ { \alpha } \cdot \sigma _ { Z } - Z < - \mu _ { Z } < z _ { \alpha } \cdot \sigma _ { Z } - Z } } \\ { { \frac { \alpha } { 2 } } } \end{array}
$$

$$
Z + z _ { \alpha } \cdot \sigma _ { Z } > \mu _ { Z } > Z - z _ { \alpha } \cdot \sigma _ { Z }
$$

$$
Z - z _ { \alpha } \cdot \sigma _ { Z } < \mu _ { Z } < Z + z _ { \alpha } \cdot \sigma _ { Z }
$$

Intervalo de confianza para μZ

Luego, despejando $\rho$ de la expresion de $\mu _ { Z }$

$$
\begin{array} { r } { \mathsf { \Pi } \mu _ { Z } = \displaystyle \frac { 1 } { 2 } . \ln \Biggl ( \frac { 1 + \mathsf { \rho } } { 1 - \mathsf { \rho } } \Biggr ) } \\ { \mathsf { \Pi } \displaystyle 2 . \mathsf { \rho } \mu _ { Z } = \ln \Biggl ( \frac { 1 + \mathsf { \rho } } { 1 - \mathsf { \rho } } \Biggr ) } \end{array}
$$

$$
\mathrm { { e } } ^ { 2 \cdot \mu _ { Z } } = \frac { 1 + \rho } { 1 - \rho }
$$

$$
( 1 - \rho ) \cdot \mathrm { e } ^ { 2 \cdot \mu _ { Z } } = 1 + \rho
$$

$$
\mathrm { e } ^ { 2 \cdot \mu _ { Z } } - 1 = \rho \cdot \left( \mathrm { e } ^ { 2 \cdot \mu _ { Z } } + 1 \right)
$$

$$
\frac { \mathrm { e } ^ { 2 \cdot \mu _ { Z } } - 1 } { \mathrm { e } ^ { 2 \cdot \mu _ { Z } } + 1 } = \rho
$$

Retomando el ejemplo anterior, un intervalo del $9 5 \%$ de confianza para ρ queda

$$
\sigma _ { \mathrm { Z } } : = \frac { 1 } { \sqrt { \mathrm { n } - 3 } } = 0 . 3 7 8 \qquad \quad z _ { \mathrm { \tiny G } } : = \mathrm { q n o r m } \Bigg ( 1 - \frac { \alpha } { 2 } , 0 , 1 \Bigg ) = 1 . 9 6
$$

$$
Z : = { \frac { 1 } { 2 } } { \cdot } \ln \left( { \frac { 1 + { \bf r } } { 1 - { \bf r } } } \right) = 0 . 9 3 3
$$

$$
\mathrm { E } : = \mathrm { z } _ { \alpha } { \cdot } \sigma _ { \mathrm { Z } } = 0 . 7 4 1
$$

$$
Z - { \mathrm { ~ E } } = 0 . 1 9 2 \qquad \quad \mathrm { ~ Z } + { \mathrm { ~ E } } = 1 . 6 7 4
$$

$0 . 1 9 2 < \mu _ { Z } < 1 . 6 7 4$ Intervalo de confianza para la media de Z

$$
\frac { \mathrm { e } ^ { 2 \cdot 0 . 1 9 2 } - 1 } { \mathrm { e } ^ { 2 \cdot 0 . 1 9 2 } + 1 } = 0 . 1 9 \qquad \frac { \mathrm { e } ^ { 2 \cdot 1 . 6 7 4 } - 1 } { \mathrm { e } ^ { 2 \cdot 1 . 6 7 4 } + 1 } = 0 . 9 3 2
$$

Vemos que el intervalo para ρ es bastante grande (ρ puede ir desde "no existe correlacion" hasta "excelente correlacion"). Esto muestra que los coeficientes de correlacion basados en muestra relativamente chicas suelen ser poco confiables.

# CORRELACION Y CAUSACION

En ocasiones, los cientíicos llegan a conclusiones injustiicadas al confundir una alta correlación observada por una relación de causa y efecto. La observación de que dos variables tienden a variar simultáneamente en la misma dirección no implica una relación directa entre ellas.

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

![](images/7b617754e40e58d316ac7a5bd10003cf6c6ae187b0a3fd843b6c1281a8a4ee28.jpg)

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

![](images/44de4171bf7ba05b43e3390a103bd5a23286a64b1d8bd25136a857c5a44222ad.jpg)

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

![](images/2b622681025e1d97c819d8ae43dbb2d7ba49d6ea3fb8dd2ea886253d7635fd48.jpg)  
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

![](images/caefb0c75d273d2667737c0a5345c168fbdde1e0272b51144843c80aa9fb0bc1.jpg)

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

![](images/0a9498571b7b1c945b6a458520b7cfdc85626a2141791233a069b6fcacbc0ff1.jpg)

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

![](images/4a4dafd59c9b080fe93326d2e36cc3f75018dd8197cad9570a2d3d7a3b41969a.jpg)

El estadístico para esta prueba es:

$$
\mathbf { t } = { \frac { \left[ \left( { \overline { { \mathbf { x } _ { 1 } } } } - { \overline { { \mathbf { x } _ { 2 } } } } \right) - \delta \right] } { \sqrt { \left( \mathbf { n } _ { 1 } - 1 \right) \cdot \left( \mathbf { s } _ { 1 } \right) ^ { 2 } + \left( \mathbf { n } _ { 2 } - 1 \right) \cdot \left( \mathbf { s } _ { 2 } \right) ^ { 2 } } } } \cdot { \sqrt { \frac { \mathbf { n } _ { 1 } \cdot \mathbf { n } _ { 2 } \cdot \left( \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } - 2 \right) } { \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } } } }
$$

$$
\mathbf { t } : = { \frac { \operatorname* { m e a n } ( \mathbf { y } \mathbf { 1 } ) - \operatorname* { m e a n } ( \mathbf { y } \mathbf { 2 } ) - 0 } { \sqrt { { \left( \mathbf { n } _ { 1 } - \mathbf { 1 } \right) } \cdot { \cfrac { \mathbf { n } _ { 1 } } { \mathbf { n } _ { 1 } } } \cdot \mathbf { v a r } ( \mathbf { y } \mathbf { 1 } ) + { \left( \mathbf { n } _ { 2 } - \mathbf { 1 } \right) } \cdot { \cfrac { \mathbf { n } _ { 2 } } { \mathbf { n } _ { 2 } - 1 } } \cdot \mathbf { v a r } ( \mathbf { y } \mathbf { 2 } ) } } }  \cdot { \sqrt { \frac { \mathbf { n } _ { 1 } \cdot \mathbf { n } _ { 2 } \cdot \left( \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } - \mathbf { 2 } \right) } { \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } } } }  = - 1 . 0 2 3
$$

![](images/96deff01195f2bf24d4b5a48845f66484c295bd16d6368a47cce02009cd191c0.jpg)

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

![](images/64512af65107262fcefb7702d74d809151aab93ac9f9aead56205651462fea1a.jpg)  
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

![](images/7bf7ae3261099853b72af7e9aa30c830e8249fc9bc336dc74cba8d42950b6c59.jpg)

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

![](images/41a50480b2409a4dde89bc01c9ae666ee515403cdcb2daf352aae34472562a83.jpg)

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

![](images/43b80fd8ce393edcca93dff0e768f87c633a1a87ab158398b0f7424269b31205.jpg)  
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

![](images/12b42386c130dabe0b26b53e339ea3410ff811e63c5ff9d2ff2d76dd80d16dde.jpg)

En consecuencia, se concluye que el Método C produce uniones con soldaduras significativamente más débiles que los Métodos A y B.

La eliminación de tres fuentes extrañas de variabilidad puede lograrse mediante el diseño de Cuadro Grecolatino. En un diseño consistente en un arreglo cuadrado de n letras latinas y n letras griegas; más exactamente, cada letra latina aparece sólo una vez al lado de cada letra griega:

<html><body><table><tr><td>Aa</td><td>Bβ</td><td>CY</td><td>D8</td></tr><tr><td>B8</td><td>AY</td><td>Dβ</td><td>Ca</td></tr><tr><td>cβ</td><td>Dα</td><td>A8</td><td>BY</td></tr><tr><td>DY</td><td>C8</td><td>Bα</td><td>Aβ</td></tr></table></body></html>

También se los llama “Cuadros Grecolatinos Ortogonales”. Como ejemplo, suponer el caso de las soldaduras, la temperatura es otra fuente de variabilidad. Si tres temperaturas de soldado, denotadas $\cdot$ , $\cdot$ y $\gamma$ se utilizan junto con los tres métodos, los tres operadores (renglones) y tres fundentes (columnas), la repetición de un experimento apropiado de Cuadro Grecolatino puede establecerse así:

<html><body><table><tr><td></td><td>Fundente1</td><td></td><td>Fundente2Fundente3</td></tr><tr><td>Operador 1</td><td>Aα</td><td>Bβ</td><td>CY</td></tr><tr><td>Operador 2</td><td>CY</td><td>Aβ</td><td>Bα</td></tr><tr><td>Operador3</td><td>Bβ</td><td>Ca</td><td>AY</td></tr></table></body></html>

Así pues, el Método A sería utilizado por el Operador 1, usando fundente 1, a la temperatura $\alpha$ , por el Operador 2, usando fundente 2, a la temperatura $\beta$ y por el Operador 3, usando fundente 3, a la temperatura $\gamma$ . En un Cuadro Grecolatino, cada variable (representada por renglones, columnas, letras latinas o letras griegas) está “distribuida equitativamente” respecto a las otras variables.