from manim import *

class ConceptosFundamentales(Scene):
    def construct(self):
        # Paleta de colores
        COLOR_POBLACION = BLUE_D
        COLOR_MUESTRA = GREEN_C
        COLOR_TEOREMA = YELLOW_B
        COLOR_TEXTO = WHITE

        # Configuración inicial
        self.camera.background_color = "#1E1E1E"

        # --- Escena 1: Título e Introducción ---
        titulo = Tex("Unidad 1: Conceptos Fundamentales", color=COLOR_TEXTO).scale(1.2)
        subtitulo = Tex("El Puente hacia la Inferencia Estadística", color=COLOR_TEOREMA).next_to(titulo, DOWN)
        self.play(Write(titulo))
        self.play(FadeIn(subtitulo, shift=UP))
        self.wait(2)
        self.play(FadeOut(titulo), FadeOut(subtitulo))

        # --- Escena 2: Población vs. Muestra ---
        titulo_escena = Tex("Población vs. Muestra", color=COLOR_TEXTO).to_edge(UP)
        self.play(Write(titulo_escena))

        # Población
        poblacion = VGroup(*[Dot(color=COLOR_POBLACION) for _ in range(100)]).arrange_in_grid(10, 10, buff=0.3)
        poblacion_rect = SurroundingRectangle(poblacion, color=COLOR_POBLACION, buff=0.3)
        poblacion_label = Tex("Población (N)", color=COLOR_POBLACION).next_to(poblacion_rect, UP)
        parametro_mu = MathTex(r"\mu, \sigma^2", color=COLOR_POBLACION).next_to(poblacion_rect, DOWN)
        self.play(Create(poblacion), Write(poblacion_label))
        self.play(Write(parametro_mu))
        self.wait(1)

        # Muestra
        indices_muestra = [13, 24, 35, 46, 57, 68, 79, 80, 91, 2]
        muestra = VGroup(*[poblacion[i].copy() for i in indices_muestra])
        muestra.set_color(COLOR_MUESTRA)
        muestra_rect = SurroundingRectangle(muestra, color=COLOR_MUESTRA, buff=0.3)
        muestra_label = Tex("Muestra (n)", color=COLOR_MUESTRA).next_to(muestra_rect, UP)
        estimador_x_bar = MathTex(r"\bar{x}, s^2", color=COLOR_MUESTRA).next_to(muestra_rect, DOWN)

        self.play(TransformFromCopy(VGroup(*[poblacion[i] for i in indices_muestra]), muestra))
        self.play(Create(muestra_rect), Write(muestra_label))
        self.play(Write(estimador_x_bar))
        self.wait(3)
        self.play(FadeOut(poblacion, poblacion_rect, poblacion_label, parametro_mu, muestra, muestra_rect, muestra_label, estimador_x_bar, titulo_escena))

        # --- Escena 3: Propiedades de los Estimadores ---
        titulo_escena = Tex("Propiedades de los Estimadores", color=COLOR_TEXTO).to_edge(UP)
        self.play(Write(titulo_escena))

        propiedades = VGroup(
            Tex("1. Insesgadez:", " $E(\hat{\theta}) = \theta$"),
            Tex("2. Eficiencia:", " $Var(\hat{\theta}_1) < Var(\hat{\theta}_2)$ "),
            Tex("3. Consistencia:", " $\lim_{n \to \infty} P(|\hat{\theta}_n - \theta| < \epsilon) = 1$ ")
        ).arrange(DOWN, buff=0.7, aligned_edge=LEFT).scale(0.9).shift(LEFT*2)

        for prop in propiedades:
            prop[0].set_color(COLOR_TEOREMA)
            self.play(Write(prop))
            self.wait(1.5)
        self.wait(2)
        self.play(FadeOut(propiedades, titulo_escena))

        # --- Escena 4: Teorema Central del Límite ---
        titulo_escena = Tex("Teorema Central del Límite (TCL)", color=COLOR_TEOREMA).to_edge(UP)
        self.play(Write(titulo_escena))

        # Distribución de la población (no normal)
        axes_poblacion = Axes(x_range=[0, 10, 2], y_range=[0, 0.4, 0.1], x_length=5, y_length=3).shift(UP*1.5 + LEFT*3.5)
        dist_poblacion = axes_poblacion.plot(lambda x: 0.2, x_range=[2,7], color=COLOR_POBLACION)
        label_poblacion = Tex("Población Original (No Normal)", color=COLOR_POBLACION).scale(0.7).next_to(axes_poblacion, DOWN)
        self.play(Create(axes_poblacion), Create(dist_poblacion), Write(label_poblacion))
        self.wait(1)

        # Distribución de las medias muestrales (normal)
        axes_medias = Axes(x_range=[0, 10, 2], y_range=[0, 1, 0.2], x_length=5, y_length=3).shift(UP*1.5 + RIGHT*3.5)
        dist_medias = axes_medias.plot(lambda x: np.exp(-0.5 * ((x - 4.5) / 0.8)**2), color=COLOR_MUESTRA)
        label_medias = Tex("Distribución de Medias Muestrales (Normal)", color=COLOR_MUESTRA).scale(0.7).next_to(axes_medias, DOWN)
        self.play(Create(axes_medias), Create(dist_medias), Write(label_medias))
        self.wait(1)

        # Flecha de transformación
        arrow = Arrow(axes_poblacion.get_right(), axes_medias.get_left(), buff=0.5, color=WHITE)
        tcl_label = Tex("TCL", color=COLOR_TEOREMA).next_to(arrow, UP)
        self.play(GrowArrow(arrow), Write(tcl_label))
        self.wait(2)

        # Fórmula del TCL
        formula_tcl = MathTex(r"Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)", color=COLOR_TEXTO).scale(1.1).next_to(VGroup(axes_poblacion, axes_medias), DOWN, buff=1)
        self.play(Write(formula_tcl))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo_escena, axes_poblacion, dist_poblacion, label_poblacion, axes_medias, dist_medias, label_medias, arrow, tcl_label, formula_tcl)))