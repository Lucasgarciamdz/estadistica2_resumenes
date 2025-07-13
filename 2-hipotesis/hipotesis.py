from manim import *

class PruebasDeHipotesis(Scene):
    def construct(self):
        # Paleta de colores
        COLOR_H0 = BLUE_D
        COLOR_H1 = GREEN_C
        COLOR_ERROR = RED_D
        COLOR_TEXTO = WHITE

        # Configuración inicial
        self.camera.background_color = "#1E1E1E"

        # --- Escena 1: Título e Introducción ---
        titulo = Tex("Unidad 2: Pruebas de Hipótesis", color=COLOR_TEXTO).scale(1.2)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # --- Escena 2: Lógica Fundamental ---
        titulo_escena = Tex("La Lógica de una Prueba de Hipótesis", color=COLOR_TEXTO).to_edge(UP)
        self.play(Write(titulo_escena))

        h0 = MathTex("H_0: \mu = 10000", color=COLOR_H0).shift(UP*2)
        h1 = MathTex("H_1: \mu < 10000", color=COLOR_H1).next_to(h0, DOWN)

        self.play(Write(h0))
        self.play(Write(h1))
        self.wait(2)

        # Tabla de Errores
        tabla_errores = Table(
            [["", "Aceptar H0", "Rechazar H0"],
             ["H0 Verdadera", "Correcto", "Error Tipo I (alpha)"],
             ["H0 Falsa", "Error Tipo II (beta)", "Correcto"]],
            include_outer_lines=True
        ).scale(0.5).next_to(h1, DOWN, buff=1)

        tabla_errores.get_cell((2,3)).set_color(COLOR_ERROR)
        tabla_errores.get_cell((3,2)).set_color(COLOR_ERROR)

        self.play(Create(tabla_errores))
        self.wait(3)
        self.play(FadeOut(h0, h1, tabla_errores, titulo_escena))

        # --- Escena 3: Pasos de una Prueba de Hipótesis ---
        titulo_escena = Tex("5 Pasos de una Prueba de Hipótesis", color=COLOR_TEXTO).to_edge(UP)
        self.play(Write(titulo_escena))

        pasos = VGroup(
            Tex("1. Formular Hipótesis ($H_0, H_1$)"),
            Tex("2. Establecer Nivel de Significancia (alpha)"),
            Tex("3. Construir Criterio de Decisión (Estadístico y Región de Rechazo)"),
            Tex("4. Calcular Estadístico de Prueba"),
            Tex("5. Tomar una Decisión")
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).scale(0.8).shift(LEFT*3)

        for i, paso in enumerate(pasos):
            self.play(Write(paso))
            if i == 2:
                # Animación del estadístico t
                t_formula = MathTex("t = \\frac{\\bar{x} - \\mu_0}{s / \\sqrt{n}}", color=YELLOW_B).scale(0.8).next_to(paso, RIGHT, buff=1)
                self.play(Write(t_formula))
            self.wait(1)
        self.wait(3)
        self.play(FadeOut(pasos, titulo_escena, t_formula))

        # --- Escena 4: Región de Rechazo ---
        titulo_escena = Tex("Región de Rechazo y Valor Crítico", color=COLOR_TEXTO).to_edge(UP)
        self.play(Write(titulo_escena))

        axes = Axes(x_range=[-4, 4, 1], y_range=[0, 0.5, 0.1], x_length=10, y_length=5).shift(DOWN*0.5)
        t_dist = axes.plot(lambda x: (1/np.sqrt(2*np.pi))*np.exp(-x**2/2), color=COLOR_H0)

        self.play(Create(axes), Create(t_dist))

        # Cola izquierda
        valor_critico = -1.8
        region_rechazo = axes.get_area(t_dist, x_range=(-4, valor_critico), color=COLOR_ERROR, opacity=0.8)
        label_rechazo = Tex("Región de Rechazo", color=COLOR_ERROR).scale(0.7).next_to(region_rechazo, DOWN)
        linea_critica = axes.get_vertical_line(axes.c2p(valor_critico, 0.5), color=RED)
        label_critico = MathTex("t_c", color=RED).next_to(linea_critica, DOWN)

        self.play(Create(region_rechazo), Write(label_rechazo))
        self.play(Create(linea_critica), Write(label_critico))

        # Estadístico de prueba
        t_obs_val = -2.5
        t_obs_dot = Dot(axes.c2p(t_obs_val, 0), color=YELLOW_B)
        t_obs_label = MathTex("t_{obs}", color=YELLOW_B).next_to(t_obs_dot, UP)
        self.play(FadeIn(t_obs_dot, scale=0.5), Write(t_obs_label))
        self.wait(1)

        # Decisión
        decision = Tex("Rechazar $H_0$", color=GREEN_C).scale(1.2).shift(UP*2)
        self.play(Write(decision))
        self.wait(3)