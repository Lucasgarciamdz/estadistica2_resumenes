from manim import *
from math import erf, gamma

class Introduccion(Scene):
    def construct(self):
        # Paleta de colores y configuración
        COLOR_TEXTO = WHITE
        self.camera.background_color = "#1E1E1E"

        # Título de la unidad
        titulo = Tex("Unidad 2: Pruebas de Hipótesis", color=COLOR_TEXTO).scale(1.5)
        self.play(Write(titulo))
        self.wait(2)

        # Transición a la lógica
        subtitulo = Tex("De la Estimación a la Toma de Decisiones", color=BLUE_C).scale(1.1)
        self.play(Transform(titulo, subtitulo))
        self.wait(2)
        self.play(FadeOut(titulo))

class LogicaDePrueba(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        COLOR_H0 = BLUE_D
        COLOR_H1 = GREEN_C
        COLOR_TEXTO = WHITE

        # Título de la escena
        titulo_escena = Tex("La Lógica de una Prueba de Hipótesis", color=COLOR_TEXTO).to_edge(UP)
        self.play(Write(titulo_escena))

        # Analogía del juicio
        balanza = VGroup(
            Line(LEFT + UP, RIGHT + UP),
            Line(ORIGIN, UP),
            Polygon(LEFT + UP, LEFT + DOWN, RIGHT + DOWN, RIGHT + UP, stroke_width=0),
        ).scale(0.5).shift(UP*0.5)
        presuncion = Tex("Presunción de Inocencia", color=COLOR_TEXTO).next_to(balanza, DOWN)
        self.play(FadeIn(balanza), Write(presuncion))
        self.wait(2)

        # Hipótesis Nula y Alternativa
        h0 = MathTex("H_0: \\mu = 500 \\text{ horas}", color=COLOR_H0).shift(UP*2.5)
        h1 = MathTex("H_1: \\mu < 500 \\text{ horas}", color=COLOR_H1).next_to(h0, DOWN)

        self.play(Transform(presuncion, h0))
        self.play(Write(h1))
        self.wait(2)

        # Recolectar evidencia
        evidencia = Tex("Evidencia (Muestra)", color=YELLOW_B).next_to(h1, DOWN, buff=1)
        self.play(Write(evidencia))
        self.wait(2)

        # Decisión
        decision = Tex("¿Es la evidencia 'rara' si H0 es cierta?", color=RED_B).next_to(evidencia, DOWN, buff=1)
        self.play(Write(decision))
        self.wait(3)
        self.play(FadeOut(balanza, presuncion, h1, evidencia, decision, titulo_escena))

class Errores(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        COLOR_ERROR_I = RED_D
        COLOR_ERROR_II = ORANGE

        titulo = Tex("Errores en la Toma de Decisiones", color=WHITE).to_edge(UP)
        self.play(Write(titulo))

        # Tabla de Errores
        tabla = Table(
            [["", "Decisión: No Rechazar $H_0$", "Decisión: Rechazar $H_0$"],
             ["Realidad: $H_0$ es Verdadera", "Decisión Correcta\n(1 - $\\alpha$)", "Error Tipo I\n(Falso Positivo)"],
             ["Realidad: $H_0$ es Falsa", "Error Tipo II\n(Falso Negativo)", "Decisión Correcta\n(Potencia, 1 - $\\beta$)"]],
            row_labels=[Text(""), Text("Realidad: $H_0$ Verdadera"), Text("Realidad: $H_0$ Falsa")],
            col_labels=[Text(""), Text("No Rechazar $H_0$"), Text("Rechazar $H_0$")],
            include_outer_lines=True
        ).scale(0.5)

        # Colorear celdas de error
        tabla.get_cell((2, 3)).set_color(COLOR_ERROR_I)
        tabla.get_cell((3, 2)).set_color(COLOR_ERROR_II)

        self.play(Create(tabla))

        # Explicaciones
        error1_exp = Tex("Error Tipo I ($\\alpha$): Rechazar $H_0$ cuando es verdadera.", color=COLOR_ERROR_I).next_to(tabla, DOWN, buff=0.5)
        error2_exp = Tex("Error Tipo II ($\\beta$): No rechazar $H_0$ cuando es falsa.", color=COLOR_ERROR_II).next_to(error1_exp, DOWN, buff=0.5)

        self.play(Write(error1_exp))
        self.wait(2)
        self.play(Write(error2_exp))
        self.wait(3)
        self.play(FadeOut(tabla, titulo, error1_exp, error2_exp))

class PasosPrueba(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        titulo = Tex("Los 5 Pasos de una Prueba de Hipótesis", color=WHITE).to_edge(UP)
        self.play(Write(titulo))

        pasos = VGroup(
            Tex("1. Formular Hipótesis ($H_0, H_1$)"),
            Tex("2. Establecer Nivel de Significancia ($\\alpha$)"),
            Tex("3. Calcular el Estadístico de Prueba"),
            Tex("4. Determinar la Regla de Decisión (Valor Crítico o p-valor)"),
            Tex("5. Tomar una Decisión y Concluir")
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).scale(0.8).shift(LEFT*3)

        for paso in pasos:
            self.play(Write(paso))
            self.wait(1.5)

        self.wait(3)
        self.play(FadeOut(pasos, titulo))

class PruebaParaMedia(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        titulo = Tex("TEMA A-2: Hipótesis para una Media", color=WHITE).to_edge(UP)
        self.play(Write(titulo))

        # Datos del problema
        datos_texto = VGroup(
            Tex("Problema: ¿Ha disminuido la duración de las bombillas?"),
            MathTex("H_0: \\mu = 1120"),
            MathTex("H_1: \\mu < 1120"),
            MathTex("\\bar{x} = 1070, s = 125, n = 8, \\alpha = 0.05")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.7).to_edge(LEFT, buff=1)
        self.play(Write(datos_texto))
        self.wait(2)

        # Gráfico de la distribución t
        axes = Axes(x_range=[-4, 4, 1], y_range=[0, 0.5, 0.1], x_length=8, y_length=4).to_edge(RIGHT, buff=1)
        t_dist = axes.plot(lambda x: (1/np.sqrt(7*np.pi)) * (gamma(4)/gamma(3.5)) * (1 + x**2/7)**(-4), color=BLUE_C)

        self.play(Create(axes), Create(t_dist))

        # Región de rechazo
        gl = 7
        alpha = 0.05
        from scipy.stats import t
        t_critico = t.ppf(alpha, gl) # -1.895

        region_rechazo = axes.get_area(t_dist, x_range=(-4, t_critico), color=RED_D, opacity=0.7)
        label_rechazo = Tex("Región de Rechazo", color=RED_D).scale(0.6).next_to(region_rechazo, DOWN)
        self.play(Create(region_rechazo), Write(label_rechazo))

        # Cálculo del estadístico t
        t_formula = MathTex("t = \\frac{\\bar{x} - \\mu_0}{s / \\sqrt{n}}", color=YELLOW_B).next_to(datos_texto, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(t_formula))
        t_calculado_val = (1070 - 1120) / (125 / np.sqrt(8)) # -1.13
        t_calculado = MathTex(f"t = \\frac{{1070 - 1120}}{{125 / \\sqrt{{8}}}} = {t_calculado_val:.2f}", color=YELLOW_B).move_to(t_formula)
        self.play(Transform(t_formula, t_calculado))

        # Visualizar t_calculado
        dot = Dot(axes.c2p(t_calculado_val, 0), color=YELLOW_B)
        label_dot = MathTex(f"t_{{obs}}={t_calculado_val:.2f}", color=YELLOW_B).next_to(dot, UP)
        self.play(FadeIn(dot), Write(label_dot))

        # Decisión
        decision = Tex("Decisión: No Rechazar $H_0$", color=GREEN_C).scale(1.1).shift(DOWN*2.5)
        self.play(Write(decision))
        self.wait(4)

class CurvasOC(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        titulo = Tex("TEMA B: Curvas Características de Operación (OC)", color=WHITE).to_edge(UP)
        self.play(Write(titulo))

        axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 1.1, 0.2],
            x_length=10, y_length=5.5,
            x_axis_config={"name": "d = |mu - mu0| / sigma"},
            y_axis_config={"name": "Prob(Aceptar H0)"}
        ).shift(DOWN*0.5)

        self.play(Create(axes))

        # Curvas para diferentes n
        def curva_oc(d, n):
            z_alpha = 1.645 # para alpha=0.05, una cola
            beta = 0.5 + 0.5 * erf((z_alpha - d * np.sqrt(n)) / np.sqrt(2))
            return beta

        curva_n10 = axes.plot(lambda d: curva_oc(d, 10), color=BLUE, x_range=[0, 4])
        label_n10 = Tex("n=10", color=BLUE).next_to(curva_n10, RIGHT)

        curva_n30 = axes.plot(lambda d: curva_oc(d, 30), color=GREEN, x_range=[0, 4])
        label_n30 = Tex("n=30", color=GREEN).next_to(curva_n30, RIGHT)

        curva_n100 = axes.plot(lambda d: curva_oc(d, 100), color=YELLOW, x_range=[0, 4])
        label_n100 = Tex("n=100", color=YELLOW).next_to(curva_n100, RIGHT)

        self.play(Create(curva_n10), Write(label_n10))
        self.play(Create(curva_n30), Write(label_n30))
        self.play(Create(curva_n100), Write(label_n100))

        # Explicación
        explicacion = Tex("A mayor tamaño de muestra (n), la prueba es más potente.", color=WHITE).scale(0.8).to_edge(DOWN)
        self.play(Write(explicacion))
        self.wait(4)

class PruebaDosMedias(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        titulo = Tex("TEMA B-3: Hipótesis para dos Medias", color=WHITE).to_edge(UP)
        self.play(Write(titulo))

        # Hipótesis
        hipotesis = VGroup(
            Tex("¿El fertilizante aumenta la producción?"),
            MathTex("H_0: \\mu_1 = \\mu_2 \\quad (\\text{o } \\mu_1 - \\mu_2 = 0)"),
            MathTex("H_1: \\mu_1 > \\mu_2")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).shift(UP*2)
        self.play(Write(hipotesis))

        # Fórmula del estadístico t para dos muestras
        t_formula = MathTex(
            "t = \\frac{(\\bar{x}_1 - \\bar{x}_2) - (\\mu_1 - \\mu_2)_0}{\\sqrt{s_p^2 (\\frac{1}{n_1} + \\frac{1}{n_2})}}",
            "s_p^2 = \\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}"
        ).arrange(DOWN).scale(0.8).next_to(hipotesis, DOWN, buff=1)
        self.play(Write(t_formula))

        # Ejemplo de decisión
        ejemplo = Tex("Ejemplo: Si $t_{obs} = 1.85$ y $t_{crit} = 1.72$, entonces...", color=YELLOW_B).next_to(t_formula, DOWN, buff=1)
        decision = Tex("Rechazamos $H_0$. El fertilizante es efectivo.", color=GREEN_C).next_to(ejemplo, DOWN)
        self.play(Write(ejemplo))
        self.wait(1)
        self.play(Write(decision))
        self.wait(4)

class ResumenFinal(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        titulo = Tex("Resumen de la Unidad 2", color=WHITE).to_edge(UP)
        self.play(Write(titulo))

        puntos_clave = VGroup(
            Tex("- Lógica de las pruebas de hipótesis (H0, H1)."),
            Tex("- Errores Tipo I ($\\alpha$) y Tipo II ($\\beta$)."),
            Tex("- Los 5 pasos de una prueba."),
            Tex("- Pruebas para una y dos medias (Z y t)."),
            Tex("- Curvas OC y potencia de la prueba."),
            Tex("- La importancia de concluir en contexto.")
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).scale(0.9)

        for punto in puntos_clave:
            self.play(Write(punto))
            self.wait(1.5)

        proximos_pasos = Tex("¡Nos vemos en la Unidad 3!", color=BLUE_C).scale(1.2).to_edge(DOWN)
        self.play(Write(proximos_pasos))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
