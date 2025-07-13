from manim import *

class PruebasNoParametricas(Scene):
    def construct(self):
        # --- ESCENA 1: INTRODUCCIÓN ---
        titulo = Tex(r"\textbf{Pruebas No Paramétricas: Más Allá de la Normalidad}", font_size=56, color=BLUE_D)
        subtitulo = Tex(r"Cuando la normalidad no es una opción", font_size=36, color=YELLOW_B).next_to(titulo, DOWN, buff=0.5)

        self.play(Write(titulo))
        self.play(FadeIn(subtitulo, shift=DOWN))
        self.wait(1.5)

        # Transición a la idea central
        parametric_text = Tex(r"Pruebas Paramétricas: Asumen Normalidad", font_size=30, color=GREEN_C).to_edge(UP + LEFT)
        non_parametric_text = Tex(r"Pruebas No Paramétricas: Sin Supuestos de Distribución", font_size=30, color=BLUE_D).to_edge(UP + RIGHT)

        self.play(
            Transform(titulo, parametric_text),
            FadeOut(subtitulo)
        )
        self.wait(0.5)
        self.play(
            Transform(titulo, non_parametric_text) # Reusing titulo Mobject
        )
        self.wait(1)

        # --- ESCENA 2: LA LÓGICA DEL RANGO ---
        self.play(FadeOut(titulo)) # Fade out the previous text

        titulo_rango = Tex(r"\textbf{La Lógica del Rango}", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_rango))
        self.wait(0.5)

        # Datos originales
        data_raw_label = Tex("Datos Originales:", font_size=30).to_edge(LEFT).shift(UP*1.5)
        data_raw = MathTex(r"\{12, 5, 18, 7, 12\}", font_size=36).next_to(data_raw_label, RIGHT)
        self.play(Write(data_raw_label), Write(data_raw))
        self.wait(1)

        # Transformación a rangos
        arrow_transform = Arrow(data_raw.get_right(), data_raw.get_right() + RIGHT*2, color=YELLOW_B)
        ranks_label = Tex("Transformación a Rangos:", font_size=30).next_to(arrow_transform, RIGHT).shift(UP*1.5)
        # Sorted data: 5, 7, 12, 12, 18
        # Ranks: 1, 2, 3.5, 3.5, 5 (12 is tied, occupies 3rd and 4th position, so (3+4)/2 = 3.5)
        data_ranks = MathTex(r"\{3.5, 1, 5, 2, 3.5\}", font_size=36).next_to(ranks_label, RIGHT) # Ranks in original order

        self.play(GrowArrow(arrow_transform))
        self.play(Write(ranks_label), Write(data_ranks))
        self.wait(1.5)

        # Explicación del "Por qué"
        why_robust = Tex(r"\textbf{¿Por qué usar rangos?}", font_size=36, color=GREEN_C).next_to(data_raw_label, DOWN*2, aligned_edge=LEFT)
        explanation_robust = Tex(r"Elimina dependencia de la distribución original.", font_size=28).next_to(why_robust, DOWN, aligned_edge=LEFT)
        explanation_robust2 = Tex(r"Robusto a no-normalidad y outliers.", font_size=28).next_to(explanation_robust, DOWN, aligned_edge=LEFT)

        self.play(Write(why_robust))
        self.play(FadeIn(explanation_robust, shift=UP))
        self.play(FadeIn(explanation_robust2, shift=UP))
        self.wait(2)

        # Costo: Pérdida de información
        why_power_loss = Tex(r"\textbf{¿Por qué se pierde potencia?}", font_size=36, color=YELLOW_B).next_to(explanation_robust2, DOWN*2, aligned_edge=LEFT)
        explanation_power_loss = Tex(r"Se pierde la \textbf{magnitud} de las diferencias.", font_size=28).next_to(why_power_loss, DOWN, aligned_edge=LEFT)
        explanation_power_loss2 = Tex(r"Ej: (1,2) vs (100,101) tienen mismo rango, diferente magnitud.", font_size=24).next_to(explanation_power_loss, DOWN, aligned_edge=LEFT)

        self.play(Write(why_power_loss))
        self.play(FadeIn(explanation_power_loss, shift=UP))
        self.play(FadeIn(explanation_power_loss2, shift=UP))
        self.wait(2.5)

        self.play(
            FadeOut(titulo_rango, data_raw_label, data_raw, arrow_transform, ranks_label, data_ranks,
                    why_robust, explanation_robust, explanation_robust2,
                    why_power_loss, explanation_power_loss, explanation_power_loss2)
        )
        self.wait(0.5)

        # --- ESCENA 3: PRUEBA DE RANGOS CON SIGNO DE WILCOXON ---
        wilcoxon_title = Tex(r"\textbf{Prueba de Rangos con Signo de Wilcoxon}", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(wilcoxon_title))
        self.wait(0.5)

        # Pasos
        step1 = Tex(r"1. Calcular diferencias $D_i = X_i - Y_i$.".replace("\\", "\\"), font_size=30).to_edge(LEFT).shift(UP*1.5)
        step2 = Tex(r"2. Ignorar $D_i = 0$.".replace("\\", "\\"), font_size=30).next_to(step1, DOWN, aligned_edge=LEFT)
        step3 = Tex(r"3. Ordenar $|D_i|$ y asignar rangos.".replace("\\", "\\"), font_size=30).next_to(step2, DOWN, aligned_edge=LEFT)
        step4 = Tex(r"4. Asignar signo original a los rangos.".replace("\\", "\\"), font_size=30).next_to(step3, DOWN, aligned_edge=LEFT)
        step5 = Tex(r"5. Calcular $W^+$ (suma rangos positivos) y $W^-$ (suma rangos negativos).".replace("\\", "\\"), font_size=30).next_to(step4, DOWN, aligned_edge=LEFT)
        step6 = Tex(r"6. Estadístico de prueba $W = \min(W^+, W^-)$.".replace("\\", "\\"), font_size=30).next_to(step5, DOWN, aligned_edge=LEFT)

        steps_group = VGroup(step1, step2, step3, step4, step5, step6)
        self.play(LaggedStart(*[Write(step) for step in steps_group], lag_ratio=0.5))
        self.wait(1)

        # Detalle: Manejo de empates
        tie_handling_text = Tex(r"\textbf{Manejo de Empates: Rango Promedio}", font_size=36, color=GREEN_C).next_to(steps_group, DOWN*2, aligned_edge=LEFT)
        tie_example = MathTex(r"\{2, 3, \textbf{5, 5}, 7\} \rightarrow \text{Rangos: } \{1, 2, \textbf{3.5, 3.5}, 5\}", font_size=30).next_to(tie_handling_text, DOWN, aligned_edge=LEFT)

        self.play(Write(tie_handling_text))
        self.play(Write(tie_example))
        self.wait(1)

        why_average_rank = Tex(r"\textbf{¿Por qué rango promedio?}", font_size=28, color=YELLOW_B).next_to(tie_example, DOWN, aligned_edge=LEFT)
        explanation_average_rank = Tex(r"Para equidad y consistencia en la asignación de rangos.", font_size=24).next_to(why_average_rank, DOWN, aligned_edge=LEFT)

        self.play(Write(why_average_rank))
        self.play(FadeIn(explanation_average_rank, shift=UP))
        self.wait(2)

        # Detalle: Por qué min(W+, W-)
        why_min_W = Tex(r"\textbf{¿Por qué $W = \min(W^+, W^-)$?}", font_size=28, color=YELLOW_B).next_to(explanation_average_rank, DOWN*2, aligned_edge=LEFT)
        explanation_min_W = Tex(r"Un $W$ pequeño indica un desequilibrio significativo de rangos.", font_size=24).next_to(why_min_W, DOWN, aligned_edge=LEFT)

        self.play(Write(why_min_W))
        self.play(FadeIn(explanation_min_W, shift=UP))
        self.wait(2)

        self.play(
            FadeOut(wilcoxon_title, steps_group, tie_handling_text, tie_example,
                    why_average_rank, explanation_average_rank, why_min_W, explanation_min_W)
        )
        self.wait(0.5)

        # --- ESCENA 4: CORRECCIÓN POR EMPATES EN LA VARIANZA ---
        correction_title = Tex(r"\textbf{Corrección por Empates en la Varianza}", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(correction_title))
        self.wait(0.5)

        variance_formula_uncorrected = MathTex(r"\sigma_W^2 = \frac{n(n+1)(2n+1)}{24}", font_size=40).shift(UP*1.5)
        self.play(Write(variance_formula_uncorrected))
        self.wait(1)

        # Introduce the correction term
        correction_term = MathTex(r"- \frac{\sum_{j=1}^{g} (t_j^3 - t_j)}{48}", font_size=40, color=RED).next_to(variance_formula_uncorrected, RIGHT, buff=0.2)
        variance_formula_corrected = MathTex(r"\sigma_W^2 = \frac{n(n+1)(2n+1)}{24} - \frac{\sum_{j=1}^{g} (t_j^3 - t_j)}{48}", font_size=40).shift(UP*1.5)

        self.play(TransformMatchingTex(variance_formula_uncorrected, variance_formula_corrected))
        self.wait(1)

        # Highlight the correction term
        rect_correction = SurroundingRectangle(variance_formula_corrected[0][12:], color=YELLOW_B, buff=0.1) # Adjust index based on the formula
        text_correction = Tex(r"Término de corrección por empates", font_size=28, color=YELLOW_B).next_to(rect_correction, DOWN)
        arrow_correction = Arrow(text_correction.get_top(), rect_correction.get_bottom(), color=YELLOW_B)

        self.play(Create(rect_correction), Write(text_correction), GrowArrow(arrow_correction))
        self.wait(1.5)

        # Why is it needed?
        why_correction = Tex(r"\textbf{¿Por qué la varianza real es menor con empates?}", font_size=36, color=GREEN_C).next_to(variance_formula_corrected, DOWN*2)
        explanation_correction = Tex(r"Los empates reducen la variabilidad en la asignación de rangos.", font_size=28).next_to(why_correction, DOWN)
        explanation_correction2 = Tex(r"Asegura una aproximación normal precisa.", font_size=28).next_to(explanation_correction, DOWN)

        self.play(Write(why_correction))
        self.play(FadeIn(explanation_correction, shift=UP))
        self.play(FadeIn(explanation_correction2, shift=UP))
        self.wait(2.5)

        self.play(
            FadeOut(correction_title, variance_formula_corrected, rect_correction, text_correction, arrow_correction,
                    why_correction, explanation_correction, explanation_correction2)
        )
        self.wait(0.5)

        # --- ESCENA 5: CIERRE ---
        closing_title = Tex(r"\textbf{Conclusiones Clave}", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(closing_title))
        self.wait(0.5)

        point1 = Tex(r"1. Usar cuando no hay normalidad, datos ordinales o outliers.", font_size=32).to_edge(LEFT).shift(UP*1.5)
        point2 = Tex(r"2. Se basan en rangos: robustez vs. potencia.", font_size=32).next_to(point1, DOWN, aligned_edge=LEFT)
        point3 = Tex(r"3. Crucial para muestras pequeñas.", font_size=32).next_to(point2, DOWN, aligned_edge=LEFT)
        point4 = Tex(r"4. Dominar su aplicación es una habilidad clave.", font_size=32).next_to(point3, DOWN, aligned_edge=LEFT)

        closing_points = VGroup(point1, point2, point3, point4)
        self.play(LaggedStart(*[Write(point) for point in closing_points], lag_ratio=0.5))
        self.wait(3)

        self.play(FadeOut(closing_title, closing_points))
        self.wait(1)
