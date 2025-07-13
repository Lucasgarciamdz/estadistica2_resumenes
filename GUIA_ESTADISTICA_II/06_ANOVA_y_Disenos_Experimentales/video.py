from manim import *

# Paleta de colores para el video
COLOR_TRATAMIENTO = BLUE_D
COLOR_BLOQUE = YELLOW_B
COLOR_INTERACCION = GREEN_C
COLOR_ERROR = RED_D
COLOR_TEXTO = WHITE

class Unidad6ANOVA(Scene):
    def construct(self):
        # Configuración inicial
        self.camera.background_color = "#1E1E1E"

        # Título del video
        titulo_principal = Tex("Unidad 6: Diseños Experimentales Avanzados", color=COLOR_TEXTO).scale(1.2)
        self.play(Write(titulo_principal))
        self.wait(2)
        self.play(FadeOut(titulo_principal))

        # --- Escena 1: Más allá del ANOVA Simple ---
        self.escena_introduccion()

        # --- Escena 2: Diseño de Bloques Completos al Azar (DBCA) ---
        self.escena_dbca()

        # --- Escena 3: Diseños Factoriales e Interacción ---
        self.escena_factorial_interaccion()
        
        # --- Escena 4: Pruebas Post-Hoc (Tukey HSD) ---
        self.escena_post_hoc()

        # --- Escena 5: Resumen y Flujo de Trabajo ---
        self.escena_resumen_workflow()
        
        self.wait(2)

    def escena_introduccion(self):
        # Título de la escena
        titulo_escena = Tex("Limitaciones del Diseño Completamente al Azar (DCA)").to_edge(UP)
        self.play(FadeIn(titulo_escena))

        # Cuadrados homogéneos
        unidades_homogeneas = VGroup(*[Square(side_length=0.8) for _ in range(12)])
        unidades_homogeneas.arrange_in_grid(3, 4, buff=0.5)
        unidades_homogeneas.set_fill(GREY_B, opacity=0.8).set_stroke(WHITE, 2)
        
        tratamientos_base_labels = VGroup(*[Tex(f"T{i+1}", color=COLOR_TRATAMIENTO) for i in range(3)])
        
        self.play(FadeIn(unidades_homogeneas, lag_ratio=0.1))
        self.wait(1)

        # Aplicar tratamientos al azar
        labels_on_units = VGroup()
        for i, unidad in enumerate(unidades_homogeneas):
            label = tratamientos_base_labels[i % 3].copy().scale(0.7).move_to(unidad)
            labels_on_units.add(label)
            self.play(FadeIn(label), run_time=0.1)
        self.wait(1)

        # Revelar heterogeneidad
        titulo_problema = Tex("¿Y si las unidades no son homogéneas?", color=YELLOW_B).next_to(titulo_escena, DOWN)
        colores_heterogeneos = [BLUE_E, GREEN_E, PURPLE_E]
        self.play(Write(titulo_problema))
        self.wait(1)

        self.play(*[
            unidades_homogeneas[i].animate.set_fill(colores_heterogeneos[i//4], opacity=0.7)
            for i in range(12)
        ], lag_ratio=0.1)

        pregunta = Tex("¿Efecto del Tratamiento o del 'Ruido'?", color=RED).scale(0.8).next_to(unidades_homogeneas, DOWN)
        self.play(Write(pregunta))
        self.wait(2)

        self.play(FadeOut(titulo_escena, unidades_homogeneas, labels_on_units, pregunta, titulo_problema))


    def escena_dbca(self):
        titulo_escena = Tex("Solución: Diseño de Bloques Completos al Azar (DBCA)").to_edge(UP)
        self.play(Write(titulo_escena))

        colores = [BLUE_E, GREEN_E, PURPLE_E]
        unidades = VGroup(*[
            Square(side_length=0.8).set_fill(colores[i//4], 0.7).set_stroke(WHITE, 2)
            for i in range(12)
        ]).arrange_in_grid(3, 4, buff=1.0)
        self.play(FadeIn(unidades))

        bloques = VGroup(
            VGroup(*unidades[0:4]),
            VGroup(*unidades[4:8]),
            VGroup(*unidades[8:12]),
        )
        
        bloque_rects = VGroup(*[
            SurroundingRectangle(b, color=COLOR_BLOQUE, buff=0.2) for b in bloques
        ])
        bloque_labels = VGroup(*[
            Tex(f"Bloque {i+1}", color=COLOR_BLOQUE).scale(0.8).next_to(b_rect, DOWN)
            for i, b_rect in enumerate(bloque_rects)
        ])

        self.play(
            bloques[0].animate.arrange(RIGHT, buff=0.2).move_to(2*UP),
            bloques[1].animate.arrange(RIGHT, buff=0.2).move_to(ORIGIN),
            bloques[2].animate.arrange(RIGHT, buff=0.2).move_to(2*DOWN),
        )
        self.play(Create(bloque_rects), Write(bloque_labels))
        self.wait(2)

        modelo_dbca = MathTex(
            "X_{ij}", "=", "\\mu", "+", "\\tau_i", "+", "\\beta_j", "+", "\\epsilon_{ij}",
            tex_to_color_map={"\\tau_i": COLOR_TRATAMIENTO, "\\beta_j": COLOR_BLOQUE, "\\epsilon_{ij}": COLOR_ERROR}
        ).shift(3*RIGHT)
        self.play(Write(modelo_dbca))
        self.wait(2)

        sct_eq1 = MathTex("SCT", "=", "SCTr", "+", "SCE").to_edge(DOWN)
        sct_eq2 = MathTex("SCT", "=", "SCTr", "+", "SCB", "+", "SCE", tex_to_color_map={"SCB": COLOR_BLOQUE}).to_edge(DOWN)

        barra_error1 = Rectangle(height=0.5, width=4, color=COLOR_ERROR, fill_opacity=0.8).next_to(sct_eq1, UP, buff=0.5)
        label_error1 = Tex("Error", color=COLOR_ERROR).scale(0.7).move_to(barra_error1)
        escena1_grupo = VGroup(sct_eq1, barra_error1, label_error1)

        self.play(FadeIn(escena1_grupo))
        self.wait(2)

        barra_error2 = Rectangle(height=0.5, width=2, color=COLOR_ERROR, fill_opacity=0.8)
        barra_bloque = Rectangle(height=0.5, width=2, color=COLOR_BLOQUE, fill_opacity=0.8)
        barras2 = VGroup(barra_error2, barra_bloque).arrange(RIGHT, buff=0).move_to(barra_error1, aligned_edge=LEFT)
        label_error2 = Tex("Error", color=COLOR_ERROR).scale(0.7).move_to(barra_error2)
        label_bloque = Tex("Bloque", color=COLOR_BLOQUE).scale(0.7).move_to(barra_bloque)

        self.play(
            TransformMatchingTex(sct_eq1, sct_eq2, fade_transform_mismatches=True),
            Transform(barra_error1, barra_error2),
            Transform(label_error1, label_error2),
            GrowFromEdge(barra_bloque, LEFT),
            FadeIn(label_bloque)
        )
        self.wait(3)
        self.play(FadeOut(VGroup(titulo_escena, unidades, bloque_rects, bloque_labels, modelo_dbca, sct_eq2, barra_bloque, barra_error1, label_bloque, label_error1)))

    def escena_factorial_interaccion(self):
        titulo_escena = Tex("Diseños Factoriales y el Efecto de Interacción").to_edge(UP)
        self.play(Write(titulo_escena))

        axes = Axes(
            x_range=[90, 210, 50], y_range=[20, 80, 10],
            x_length=7, y_length=4.5,
            x_axis_config={"numbers_to_include": [100, 150, 200]},
            y_axis_config={"numbers_to_include": [30, 50, 70]},
        ).to_edge(LEFT, buff=1)
        x_label = axes.get_x_axis_label("Temperatura (°C)")
        y_label = axes.get_y_axis_label("Resistencia", edge=LEFT, direction=UP)
        graph_labels = VGroup(x_label, y_label)

        self.play(Create(axes), Write(graph_labels))
        
        p_alta_no_int = axes.plot(lambda x: 0.15*x + 25, x_range=[100,200], color=RED)
        p_baja_no_int = axes.plot(lambda x: 0.15*x + 10, x_range=[100,200], color=BLUE)
        label_alta_1 = Tex("Presión Alta", color=RED).scale(0.7).next_to(p_alta_no_int.get_end(), RIGHT)
        label_baja_1 = Tex("Presión Baja", color=BLUE).scale(0.7).next_to(p_baja_no_int.get_end(), RIGHT)
        
        titulo_no_int = Tex("Caso A: Sin Interacción", color=WHITE).scale(0.8).next_to(axes, UP, buff=0.5, aligned_edge=LEFT)
        self.play(Write(titulo_no_int))
        self.play(Create(p_alta_no_int), Create(p_baja_no_int), Write(label_alta_1), Write(label_baja_1))
        self.wait(2)

        p_alta_int = axes.plot(lambda x: 0.4*x - 10, x_range=[100,200], color=RED)
        p_baja_int = axes.plot(lambda x: -0.1*x + 50, x_range=[100,200], color=BLUE)
        label_alta_2 = Tex("Presión Alta", color=RED).scale(0.7).next_to(p_alta_int.get_end(), RIGHT)
        label_baja_2 = Tex("Presión Baja", color=BLUE).scale(0.7).next_to(p_baja_int.get_start(), LEFT)
        
        titulo_int = Tex("Caso B: Con Interacción", color=COLOR_INTERACCION).scale(0.8).next_to(axes, UP, buff=0.5, aligned_edge=LEFT)
        interaction_label = Tex("¡INTERACCIÓN!", color=COLOR_INTERACCION).scale(1.2).move_to(axes.get_center())

        self.play(
            Transform(p_alta_no_int, p_alta_int), Transform(p_baja_no_int, p_baja_int),
            Transform(label_alta_1, label_alta_2), Transform(label_baja_1, label_baja_2),
            Transform(titulo_no_int, titulo_int),
            rate_func=smooth, run_time=3
        )
        self.play(Write(interaction_label))
        self.wait(3)

        modelo_factorial = MathTex(
            "X_{ijk}", "=", "\\mu", "+", "\\alpha_i", "+", "\\beta_j", "+", "(\\alpha\\beta)_{ij}", "+", "\\epsilon_{ijk}",
            tex_to_color_map={"(\\alpha\\beta)_{ij}": COLOR_INTERACCION}
        ).shift(2.5*RIGHT).to_edge(DOWN)
        rect_interaccion = SurroundingRectangle(modelo_factorial.get_part_by_tex("(\\alpha\\beta)_{ij}"), color=COLOR_INTERACCION)

        self.play(Write(modelo_factorial))
        self.play(Create(rect_interaccion))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo_escena, axes, graph_labels, p_alta_no_int, p_baja_no_int, label_alta_1, label_baja_1, titulo_no_int, interaction_label, modelo_factorial, rect_interaccion)))
        
    def escena_post_hoc(self):
        titulo_escena = Tex("Pruebas Post-Hoc: ¿Dónde está la diferencia?").to_edge(UP)
        self.play(Write(titulo_escena))

        axes = Axes(x_range=[0, 20, 5], y_range=[0, 0.5, 0.1], x_length=10, y_length=3).shift(DOWN)
        means = [5, 8, 12, 16]
        colors = [BLUE, GREEN, YELLOW, RED]
        distributions = VGroup(*[
            axes.plot(lambda x: np.exp(-0.5 * ((x - mean))**2), color=color)
            for mean, color in zip(means, colors)
        ])
        
        self.play(Create(distributions, lag_ratio=0.5))

        sello_anova = Tex("ANOVA: $p < 0.05$", color=GREEN_C).scale(1.2).next_to(axes, UP)
        self.play(Write(sello_anova))
        self.wait(1)

        hsd_formula = MathTex("HSD = q_{\\alpha, k, gl_E}", "\\sqrt{\\frac{CME}{n}}", color=WHITE).next_to(sello_anova, UP)
        hsd_formula.get_part_by_tex("q").set_color(COLOR_BLOQUE)
        self.play(Write(hsd_formula))
        self.wait(2)

        hsd_value = 5.0
        hsd_ruler = DoubleArrow(axes.c2p(0, -0.1), axes.c2p(hsd_value, -0.1), buff=0, color=COLOR_BLOQUE)
        hsd_label = Tex("HSD").next_to(hsd_ruler, DOWN, buff=0.1).scale(0.8).set_color(COLOR_BLOQUE)
        ruler_group = VGroup(hsd_ruler, hsd_label)
        self.play(FadeIn(ruler_group))
        self.wait(1)

        mean_dots = VGroup(*[Dot(axes.c2p(m, 0), color=c) for m,c in zip(means, colors)])
        self.play(Create(mean_dots))

        comparisons = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        sig_indicators = VGroup()
        for i, j in comparisons:
            start_point = mean_dots[i].get_center()
            end_point = mean_dots[j].get_center()
            self.play(ruler_group.animate.move_to(midpoint(start_point, end_point) + 0.5*DOWN))
            
            if abs(means[j] - means[i]) > hsd_value:
                line = Line(start_point, end_point, color=GREEN_C, stroke_width=5)
                sig_label = Tex("Sig.", color=GREEN_C).scale(0.7).next_to(line, UP, buff=0.1)
                sig_indicators.add(line, sig_label)
                self.play(Create(line), Write(sig_label))
            self.wait(0.5)
        self.wait(3)
        self.play(FadeOut(titulo_escena, axes, distributions, sello_anova, hsd_formula, ruler_group, mean_dots, sig_indicators))

    def escena_resumen_workflow(self):
        titulo = Tex("Flujo de Trabajo del Análisis").to_edge(UP)
        self.play(Write(titulo))

        nodos_texto = [
            "1. Identificar\nTratamientos", "2. ¿Variables\nde Molestia?",
            "3. ¿Múltiples\nFactores?", "4. Realizar ANOVA",
            "5. ¿Interacción\nSignificativa?", "6. Interpretar\nInteracción",
            "7. Interpretar\nEfectos Principales", "8. ¿Efecto Principal\nSignificativo?",
            "9. Pruebas\nPost-Hoc (Tukey)"
        ]
        
        nodos_group = Group()
        for txt in nodos_texto:
            rect = Rectangle(width=3, height=1.5)
            label = Tex(txt, font_size=24)
            nodo = Group(rect, label)
            nodos_group.add(nodo)
        
        nodos_group[0].move_to(3*UP + 4.5*LEFT)
        nodos_group[1].next_to(nodos_group[0], DOWN, buff=1.0)
        nodos_group[2].next_to(nodos_group[1], DOWN, buff=1.0)
        nodos_group[3].move_to(0.5*UP)
        nodos_group[4].next_to(nodos_group[3], DOWN, buff=1).shift(2*RIGHT)
        nodos_group[5].next_to(nodos_group[4], RIGHT, buff=1.5)
        nodos_group[6].next_to(nodos_group[3], DOWN, buff=1).shift(2*LEFT)
        nodos_group[7].next_to(nodos_group[6], DOWN, buff=1)
        nodos_group[8].next_to(nodos_group[7], DOWN, buff=1)
        
        flechas = VGroup(
            Arrow(nodos_group[0].get_bottom(), nodos_group[1].get_top()),
            Arrow(nodos_group[1].get_bottom(), nodos_group[2].get_top()),
            Arrow(nodos_group[2].get_right(), nodos_group[3].get_left()),
            Arrow(nodos_group[3].get_bottom(), nodos_group[6].get_top()),
            Arrow(nodos_group[6].get_right(), nodos_group[4].get_left()).add(Tex("No", font_size=24).next_to(nodos_group[6].get_right(), buff=0.1)),
            Arrow(nodos_group[4].get_right(), nodos_group[5].get_left()).add(Tex("Sí", font_size=24).next_to(nodos_group[4].get_right(), buff=0.1)),
            Arrow(nodos_group[6].get_bottom(), nodos_group[7].get_top()),
            Arrow(nodos_group[7].get_bottom(), nodos_group[8].get_top()).add(Tex("Sí", font_size=24).next_to(nodos_group[7].get_right(), buff=0.1)),
        )
        
        self.play(FadeIn(nodos_group[0]))
        self.play(GrowArrow(flechas[0]), FadeIn(nodos_group[1])); self.wait(0.5)
        self.play(GrowArrow(flechas[1]), FadeIn(nodos_group[2])); self.wait(0.5)
        self.play(GrowArrow(flechas[2]), FadeIn(nodos_group[3])); self.wait(0.5)
        self.play(GrowArrow(flechas[3]), FadeIn(nodos_group[6])); self.wait(0.5)
        self.play(GrowArrow(flechas[4]), FadeIn(nodos_group[4])); self.wait(0.5)
        self.play(GrowArrow(flechas[5]), FadeIn(nodos_group[5])); self.wait(0.5)
        self.play(GrowArrow(flechas[6]), FadeIn(nodos_group[7])); self.wait(0.5)
        self.play(GrowArrow(flechas[7]), FadeIn(nodos_group[8])); self.wait(1)

        path = Group(nodos_group[0], nodos_group[1], nodos_group[2], nodos_group[3], nodos_group[6], nodos_group[7], nodos_group[8])
        path_rects = [SurroundingRectangle(p, color=GREEN_C) for p in path]
        
        self.play(Create(path_rects[0]))
        for i in range(len(path_rects)-1):
            self.play(ReplacementTransform(path_rects[i], path_rects[i+1]), run_time=1)
            self.wait(0.5)

        self.wait(3)
