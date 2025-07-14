from manim import *

class PruebasNoParametricas(Scene):
    def construct(self):
        # --- INTRODUCCIÓN ---
        titulo = Tex(r"\textbf{Pruebas No Paramétricas}", font_size=56, color=BLUE_D)
        subtitulo = Tex(r"Más allá de la normalidad", font_size=36, color=YELLOW_B).next_to(titulo, DOWN, buff=0.5)
        self.play(Write(titulo), FadeIn(subtitulo, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(titulo), FadeOut(subtitulo))

        # --- PRUEBA DEL SIGNO ---
        titulo_signo = Tex(r"\textbf{Prueba del Signo}", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_signo))

        datos = MathTex(r"10, 12, 8, 15, 9", font_size=36)
        mediana_hipotetica = MathTex(r"H_0: \text{Mediana} = 11", font_size=36).next_to(datos, DOWN, buff=0.5)
        self.play(Write(datos), Write(mediana_hipotetica))
        self.wait(2)

        signos = MathTex(r"-", r"+", r"-", r"+", r"-", font_size=48).next_to(mediana_hipotetica, DOWN, buff=0.5)
        for i in range(len(signos)):
            signos[i].set_color(RED if i % 2 == 0 else GREEN)

        self.play(TransformFromCopy(datos, signos))
        self.wait(2)
        self.play(FadeOut(datos), FadeOut(mediana_hipotetica), FadeOut(signos), FadeOut(titulo_signo))

        # --- PRUEBA DE WILCOXON ---
        titulo_wilcoxon = Tex(r"\textbf{Prueba de Suma de Rangos de Wilcoxon}", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_wilcoxon))

        tabla_wilcoxon = Table(
            [["Antes", "Después", "Diferencia", "|Diferencia|", "Rango"],
             ["110", "105", "-5", "5", "2"],
             ["120", "110", "-10", "10", "4"],
             ["115", "112", "-3", "3", "1"],
             ["125", "122", "-3", "3", "1"],
             ["130", "120", "-10", "10", "4"],
             ["118", "112", "-6", "6", "3"]],
            row_labels=[Text("Sujeto 1"), Text("Sujeto 2"), Text("Sujeto 3"), Text("Sujeto 4"), Text("Sujeto 5"), Text("Sujeto 6")],
            col_labels=[Text("Presión Sistólica"), Text("Presión Sistólica"), Text(""), Text(""), Text("")],
            include_outer_lines=True
        ).scale(0.5)
        self.play(Write(tabla_wilcoxon))
        self.wait(4)

        suma_rangos_pos = MathTex(r"W^+ = 0", font_size=36).next_to(tabla_wilcoxon, DOWN, buff=0.5)
        suma_rangos_neg = MathTex(r"W^- = 2+4+1+1+4+3 = 15", font_size=36).next_to(suma_rangos_pos, DOWN, buff=0.2)
        self.play(Write(suma_rangos_pos), Write(suma_rangos_neg))
        self.wait(2)
        self.play(FadeOut(tabla_wilcoxon), FadeOut(suma_rangos_pos), FadeOut(suma_rangos_neg), FadeOut(titulo_wilcoxon))

        # --- PRUEBA DE KRUSKAL-WALLIS ---
        titulo_kruskal = Tex(r"\textbf{Prueba de Kruskal-Wallis}", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_kruskal))

        tabla_kruskal = Table(
            [["Grupo A", "Grupo B", "Grupo C"],
             ["2.9", "3.8", "4.1"],
             ["3.1", "4.2", "4.5"],
             ["3.3", "4.0", "4.3"],
             ["3.0", "3.9", "4.4"]],
            row_labels=[Text(""), Text(""), Text(""), Text("")],
            col_labels=[Text("Tratamiento 1"), Text("Tratamiento 2"), Text("Tratamiento 3")],
            include_outer_lines=True
        ).scale(0.6)
        self.play(Write(tabla_kruskal))
        self.wait(4)

        formula_h = MathTex(r"H = \frac{12}{N(N+1)} \sum_{i=1}^{k} \frac{R_i^2}{n_i} - 3(N+1)", font_size=40).next_to(tabla_kruskal, DOWN, buff=0.5)
        self.play(Write(formula_h))
        self.wait(3)
        self.play(FadeOut(tabla_kruskal), FadeOut(formula_h), FadeOut(titulo_kruskal))

        # --- PRUEBAS DE ALEATORIEDAD ---
        titulo_rachas = Tex(r"\textbf{Pruebas de Aleatoriedad (Rachas)}", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_rachas))

        secuencia = MathTex(r"A, B, B, A, A, A, B", font_size=40)
        self.play(Write(secuencia))
        self.wait(2)

        rachas = VGroup(
            Line(secuencia[0].get_bottom(), secuencia[0].get_bottom() + DOWN * 0.2, color=YELLOW),
            Line(secuencia[2].get_bottom(), secuencia[4].get_bottom() + DOWN * 0.2, color=YELLOW),
            Line(secuencia[6].get_bottom(), secuencia[10].get_bottom() + DOWN * 0.2, color=YELLOW),
            Line(secuencia[12].get_bottom(), secuencia[12].get_bottom() + DOWN * 0.2, color=YELLOW)
        )
        self.play(ShowCreation(rachas))
        self.wait(2)
        self.play(FadeOut(secuencia), FadeOut(rachas), FadeOut(titulo_rachas))

        # --- PRUEBAS DE KOLMOGOROV-SMIRNOV ---
        titulo_ks = Tex(r"\textbf{Pruebas de Kolmogorov-Smirnov}", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_ks))

        axes = Axes(
            x_range=[0, 1, 0.2],
            y_range=[0, 1, 0.2],
            width=6,
            height=4,
            x_axis_config={"numbers_to_include": np.arange(0.2, 1.1, 0.2)},
            y_axis_config={"numbers_to_include": np.arange(0.2, 1.1, 0.2)}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="F(x)")

        cdf_empirica = axes.get_graph(lambda x: x**2, color=BLUE)
        cdf_teorica = axes.get_graph(lambda x: x, color=GREEN)

        self.play(Write(axes), Write(labels))
        self.play(ShowCreation(cdf_empirica), ShowCreation(cdf_teorica))
        self.wait(2)

        d_max = Brace(Line(axes.c2p(0.5, 0.25), axes.c2p(0.5, 0.5)), direction=RIGHT)
        d_max_text = d_max.get_text("D").scale(0.8)
        self.play(GrowFromCenter(d_max), Write(d_max_text))
        self.wait(3)
        self.play(FadeOut(axes), FadeOut(labels), FadeOut(cdf_empirica), FadeOut(cdf_teorica), FadeOut(d_max), FadeOut(d_max_text), FadeOut(titulo_ks))

        # --- CIERRE ---
        cierre = Tex(r"\textbf{¡Gracias por ver!}", font_size=56, color=BLUE_D)
        self.play(Write(cierre))
        self.wait(2)
        self.play(FadeOut(cierre))
