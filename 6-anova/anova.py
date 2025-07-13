from manim import *

class AnovaVideo(Scene):
    def construct(self):
        # Colores personalizados
        BLUE_D = "#336699"
        GREEN_C = "#66CC99"
        YELLOW_B = "#FFCC66"

        # ESCENA 1: INTRODUCCIÓN
        titulo = Tex(r"ANOVA y Diseños Experimentales Avanzados", font_size=60, color=BLUE_D)
        subtitulo = Tex(r"Más allá del ANOVA simple", font_size=36, color=YELLOW_B).next_to(titulo, DOWN)
        
        self.play(Write(titulo), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(subtitulo, shift=UP), run_time=1, rate_func=smooth)
        self.wait(1)

        # Detalle crítico de introducción
        detalle_intro = Tex(r"¡Crucial para conclusiones precisas y robustas!", font_size=30, color=GREEN_C).next_to(subtitulo, DOWN, buff=0.5)
        self.play(Write(detalle_intro), run_time=1.5, rate_func=smooth)
        self.wait(2)
        self.play(FadeOut(VGroup(titulo, subtitulo, detalle_intro)))

        # ESCENA 2: TEORÍA - DBCA
        titulo_dbca = Tex(r"Diseño de Bloques Completos al Azar (DBCA)", font_size=48, color=BLUE_D)
        self.play(Write(titulo_dbca), run_time=1, rate_func=smooth)
        self.wait(0.5)

        modelo_dbca_tex = MathTex(r"X_{ij} = \mu + \tau_i + \beta_j + \epsilon_{ij}", font_size=40)
        modelo_dbca_desc = VGroup(
            Tex(r"$X_{ij}$: Observación", font_size=28),
            Tex(r"$\mu$: Gran media", font_size=28),
            Tex(r"$\tau_i$: Efecto Tratamiento $i$", font_size=28),
            Tex(r"$\beta_j$: Efecto Bloque $j$", font_size=28),
            Tex(r"$\epsilon_{ij}$: Error aleatorio", font_size=28)
        ).arrange(DOWN).next_to(modelo_dbca_tex, RIGHT, buff=1)

        self.play(Write(modelo_dbca_tex), run_time=2)
        self.play(FadeIn(modelo_dbca_desc, shift=RIGHT), run_time=1.5)
        self.wait(2)

        # Explicación de la necesidad del DBCA
        problema_texto = Tex(r"Problema: Fuentes de variabilidad externas (molestia)", font_size=32, color=YELLOW_B).to_edge(UP).shift(DOWN*1.5)
        solucion_texto = Tex(r"Solución: Agrupar en Bloques Homogéneos", font_size=32, color=GREEN_C).next_to(problema_texto, DOWN, buff=0.5)
        
        self.play(Transform(titulo_dbca, problema_texto), run_time=1)
        self.play(FadeOut(modelo_dbca_tex, modelo_dbca_desc), FadeIn(solucion_texto, shift=UP), run_time=1)
        self.wait(1)

        # Descomposición de la varianza DBCA
        descomposicion_sct = MathTex(r"SCT = SCTr + SCB + SCE", font_size=48).move_to(ORIGIN)
        
        self.play(Write(descomposicion_sct), run_time=2)
        self.wait(1)

        # Explicación de por qué SCB reduce SCE
        sct_rect = Rectangle(width=6, height=1, color=BLUE_D, fill_opacity=0.5).to_edge(UP, buff=1)
        sctr_rect = Rectangle(width=2, height=0.8, color=GREEN_C, fill_opacity=0.5).next_to(sct_rect, DOWN, buff=0.5).align_to(sct_rect, LEFT)
        scb_rect = Rectangle(width=2, height=0.8, color=YELLOW_B, fill_opacity=0.5).next_to(sctr_rect, RIGHT, buff=0.2)
        sce_rect_large = Rectangle(width=2, height=0.8, color=RED, fill_opacity=0.5).next_to(scb_rect, RIGHT, buff=0.2)

        sct_label = Tex("SCT", font_size=30).next_to(sct_rect, LEFT)
        sctr_label = Tex("SCTr", font_size=30).next_to(sctr_rect, DOWN)
        scb_label = Tex("SCB", font_size=30).next_to(scb_rect, DOWN)
        sce_label_large = Tex("SCE (sin bloqueo)", font_size=30).next_to(sce_rect_large, DOWN)

        self.play(FadeOut(solucion_texto, descomposicion_sct), FadeIn(sct_rect, sct_label), run_time=1)
        self.play(FadeIn(sctr_rect, sctr_label, scb_rect, scb_label, sce_rect_large, sce_label_large), run_time=2)
        self.wait(1)

        # Animación de reducción de SCE
        sce_rect_small = Rectangle(width=1, height=0.8, color=RED, fill_opacity=0.5).next_to(scb_rect, RIGHT, buff=0.2)
        sce_label_small = Tex("SCE (con bloqueo)", font_size=30).next_to(sce_rect_small, DOWN)
        
        arrow_scb_sce = Arrow(scb_rect.get_right(), sce_rect_large.get_left(), color=WHITE)
        text_scb_absorbs = Tex(r"SCB 'absorbe' variabilidad", font_size=28, color=YELLOW_B).next_to(arrow_scb_sce, UP)

        self.play(Create(arrow_scb_sce), Write(text_scb_absorbs), run_time=1.5)
        self.play(Transform(sce_rect_large, sce_rect_small), Transform(sce_label_large, sce_label_small), run_time=1.5)
        self.wait(1)

        power_up_arrow = Arrow(sce_rect_small.get_bottom(), sce_rect_small.get_bottom() + UP*0.5, color=GREEN_C)
        power_up_text = Tex(r"$\downarrow$ CME $\implies \uparrow$ Potencia", font_size=32, color=GREEN_C).next_to(power_up_arrow, RIGHT)
        self.play(GrowArrow(power_up_arrow), Write(power_up_text), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(VGroup(sct_rect, sct_label, sctr_rect, sctr_label, scb_rect, scb_label, sce_rect_large, sce_label_large, arrow_scb_sce, text_scb_absorbs, power_up_arrow, power_up_text)))

        # ESCENA 3: TEORÍA - DISEÑOS FACTORIALES
        titulo_factorial = Tex(r"Diseños Factoriales", font_size=48, color=BLUE_D)
        self.play(Write(titulo_factorial), run_time=1, rate_func=smooth)
        self.wait(0.5)

        modelo_factorial_tex = MathTex(r"X_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \epsilon_{ijk}", font_size=40)
        modelo_factorial_desc = VGroup(
            Tex(r"$\alpha_i$: Efecto Factor A", font_size=28),
            Tex(r"$\beta_j$: Efecto Factor B", font_size=28),
            Tex(r"$(\alpha\beta)_{ij}$: Interacción A y B", font_size=28)
                ).arrange(DOWN).next_to(modelo_factorial_tex, RIGHT, buff=1)

        self.play(Write(modelo_factorial_tex), run_time=2)
        self.play(FadeIn(modelo_factorial_desc, shift=RIGHT), run_time=1.5)
        self.wait(2)

        interaccion_texto = Tex(r"Interacción: El efecto de un factor cambia según el nivel de otro.", font_size=32, color=YELLOW_B).to_edge(UP).shift(DOWN*1.5)
        self.play(Transform(titulo_factorial, interaccion_texto), run_time=1)
        self.play(FadeOut(modelo_factorial_tex, modelo_factorial_desc), run_time=1)
        self.wait(1)

        # Gráfico de interacción dinámico
        axes = Axes(
            x_range=[0, 2, 1],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": GRAY},
            x_axis_config={"numbers_to_include": [0, 1]},
            y_axis_config={"numbers_to_include": [0, 2, 4, 6, 8, 10]}
        ).add_coordinates()
        axes.to_edge(LEFT, buff=1)

        x_labels = VGroup(Tex("Nivel 1", font_size=24).next_to(axes.x_axis.get_start(), DOWN),
                          Tex("Nivel 2", font_size=24).next_to(axes.x_axis.get_end(), DOWN))
        y_label = Tex("Respuesta", font_size=24).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_labels), Write(y_label), run_time=1.5)

        # Líneas para Factor B (sin interacción inicial)
        line1_no_int = Line(axes.c2p(0, 2), axes.c2p(1, 4), color=GREEN_C)
        line2_no_int = Line(axes.c2p(0, 6), axes.c2p(1, 8), color=BLUE_D)
        label1_no_int = Tex("B1", font_size=24, color=GREEN_C).next_to(line1_no_int.get_end(), RIGHT)
        label2_no_int = Tex("B2", font_size=24, color=BLUE_D).next_to(line2_no_int.get_end(), RIGHT)

        self.play(Create(line1_no_int), Create(line2_no_int), Write(label1_no_int), Write(label2_no_int), run_time=2)
        self.wait(1)

        no_int_text = Tex(r"Sin Interacción: Líneas Paralelas", font_size=30, color=GREEN_C).to_edge(UP).shift(DOWN*1.5)
        self.play(Write(no_int_text), run_time=1)
        self.wait(1.5)

        # Transformación a interacción
        line1_int = Line(axes.c2p(0, 2), axes.c2p(1, 8), color=GREEN_C)
        line2_int = Line(axes.c2p(0, 6), axes.c2p(1, 4), color=BLUE_D)

        self.play(Transform(line1_no_int, line1_int), Transform(line2_no_int, line2_int), run_time=2, rate_func=smooth)
        self.wait(1)

        int_text = Tex(r"Con Interacción: Líneas No Paralelas", font_size=30, color=YELLOW_B).to_edge(UP).shift(DOWN*1.5)
        self.play(Transform(no_int_text, int_text), run_time=1)
        self.wait(2)
        self.play(FadeOut(VGroup(axes, x_labels, y_label, line1_no_int, line2_no_int, label1_no_int, label2_no_int, no_int_text, int_text, titulo_factorial)))

        # ESCENA 4: TEORÍA - PRUEBAS POST-HOC (TUKEY HSD)
        titulo_posthoc = Tex(r"Pruebas Post-Hoc: Tukey HSD", font_size=48, color=BLUE_D)
        self.play(Write(titulo_posthoc), run_time=1, rate_func=smooth)
        self.wait(0.5)

        pregunta_posthoc = Tex(r"¿Cuál o cuáles medias son diferentes?", font_size=36, color=YELLOW_B).next_to(titulo_posthoc, DOWN, buff=0.5)
        self.play(Write(pregunta_posthoc), run_time=1.5)
        self.wait(1)

        error_tipo1_texto = Tex(r"¡Cuidado con la inflación del Error Tipo I!", font_size=32, color=RED).next_to(pregunta_posthoc, DOWN, buff=0.5)
        self.play(Write(error_tipo1_texto), run_time=1.5)
        self.wait(1.5)

        formula_tukey = MathTex(r"HSD = q_{\alpha, k, gl_E} \sqrt{\frac{CME}{n}}", font_size=48).move_to(ORIGIN)
        
        self.play(FadeOut(pregunta_posthoc, error_tipo1_texto), Write(formula_tukey), run_time=2)
        self.wait(1)

        # Explicación de términos de Tukey
        q_term = formula_tukey[0][4:14] # q_alpha, k, gl_E
        sqrt_term = formula_tukey[0][15:] # sqrt(CME/n)

        q_desc = Tex(r"$q$: Valor crítico del rango estudentizado", font_size=28, color=GREEN_C).next_to(q_term, DOWN, buff=0.5)
        sqrt_desc = Tex(r"$\sqrt{CME/n}$: Error estándar de la diferencia de medias", font_size=28, color=GREEN_C).next_to(sqrt_term, DOWN, buff=0.5)

        self.play(Indicate(q_term), Write(q_desc), run_time=1.5)
        self.wait(1)
        self.play(Indicate(sqrt_term), Write(sqrt_desc), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(VGroup(titulo_posthoc, formula_tukey, q_desc, sqrt_desc)))

        # ESCENA 5: EJEMPLO PRÁCTICO (AGRICULTURA)
        titulo_ejemplo = Tex(r"Ejemplo: Rendimiento de Trigo", font_size=48, color=BLUE_D)
        self.play(Write(titulo_ejemplo), run_time=1, rate_func=smooth)
        self.wait(0.5)

        # Factores y Bloqueo
        factores_text = VGroup(
            Tex(r"Factor A: Variedad de Trigo (3 niveles)", font_size=32, color=GREEN_C),
            Tex(r"Factor B: Tipo de Fertilizante (2 niveles)", font_size=32, color=GREEN_C),
            Tex(r"Bloqueo: Fertilidad del Suelo", font_size=32, color=YELLOW_B)
        ).arrange(DOWN).move_to(ORIGIN).shift(UP*1.5)

        self.play(FadeIn(factores_text, shift=UP), run_time=2)
        self.wait(1.5)

        # Preguntas clave
        preguntas_text = VGroup(
            Tex(r"1. ¿Efecto principal de Variedad?", font_size=28),
            Tex(r"2. ¿Efecto principal de Fertilizante?", font_size=28),
            Tex(r"3. ¿Interacción Variedad x Fertilizante?", font_size=28, color=YELLOW_B),
            Tex(r"4. Si hay efecto, ¿qué variedades difieren? (Tukey)", font_size=28)
        ).arrange(DOWN).next_to(factores_text, DOWN, buff=0.8)

        self.play(FadeIn(preguntas_text, shift=UP), run_time=2)
        self.wait(3)

        # Destacar la interacción
        interaccion_pregunta = preguntas_text[2]
        self.play(Indicate(interaccion_pregunta), run_time=1.5)
        self.wait(1)

        self.play(FadeOut(VGroup(titulo_ejemplo, factores_text, preguntas_text)))

        # ESCENA 6: CIERRE
        titulo_cierre = Tex(r"Conclusiones Clave", font_size=60, color=BLUE_D)
        self.play(Write(titulo_cierre), run_time=1.5, rate_func=smooth)
        self.wait(0.5)

        puntos_clave = VGroup(
            Tex(r"Control de variabilidad (DBCA)", font_size=36, color=GREEN_C),
            Tex(r"Análisis de interacciones (Factoriales)", font_size=36, color=GREEN_C),
            Tex(r"Comparaciones controladas (Post-Hoc)", font_size=36, color=GREEN_C)
        ).arrange(DOWN, buff=0.8).next_to(titulo_cierre, DOWN, buff=1)

        self.play(FadeIn(puntos_clave[0], shift=UP), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(puntos_clave[1], shift=UP), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(puntos_clave[2], shift=UP), run_time=1)
        self.wait(2)

        mensaje_final = Tex(r"¡Dominar estas técnicas es fundamental!", font_size=40, color=YELLOW_B).next_to(puntos_clave, DOWN, buff=1)
        self.play(Write(mensaje_final), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(VGroup(titulo_cierre, puntos_clave, mensaje_final)))
