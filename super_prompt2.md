Crea un vídeo interactivo sobre [NOMBRE DE LA UNIDAD] usando Manim Community. Sigue este proceso:

1. **INVESTIGACIÓN PREVIA** (usar herramientas):
   # Buscar en codebase_search
   ejemplos = codebase_search("animación de [CONCEPTO CLAVE] en videos de ejemplo")
   
   # Consultar Context-7
   docs = Context-7("/manimcommunity/manim [TÉCNICA ESPECÍFICA]")

   # Busqueda de información estadística
   hay muchos archivos que puedes leer sobre la unidad correspondiente

2. **SCRIPT DE NARRACIÓN** (`[unidad]_script.txt`):
   - Español natural continuo (sin marcas temporales)
   - Estilo: profesor universitario experto

3. **CÓDIGO MANIM** (`[unidad].py`):

           # VERIFICACIÓN POST-ESCENA
           # Simular comando: manim -ql -s [unidad].py
           # Ajustar posiciones si hay solapamientos


4. **TÉCNICAS AVANZADAS OBLIGATORIAS** (por escena):
   - 1 técnica de animación compleja (ej: TransformMatchingTex)
   - 1 elemento interactivo (ValueTracker/graficos dinámicos)
   - Uso profesional de colores (paleta: BLUE_D, GREEN_C, YELLOW_B)
   - Transiciones fluidas con rate_func=smooth

5. **VERIFICACIÓN FINAL**:
   ```bash
   manim -ql -s /ruta/[unidad].py  # Debe compilar sin errores
   ```

6. **EJEMPLOS CONCRETOS** (inspiración):
   ```python
   # Animación de distribuciones (codebase_search)
   class DistribucionNormal(Scene):
       def construct(self):
           axes = Axes()
           graph = axes.plot(lambda x: np.exp(-x**2), color=BLUE)
           self.play(Create(axes), Create(graph))
           
   # Uso de ValueTracker (Context-7)
   class GraficoDinamico(Scene):
       def construct(self):
           x_tracker = ValueTracker(0)
           graph = always_redraw(lambda: 
                axes.plot(lambda x: x*x_tracker.get_value())
           )
   ```

7. **PRECAUCIONES**:
   - Evitar plantillas predefinidas: cada escena debe ser única
   - Priorizar claridad sobre complejidad innecesaria
   - Usar .scale(0.8) en móviles complejos
   - Comprobar renderización móvil (manim -ql -s [unidad].py)

Entrega: Archivo .py compilable + script.txt listo para TTS

Crea un vídeo interactivo sobre [NOMBRE DE LA UNIDAD] usando Manim Community. Sigue este proceso:

1. **INVESTIGACIÓN PROFUNDA** (usar herramientas):
   ```python
   # Buscar detalles críticos
   detalles = codebase_search("detalles específicos profesor en [CONCEPTO CLAVE]")
   
   # Consultar Context-7 para técnicas avanzadas
   docs = Context-7("/manimcommunity/manim [MÉTODO_AVANZADO]")
   ```

2. **SCRIPT CON EXPLICACIONES DE DETALLE** (`[unidad]_script.txt`):
   - Estructura:
     ```txt
     [INTRO 15s] Contexto y motivación
     [TEORÍA 2-3min] Explicación conceptual + "¿Por qué?": 
        "Observen este signo negativo... surge porque..."
        "Dividimos por n-1 en lugar de n debido a..."
     [DEMOSTRACIÓN 3-4min] Paso a paso con justificaciones:
        "Paso 1: Aplicamos X propiedad... ¿Por qué es válido? Porque..."
        "Paso 2: Aquí aparece un cuadrado... ¿Qué representa?"
     [EJEMPLO 2min] Caso práctico con énfasis en detalles críticos
     [CIERRE 30s] Resumen de implicaciones prácticas
     ```
   - Lenguaje: Profesor universitario riguroso
   - Incluir mínimo 3 "¿Por qué?" por demostración

3. **CÓDIGO MANIM CON ANOTACIONES DE DETALLE** (`[unidad].py`):
   ```python
   from manim import *
   
   class VideoUnidad(Scene):
       def construct(self):
           # ESCENA 1: INTRODUCCIÓN CON DETALLE
           titulo = Tex(r"\text{[TÍTULO]}", font_size=48)
           detalle_intro = Tex(r"\text{¡Ojo! Esta unidad es fundamental porque...}", color=YELLOW).next_to(titulo, DOWN)
           self.play(Write(VGroup(titulo, detalle_intro)))
           self.wait(1)
           
           # ESCENA 2: DEMOSTRACIÓN PASO A PASO
           # Uso OBLIGATORIO de TransformMatchingTex con desglose
           paso1 = MathTex(r"\text{Paso 1: }", r"\sum (X_i - \mu)^2", r"= \cdots")
           explicacion1 = Tex(r"¿Por qué al cuadrado?\\ Para eliminar signos negativos\\ y enfatizar desviaciones", font_size=24).next_to(paso1, DOWN)
           
           self.play(TransformMatchingTex(paso1, paso2), 
                    FadeIn(explicacion1))
           self.wait(2)
           
           # Indicador de detalle crítico
           rect_detalle = SurroundingRectangle(paso2[1], color=RED, buff=0.1)
           flecha = Arrow(explicacion1.get_top(), rect_detalle.get_bottom(), color=BLUE)
           self.play(Create(rect_detalle), Create(flecha))
           self.wait(1.5)
           
           # ESCENA 3: EJEMPLO CON VALIDACIÓN
           # Uso de ValueTracker para mostrar efectos
           valor = ValueTracker(1)
           grafico = always_redraw(lambda: 
                self.get_grafico_dinamico(valor.get_value())
           )
           self.add(grafico)
           self.play(valor.animate.set_value(3), run_time=3)
           
           # Anotación interactiva
           pregunta = Tex(r"¿Por qué cambia la forma así?", color=RED).next_to(grafico, UP)
           self.play(Write(pregunta))
           self.wait(2)

   def get_grafico_dinamico(self, param):
       # Implementar gráfico sensible a parámetros
       return VGroup(...)
   ```

4. **TÉCNICAS ESPECÍFICAS PARA DETALLES**:
   - **Sistemass de anotación**:
     ```python
     # Sistema 1: Cajas y flechas explicativas
     caja_detalle = SurroundingRectangle(objeto_math, color=YELLOW, buff=0.1)
     texto_explicacion = Tex(r"\text{¡Detalle clave!}", color=YELLOW).next_to(caja_detalle, DOWN)
     ```
     
     ```python
     # Sistema 2: Destacado secuencial
     self.play(objeto_math.animate.set_color(RED))
     self.wait(0.5)
     self.play(Write(Tex(r"\text{Signo negativo aparece por...}").next_to(objeto_math, RIGHT)))
     ```
   
   - **Animaciones de deconstrucción**:
     ```python
     # Deconstruir fórmula (requiere Context-7)
     terminos = [MathTex(part) for part in ["-", r"\frac{1}{2}", "x^2"]]
     self.play(TransformMatchingShapes(formula_completa, VGroup(*terminos).arrange(RIGHT)))
     ```

5. **VERIFICACIÓN MEJORADA**:
   ```bash
   manim -ql -s /ruta/[unidad].py
   ```
   - Checklist adicional:
     [ ] Todos los "¿Por qué?" tienen animación asociada
     [ ] Detalles críticos destacados con 2+ métodos visuales
     [ ] Timing permite 3s mínimo por explicación compleja
     [ ] Coherencia entre script y animaciones (1:1)

6. **EJEMPLOS CONCRETOS POR UNIDAD**:
   **Unidad 4 (Pruebas no paramétricas)**:
   ```python
   class DetalleWilcoxon(Scene):
       def construct(self):
           # Explicación corrección por empates
           formula = MathTex(r"T = \frac{T - \mu_T}{\sigma_T}", 
                             r"\quad \sigma^2_T = \cdots - \frac{\sum t_j^3 - t_j}{48}")
           
           # Anotación para detalle de corrección
            rect_correccion = SurroundingRectangle(formula[1][20:], color=RED)
            texto = Tex(r"¡Corrección por empates!\\ $t_j$: tamaño del empate $j$", color=BLUE).next_to(rect_correccion, DOWN)
            
            self.play(Write(formula))
            self.play(Create(rect_correccion), Write(texto))
            self.wait(3)
   ```

   **Unidad 5 (Regresión)**:
   ```python
   class DetalleMinimosCuadrados(Scene):
       def construct(self):
           # Demostración división por n-2
           formula = MathTex(r"s^2 = \frac{1}{n-2}\sum (y_i - \hat{y}_i)^2")
           flecha = Arrow(ORIGIN, DOWN*0.8, color=YELLOW).next_to(formula[0][7], DOWN)
           explicacion = Tex(r"Grados de libertad:\\ n-2 = observaciones - parámetros", color=YELLOW).next_to(flecha, DOWN)
           
           self.play(Write(formula))
           self.play(GrowArrow(flecha), FadeIn(explicacion))
   ```