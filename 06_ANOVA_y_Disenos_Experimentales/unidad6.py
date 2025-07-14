from manim import *

class Unidad6ANOVA(Scene):
    def construct(self):
        # Colores personalizados
        BLUE_D = "#336699"
        GREEN_C = "#66CC99"
        YELLOW_B = "#FFCC66"
        RED_A = "#CC3333"

        # Escena 1: Introducción
        titulo = Tex(r"Análisis de Varianza (ANOVA)", font_size=60, color=BLUE_D)
        subtitulo = Tex(r"Diseños Experimentales Avanzados", font_size=40, color=YELLOW_B).next_to(titulo, DOWN)

        self.play(Write(titulo))
        self.play(FadeIn(subtitulo, shift=UP))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo, subtitulo)))

        # Escena 2: Diseño Completamente Aleatorio
        titulo_dca = Tex(r"Diseño Completamente Aleatorio (DCA)", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_dca))

        grupo_a = VGroup(*[Circle(radius=0.2, color=GREEN_C, fill_opacity=0.5) for _ in range(5)]).arrange(RIGHT)
        grupo_b = VGroup(*[Square(side_length=0.4, color=YELLOW_B, fill_opacity=0.5) for _ in range(5)]).arrange(RIGHT)
        grupo_c = VGroup(*[Triangle(color=RED_A, fill_opacity=0.5) for _ in range(5)]).arrange(RIGHT)

        grupos = VGroup(grupo_a, grupo_b, grupo_c).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(FadeIn(grupos, shift=UP))

        texto_dca = Tex(r"Tratamientos asignados aleatoriamente a unidades homogéneas.", font_size=32).next_to(grupos, DOWN, buff=0.5)
        self.play(Write(texto_dca))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo_dca, grupos, texto_dca)))

        # Escena 3: Tamaños Muestrales Distintos
        titulo_tmd = Tex(r"Tamaños Muestrales Distintos", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_tmd))

        grupo_a_tmd = VGroup(*[Circle(radius=0.2, color=GREEN_C, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT)
        grupo_b_tmd = VGroup(*[Square(side_length=0.4, color=YELLOW_B, fill_opacity=0.5) for _ in range(6)]).arrange(RIGHT)
        grupo_c_tmd = VGroup(*[Triangle(color=RED_A, fill_opacity=0.5) for _ in range(5)]).arrange(RIGHT)

        grupos_tmd = VGroup(grupo_a_tmd, grupo_b_tmd, grupo_c_tmd).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(FadeIn(grupos_tmd, shift=UP))

        texto_tmd = Tex(r"Los cálculos se ajustan, pero la lógica de ANOVA se mantiene.", font_size=32).next_to(grupos_tmd, DOWN, buff=0.5)
        self.play(Write(texto_tmd))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo_tmd, grupos_tmd, texto_tmd)))

        # Escena 4: Diseño en Bloques Aleatorios
        titulo_dba = Tex(r"Diseño en Bloques Aleatorios (DBA)", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_dba))

        bloque1 = Rectangle(width=5, height=1.5, color=WHITE).move_to(LEFT*3)
        bloque2 = Rectangle(width=5, height=1.5, color=WHITE).move_to(RIGHT*3)

        texto_b1 = Tex("Bloque 1").next_to(bloque1, UP)
        texto_b2 = Tex("Bloque 2").next_to(bloque2, UP)

        self.play(Create(bloque1), Create(bloque2), Write(texto_b1), Write(texto_b2))

        grupo_a_b1 = Circle(radius=0.2, color=GREEN_C, fill_opacity=0.5).move_to(bloque1.get_center() + LEFT*1.5)
        grupo_b_b1 = Square(side_length=0.4, color=YELLOW_B, fill_opacity=0.5).move_to(bloque1.get_center())
        grupo_c_b1 = Triangle(color=RED_A, fill_opacity=0.5).move_to(bloque1.get_center() + RIGHT*1.5)

        grupo_a_b2 = Circle(radius=0.2, color=GREEN_C, fill_opacity=0.5).move_to(bloque2.get_center() + LEFT*1.5)
        grupo_b_b2 = Square(side_length=0.4, color=YELLOW_B, fill_opacity=0.5).move_to(bloque2.get_center())
        grupo_c_b2 = Triangle(color=RED_A, fill_opacity=0.5).move_to(bloque2.get_center() + RIGHT*1.5)

        self.play(FadeIn(VGroup(grupo_a_b1, grupo_b_b1, grupo_c_b1, grupo_a_b2, grupo_b_b2, grupo_c_b2)))

        texto_dba = Tex(r"Controla una fuente de variabilidad externa.", font_size=32).to_edge(DOWN)
        self.play(Write(texto_dba))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo_dba, bloque1, bloque2, texto_b1, texto_b2, grupo_a_b1, grupo_b_b1, grupo_c_b1, grupo_a_b2, grupo_b_b2, grupo_c_b2, texto_dba)))

        # Escena 5: Comparaciones Múltiples
        titulo_cm = Tex(r"Comparaciones Múltiples", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_cm))

        texto_cm = Tex(r"¿Qué grupos son específicamente diferentes?", font_size=36).move_to(ORIGIN)
        self.play(Write(texto_cm))
        self.wait(2)

        formula_cm = MathTex(r"\mu_i \neq \mu_j", font_size=48).next_to(texto_cm, DOWN)
        self.play(Write(formula_cm))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo_cm, texto_cm, formula_cm)))

        # Escena 6: Rango Mínimo de Duncan
        titulo_duncan = Tex(r"Rango Mínimo de Duncan", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_duncan))

        texto_duncan = Tex(r"Una prueba de comparación múltiple.", font_size=36).move_to(ORIGIN)
        self.play(Write(texto_duncan))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo_duncan, texto_duncan)))

        # Escena 7: Cuadros Latinos
        titulo_cl = Tex(r"Diseño de Cuadros Latinos", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_cl))

        texto_cl = Tex(r"Controla dos fuentes de variabilidad.", font_size=36).move_to(ORIGIN)
        self.play(Write(texto_cl))
        self.wait(2)

        grid = Square().to_edge(LEFT)
        row1 = VGroup(*[Tex("A"), Tex("B"), Tex("C")]).arrange(RIGHT).move_to(grid.get_center() + UP*0.5)
        row2 = VGroup(*[Tex("B"), Tex("C"), Tex("A")]).arrange(RIGHT).move_to(grid.get_center())
        row3 = VGroup(*[Tex("C"), Tex("A"), Tex("B")]).arrange(RIGHT).move_to(grid.get_center() + DOWN*0.5)

        self.play(Write(VGroup(row1, row2, row3)))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo_cl, texto_cl, row1, row2, row3)))

        # Escena 8: Cuadros Grecolatinos
        titulo_cgl = Tex(r"Diseño de Cuadros Grecolatinos", font_size=48, color=BLUE_D).to_edge(UP)
        self.play(Write(titulo_cgl))

        texto_cgl = Tex(r"Controla tres fuentes de variabilidad.", font_size=36).move_to(ORIGIN)
        self.play(Write(texto_cgl))
        self.wait(2)

        grid_gl = Square().to_edge(LEFT)
        row1_gl = VGroup(*[Tex(r"A$\alpha$"), Tex(r"B$\beta$"), Tex(r"C$\gamma$")]).arrange(RIGHT).move_to(grid_gl.get_center() + UP*0.5)
        row2_gl = VGroup(*[Tex(r"B$\gamma$"), Tex(r"C$\alpha$"), Tex(r"A$\beta$")]).arrange(RIGHT).move_to(grid_gl.get_center())
        row3_gl = VGroup(*[Tex(r"C$\beta$"), Tex(r"A$\gamma$"), Tex(r"B$\alpha$")]).arrange(RIGHT).move_to(grid_gl.get_center() + DOWN*0.5)

        self.play(Write(VGroup(row1_gl, row2_gl, row3_gl)))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo_cgl, texto_cgl, row1_gl, row2_gl, row3_gl)))

        # Escena 9: Cierre
        titulo_cierre = Tex(r"Resumen", font_size=60, color=BLUE_D)
        self.play(Write(titulo_cierre))

        puntos_clave = VGroup(
            Tex(r"- Diseño Completamente Aleatorio"),
            Tex(r"- Tamaños Muestrales Distintos"),
            Tex(r"- Diseño en Bloques Aleatorios"),
            Tex(r"- Comparaciones Múltiples"),
            Tex(r"- Rango Mínimo de Duncan"),
            Tex(r"- Cuadros Latinos y Grecolatinos"),
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.7).next_to(titulo_cierre, DOWN, buff=0.5)

        self.play(Write(puntos_clave))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo_cierre, puntos_clave)))
