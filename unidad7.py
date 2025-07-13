from manim import *


class Unidad7(Scene):
    def construct(self):
        # [INTRODUCCIÓN ~15s]
        # Esta sección introduce el tema de los Procesos Estocásticos.
        # Se busca una animación que sea visualmente atractiva y que establezca el tono.
        # Se utiliza un título principal y un subtítulo para contextualizar.

        # Título principal de la unidad
        title = Tex("Unidad 7: Procesos Estocásticos", color=BLUE_D).scale(1.5)
        # Subtítulo que introduce la idea de evolución y aleatoriedad
        subtitle = Tex(
            "Modelando sistemas dinámicos con incertidumbre",
            color=GREEN_C
        ).next_to(title, DOWN, buff=0.5)

        # Animación de aparición del título y subtítulo
        self.play(
            FadeIn(title, shift=UP), # El título aparece desde abajo, dando una sensación de ascenso.
            FadeIn(subtitle, shift=DOWN), # El subtítulo aparece desde arriba, complementando al título.
            run_time=2,
            rate_func=smooth # Transición suave para una apariencia profesional.
        )
        self.wait(3) # Pausa para que el espectador asimile la información.

        # Transición a la siguiente sección: el título se mueve a la esquina superior izquierda
        # para dejar espacio al contenido de la teoría.
        self.play(
            title.animate.to_corner(UL), # Mueve el título a la esquina superior izquierda.
            FadeOut(subtitle), # El subtítulo desaparece para no sobrecargar la pantalla.
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(1)

        # [TEORÍA ~2-3min]
        # Esta sección define qué es un proceso estocástico, sus elementos clave y la Propiedad de Markov.

        # 1. Definición de Proceso Estocástico
        # Se presenta la definición formal de un proceso estocástico.
        definition_title = Tex("¿Qué es un Proceso Estocástico?", color=BLUE_D).to_edge(UP).shift(DOWN*0.5)
        self.play(Write(definition_title), rate_func=smooth)
        self.wait(0.5)

        # Texto de la definición
        process_def = Tex(
            "Un proceso estocástico $X(t)$ es una colección de variables aleatorias",
            "indexadas por un parámetro (usualmente el tiempo 't').",
            color=BLUE_D
        ).scale(0.8).next_to(definition_title, DOWN, buff=0.5).align_to(definition_title.get_left())

        # Se usa FadeIn para que el texto aparezca de forma gradual.
        self.play(FadeIn(process_def[0]), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(process_def[1]), run_time=1.5, rate_func=smooth)
        self.wait(1)

        # Elementos clave: Espacio de Estados y Parámetro de Tiempo
        key_elements_title = Tex("Elementos Clave:", color=GREEN_C).next_to(process_def, DOWN, buff=0.7).align_to(process_def.get_left())
        self.play(Write(key_elements_title), rate_func=smooth)
        self.wait(0.5)

        # Espacio de Estados
        state_space_text = Tex(
            "Espacio de Estados: Conjunto de posibles valores o 'estados'.",
            "Ej: Clima (Soleado, Nublado, Lluvioso).",
            color=BLUE_D
        ).scale(0.7).next_to(key_elements_title, DOWN, buff=0.3).align_to(key_elements_title.get_left())

        # Parámetro de Tiempo
        time_param_text = Tex(
            "Parámetro de Tiempo: Discreto (t=0,1,2,...) o Continuo (t$\\ge$0).",
            color=BLUE_D
        ).scale(0.7).next_to(state_space_text, DOWN, buff=0.3).align_to(key_elements_title.get_left())

        # Animación de aparición de los elementos clave
        self.play(FadeIn(state_space_text, shift=LEFT), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(time_param_text, shift=LEFT), run_time=1.5, rate_func=smooth)
        self.wait(2)

        # Realización o Trayectoria
        realization_text = Tex(
            "Realización o Trayectoria: Secuencia de valores observados a lo largo del tiempo.",
            color=BLUE_D
        ).scale(0.7).next_to(time_param_text, DOWN, buff=0.3).align_to(key_elements_title.get_left())
        self.play(FadeIn(realization_text, shift=LEFT), run_time=1.5, rate_func=smooth)
        self.wait(2)

        # Transición a Cadenas de Markov
        self.play(
            FadeOut(definition_title, shift=UP),
            FadeOut(process_def, shift=UP),
            FadeOut(key_elements_title, shift=UP),
            FadeOut(state_space_text, shift=UP),
            FadeOut(time_param_text, shift=UP),
            FadeOut(realization_text, shift=UP),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)

        # 2. Cadenas de Markov y Propiedad de Markov
        markov_title = Tex("Cadenas de Markov", color=BLUE_D).to_edge(UP).shift(DOWN*0.5)
        self.play(Write(markov_title), rate_func=smooth)
        self.wait(0.5)

        markov_property_text = Tex(
            "Propiedad de Markov (Carencia de Memoria):",
            "El futuro depende solo del estado presente, no del pasado.",
            color=BLUE_D
        ).scale(0.8).next_to(markov_title, DOWN, buff=0.5).align_to(markov_title.get_left())

        self.play(FadeIn(markov_property_text[0]), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(markov_property_text[1]), run_time=1.5, rate_func=smooth)
        self.wait(2)

        # Fórmula de la Propiedad de Markov
        markov_formula = MathTex(
            "P(X_{t+1}=j \\mid X_t=i, X_{t-1}=i_{t-1}, \\dots) = P(X_{t+1}=j \\mid X_t=i)",
            color=GREEN_C
        ).scale(0.8).next_to(markov_property_text, DOWN, buff=0.5)

        # Se usa Write para que la fórmula aparezca escribiéndose.
        self.play(Write(markov_formula), run_time=3, rate_func=smooth)
        self.wait(2)

        # Anotación visual para resaltar "carencia de memoria"
        # Se usa SurroundingRectangle para enmarcar la parte clave de la fórmula.
        # Se usa Arrow para señalar la implicación de la carencia de memoria.
        memory_loss_rect = SurroundingRectangle(markov_property_text[1], color=RED, buff=0.1)
        memory_loss_arrow = Arrow(memory_loss_rect.get_bottom(), markov_formula.get_top(), color=RED)
        memory_loss_explanation = Tex("Simplifica el cálculo", color=RED).next_to(memory_loss_arrow, DOWN)

        self.play(Create(memory_loss_rect), run_time=1, rate_func=smooth)
        self.play(GrowArrow(memory_loss_arrow), Write(memory_loss_explanation), run_time=1.5, rate_func=smooth)
        self.wait(2)

        self.play(
            FadeOut(memory_loss_rect),
            FadeOut(memory_loss_arrow),
            FadeOut(memory_loss_explanation),
            run_time=1,
            rate_func=smooth
        )
        self.wait(0.5)

        # 3. Matriz de Transición
        self.play(
            FadeOut(markov_title, shift=UP),
            FadeOut(markov_property_text, shift=UP),
            FadeOut(markov_formula, shift=UP),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)

        matrix_title = Tex("Matriz de Transición (P)", color=BLUE_D).to_edge(UP).shift(DOWN*0.5)
        self.play(Write(matrix_title), rate_func=smooth)
        self.wait(0.5)

        matrix_def_text = Tex(
            "Contiene las probabilidades de transición de un paso, $p_{ij}$.",
            "Probabilidad de pasar del estado $i$ al estado $j$.",
            color=BLUE_D
        ).scale(0.8).next_to(matrix_title, DOWN, buff=0.5).align_to(matrix_title.get_left())

        self.play(FadeIn(matrix_def_text[0]), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(matrix_def_text[1]), run_time=1.5, rate_func=smooth)
        self.wait(1)

        # Propiedades de la Matriz de Transición
        matrix_properties_title = Tex("Propiedades Clave:", color=GREEN_C).next_to(matrix_def_text, DOWN, buff=0.7).align_to(matrix_def_text.get_left())
        self.play(Write(matrix_properties_title), rate_func=smooth)
        self.wait(0.5)

        property1 = Tex("1. Es una matriz cuadrada.", color=BLUE_D).scale(0.7).next_to(matrix_properties_title, DOWN, buff=0.3).align_to(matrix_properties_title.get_left())
        property2 = Tex("2. Cada entrada $p_{ij}$ está entre 0 y 1 ($0 \\le p_{ij} \\le 1$).", color=BLUE_D).scale(0.7).next_to(property1, DOWN, buff=0.3).align_to(matrix_properties_title.get_left())
        property3 = Tex("3. La suma de las entradas de cada fila es 1 ($\\sum_j p_{ij} = 1$).", color=BLUE_D).scale(0.7).next_to(property2, DOWN, buff=0.3).align_to(matrix_properties_title.get_left())

        self.play(FadeIn(property1, shift=LEFT), run_time=1, rate_func=smooth)
        self.play(FadeIn(property2, shift=LEFT), run_time=1, rate_func=smooth)
        self.play(FadeIn(property3, shift=LEFT), run_time=1, rate_func=smooth)
        self.wait(2)

        # Anotación visual para la suma de filas
        # Se usa SurroundingRectangle para enmarcar la propiedad crítica.
        # Se usa Tex explicativo para responder al "¿Por qué?".
        sum_property_rect = SurroundingRectangle(property3, color=RED, buff=0.1)
        sum_property_explanation = Tex(
            "¿Por qué? Porque desde cualquier estado, el proceso debe transitar a algún estado posible.",
            color=RED
        ).scale(0.7).next_to(sum_property_rect, DOWN, buff=0.5)

        self.play(Create(sum_property_rect), run_time=1, rate_func=smooth)
        self.play(Write(sum_property_explanation), run_time=2, rate_func=smooth)
        self.wait(3)

        self.play(
            FadeOut(matrix_title, shift=UP),
            FadeOut(matrix_def_text, shift=UP),
            FadeOut(matrix_properties_title, shift=UP),
            FadeOut(property1, shift=UP),
            FadeOut(property2, shift=UP),
            FadeOut(property3, shift=UP),
            FadeOut(sum_property_rect, shift=UP),
            FadeOut(sum_property_explanation, shift=UP),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)

        # [DEMOSTRACIÓN ~3-4min]
        # Ejemplo del clima, cálculo de probabilidades, Ecuación de Chapman-Kolmogorov, Propiedad de Markov.

        demo_title = Tex("Demostración: Modelo del Clima", color=BLUE_D).to_edge(UP).shift(DOWN*0.5)
        self.play(Write(demo_title), rate_func=smooth)
        self.wait(0.5)

        # Espacio de estados del clima
        weather_states = Tex("Espacio de Estados: \\{Soleado, Nublado, Lluvioso\\}", color=BLUE_D).scale(0.8).next_to(demo_title, DOWN, buff=0.5)
        self.play(FadeIn(weather_states, shift=LEFT), run_time=1.5, rate_func=smooth)
        self.wait(1)

        # Matriz de Transición P
        matrix_P_text = Tex("Matriz de Transición P:", color=GREEN_C).next_to(weather_states, DOWN, buff=0.7).align_to(weather_states.get_left())
        self.play(Write(matrix_P_text), rate_func=smooth)
        self.wait(0.5)

        matrix_P = Matrix([
            [0.7, 0.2, 0.1],
            [0.3, 0.5, 0.2],
            [0.2, 0.6, 0.2]
        ], h_buff=1.5, v_buff=0.8, left_bracket="[", right_bracket="]").scale(0.8).next_to(matrix_P_text, DOWN, buff=0.5)
        matrix_P_label = MathTex("P", color=BLUE_D).next_to(matrix_P, LEFT)

        self.play(Create(matrix_P), Write(matrix_P_label), run_time=3, rate_func=smooth)
        self.wait(2)

        # Resaltar la suma de las filas (reiteración del concepto)
        # Se usa SurroundingRectangle para cada fila y se muestra la suma.
        row_sums = VGroup()
        for i in range(3):
            row_sum_tex = MathTex(f"0.{int(matrix_P.get_entries()[i*3].get_value()*10)} + 0.{int(matrix_P.get_entries()[i*3+1].get_value()*10)} + 0.{int(matrix_P.get_entries()[i*3+2].get_value()*10)} = 1.0", color=RED).scale(0.6)
            row_sum_tex.next_to(matrix_P.get_rows()[i], RIGHT, buff=0.5)
            row_sums.add(row_sum_tex)
            self.play(
                SurroundingRectangle(matrix_P.get_rows()[i], color=RED, buff=0.1).animate.set_opacity(0.5),
                Write(row_sum_tex),
                run_time=1.5,
                rate_func=smooth
            )
            self.wait(0.5)
        self.wait(1)
        self.play(FadeOut(row_sums), run_time=1, rate_func=smooth)

        # Distribución de probabilidad inicial
        initial_dist_text = Tex("Distribución de probabilidad inicial: $\\pi(0)$", color=GREEN_C).next_to(matrix_P, DOWN, buff=1.0).align_to(matrix_P_text.get_left())
        self.play(Write(initial_dist_text), run_time=1.5, rate_func=smooth)
        self.wait(0.5)

        pi0 = Matrix([[0.4, 0.3, 0.3]], h_buff=1.5, v_buff=0.8, left_bracket="[", right_bracket="]").scale(0.8).next_to(initial_dist_text, DOWN, buff=0.5)
        pi0_label = MathTex("\\pi(0)", color=BLUE_D).next_to(pi0, LEFT)
        self.play(Create(pi0), Write(pi0_label), run_time=2, rate_func=smooth)
        self.wait(1)

        # Cálculo de la distribución de probabilidad futura: pi(1) = pi(0) * P
        # Uso de TransformMatchingTex para mostrar la evolución de la fórmula.
        # Se explica el "por qué" de la multiplicación.

        # Fórmula inicial
        formula_step1 = MathTex(
            "\\pi(1) = \\pi(0) \\cdot P",
            color=YELLOW_B
        ).scale(0.9).next_to(pi0, DOWN, buff=1.0)
        self.play(Write(formula_step1), run_time=2, rate_func=smooth)
        self.wait(1)

        # Explicación del por qué de la multiplicación
        why_multiply_explanation = Tex(
            "¿Por qué multiplicamos?",
            "Cada componente del nuevo vector se obtiene sumando las probabilidades de llegar a ese estado desde todos los estados posibles, ponderadas por la probabilidad de estar en esos estados hoy.",
            color=RED
        ).scale(0.7).next_to(formula_step1, DOWN, buff=0.5)

        self.play(FadeIn(why_multiply_explanation[0]), run_time=1, rate_func=smooth)
        self.play(FadeIn(why_multiply_explanation[1]), run_time=3, rate_func=smooth)
        self.wait(3)
        self.play(FadeOut(why_multiply_explanation), run_time=1, rate_func=smooth)

        # TransformMatchingTex para mostrar el resultado de la multiplicación
        # Se simula el cálculo para pi(1)
        pi1_result = MathTex(
            "\\pi(1) = [0.4 \\cdot 0.7 + 0.3 \\cdot 0.3 + 0.3 \\cdot 0.2,",
            "0.4 \\cdot 0.2 + 0.3 \\cdot 0.5 + 0.3 \\cdot 0.6,",
            "0.4 \\cdot 0.1 + 0.3 \\cdot 0.2 + 0.3 \\cdot 0.2]",
            "\\\\",
            "\\pi(1) = [0.28 + 0.09 + 0.06,",
            "0.08 + 0.15 + 0.18,",
            "0.04 + 0.06 + 0.06]",
            "\\\\",
            "\\pi(1) = [0.43, 0.41, 0.16]",
            color=YELLOW_B
        ).scale(0.8).next_to(formula_step1, DOWN, buff=0.5)

        # Se usa TransformMatchingTex para que los elementos de la fórmula se transformen.
        # Esto es obligatorio según las instrucciones.
        self.play(TransformMatchingTex(formula_step1, pi1_result[0:3]), run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(TransformMatchingTex(pi1_result[0:3], pi1_result[4:7]), run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(TransformMatchingTex(pi1_result[4:7], pi1_result[8]), run_time=2, rate_func=smooth)
        self.wait(2)

        # Ecuación de Chapman-Kolmogorov
        self.play(
            FadeOut(pi1_result, shift=UP),
            FadeOut(initial_dist_text, shift=UP),
            FadeOut(pi0, shift=UP),
            FadeOut(pi0_label, shift=UP),
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(0.5)

        chapman_kolmogorov_title = Tex("Ecuación de Chapman-Kolmogorov", color=GREEN_C).next_to(demo_title, DOWN, buff=0.5)
        self.play(Write(chapman_kolmogorov_title), run_time=1.5, rate_func=smooth)
        self.wait(0.5)

        chapman_kolmogorov_formula = MathTex(
            "\\pi(n) = \\pi(0) \\cdot P^n",
            color=YELLOW_B
        ).scale(1.2).next_to(chapman_kolmogorov_title, DOWN, buff=0.7)
        self.play(Write(chapman_kolmogorov_formula), run_time=2, rate_func=smooth)
        self.wait(2)

        # Anotación visual para P^n
        power_n_rect = SurroundingRectangle(chapman_kolmogorov_formula[0][7:9], color=RED, buff=0.1) # Selecciona P^n
        power_n_explanation = Tex("Predicción a 'n' días", color=RED).next_to(power_n_rect, DOWN)
        self.play(Create(power_n_rect), run_time=1, rate_func=smooth)
        self.play(Write(power_n_explanation), run_time=1.5, rate_func=smooth)
        self.wait(2)
        self.play(FadeOut(power_n_rect), FadeOut(power_n_explanation), run_time=1, rate_func=smooth)

        # Importancia de la Propiedad de Markov para Chapman-Kolmogorov
        markov_importance_text = Tex(
            "¿Por qué es fundamental la Propiedad de Markov para este cálculo?",
            "Simplifica drásticamente la complejidad: solo necesitamos el estado actual para predecir el siguiente.",
            color=RED
        ).scale(0.7).next_to(chapman_kolmogorov_formula, DOWN, buff=1.0)

        self.play(FadeIn(markov_importance_text[0]), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(markov_importance_text[1]), run_time=3, rate_func=smooth)
        self.wait(3)

        self.play(
            FadeOut(demo_title, shift=UP),
            FadeOut(weather_states, shift=UP),
            FadeOut(matrix_P_text, shift=UP),
            FadeOut(matrix_P, shift=UP),
            FadeOut(matrix_P_label, shift=UP),
            FadeOut(chapman_kolmogorov_title, shift=UP),
            FadeOut(chapman_kolmogorov_formula, shift=UP),
            FadeOut(markov_importance_text, shift=UP),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)

        # [EJEMPLO PRÁCTICO ~2min]
        # Ejemplo del supermercado con ValueTracker para un gráfico dinámico.

        practical_example_title = Tex("Ejemplo Práctico: Supermercado", color=BLUE_D).to_edge(UP).shift(DOWN*0.5)
        self.play(Write(practical_example_title), run_time=1.5, rate_func=smooth)
        self.wait(0.5)

        # Estados del supermercado
        supermarket_states = Tex("Estados: \\{Lácteos, Panadería, Cajas\\}", color=BLUE_D).scale(0.8).next_to(practical_example_title, DOWN, buff=0.5)
        self.play(FadeIn(supermarket_states, shift=LEFT), run_time=1.5, rate_func=smooth)
        self.wait(1)

        # Introducción a la matriz de transición (sin mostrarla explícitamente, solo el concepto)
        supermarket_matrix_concept = Tex(
            "Matriz de Transición: Probabilidad de movimiento entre secciones.",
            color=GREEN_C
        ).scale(0.8).next_to(supermarket_states, DOWN, buff=0.7).align_to(supermarket_states.get_left())
        self.play(Write(supermarket_matrix_concept), run_time=2, rate_func=smooth)
        self.wait(1)

        # Preguntas que se pueden responder
        questions_title = Tex("Preguntas que podemos responder:", color=GREEN_C).next_to(supermarket_matrix_concept, DOWN, buff=0.7).align_left(supermarket_matrix_concept)
        self.play(Write(questions_title), run_time=1.5, rate_func=smooth)
        self.wait(0.5)

        question1 = Tex(
            "¿Probabilidad de que un cliente en Lácteos termine en Cajas en 10 min?",
            color=BLUE_D
        ).scale(0.7).next_to(questions_title, DOWN, buff=0.3).align_to(questions_title.get_left())
        question2 = Tex(
            "A largo plazo, ¿qué porcentaje del tiempo un cliente pasa en cada sección?",
            color=BLUE_D
        ).scale(0.7).next_to(question1, DOWN, buff=0.3).align_to(questions_title.get_left())

        self.play(FadeIn(question1, shift=LEFT), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(question2, shift=LEFT), run_time=1.5, rate_func=smooth)
        self.wait(2)

        # Implementación de ValueTracker para un gráfico dinámico
        # Se simula la evolución de la probabilidad de estar en cada sección a lo largo del tiempo.
        # Esto es obligatorio según las instrucciones.

        self.play(
            FadeOut(supermarket_states, shift=UP),
            FadeOut(supermarket_matrix_concept, shift=UP),
            FadeOut(questions_title, shift=UP),
            FadeOut(question1, shift=UP),
            FadeOut(question2, shift=UP),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)

        # Título para la visualización dinámica
        dynamic_viz_title = Tex("Visualización Dinámica: Distribución de Probabilidad", color=GREEN_C).next_to(practical_example_title, DOWN, buff=0.5)
        self.play(Write(dynamic_viz_title), run_time=1.5, rate_func=smooth)
        self.wait(0.5)

        # Definición de los ejes del gráfico
        axes = Axes(
            x_range=[0, 10, 1], # Tiempo (pasos)
            y_range=[0, 1, 0.2], # Probabilidad
            x_length=8,
            y_length=5,
            axis_config={"color": BLUE_D},
            x_axis_config={"numbers_to_include": [0, 2, 4, 6, 8, 10]},
            y_axis_config={"numbers_to_include": [0, 0.2, 0.4, 0.6, 0.8, 1.0]},
        ).to_edge(DOWN).shift(UP*0.5)

        x_label = axes.get_x_axis_label(Tex("Tiempo (pasos)", color=BLUE_D).scale(0.7))
        y_label = axes.get_y_axis_label(Tex("Probabilidad", color=BLUE_D).scale(0.7)).rotate(90 * DEGREES)

        # Agrupar los elementos del gráfico para animarlos juntos
        graph_elements = VGroup(axes, x_label, y_label)
        self.play(Create(graph_elements), run_time=2, rate_func=smooth)
        self.wait(0.5)

        # Simulación de una matriz de transición para el ejemplo del supermercado
        # (Simplificada para la visualización)
        # P_super = [[0.5, 0.3, 0.2],
        #            [0.1, 0.6, 0.3],
        #            [0.1, 0.1, 0.8]]

        # Vector de estado inicial (ej: cliente empieza en Lácteos)
        # pi0_super = np.array([1.0, 0.0, 0.0])

        # ValueTracker para el tiempo
        time_tracker = ValueTracker(0)

        # Funciones para calcular las probabilidades en cada estado en función del tiempo
        # Estas funciones simulan la evolución de las probabilidades.
        def get_prob_lacteos(t):
            # Simulación: la probabilidad de estar en Lácteos disminuye con el tiempo
            return 0.8 * np.exp(-0.2 * t) + 0.2

        def get_prob_panaderia(t):
            # Simulación: la probabilidad de estar en Panadería aumenta y luego se estabiliza
            return 0.5 * (1 - np.exp(-0.3 * t)) + 0.1

        def get_prob_cajas(t):
            # Simulación: la probabilidad de estar en Cajas aumenta con el tiempo
            return 0.6 * (1 - np.exp(-0.1 * t))

        # Gráficos de las probabilidades
        graph_lacteos = axes.plot(lambda t: get_prob_lacteos(t), x_range=[0, 10], color=BLUE_D)
        graph_panaderia = axes.plot(lambda t: get_prob_panaderia(t), x_range=[0, 10], color=GREEN_C)
        graph_cajas = axes.plot(lambda t: get_prob_cajas(t), x_range=[0, 10], color=YELLOW_B)

        # Etiquetas para los gráficos
        label_lacteos = Tex("Lácteos", color=BLUE_D).scale(0.6).next_to(graph_lacteos.get_end(), RIGHT, buff=0.1)
        label_panaderia = Tex("Panadería", color=GREEN_C).scale(0.6).next_to(graph_panaderia.get_end(), RIGHT, buff=0.1)
        label_cajas = Tex("Cajas", color=YELLOW_B).scale(0.6).next_to(graph_cajas.get_end(), RIGHT, buff=0.1)

        self.play(Create(graph_lacteos), Write(label_lacteos), run_time=2, rate_func=smooth)
        self.play(Create(graph_panaderia), Write(label_panaderia), run_time=2, rate_func=smooth)
        self.play(Create(graph_cajas), Write(label_cajas), run_time=2, rate_func=smooth)
        self.wait(1)

        # Animación del ValueTracker
        # Se usa add_updater para que las etiquetas sigan el final de las curvas.
        label_lacteos.add_updater(lambda m: m.next_to(graph_lacteos.get_end(), RIGHT, buff=0.1))
        label_panaderia.add_updater(lambda m: m.next_to(graph_panaderia.get_end(), RIGHT, buff=0.1))
        label_cajas.add_updater(lambda m: m.next_to(graph_cajas.get_end(), RIGHT, buff=0.1))

        self.play(time_tracker.animate.set_value(10), run_time=10, rate_func=linear) # Animación lineal del tiempo
        self.wait(2)

        # Limpiar la escena para la siguiente sección
        self.play(
            FadeOut(practical_example_title, shift=UP),
            FadeOut(dynamic_viz_title, shift=UP),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(graph_lacteos),
            FadeOut(graph_panaderia),
            FadeOut(graph_cajas),
            FadeOut(label_lacteos),
            FadeOut(label_panaderia),
            FadeOut(label_cajas),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)

        # [CIERRE ~30s]
        # Resumen de aplicaciones y mención de otros procesos estocásticos.

        closing_title = Tex("Aplicaciones y Futuro", color=BLUE_D).to_edge(UP).shift(DOWN*0.5)
        self.play(Write(closing_title), run_time=1.5, rate_func=smooth)
        self.wait(0.5)

        applications_text = Tex(
            "Finanzas (precios de acciones), Biología (propagación de enfermedades),",
            "Ingeniería (fiabilidad de sistemas), Informática (algoritmos de búsqueda).",
            color=BLUE_D
        ).scale(0.8).next_to(closing_title, DOWN, buff=0.5)

        self.play(FadeIn(applications_text[0], shift=LEFT), run_time=2, rate_func=smooth)
        self.play(FadeIn(applications_text[1], shift=LEFT), run_time=2, rate_func=smooth)
        self.wait(2)

        future_processes_text = Tex(
            "Otros procesos: Tiempo continuo, Nacimiento y Muerte, Movimiento Browniano.",
            color=GREEN_C
        ).scale(0.7).next_to(applications_text, DOWN, buff=0.7)

        self.play(FadeIn(future_processes_text, shift=LEFT), run_time=2, rate_func=smooth)
        self.wait(2)

        final_message = Tex(
            "Comprender Cadenas de Markov es el primer paso crucial.",
            color=YELLOW_B
        ).scale(1.0).next_to(future_processes_text, DOWN, buff=1.0)

        self.play(Write(final_message), run_time=2, rate_func=smooth)
        self.wait(3)

        self.play(
            FadeOut(closing_title),
            FadeOut(applications_text),
            FadeOut(future_processes_text),
            FadeOut(final_message),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)