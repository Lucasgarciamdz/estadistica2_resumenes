from manim import *
import numpy as np

class AjusteDeCurvasVideo(Scene):
    def construct(self):
        # --- SECCIÓN 1: INTRODUCCIÓN ---
        self.intro_ajuste_curvas()

        # --- SECCIÓN 2: REGRESIÓN SIMPLE ---
        self.regresion_lineal_simple()

        # --- SECCIÓN 3: INFERENCIAS ---
        self.inferencias_regresion()

        # --- SECCIÓN 4: REGRESIÓN CURVILÍNEA ---
        self.regresion_curvilinea()

        # --- SECCIÓN 5: REGRESIÓN MÚLTIPLE Y POLINÓMICA ---
        self.regresion_multiple_polinomica()

        # --- SECCIÓN 6: SELECCIÓN DEL MODELO Y CORRELACIÓN ---
        self.seleccion_modelo_correlacion()

        # --- SECCIÓN 7: CIERRE ---
        self.cierre()

    def intro_ajuste_curvas(self):
        titulo = Tex(r"Unidad 5: Ajuste de Curvas", font_size=48, color=BLUE_D)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Datos de ejemplo (Tensión Arterial vs Edad)
        datos = np.array([
            [20, 120], [25, 125], [30, 130], [35, 128], [40, 135],
            [45, 140], [50, 142], [55, 148], [60, 155], [65, 158]
        ])

        axes = Axes(
            x_range=[15, 70, 5],
            y_range=[110, 170, 10],
            x_length=9,
            y_length=6,
            axis_config={"color": GRAY},
            x_axis_config={"numbers_to_include": np.arange(20, 71, 10), "label_direction": DOWN},
            y_axis_config={"numbers_to_include": np.arange(120, 171, 10)},
        ).add_coordinates()

        x_label = axes.get_x_axis_label("Edad", edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label("Tensión Arterial", edge=LEFT, direction=LEFT, buff=0.4)

        puntos = VGroup(*[Dot(axes.c2p(x, y), color=YELLOW) for x, y in datos])

        intro_text = Tex("¿Relación entre dos variables?", font_size=36).to_edge(UP)
        self.play(Write(intro_text))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in puntos]), run_time=2)
        self.wait(2)

        pregunta = Tex("¿Cómo predecir 'y' a partir de 'x'?", font_size=36).next_to(intro_text, DOWN)
        self.play(Write(pregunta))
        self.wait(2)

        # Línea "a ojo"
        linea_ojo = axes.plot(lambda x: 1.1 * x + 95, color=RED)
        self.play(Create(linea_ojo))
        self.play(linea_ojo.animate.set_color(WHITE), run_time=1)
        self.play(FadeOut(linea_ojo, intro_text, pregunta, puntos, axes, x_label, y_label))

    def regresion_lineal_simple(self):
        titulo = Tex("Tema A: Regresión Lineal Simple", font_size=40).to_edge(UP)
        self.play(Write(titulo))

        ecuacion_recta = MathTex(r"y = a + bx", font_size=48).shift(UP*1.5)
        self.play(Write(ecuacion_recta))
        self.wait(2)

        # Residuos
        axes = Axes(x_range=[0, 5], y_range=[0, 5], x_length=5, y_length=5).add_coordinates()
        datos_simples = np.array([[1, 2], [2, 3], [3, 4.5], [4, 4]])
        puntos = VGroup(*[Dot(axes.c2p(x, y), color=YELLOW) for x, y in datos_simples])
        recta_ajuste = axes.plot(lambda x: 0.8*x + 1.2, color=BLUE)

        residuos = VGroup()
        for x, y in datos_simples:
            punto_en_recta = axes.c2p(x, 0.8*x + 1.2)
            residuo = DashedLine(axes.c2p(x, y), punto_en_recta, color=RED)
            residuos.add(residuo)

        self.play(Create(axes), Create(puntos), Create(recta_ajuste))
        self.play(Create(residuos))
        self.wait(2)

        # Mínimos Cuadrados
        formula_mc = MathTex(r"\text{Minimizar } \sum (y_i - \hat{y}_i)^2 = \sum e_i^2", font_size=48).next_to(axes, DOWN, buff=0.5)
        self.play(Write(formula_mc))
        self.wait(3)
        self.play(FadeOut(titulo, ecuacion_recta, axes, puntos, recta_ajuste, residuos, formula_mc))

    def inferencias_regresion(self):
        titulo = Tex("Inferencias en Regresión", font_size=40).to_edge(UP)
        self.play(Write(titulo))

        # Intervalos de confianza
        axes = Axes(x_range=[0, 10], y_range=[0, 10], x_length=8, y_length=6)
        recta = axes.plot(lambda x: 0.5*x + 2, color=BLUE)
        banda_confianza = axes.get_area(
            graph=axes.plot(lambda x: 0.5*x + 2.5, color=GREEN),
            x_range=[0, 10],
            color=GREEN,
            opacity=0.3
        )
        banda_confianza_inf = axes.get_area(
            graph=axes.plot(lambda x: 0.5*x + 1.5, color=GREEN),
            x_range=[0, 10],
            color=GREEN,
            opacity=0.3
        )

        ic_texto = Tex("Intervalo de Confianza para la recta", font_size=32).to_edge(DOWN)
        self.play(Create(axes), Create(recta))
        self.play(FadeIn(banda_confianza), FadeIn(banda_confianza_inf))
        self.play(Write(ic_texto))
        self.wait(3)
        self.play(FadeOut(axes, recta, banda_confianza, banda_confianza_inf, ic_texto))

        # Prueba de hipótesis para b
        hipotesis_b = VGroup(
            Tex(r"$H_0: \beta = 0$ (No hay relación lineal)", font_size=36),
            Tex(r"$H_1: \beta \neq 0$ (Sí hay relación lineal)", font_size=36)
        ).arrange(DOWN, buff=0.5)
        self.play(Write(hipotesis_b))
        self.wait(3)
        self.play(FadeOut(titulo, hipotesis_b))

    def regresion_curvilinea(self):
        titulo = Tex("Regresión Curvilínea", font_size=40).to_edge(UP)
        self.play(Write(titulo))

        # Gráfico exponencial
        axes_exp = Axes(x_range=[0, 5], y_range=[0, 20], x_length=5, y_length=5)
        datos_exp = np.array([[1, 2.7], [2, 7.3], [3, 20.0], [4, 15.0]])
        puntos_exp = VGroup(*[Dot(axes_exp.c2p(x, y), color=YELLOW) for x, y in datos_exp])
        curva_exp = axes_exp.plot(lambda x: np.exp(x), color=BLUE)

        # Gráfico linealizado
        axes_log = Axes(x_range=[0, 5], y_range=[0, 3], x_length=5, y_length=5).shift(RIGHT*6)
        datos_log = np.array([[1, np.log(2.7)], [2, np.log(7.3)], [3, np.log(20.0)], [4, np.log(15.0)]])
        puntos_log = VGroup(*[Dot(axes_log.c2p(x, y), color=YELLOW) for x, y in datos_log])
        recta_log = axes_log.plot(lambda x: x, color=BLUE)

        transform_arrow = Arrow(axes_exp.get_right(), axes_log.get_left(), buff=0.5)
        log_text = Tex("Aplicar log(y)", font_size=32).next_to(transform_arrow, UP)

        self.play(Create(axes_exp), Create(puntos_exp), Create(curva_exp))
        self.play(Create(axes_log), Create(puntos_log), Create(recta_log), Write(transform_arrow), Write(log_text))
        self.wait(3)
        self.play(FadeOut(titulo, axes_exp, puntos_exp, curva_exp, axes_log, puntos_log, recta_log, transform_arrow, log_text))

    def regresion_multiple_polinomica(self):
        titulo = Tex("Tema B: Regresión Múltiple y Polinómica", font_size=40).to_edge(UP)
        self.play(Write(titulo))

        # Regresión Múltiple (plano 3D)
        axes_3d = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3])
        plano = Surface(
            lambda u, v: np.array([u, v, 0.5*u + 0.3*v]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            checkerboard_colors=[BLUE_D, BLUE_E],
            opacity=0.5
        )

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes_3d))
        self.play(Create(plano))
        self.wait(3)
        self.play(FadeOut(axes_3d, plano))
        self.move_camera(phi=0, theta=-90*DEGREES) # Reset camera

        # Ajuste Polinómico
        titulo_pol = Tex("Ajuste de un Polinomio", font_size=36).to_edge(UP)
        self.play(Transform(titulo, titulo_pol))

        axes_pol = Axes(x_range=[0, 8], y_range=[6, 13], x_length=9, y_length=6)
        datos_pol = np.array([
            [0, 12.0], [1, 10.5], [2, 10.0], [3, 8.0], [4, 7.0],
            [5, 8.0], [6, 7.5], [7, 8.5], [8, 9.0]
        ])
        puntos_pol = VGroup(*[Dot(axes_pol.c2p(x, y), color=YELLOW) for x, y in datos_pol])

        # Polinomio de grado 2 (parábola)
        poly_fit = np.poly1d(np.polyfit(datos_pol[:, 0], datos_pol[:, 1], 2))
        parabola = axes_pol.plot(lambda x: poly_fit(x), color=GREEN)

        self.play(Create(axes_pol), Create(puntos_pol))
        self.play(Create(parabola))
        self.wait(3)
        self.play(FadeOut(titulo, axes_pol, puntos_pol, parabola))

    def seleccion_modelo_correlacion(self):
        titulo = Tex("Selección del Modelo y Correlación", font_size=40).to_edge(UP)
        self.play(Write(titulo))

        # Varianza Residual
        tabla_varianza = Table(
            [["Grado", "Varianza Residual"],
             ["1 (Lineal)", "7.21"],
             ["2 (Cuadrático)", "1.02"],
             ["3 (Cúbico)", "0.99"],
             ["4 (Cuártico)", "1.24"]],
            row_labels=[Text("Grado"), Text("1"), Text("2"), Text("3"), Text("4")],
            col_labels=[Text("Varianza")],
            include_outer_lines=True
        ).scale(0.7)

        self.play(Write(tabla_varianza))
        arrow = Arrow(start=tabla_varianza.get_cell((2,2)).get_center(), end=tabla_varianza.get_cell((3,2)).get_center(), color=RED, buff=0.1)
        salto_text = Tex("Salto más significativo", font_size=32).next_to(arrow, RIGHT)
        self.play(Create(arrow), Write(salto_text))
        self.wait(3)
        self.play(FadeOut(tabla_varianza, arrow, salto_text))

        # Correlación vs Regresión
        corr_vs_reg = VGroup(
            Tex("Correlación: ¿Están asociadas?", font_size=36),
            Tex("Regresión: ¿Se puede predecir Y desde X?", font_size=36)
        ).arrange(DOWN, buff=1)
        self.play(Write(corr_vs_reg))
        self.wait(3)
        self.play(FadeOut(titulo, corr_vs_reg))

    def cierre(self):
        cierre_title = Tex("En Resumen...", font_size=48, color=BLUE_D)
        self.play(Write(cierre_title))
        self.wait(1)

        resumen_puntos = VGroup(
            Tex(r"- Visualizamos datos con diagramas de dispersión.", font_size=32),
            Tex(r"- Ajustamos modelos (lineales, polinómicos) con Mínimos Cuadrados.", font_size=32),
            Tex(r"- Realizamos inferencias para validar nuestros modelos.", font_size=32),
            Tex(r"- Elegimos el mejor modelo analizando los residuos.", font_size=32)
        ).arrange(DOWN, align=LEFT, buff=0.4).next_to(cierre_title, DOWN, buff=0.5)

        for punto in resumen_puntos:
            self.play(FadeIn(punto, shift=UP))
            self.wait(1.5)

        self.play(FadeOut(cierre_title, resumen_puntos))

        fin_text = Tex("¡Fin de la Unidad 5!", font_size=48)
        self.play(Write(fin_text))
        self.wait(2)
        self.play(FadeOut(fin_text))
