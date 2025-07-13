# Plan Visual - Conceptos Fundamentales de Estadística

## **FASE 2: STORYBOARD Y PLANIFICACIÓN VISUAL**

### **ESTRUCTURA GENERAL DEL VIDEO**
- **Duración estimada**: 12-15 minutos
- **Estilo visual**: Matemático universitario con animaciones dinámicas
- **Paleta de colores**: Azul (#2E86AB), Verde (#A23B72), Naranja (#F18F01), Púrpura (#C73E1D)

---

## **ESCENA 1: INTRODUCCIÓN Y TÍTULO (0:00 - 0:30)**

### **Elementos Visuales:**
- **MathTex principal**: "Estadística Aplicada II"
- **Subtitle**: "Conceptos Fundamentales"
- **Background**: NumberPlane tenue
- **Decoraciones**: Símbolos matemáticos flotantes (σ, μ, χ², t, F)

### **Código Manim:**
```python
# Título principal
titulo = MathTex(r"\text{Estadística Aplicada II}", font_size=72)
subtitulo = MathTex(r"\text{Conceptos Fundamentales}", font_size=48)

# Fondo matemático
fondo = NumberPlane(
    x_range=[-8, 8], y_range=[-6, 6],
    background_line_style={"stroke_opacity": 0.1}
)

# Símbolos flotantes
simbolos = VGroup(
    MathTex(r"\sigma", font_size=36),
    MathTex(r"\mu", font_size=36),
    MathTex(r"\chi^2", font_size=36),
    MathTex(r"t", font_size=36),
    MathTex(r"F", font_size=36)
)
```

### **Animaciones:**
1. `FadeIn(fondo)`
2. `Write(titulo)` con `shift=UP`
3. `Write(subtitulo)` con `shift=DOWN`
4. `LaggedStart(*[FadeIn(sym, shift=random_direction) for sym in simbolos])`
5. `Wait(2)`
6. `FadeOut(titulo, subtitulo, simbolos)`, mantener fondo

---

## **ESCENA 2: TEOREMA CENTRAL DEL LÍMITE (0:30 - 4:00)**

### **Sub-escena 2.1: Enunciado Matemático (0:30 - 1:30)**

#### **Elementos Visuales:**
- **Fórmula principal**: TCL completo con límite
- **Condiciones**: Destacadas en cajas
- **Interpretación visual**: Flecha hacia distribución normal

#### **Código Manim:**
```python
# Enunciado TCL
tcl_titulo = MathTex(
    r"\text{Teorema Central del Límite}",
    font_size=56, color=BLUE
)

tcl_formula = MathTex(
    r"\lim_{n \to \infty} P\left(\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \leq z\right) = \Phi(z)",
    font_size=48
)

# Condiciones
condiciones = VGroup(
    MathTex(r"X_1, X_2, \ldots \text{ i.i.d.}", font_size=36),
    MathTex(r"E[X_i] = \mu < \infty", font_size=36),
    MathTex(r"\text{Var}(X_i) = \sigma^2 < \infty", font_size=36)
)

# Cajas para destacar
cajas = VGroup(*[
    SurroundingRectangle(cond, buff=0.1, color=GREEN)
    for cond in condiciones
])
```

#### **Animaciones:**
1. `Write(tcl_titulo)`
2. `tcl_titulo.animate.to_corner(UP + LEFT)`
3. `Write(tcl_formula)`
4. `tcl_formula.animate.shift(UP)`
5. `LaggedStart(*[Write(cond) for cond in condiciones])`
6. `LaggedStart(*[Create(caja) for caja in cajas])`

### **Sub-escena 2.2: Visualización con Distribuciones (1:30 - 4:00)**

#### **Elementos Visuales:**
- **Axes**: Sistema coordenado para gráficos
- **Distribuciones**: Población original vs Normal limitante
- **Animación**: Convergencia de n pequeño a n grande
- **ValueTracker**: Para controlar n dinámicamente

#### **Código Manim:**
```python
# Sistema de ejes
axes = Axes(
    x_range=[-4, 4, 1], y_range=[0, 0.5, 0.1],
    x_length=10, y_length=6,
    axis_config={"color": WHITE}
)

# Etiquetas de ejes
labels = axes.get_axis_labels(
    x_label=MathTex(r"z = \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}}"),
    y_label=MathTex(r"f(z)")
)

# ValueTracker para n
n_tracker = ValueTracker(2)
n_display = DecimalNumber(
    n_tracker.get_value(),
    num_decimal_places=0
).add_updater(lambda m: m.set_value(n_tracker.get_value()))

# Función para distribución dependiente de n
def get_distribution_curve():
    n = n_tracker.get_value()
    if n <= 5:
        # Distribución más irregular para n pequeño
        return axes.plot(
            lambda x: 0.3 * np.exp(-0.8 * x**2) * (1 + 0.3 * np.sin(2*x)),
            color=RED, x_range=[-3, 3]
        )
    else:
        # Converge a normal estándar
        return axes.plot(
            lambda x: (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * x**2),
            color=BLUE, x_range=[-3, 3]
        )

# Curva que se actualiza automáticamente
curva = always_redraw(get_distribution_curve)

# Distribución normal de referencia
normal_ref = axes.plot(
    lambda x: (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * x**2),
    color=GREEN, stroke_width=2, stroke_dash=[5, 5]
)
```

#### **Animaciones:**
1. `Create(axes), Write(labels)`
2. `FadeIn(curva)`
3. `n_tracker.animate.set_value(30)` con `run_time=6`
4. `Create(normal_ref)`
5. `Transform(curva, normal_ref)` para mostrar convergencia

---

## **ESCENA 3: LEY DE LOS GRANDES NÚMEROS (4:00 - 7:30)**

### **Sub-escena 3.1: Enunciado Matemático (4:00 - 5:00)**

#### **Elementos Visuales:**
- **Título**: Ley de los Grandes Números
- **Fórmula**: Convergencia en probabilidad
- **Interpretación**: Texto explicativo

#### **Código Manim:**
```python
# Título LGN
lgn_titulo = MathTex(
    r"\text{Ley de los Grandes Números}",
    font_size=56, color=GREEN
)

# Enunciado formal
lgn_formula = MathTex(
    r"\lim_{n \to \infty} P\left(|\bar{X}_n - \mu| > \epsilon\right) = 0",
    font_size=48
)

# Equivalentemente
equivalente = MathTex(
    r"\bar{X}_n \xrightarrow{P} \mu \quad \text{cuando } n \to \infty",
    font_size=44
)

# Interpretación
interpretacion = MathTex(
    r"\text{La media muestral converge a la media poblacional}",
    font_size=36, color=YELLOW
)
```

#### **Animaciones:**
1. `Write(lgn_titulo)`
2. `lgn_titulo.animate.to_corner(UP + LEFT)`
3. `Write(lgn_formula)`
4. `lgn_formula.animate.shift(UP)`
5. `Write(equivalente)`
6. `Write(interpretacion)`

### **Sub-escena 3.2: Simulación Visual (5:00 - 7:30)**

#### **Elementos Visuales:**
- **Gráfico dinámico**: Media acumulada vs n
- **Línea horizontal**: μ verdadero
- **Puntos**: Medias muestrales para diferentes n
- **Convergencia visual**: Oscilación que decrece

#### **Código Manim:**
```python
# Ejes para simulación
sim_axes = Axes(
    x_range=[1, 100, 10], y_range=[0, 10, 2],
    x_length=12, y_length=7,
    x_axis_config={"numbers_to_include": range(10, 101, 20)},
    y_axis_config={"numbers_to_include": range(2, 11, 2)}
)

sim_labels = sim_axes.get_axis_labels(
    x_label=MathTex(r"n \text{ (tamaño muestral)}"),
    y_label=MathTex(r"\bar{X}_n")
)

# Línea de la media verdadera μ = 5
mu_line = sim_axes.plot(lambda x: 5, color=RED, stroke_width=3)
mu_label = MathTex(r"\mu = 5", color=RED).next_to(mu_line, UP)

# Datos simulados (predefinidos para consistencia)
n_values = list(range(1, 101))
medias_acumuladas = [
    5 + 2*np.exp(-n/20) * np.sin(n/3) + np.random.normal(0, 1/np.sqrt(n))
    for n in n_values
]

# Función para crear gráfico progresivo
def create_progressive_graph(up_to_n):
    points = [
        sim_axes.c2p(n, medias_acumuladas[n-1])
        for n in range(1, min(up_to_n + 1, 101))
    ]
    if len(points) <= 1:
        return Dot(points[0] if points else ORIGIN, radius=0.02, color=BLUE)
    return sim_axes.plot_line_graph(
        x_values=list(range(1, len(points) + 1)),
        y_values=medias_acumuladas[:len(points)],
        line_color=BLUE,
        vertex_dot_radius=0.02
    )

# ValueTracker para simulación progresiva
sim_n_tracker = ValueTracker(1)
grafico_progresivo = always_redraw(
    lambda: create_progressive_graph(int(sim_n_tracker.get_value()))
)
```

#### **Animaciones:**
1. `Create(sim_axes), Write(sim_labels)`
2. `Create(mu_line), Write(mu_label)`
3. `FadeIn(grafico_progresivo)`
4. `sim_n_tracker.animate.set_value(100)` con `run_time=8`
5. Efectos de zoom para mostrar convergencia final

---

## **ESCENA 4: DELTA METHOD (7:30 - 11:00)**

### **Sub-escena 4.1: Enunciado y Condiciones (7:30 - 9:00)**

#### **Elementos Visuales:**
- **Título**: Delta Method
- **Fórmula principal**: Con derivada de g
- **Condiciones**: g diferenciable, derivada no nula
- **Esquema visual**: Función g y su linealización

#### **Código Manim:**
```python
# Título Delta Method
delta_titulo = MathTex(
    r"\text{Delta Method}",
    font_size=56, color=PURPLE
)

# Enunciado principal
delta_formula = MathTex(
    r"\sqrt{n}(g(\bar{X}_n) - g(\mu)) \xrightarrow{d} N(0, [g'(\mu)]^2 \sigma^2)",
    font_size=42
)

# Condiciones
delta_condiciones = VGroup(
    MathTex(r"g \text{ diferenciable en } \mu", font_size=36),
    MathTex(r"g'(\mu) \neq 0", font_size=36),
    MathTex(r"\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} N(0, \sigma^2)", font_size=36)
)

# Interpretación
delta_interpretacion = MathTex(
    r"\text{Transformaciones de estimadores asintóticamente normales}",
    font_size=32, color=ORANGE
).shift(DOWN * 2)
```

#### **Animaciones:**
1. `Write(delta_titulo)`
2. `delta_titulo.animate.to_corner(UP + LEFT)`
3. `Write(delta_formula)`
4. `LaggedStart(*[Write(cond) for cond in delta_condiciones])`
5. `Write(delta_interpretacion)`

### **Sub-escena 4.2: Ejemplo Visual con g(x) = x² (9:00 - 11:00)**

#### **Elementos Visuales:**
- **Función g(x) = x²**: Gráfico curvo
- **Tangente en μ**: Aproximación lineal
- **Distribución original**: En el eje X
- **Distribución transformada**: En el eje Y
- **Comparación**: Normal teórica vs empírica

#### **Código Manim:**
```python
# Ejes para Delta Method
delta_axes = Axes(
    x_range=[0, 6, 1], y_range=[0, 25, 5],
    x_length=10, y_length=8,
    axis_config={"color": WHITE}
)

delta_labels = delta_axes.get_axis_labels(
    x_label=MathTex(r"x"), y_label=MathTex(r"g(x) = x^2")
)

# Función g(x) = x²
g_function = delta_axes.plot(lambda x: x**2, color=BLUE, x_range=[0.5, 5])
g_label = MathTex(r"g(x) = x^2", color=BLUE).next_to(g_function, UP)

# Punto μ = 2
mu_point = Dot(delta_axes.c2p(2, 4), color=RED, radius=0.08)
mu_coords = MathTex(r"(\mu, g(\mu))", color=RED).next_to(mu_point, UR)

# Tangente en μ = 2: g'(2) = 4
tangent_line = delta_axes.plot(
    lambda x: 4 + 4*(x - 2),  # g(2) + g'(2)(x - 2)
    color=GREEN, x_range=[1, 3], stroke_dash=[3, 3]
)
tangent_label = MathTex(
    r"y = g(\mu) + g'(\mu)(x - \mu)", color=GREEN, font_size=32
).to_corner(UP + RIGHT)

# Distribución en X (entrada)
x_dist_center = delta_axes.c2p(2, 0)
x_distribution = VGroup(*[
    Dot(delta_axes.c2p(2 + 0.5*np.sin(i*0.3), 0), radius=0.03, color=YELLOW)
    for i in range(20)
])

# Distribución en Y (salida transformada)
y_dist_center = delta_axes.c2p(0, 4)
y_distribution = VGroup(*[
    Dot(delta_axes.c2p(0, 4 + 2*np.sin(i*0.3)), radius=0.03, color=ORANGE)
    for i in range(20)
])

# Flechas de transformación
arrows = VGroup(*[
    Arrow(
        delta_axes.c2p(2 + 0.1*np.sin(i*0.5), 0),
        delta_axes.c2p(2 + 0.1*np.sin(i*0.5), (2 + 0.1*np.sin(i*0.5))**2),
        buff=0, stroke_width=2, color=GRAY
    ) for i in range(10)
])
```

#### **Animaciones:**
1. `Create(delta_axes), Write(delta_labels)`
2. `Create(g_function), Write(g_label)`
3. `Create(mu_point), Write(mu_coords)`
4. `FadeIn(x_distribution)`
5. `LaggedStart(*[Create(arrow) for arrow in arrows])`
6. `FadeIn(y_distribution)`
7. `Create(tangent_line), Write(tangent_label)`

---

## **ESCENA 5: SÍNTESIS Y CONEXIONES (11:00 - 12:30)**

### **Elementos Visuales:**
- **Diagrama conceptual**: Los tres teoremas conectados
- **Flechas**: Relaciones entre conceptos
- **Aplicaciones**: Ejemplos prácticos
- **Resumen**: Puntos clave

#### **Código Manim:**
```python
# Círculos para cada teorema
circulo_tcl = Circle(radius=1.5, color=BLUE).shift(UP + LEFT * 3)
circulo_lgn = Circle(radius=1.5, color=GREEN).shift(UP + RIGHT * 3)
circulo_delta = Circle(radius=1.5, color=PURPLE).shift(DOWN)

# Etiquetas
label_tcl = MathTex(r"\text{TCL}", font_size=36).move_to(circulo_tcl)
label_lgn = MathTex(r"\text{LGN}", font_size=36).move_to(circulo_lgn)
label_delta = MathTex(r"\text{Delta}", font_size=36).move_to(circulo_delta)

# Conectores
flecha_1 = Arrow(circulo_tcl.get_right(), circulo_lgn.get_left(), buff=0.1)
flecha_2 = Arrow(circulo_tcl.get_bottom(), circulo_delta.get_top() + LEFT, buff=0.1)
flecha_3 = Arrow(circulo_lgn.get_bottom(), circulo_delta.get_top() + RIGHT, buff=0.1)

# Texto central
conexion_central = MathTex(
    r"\text{Teoría Asintótica}", font_size=48, color=YELLOW
).shift(UP * 2.5)

# Aplicaciones
aplicaciones = VGroup(
    MathTex(r"\text{• Intervalos de confianza}", font_size=28),
    MathTex(r"\text{• Pruebas de hipótesis}", font_size=28),
    MathTex(r"\text{• Estimación por máxima verosimilitud}", font_size=28),
    MathTex(r"\text{• Métodos robustos}", font_size=28)
).arrange(DOWN, aligned_edge=LEFT).shift(DOWN * 2.5 + RIGHT * 3)
```

#### **Animaciones:**
1. `LaggedStart(*[Create(circ) for circ in [circulo_tcl, circulo_lgn, circulo_delta]])`
2. `LaggedStart(*[Write(label) for label in [label_tcl, label_lgn, label_delta]])`
3. `LaggedStart(*[Create(flecha) for flecha in [flecha_1, flecha_2, flecha_3]])`
4. `Write(conexion_central)`
5. `LaggedStart(*[Write(app) for app in aplicaciones])`

---

## **ESCENA 6: CIERRE Y NEXT STEPS (12:30 - 13:00)**

### **Elementos Visuales:**
- **Mensaje final**: "Próximo: Pruebas de Hipótesis"
- **Fade out**: Todos los elementos
- **Logo/Signature**: Matemática elegante

#### **Código Manim:**
```python
# Mensaje final
mensaje_final = VGroup(
    MathTex(r"\text{Próximo Video:}", font_size=44),
    MathTex(r"\text{Pruebas de Hipótesis}", font_size=52, color=BLUE),
    MathTex(r"\text{Estadística Aplicada II}", font_size=32, color=GRAY)
).arrange(DOWN)

# Decoración matemática
decoracion = MathTex(
    r"\int_{-\infty}^{\infty} f(x) dx = 1",
    font_size=24, color=GRAY, fill_opacity=0.3
).to_corner(DOWN + RIGHT)
```

#### **Animaciones:**
1. `FadeOut(*[todo_lo_anterior])`
2. `Write(mensaje_final[0])`
3. `Write(mensaje_final[1])` con efecto especial
4. `Write(mensaje_final[2])`
5. `FadeIn(decoracion)`
6. `Wait(3)`
7. `FadeOut(*[todo])`

---

## **CONFIGURACIÓN TÉCNICA**

### **Resolución y Calidad:**
```python
# En config
config.frame_rate = 60
config.pixel_height = 1080
config.pixel_width = 1920
config.background_color = "#0E1117"  # Azul muy oscuro
```

### **Paleta de Colores Personalizada:**
```python
# Colores personalizados
AZUL_ESTADISTICA = "#2E86AB"
VERDE_ESTADISTICA = "#A23B72"
NARANJA_ESTADISTICA = "#F18F01"
PURPURA_ESTADISTICA = "#C73E1D"
GRIS_TEXTO = "#8E9AAF"
```

### **Fuentes y Estilos:**
```python
# Configuración de texto
MathTex.set_default(font_size=40)
Tex.set_default(font_size=36)

# Template personalizado si es necesario
from manim import TexTemplate
custom_template = TexTemplate()
custom_template.add_to_preamble(r"\usepackage{amsmath, amssymb, amsthm}")
```

---

## **NOTAS DE IMPLEMENTACIÓN**

1. **Timing**: Cada sub-escena debe tener transiciones suaves de 0.5-1 segundo
2. **Audio Sync**: Las animaciones deben coincidir con el guion narrado
3. **Performance**: Usar `always_redraw` con cuidado para no sobrecargar
4. **Consistencia**: Mantener mismo estilo de ejes y colores en todo el video
5. **Testing**: Renderizar cada escena por separado antes del video completo

**¡El plan visual está completo y listo para la implementación en Python/Manim!**
