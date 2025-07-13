from manim import *
import numpy as np

class AnalisisDeLaVarianza(Scene):
    def construct(self):
        # --- INTRODUCCIÓN ---
        titulo = Tex(r"Unidad 3: An\'alisis de la Varianza (ANOVA)", font_size=48).to_edge(UP)
        self.play(Write(titulo))
        self.wait(0.5)

        problema_t = Tex(r"\\textbf{El Problema de M\'ultiples Pruebas t}", font_size=36).next_to(titulo, DOWN, buff=0.8)
        prob_text = Tex(
            r"Comparar $k$ grupos con pruebas t individuales aumenta el \\textbf{Error de Tipo I}.",
            font_size=30
        ).next_to(problema_t, DOWN)

        self.play(FadeIn(problema_t, shift=UP))
        self.play(Write(prob_text))
        self.wait(1)

        # Simulación de pruebas t
        grupos = VGroup(*[Circle(radius=0.3, color=BLUE_D).set_fill(BLUE_D, opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0.5)
        grupos.next_to(prob_text, DOWN, buff=0.5)
        self.play(Create(grupos))

        flechas = []
        pares = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
        for i, j in pares:
            flecha = Arrow(grupos[i].get_right(), grupos[j].get_left(), buff=0.1, color=YELLOW_B, stroke_width=3)
            flechas.append(flecha)
        
        self.play(LaggedStart(*[GrowArrow(f) for f in flechas], lag_ratio=0.2))
        self.wait(1)

        solucion_anova = Tex(r"\\textbf{ANOVA: Una \'Unica Prueba Global}", font_size=36, color=GREEN_C).next_to(grupos, DOWN, buff=0.8)
        self.play(FadeOut(VGroup(*flechas, grupos, problema_t, prob_text)), FadeIn(solucion_anova, shift=UP))
        self.wait(1)
        self.play(FadeOut(solucion_anova, shift=DOWN))
        self.wait(0.5)

        # --- IDEA CENTRAL: DESCOMPOSICIÓN DE LA VARIANZA ---
        idea_central_titulo = Tex(r"\\textbf{La Idea Central: Descomposici\'on de la Varianza}", font_size=40).to_edge(UP)
        self.play(Transform(titulo, idea_central_titulo))
        self.wait(0.5)

        formula_sct = MathTex(r"SCT = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{\bar{X}})^2", font_size=36).next_to(titulo, DOWN, buff=0.8)
        sct_text = Tex(r"Suma de Cuadrados Total (SCT): Variabilidad total de los datos.", font_size=28).next_to(formula_sct, DOWN)
        self.play(Write(formula_sct))
        self.play(Write(sct_text))
        self.wait(1.5)

        self.play(FadeOut(sct_text))

        descomposicion_formula = MathTex(r"SCT = SCTr + SCE", font_size=48, color=GREEN_C).next_to(formula_sct, DOWN, buff=1.0)
        self.play(Write(descomposicion_formula))
        self.wait(1)

        sctr_def = Tex(r"\\textbf{SCTr (Entre Grupos):} Variabilidad explicada por las diferencias entre medias de grupo.", font_size=28).next_to(descomposicion_formula, DOWN, buff=0.5)
        sce_def = Tex(r"\\textbf{SCE (Dentro de Grupos):} Variabilidad no explicada (error aleatorio) dentro de cada grupo.", font_size=28).next_to(sctr_def, DOWN)

        self.play(FadeIn(sctr_def, shift=UP))
        self.play(FadeIn(sce_def, shift=UP))
        self.wait(2)

        self.play(FadeOut(VGroup(formula_sct, descomposicion_formula, sctr_def, sce_def)))

        # --- EL ESTADÍSTICO F ---
        estadistico_f_titulo = Tex(r"\\textbf{El Estad\'istico F}", font_size=40).to_edge(UP)
        self.play(Transform(titulo, estadistico_f_titulo))
        self.wait(0.5)

        cmtr_formula = MathTex(r"CMTr = \frac{SCTr}{k-1}", font_size=36).next_to(titulo, DOWN, buff=0.8)
        cme_formula = MathTex(r"CME = \frac{SCE}{N-k}", font_size=36).next_to(cmtr_formula, DOWN, buff=0.5)
        self.play(Write(cmtr_formula))
        self.play(Write(cme_formula))
        self.wait(1)

        f_formula = MathTex(r"F = \frac{CMTr}{CME}", font_size=48, color=YELLOW_B).next_to(cme_formula, DOWN, buff=1.0)
        self.play(Write(f_formula))
        self.wait(1)

        # Lógica de la decisión
        h0_text = Tex(r"\\textbf{Bajo $H_0$ (medias iguales):}", font_size=30).next_to(f_formula, DOWN, buff=0.8)
        h0_f_approx = MathTex(r"F \approx 1", font_size=36, color=BLUE_D).next_to(h0_text, DOWN)
        self.play(Write(h0_text))
        self.play(Write(h0_f_approx))
        self.wait(1.5)

        h1_text = Tex(r"\\textbf{Bajo $H_1$ (al menos una media diferente):}", font_size=30).next_to(h0_f_approx, DOWN, buff=0.8)
        h1_f_greater = MathTex(r"F > 1", font_size=36, color=RED).next_to(h1_text, DOWN)
        self.play(Write(h1_text))
        self.play(Write(h1_f_greater))
        self.wait(2)

        self.play(FadeOut(VGroup(cmtr_formula, cme_formula, f_formula, h0_text, h0_f_approx, h1_text, h1_f_greater)))

        # --- DETALLES MATEMÁTICOS: ANULACIÓN DEL TÉRMINO CRUZADO ---
        detalle_cruzado_titulo = Tex(r"\\textbf{Detalle: Anulaci\'on del T\'ermino Cruzado}", font_size=40).to_edge(UP)
        self.play(Transform(titulo, detalle_cruzado_titulo))
        self.wait(0.5)

        termino_cruzado = MathTex(r"2\sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)(\bar{X}_i - \bar{\bar{X}})", font_size=36).next_to(titulo, DOWN, buff=0.8)
        self.play(Write(termino_cruzado))
        self.wait(1)

        propiedad_media = MathTex(r"\sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i) = 0", font_size=40, color=GREEN_C).next_to(termino_cruzado, DOWN, buff=1.0)
        explicacion_propiedad = Tex(r"La suma de las desviaciones respecto a la media es cero.", font_size=28).next_to(propiedad_media, DOWN)
        self.play(Write(propiedad_media))
        self.play(Write(explicacion_propiedad))
        self.wait(2.5)

        self.play(FadeOut(VGroup(termino_cruzado, propiedad_media, explicacion_propiedad)))

        # --- GRADOS DE LIBERTAD ---
        gl_titulo = Tex(r"\\textbf{Grados de Libertad (gl)}", font_size=40).to_edge(UP)
        self.play(Transform(titulo, gl_titulo))
        self.wait(0.5)

        gl_total = MathTex(r"gl_{Total} = N-1", font_size=36).next_to(titulo, DOWN, buff=0.8)
        gl_tr = MathTex(r"gl_{Tr} = k-1", font_size=36).next_to(gl_total, DOWN, buff=0.5)
        gl_e = MathTex(r"gl_{E} = N-k", font_size=36).next_to(gl_tr, DOWN, buff=0.5)

        self.play(Write(gl_total))
        self.play(Write(gl_tr))
        self.play(Write(gl_e))
        self.wait(1.5)

        aditividad_gl = MathTex(r"gl_{Total} = gl_{Tr} + gl_{E}", font_size=40, color=YELLOW_B).next_to(gl_e, DOWN, buff=1.0)
        self.play(Write(aditividad_gl))
        self.wait(2)

        self.play(FadeOut(VGroup(gl_total, gl_tr, gl_e, aditividad_gl)))

        # --- EJEMPLO PRÁCTICO (Simplificado) ---
        ejemplo_titulo = Tex(r"\\textbf{Ejemplo Pr\'actico}", font_size=40).to_edge(UP)
        self.play(Transform(titulo, ejemplo_titulo))
        self.wait(0.5)

        # Simulación de datos con ValueTracker para mostrar variabilidad
        # Usaremos un gráfico de puntos para representar los datos de 3 grupos
        # y cómo sus medias pueden variar.

        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=5,
            axis_config={"color": GRAY},
            x_axis_config={"numbers_to_include": [1, 2, 3]},
            y_axis_config={"numbers_to_include": [0, 2, 4, 6, 8, 10]}
        ).scale(0.8).to_edge(DOWN)
        axes.add_coordinates()
        self.play(Create(axes))

        mean_shift = ValueTracker(0) # Controls the shift of the means
        base_means = np.array([3, 5, 7]) # Base means for 3 groups
        
        # Function to create points for each group
        def get_group_points(shift_val):
            points = VGroup()
            current_means = base_means + shift_val
            for i, mean in enumerate(current_means):
                # Simulate data around the mean
                np.random.seed(i) # for reproducibility
                data = np.random.normal(mean, 1, 5) # 5 points per group, std dev 1
                for d in data:
                    point = Dot(axes.coords_to_point(i + 1, d), color=BLUE_D)
                    points.add(point)
            return points

        initial_points = always_redraw(lambda: get_group_points(mean_shift.get_value()))
        self.add(initial_points)
        self.wait(1)

        # Animate change in means to show effect
        self.play(
            mean_shift.animate.set_value(-1), # Shift means down
            run_time=1.5,
            rate_func=smooth
        )
        self.play(
            mean_shift.animate.set_value(1), # Shift means up
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(1)

        # Highlight the variability between groups
        mean_lines = always_redraw(lambda: VGroup(
            *[Line(axes.coords_to_point(i + 1, base_means[i] + mean_shift.get_value()),
                   axes.coords_to_point(i + 1, base_means[i] + mean_shift.get_value() + 0.001),
                   color=YELLOW_B, stroke_width=5) for i in range(3)]
        ))
        self.add(mean_lines)
        self.wait(1)

        # Explain the concept of "between" and "within" variability visually
        between_text = Tex(r"Variabilidad Entre Grupos (SCTr)", font_size=28, color=YELLOW_B).next_to(axes, UP, buff=0.5)
        within_text = Tex(r"Variabilidad Dentro de Grupos (SCE)", font_size=28, color=BLUE_D).next_to(between_text, DOWN)
        self.play(Write(between_text))
        self.play(Write(within_text))
        self.wait(2)

        self.play(FadeOut(VGroup(axes, initial_points, mean_lines, between_text, within_text)))

        # --- CIERRE ---
        cierre_titulo = Tex(r"\\textbf{Cierre}", font_size=40).to_edge(UP)
        self.play(Transform(titulo, cierre_titulo))
        self.wait(0.5)

        resumen_text = Tex(
            r"ANOVA: Compara m\'ultiples medias, evita inflaci\'on de Error Tipo I.\\"
            r"Descompone varianza: SCT = SCTr + SCE.\\"
            r"Estad\'istico F: compara variabilidad entre vs. dentro de grupos.\\"
            r"Grados de libertad: informaci\'on independiente para estimar variabilidad.",
            font_size=30,
        ).next_to(titulo, DOWN, buff=0.8)
        self.play(Write(resumen_text))
        self.wait(3)

        despedida = Tex(r"\\textbf{¡Hasta la pr\'oxima!}", font_size=48, color=GREEN_C).next_to(resumen_text, DOWN, buff=1.5)
        self.play(Write(despedida))
        self.wait(1)
