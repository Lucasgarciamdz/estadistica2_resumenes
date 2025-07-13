from manim import *

class Unidad5Video(Scene):
    def construct(self):
        # --- INTRODUCCIÓN ---
        titulo = Tex(r"Unidad 5: Bondad de Ajuste e Independencia", font_size=48, color=BLUE_D)
        subtitulo = Tex(r"El Poder del Estadístico $\chi^2$", font_size=36, color=GREEN_C).next_to(titulo, DOWN)
        
        self.play(Write(titulo), run_time=1.5)
        self.play(FadeIn(subtitulo, shift=DOWN), run_time=1)
        self.wait(1)
        
        intro_text = Text("¡Bienvenidos a la Unidad 5 de Estadística Aplicada II!", font_size=28).to_edge(UP).shift(DOWN*1.5)
        intro_text2 = Text("Exploraremos las pruebas de Bondad de Ajuste y de Independencia.", font_size=28).next_to(intro_text, DOWN)
        intro_text3 = Text("Ambas basadas en el estadístico Chi-Cuadrado.", font_size=28).next_to(intro_text2, DOWN)
        
        self.play(FadeOut(titulo, shift=UP), FadeOut(subtitulo, shift=UP))
        self.play(Write(intro_text), Write(intro_text2), Write(intro_text3))
        self.wait(2)
        self.play(FadeOut(intro_text, intro_text2, intro_text3))

        # --- TEORÍA: FÓRMULA CHI-CUADRADO ---
        formula_chi2_title = Tex(r"Estadístico Chi-Cuadrado ($\chi^2$)", font_size=40, color=BLUE_D).to_edge(UP)
        formula_chi2 = MathTex(r"\chi^2 = \sum_{\text{todas las celdas}} \frac{(F_o - F_e)^2}{F_e}", font_size=60)
        
        self.play(Write(formula_chi2_title))
        self.play(Write(formula_chi2))
        self.wait(1)

        # Explicación Fo y Fe
        fo_text = Tex(r"$F_o$: Frecuencia Observada (conteo real)", font_size=30, color=YELLOW_B).next_to(formula_chi2, DOWN, buff=0.5).align_to(formula_chi2, LEFT)
        fe_text = Tex(r"$F_e$: Frecuencia Esperada (conteo si $H_0$ es cierta)", font_size=30, color=YELLOW_B).next_to(fo_text, DOWN).align_to(fo_text, LEFT)
        
        self.play(FadeIn(fo_text, shift=LEFT), FadeIn(fe_text, shift=LEFT))
        self.wait(2)

        # ¿Por qué al cuadrado?
        self.play(FadeOut(fo_text, fe_text))
        self.play(formula_chi2.animate.shift(UP*1.5))
        
        why_squared_q = Tex(r"¿Por qué $(F_o - F_e)^2$?", font_size=35, color=GREEN_C).next_to(formula_chi2, DOWN, buff=0.5)
        why_squared_ans1 = Tex(r"1. Evitar anulación de diferencias $\pm$", font_size=28).next_to(why_squared_q, DOWN).align_to(why_squared_q, LEFT)
        why_squared_ans2 = Tex(r"2. Magnificar grandes desviaciones", font_size=28).next_to(why_squared_ans1, DOWN).align_to(why_squared_ans1, LEFT)
        
        self.play(Write(why_squared_q))
        self.play(FadeIn(why_squared_ans1, shift=LEFT))
        self.play(FadeIn(why_squared_ans2, shift=LEFT))
        self.wait(3)
        
        self.play(FadeOut(why_squared_q, why_squared_ans1, why_squared_ans2))

        # ¿Por qué dividir por Fe?
        why_fe_q = Tex(r"¿Por qué dividir por $F_e$?", font_size=35, color=GREEN_C).next_to(formula_chi2, DOWN, buff=0.5)
        why_fe_ans1 = Tex(r"1. Ponderación por magnitud (normaliza)", font_size=28).next_to(why_fe_q, DOWN).align_to(why_fe_q, LEFT)
        why_fe_ans2 = Tex(r"2. Aproximación a la distribución $\chi^2$", font_size=28).next_to(why_fe_ans1, DOWN).align_to(why_fe_ans1, LEFT)
        
        self.play(Write(why_fe_q))
        self.play(FadeIn(why_fe_ans1, shift=LEFT))
        self.play(FadeIn(why_fe_ans2, shift=LEFT))
        self.wait(3)
        
        self.play(FadeOut(why_fe_q, why_fe_ans1, why_fe_ans2, formula_chi2, formula_chi2_title))

        # --- DEMOSTRACIÓN: BONDAD DE AJUSTE ---
        goodness_title = Tex(r"Prueba de Bondad de Ajuste", font_size=40, color=BLUE_D).to_edge(UP)
        self.play(Write(goodness_title))
        
        question_goa = Tex(r"¿Sigue una variable categórica una distribución teórica específica?", font_size=30).next_to(goodness_title, DOWN, buff=0.5)
        self.play(Write(question_goa))
        self.wait(1)

        h0_goa = Tex(r"$H_0$: La distribución sigue el modelo teórico.", font_size=28).next_to(question_goa, DOWN).align_to(question_goa, LEFT)
        fe_goa = MathTex(r"F_e = n \times p_i", font_size=40).next_to(h0_goa, DOWN, buff=0.5).align_to(h0_goa, LEFT)
        gl_goa = MathTex(r"gl = k - 1 - m", font_size=40).next_to(fe_goa, DOWN, buff=0.5).align_to(fe_goa, LEFT)
        
        self.play(FadeIn(h0_goa, shift=LEFT))
        self.play(Write(fe_goa))
        self.play(Write(gl_goa))
        self.wait(1)

        # ¿Por qué gl = k - 1 - m?
        why_gl_goa_q = Tex(r"¿Por qué $gl = k - 1 - m$?", font_size=30, color=GREEN_C).next_to(gl_goa, DOWN, buff=0.5).align_to(gl_goa, LEFT)
        why_gl_goa_ans = Tex(r"Se resta 1 porque $\sum F_o = \sum F_e = n$.", font_size=28).next_to(why_gl_goa_q, DOWN).align_to(why_gl_goa_q, LEFT)
        why_gl_goa_ans2 = Tex(r"$m$: parámetros estimados de la muestra.", font_size=28).next_to(why_gl_goa_ans, DOWN).align_to(why_gl_goa_ans, LEFT)
        
        self.play(Write(why_gl_goa_q))
        self.play(FadeIn(why_gl_goa_ans, shift=LEFT))
        self.play(FadeIn(why_gl_goa_ans2, shift=LEFT))
        self.wait(3)
        
        self.play(FadeOut(goodness_title, question_goa, h0_goa, fe_goa, gl_goa, why_gl_goa_q, why_gl_goa_ans, why_gl_goa_ans2))

        # --- DEMOSTRACIÓN: INDEPENDENCIA ---
        independence_title = Tex(r"Prueba de Independencia", font_size=40, color=BLUE_D).to_edge(UP)
        self.play(Write(independence_title))
        
        question_ind = Tex(r"¿Existe asociación entre dos variables categóricas?", font_size=30).next_to(independence_title, DOWN, buff=0.5)
        self.play(Write(question_ind))
        self.wait(1)

        h0_ind = Tex(r"$H_0$: Las dos variables son independientes.", font_size=28).next_to(question_ind, DOWN).align_to(question_ind, LEFT)
        fe_ind = MathTex(r"F_e = \frac{(\text{Total Fila } i) \times (\text{Total Columna } j)}{\text{Gran Total}}", font_size=40).next_to(h0_ind, DOWN, buff=0.5).align_to(h0_ind, LEFT)
        gl_ind = MathTex(r"gl = (r-1)(c-1)", font_size=40).next_to(fe_ind, DOWN, buff=0.5).align_to(fe_ind, LEFT)
        
        self.play(FadeIn(h0_ind, shift=LEFT))
        self.play(Write(fe_ind))
        self.play(Write(gl_ind))
        self.wait(1)

        # ¿Por qué esta fórmula para Fe en independencia?
        why_fe_ind_q = Tex(r"¿Por qué esta fórmula para $F_e$?", font_size=30, color=GREEN_C).next_to(fe_ind, DOWN, buff=0.5).align_to(fe_ind, LEFT)
        why_fe_ind_ans = Tex(r"Deriva de $P(A \cap B) = P(A) \times P(B)$ para eventos independientes.", font_size=28).next_to(why_fe_ind_q, DOWN).align_to(why_fe_ind_q, LEFT)
        
        self.play(Write(why_fe_ind_q))
        self.play(FadeIn(why_fe_ind_ans, shift=LEFT))
        self.wait(3)
        
        self.play(FadeOut(why_fe_ind_q, why_fe_ind_ans))

        # ¿Por qué gl = (r-1)(c-1)?
        why_gl_ind_q = Tex(r"¿Por qué $gl = (r-1)(c-1)$?", font_size=30, color=GREEN_C).next_to(gl_ind, DOWN, buff=0.5).align_to(gl_ind, LEFT)
        why_gl_ind_ans = Tex(r"Número de celdas 'libres' antes de que los marginales fijen el resto.", font_size=28).next_to(why_gl_ind_q, DOWN).align_to(why_gl_ind_q, LEFT)
        
        self.play(Write(why_gl_ind_q))
        self.play(FadeIn(why_gl_ind_ans, shift=LEFT))
        self.wait(3)
        
        self.play(FadeOut(independence_title, question_ind, h0_ind, fe_ind, gl_ind, why_gl_ind_q, why_gl_ind_ans))

        # --- EJEMPLO: BONDAD DE AJUSTE (Producto A, B, C) ---
        example_title = Tex(r"Ejemplo: Bondad de Ajuste (Productos)", font_size=40, color=BLUE_D).to_edge(UP)
        self.play(Write(example_title))

        # Datos del problema
        problem_text1 = Tex(r"Empresa: 30\% A, 50\% B, 20\% C.", font_size=28).next_to(example_title, DOWN, buff=0.5).align_to(example_title, LEFT)
        problem_text2 = Tex(r"Encuesta (n=200): 50 A, 110 B, 40 C.", font_size=28).next_to(problem_text1, DOWN).align_to(problem_text1, LEFT)
        
        self.play(Write(problem_text1), Write(problem_text2))
        self.wait(1)

        # Frecuencias Observadas
        fo_table = MobjectTable(
            [[Tex("Producto A"), Tex("Producto B"), Tex("Producto C")],
             [MathTex("F_o = 50"), MathTex("F_o = 110"), MathTex("F_o = 40")]],
            include_outer_lines=True
        ).scale(0.7).next_to(problem_text2, DOWN, buff=0.5)
        self.play(Create(fo_table))
        self.wait(1)

        # Frecuencias Esperadas
        fe_calc_title = Tex(r"Cálculo de $F_e$ (bajo $H_0$):", font_size=30, color=YELLOW_B).next_to(fo_table, DOWN, buff=0.5).align_to(fo_table, LEFT)
        fe_a = MathTex(r"F_{e,A} = 200 \times 0.30 = 60", font_size=30).next_to(fe_calc_title, DOWN).align_to(fe_calc_title, LEFT)
        fe_b = MathTex(r"F_{e,B} = 200 \times 0.50 = 100", font_size=30).next_to(fe_a, DOWN).align_to(fe_a, LEFT)
        fe_c = MathTex(r"F_{e,C} = 200 \times 0.20 = 40", font_size=30).next_to(fe_b, DOWN).align_to(fe_b, LEFT)
        
        self.play(Write(fe_calc_title))
        self.play(Write(fe_a), Write(fe_b), Write(fe_c))
        self.wait(2)

        # Cálculo del Estadístico Chi-Cuadrado
        self.play(FadeOut(problem_text1, problem_text2, fo_table, fe_calc_title, fe_a, fe_b, fe_c))
        
        chi2_calc_title = Tex(r"Cálculo de $\chi^2$:", font_size=35, color=BLUE_D).to_edge(UP)
        self.play(Transform(example_title, chi2_calc_title))

        chi2_term1 = MathTex(r"\frac{(50-60)^2}{60}", font_size=40)
        chi2_term2 = MathTex(r"\frac{(110-100)^2}{100}", font_size=40)
        chi2_term3 = MathTex(r"\frac{(40-40)^2}{40}", font_size=40)
        
        chi2_sum = VGroup(chi2_term1, MathTex("+"), chi2_term2, MathTex("+"), chi2_term3).arrange(RIGHT, buff=0.3).shift(UP*1)
        self.play(Write(chi2_sum))
        self.wait(1)

        chi2_res1 = MathTex(r"\frac{(-10)^2}{60}", font_size=40)
        chi2_res2 = MathTex(r"\frac{(10)^2}{100}", font_size=40)
        chi2_res3 = MathTex(r"\frac{(0)^2}{40}", font_size=40)
        
        chi2_sum_res = VGroup(chi2_res1, MathTex("+"), chi2_res2, MathTex("+"), chi2_res3).arrange(RIGHT, buff=0.3).next_to(chi2_sum, DOWN, buff=0.5)
        self.play(TransformMatchingTex(chi2_sum, chi2_sum_res))
        self.wait(1)

        chi2_val1 = MathTex(r"1.667", font_size=40)
        chi2_val2 = MathTex(r"1", font_size=40)
        chi2_val3 = MathTex(r"0", font_size=40)
        
        chi2_final_sum = VGroup(chi2_val1, MathTex("+"), chi2_val2, MathTex("+"), chi2_val3).arrange(RIGHT, buff=0.3).next_to(chi2_sum_res, DOWN, buff=0.5)
        self.play(TransformMatchingTex(chi2_sum_res, chi2_final_sum))
        self.wait(1)

        chi2_result = MathTex(r"\chi^2 = 2.667", font_size=50, color=GREEN_C).next_to(chi2_final_sum, DOWN, buff=0.7)
        self.play(Write(chi2_result))
        self.wait(2)

        # Grados de Libertad y Conclusión
        gl_example = MathTex(r"gl = k - 1 = 3 - 1 = 2", font_size=40).next_to(chi2_result, DOWN, buff=0.5)
        self.play(Write(gl_example))
        self.wait(1)

        conclusion_text = Tex(r"Con $\alpha=0.05$, si $\chi^2_{calc} < \chi^2_{crit}$, no rechazamos $H_0$.", font_size=30).next_to(gl_example, DOWN, buff=0.5)
        self.play(Write(conclusion_text))
        self.wait(2)

        # --- Condición F_e >= 5 ---
        self.play(FadeOut(chi2_calc_title, chi2_result, gl_example, conclusion_text, chi2_final_sum))
        
        fe_condition_title = Tex(r"Condición Crítica: $F_e \ge 5$", font_size=40, color=BLUE_D).to_edge(UP)
        self.play(Transform(example_title, fe_condition_title))

        why_fe5_q = Tex(r"¿Por qué $F_e \ge 5$ es tan crítica?", font_size=35, color=GREEN_C).next_to(fe_condition_title, DOWN, buff=0.5)
        why_fe5_ans1 = Tex(r"1. Aproximación discreta a continua (Chi-Cuadrado).", font_size=28).next_to(why_fe5_q, DOWN).align_to(why_fe5_q, LEFT)
        why_fe5_ans2 = Tex(r"2. Evita p-valores incorrectos y decisiones erróneas.", font_size=28).next_to(why_fe5_ans1, DOWN).align_to(why_fe5_ans1, LEFT)
        
        self.play(Write(why_fe5_q))
        self.play(FadeIn(why_fe5_ans1, shift=LEFT))
        self.play(FadeIn(why_fe5_ans2, shift=LEFT))
        self.wait(3)

        # --- CIERRE ---
        self.play(FadeOut(fe_condition_title, why_fe5_q, why_fe5_ans1, why_fe5_ans2))
        
        closure_title = Tex(r"Conclusión", font_size=40, color=BLUE_D).to_edge(UP)
        self.play(Transform(example_title, closure_title))

        closure_text1 = Tex(r"Herramientas esenciales para analizar datos categóricos.", font_size=30).next_to(closure_title, DOWN, buff=0.5)
        closure_text2 = Tex(r"Comparan $F_o$ y $F_e$ usando el estadístico $\chi^2$.", font_size=30).next_to(closure_text1, DOWN)
        closure_text3 = Tex(r"Comprender los 'porqués' es clave para una interpretación rigurosa.", font_size=30).next_to(closure_text2, DOWN)
        
        self.play(Write(closure_text1), Write(closure_text2), Write(closure_text3))
        self.wait(3)
        
        self.play(FadeOut(closure_title, closure_text1, closure_text2, closure_text3))
        self.wait(1)

    # Placeholder for dynamic graph, not used in this specific script but kept for future use
    def get_grafico_dinamico(self, param):
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1, 0.2],
            axis_config={"color": GRAY},
            x_axis_config={"numbers_to_include": [0, 2, 4, 6, 8, 10]},
            y_axis_config={"numbers_to_include": [0, 0.2, 0.4, 0.6, 0.8, 1]},
        )
        
        # Example: a simple parabola whose shape changes with 'param'
        graph = axes.plot(lambda x: (x - 5)**2 * param * 0.01, color=BLUE)
        
        return VGroup(axes, graph)
