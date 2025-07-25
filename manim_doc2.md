TITLE: Instantiate Manim Circle Object
DESCRIPTION: Creates an instance of the `Circle` class, which represents a circular mathematical object (mobject) in Manim. This object can then be manipulated and animated within the scene.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_7

LANGUAGE: python
CODE:
```
circle = Circle()
```

----------------------------------------

TITLE: Set Manim Mobject Fill and Stroke Styles
DESCRIPTION: Applies visual styling to a Manim mobject. `set_fill()` sets the interior color and transparency, while `set_stroke()` defines the border color and width. These methods customize the appearance of the mobject.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_8

LANGUAGE: python
CODE:
```
circle.set_fill(BLUE, opacity=0.5)
circle.set_stroke(BLUE_E, width=4)
```

----------------------------------------

TITLE: Add Mobject to Manim Scene
DESCRIPTION: Adds a created mobject (e.g., `circle`) to the Manim scene using `self.add()`. Mobjects must be added to the scene to be rendered or animated.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_9

LANGUAGE: python
CODE:
```
self.add(circle)
```

----------------------------------------

TITLE: Render Manim Scene to Image File
DESCRIPTION: Executes the `SquareToCircle` scene from `start.py` to render and save a static image file. The `-os` flag ensures no interactive window pops up, and the output is saved in the `images/` subdirectory.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_3

LANGUAGE: sh
CODE:
```
manimgl start.py SquareToCircle -os
```

----------------------------------------

TITLE: Pause Manim Scene Animation
DESCRIPTION: Demonstrates how to pause the Manim animation using the `Scene`'s `.wait()` method. By default, it pauses for 1 second, but a custom duration can be specified as an argument.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_14

LANGUAGE: python
CODE:
```
self.wait()
```

----------------------------------------

TITLE: Define Manim Scene with Square to Circle Animation
DESCRIPTION: Extends the basic Manim scene to include a sequence of animations. It creates a square, shows its creation, pauses, then transforms it into a circle, demonstrating basic animation sequencing with `self.play()` and `self.wait()`.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_10

LANGUAGE: python
CODE:
```
from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
```

----------------------------------------

TITLE: Define Scene Construct Method
DESCRIPTION: Defines the `construct()` method within a Manim scene class. This method is automatically called by Manim to build the scene's mobjects and define the sequence of animations.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_6

LANGUAGE: python
CODE:
```
def construct(self):
```

----------------------------------------

TITLE: Manim Project Directory Structure Example
DESCRIPTION: Illustrates the recommended directory structure for a Manim project, highlighting the placement of custom scene files like 'start.py' alongside Manim's core libraries and configuration.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_0

LANGUAGE: text
CODE:
```
manim/
├── manimlib/
│   ├── animation/
│   ├── ...
│   ├── default_config.yml
│   └── window.py
├── custom_config.yml
└── start.py
```

----------------------------------------

TITLE: Enable Manim Interactive IPython Session
DESCRIPTION: Shows how to enable Manim's interactive mode by adding `self.embed()` at the end of a scene. This opens an IPython terminal after the animation, allowing real-time code execution to manipulate the scene.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_16

LANGUAGE: python
CODE:
```
self.embed()
```

----------------------------------------

TITLE: Play Manim Animation
DESCRIPTION: Initiates an animation within a Manim scene using `self.play()`. This example demonstrates `ShowCreation(square)`, which animates the process of drawing a square onto the screen.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_13

LANGUAGE: python
CODE:
```
self.play(ShowCreation(square))
```

----------------------------------------

TITLE: Define Basic Manim Scene with Circle
DESCRIPTION: Defines a simple Manim scene named `SquareToCircle` by subclassing `Scene`. This scene constructs a blue circle with a dark blue stroke and adds it to the display, serving as a foundational example for Manim rendering.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_1

LANGUAGE: python
CODE:
```
from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        self.add(circle)
```

----------------------------------------

TITLE: Run Manim Scene with Animation in Interactive Window
DESCRIPTION: Executes the `SquareToCircle` scene from `start.py`, which now contains animations. The `manimgl` command displays the animated output in an interactive preview window.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_11

LANGUAGE: sh
CODE:
```
manimgl start.py SquareToCircle
```

----------------------------------------

TITLE: Manim Interactive Mode Example Commands
DESCRIPTION: Provides examples of Python commands that can be executed within the Manim interactive IPython session. These commands demonstrate real-time manipulation of scene objects, including stretching, rotating, scaling, applying complex functions, and exiting the session.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_17

LANGUAGE: python
CODE:
```
play(circle.animate.stretch(4, dim=0))
play(Rotate(circle, TAU / 4))
play(circle.animate.shift(2 * RIGHT), circle.animate.scale(0.25))
circle.insert_n_curves(10)
play(circle.animate.apply_complex_function(lambda z: z**2))
exit()
```

----------------------------------------

TITLE: Define Manim Scene Class
DESCRIPTION: Defines a custom scene class, `SquareToCircle`, which inherits from `Scene`. All Manim animations and static renders are created within methods of a `Scene` subclass.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_5

LANGUAGE: python
CODE:
```
class SquareToCircle(Scene):
```

----------------------------------------

TITLE: Launch Manim Interactive Mode Directly
DESCRIPTION: Explains how to directly launch the Manim interactive IPython terminal and display window without needing a scene file. This is achieved by running the `manimgl` command in the shell.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_18

LANGUAGE: sh
CODE:
```
manimgl
```

----------------------------------------

TITLE: Transform Manim Object with ReplacementTransform
DESCRIPTION: Illustrates playing an animation that transforms one Manim object (`square`) into another (`circle`). `ReplacementTransform(A, B)` animates A changing into B's appearance and then replaces A with B.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_15

LANGUAGE: python
CODE:
```
self.play(ReplacementTransform(square, circle))
```

----------------------------------------

TITLE: Render Manim Scene to Video File
DESCRIPTION: Executes the `SquareToCircle` scene from `start.py` to render and save a video file of the animation. The `-o` flag ensures no interactive window pops up, and the output video is saved in the `videos/` subdirectory.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/quickstart.rst#_snippet_12

LANGUAGE: sh
CODE:
```
manimgl start.py SquareToCircle -o
```

----------------------------------------

TITLE: Manim: Animating Mobject Methods
DESCRIPTION: This Manim scene illustrates various techniques for animating mobject methods. It showcases the `.animate` syntax for smooth transitions, the older method-passing syntax, and advanced transformations using `apply_complex_function` and `apply_function`. It also demonstrates how to apply color gradients, resize mobjects dynamically, and use the `.get_grid()` method to arrange mobjects.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_1

LANGUAGE: python
CODE:
```
class AnimatingMethods(Scene):
    def construct(self):
        grid = OldTex(r"\pi").get_grid(10, 10, height=4)
        self.add(grid)

        # You can animate the application of mobject methods with the
        # ".animate" syntax:
        self.play(grid.animate.shift(LEFT))

        # Alternatively, you can use the older syntax by passing the
        # method and then the arguments to the scene's "play" function:
        self.play(grid.shift, LEFT)

        # Both of those will interpolate between the mobject's initial
        # state and whatever happens when you apply that method.
        # For this example, calling grid.shift(LEFT) would shift the
        # grid one unit to the left, but both of the previous calls to
        # "self.play" animate that motion.

        # The same applies for any method, including those setting colors.
        self.play(grid.animate.set_color(YELLOW))
        self.wait()
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()

        # The method Mobject.apply_complex_function lets you apply arbitrary
        # complex functions, treating the points defining the mobject as
        # complex numbers.
        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.wait()

        # Even more generally, you could apply Mobject.apply_function,
        # which takes in functions form R^3 to R^3
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * math.sin(p[1]),
                    p[1] + 0.5 * math.sin(p[0]),
                    p[2]
                ]
            ),
            run_time=5,
        )
        self.wait()
```

----------------------------------------

TITLE: Manim 3D Textured Surface and Camera Animation
DESCRIPTION: This Manim scene segment demonstrates the creation and animation of 3D textured surfaces (sphere, tori), manipulation of camera perspective, and dynamic control of a light source. It showcases surface transformations, mesh rendering, and interactive elements like light source movement.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_15

LANGUAGE: python
CODE:
```
            day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg"
            night_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night.jpg"

            surfaces = [
                TexturedSurface(surface, day_texture, night_texture)
                for surface in [sphere, torus1, torus2]
            ]

            for mob in surfaces:
                mob.shift(IN)
                mob.mesh = SurfaceMesh(mob)
                mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

            # Set perspective
            frame = self.camera.frame
            frame.set_euler_angles(
                theta=-30 * DEG,
                phi=70 * DEG,
            )

            surface = surfaces[0]

            self.play(
                FadeIn(surface),
                ShowCreation(surface.mesh, lag_ratio=0.01, run_time=3)
            )
            for mob in surfaces:
                mob.add(mob.mesh)
            surface.save_state()
            self.play(Rotate(surface, PI / 2), run_time=2)
            for mob in surfaces[1:]:
                mob.rotate(PI / 2)

            self.play(
                Transform(surface, surfaces[1]),
                run_time=3
            )

            self.play(
                Transform(surface, surfaces[2]),
                # Move camera frame during the transition
                frame.animate.increment_phi(-10 * DEG),
                frame.animate.increment_theta(-20 * DEG),
                run_time=3
            )
            # Add ambient rotation
            frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

            # Play around with where the light is
            light_text = Text("You can move around the light source")
            light_text.move_to(surface_text)
            light_text.fix_in_frame()

            self.play(FadeTransform(surface_text, light_text))
            light = self.camera.light_source
            self.add(light)
            light.save_state()
            self.play(light.animate.move_to(3 * IN), run_time=5)
            self.play(light.animate.shift(10 * OUT), run_time=5)

            drag_text = Text("Try moving the mouse while pressing d or s")
            drag_text.move_to(light_text)
            drag_text.fix_in_frame()

            self.play(FadeTransform(light_text, drag_text))
            self.wait()
```

----------------------------------------

TITLE: Manim: Creating and Texturing 3D Surfaces
DESCRIPTION: This example demonstrates how to create 3D scenes in Manim by setting the `camera_class` to `ThreeDCamera` and defining 3D objects like `Torus` and `Sphere`. It also introduces the concept of texturing surfaces with up to two images (for light and dark sides), though the texture paths are commented out.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_14

LANGUAGE: Python
CODE:
```
class SurfaceExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.fix_in_frame()
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

        torus1 = Torus(r1=1, r2=1)
        torus2 = Torus(r1=3, r2=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)
        # You can texture a surface with up to two images, which will
        # be interpreted as the side towards the light, and away from
        # the light.  These can be either urls, or paths to a local file
        # in whatever you've set as the image directory in
        # the custom_config.yml file

        # day_texture = "EarthTextureMap"
        # night_texture = "NightEarthTextureMap"
```

----------------------------------------

TITLE: Manim Mobject.fix_in_frame() Method
DESCRIPTION: Documentation for the `.fix_in_frame()` method available on Manim Mobjects. This method ensures that the object remains fixed relative to the screen's view angle, always displaying at a consistent position regardless of camera movement.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_17

LANGUAGE: APIDOC
CODE:
```
Mobject.fix_in_frame()
  Description: Makes the object not change with the view angle of the screen, and is always displayed at a fixed position on the screen.
```

----------------------------------------

TITLE: Transforming Text with TransformMatchingTex in Manim
DESCRIPTION: Demonstrates `TransformMatchingTex` for animating text transformations, showing how to handle mismatches and use `key_map` for specific character transformations. It illustrates transforming parts of a TeX string while preserving others, and how `transform_mismatches` can animate non-matching elements.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_5

LANGUAGE: Python
CODE:
```
self.play(
    TransformMatchingTex(lines[1].copy(), lines[2]),
    **play_kw
)
self.wait()
self.play(FadeOut(lines[2]))
self.play(
    TransformMatchingTex(
        lines[1].copy(), lines[2],
        key_map={
            "C^2": "C",
            "B^2": "B",
        }
    ),
    **play_kw
)
self.wait()

new_line2 = OldTex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
new_line2.replace(lines[2])
new_line2.match_style(lines[2])

self.play(
    TransformMatchingTex(
        new_line2, lines[3],
        transform_mismatches=True,
    ),
    **play_kw
)
self.wait(3)
self.play(FadeOut(lines, RIGHT))
```

----------------------------------------

TITLE: Manim Core Classes: Text, VGroup, Write, FadeIn, FadeOut
DESCRIPTION: Documentation for fundamental Manim classes and animations used for text rendering, object grouping, and scene transitions.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_3

LANGUAGE: APIDOC
CODE:
```
Text:
  - Purpose: Creates text, defines fonts, etc.
  - Usage: Clearly reflected in the provided examples.
VGroup:
  - Purpose: Groups multiple `VMobject` instances together as a whole.
  - Usage: The `.arrange()` method can be called to arrange sub-mobjects in sequence (e.g., `DOWN`), with specified spacing (`buff`).
Write:
  - Purpose: An animation that shows similar writing effects.
FadeIn:
  - Purpose: Fades an object into the scene.
  - Parameters: The second parameter indicates the direction of the fade in.
FadeOut:
  - Purpose: Fades an object out of the scene.
  - Parameters: The second parameter indicates the direction of the fade out.
```

----------------------------------------

TITLE: Manim Scene Animation Timing and Pause
DESCRIPTION: This snippet illustrates how to control the duration of an animation using `run_time` and how to introduce a pause in the scene's execution using `self.wait()`. These are common patterns for orchestrating visual sequences in Manim.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_18

LANGUAGE: Python
CODE:
```
                run_time=6,
            )
            self.wait(2)
```

----------------------------------------

TITLE: Manim: Interactive Scene Development
DESCRIPTION: This Manim scene demonstrates interactive development using an embedded iPython terminal. It shows how to manipulate mobjects like `Circle` and `Square` dynamically, allowing real-time experimentation with transformations, rotations, and shifts. The `self.embed()` method facilitates interactive debugging and scene construction, enabling users to type commands directly into the shell to modify the scene.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_0

LANGUAGE: python
CODE:
```
from manimlib import *

class InteractiveDevelopment(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()

        # This opens an iPython terminal where you can keep writing
        # lines as if they were part of this construct method.
        # In particular, 'square', 'circle' and 'self' will all be
        # part of the local namespace in that terminal.
        self.embed()

        # Try copying and pasting some of the lines below into
        # the interactive shell
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.stretch(4, 0))
        self.play(Rotate(circle, 90 * DEG))
        self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        text = Text("""
            In general, using the interactive shell
            is very helpful when developing new scenes
        """)
        self.play(Write(text))

        # In the interactive shell, you can just type
        # play, add, remove, clear, wait, save_state and restore,
        # instead of self.play, self.add, self.remove, etc.

        # To interact with the window, type touch().  You can then
        # scroll in the window, or zoom by holding down 'z' while scrolling,
        # and change camera perspective by holding down 'd' while moving
        # the mouse.  Press 'r' to reset to the standard camera position.
        # Press 'q' to stop interacting with the window and go back to
        # typing new commands into the shell.

        # In principle you can customize a scene to be responsive to
        # mouse and keyboard interactions
        always(circle.move_to, self.mouse_point)
```

----------------------------------------

TITLE: Manim Text Object Creation and Animation
DESCRIPTION: Demonstrates how to create and manipulate `Text` objects in Manim, including setting fonts, sizes, colors, and applying various text styles. It also shows how to arrange multiple objects using `VGroup` and animate them with `Write`, `FadeIn`, and `FadeOut`.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_2

LANGUAGE: python
CODE:
```
class TextExample(Scene):
    def construct(self):
        # To run this scene properly, you should have "Consolas" font in your computer
        # for full usage, you can see https://github.com/3b1b/manim/pull/680
        text = Text("Here is a text", font="Consolas", font_size=90)
        difference = Text(
            """
            The most important difference between Text and TexText is that\n
            you can change the font more easily, but can't use the LaTeX grammar
            """,
            font="Arial", font_size=24,
            # t2c is a dict that you can choose color for different text
            t2c={"Text": BLUE, "TexText": BLUE, "LaTeX": ORANGE}
        )
        VGroup(text, difference).arrange(DOWN, buff=1)
        self.play(Write(text))
        self.play(FadeIn(difference, UP))
        self.wait(3)

        fonts = Text(
            "And you can also set the font according to different words",
            font="Arial",
            t2f={"font": "Consolas", "words": "Consolas"},
            t2c={"font": BLUE, "words": GREEN}
        )
        fonts.set_width(FRAME_WIDTH - 1)
        slant = Text(
            "And the same as slant and weight",
            font="Consolas",
            t2s={"slant": ITALIC},
            t2w={"weight": BOLD},
            t2c={"slant": ORANGE, "weight": RED}
        )
        VGroup(fonts, slant).arrange(DOWN, buff=0.8)
        self.play(FadeOut(text), FadeOut(difference, shift=DOWN))
        self.play(Write(fonts))
        self.wait()
        self.play(Write(slant))
        self.wait()
```

----------------------------------------

TITLE: Manim Object Animation and Dynamic Updaters
DESCRIPTION: This snippet demonstrates how to animate Manim mobjects (like a square) using `self.play` with `.animate` for scaling and resizing. It also illustrates the use of `add_updater` to continuously modify a mobject's property (e.g., width) based on a lambda function, allowing for dynamic, frame-by-frame updates.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_9

LANGUAGE: Python
CODE:
```
self.add(square, brace, label)

# Notice that the brace and label track with the square
self.play(
    square.animate.scale(2),
    rate_func=there_and_back,
    run_time=2,
)
self.wait()
self.play(
    square.animate.set_width(5, stretch=True),
    run_time=3,
)
self.wait()
self.play(
    square.animate.set_width(2),
    run_time=3
)
self.wait()

# In general, you can alway call Mobject.add_updater, and pass in
# a function that you want to be called on every frame.  The function
# should take in either one argument, the mobject, or two arguments,
# the mobject and the amount of time since the last frame.
now = self.time
w0 = square.get_width()
square.add_updater(
    lambda m: m.set_width(w0 * math.cos(self.time - now))
)
self.wait(4 * PI)
```

----------------------------------------

TITLE: Manim Class Definitions and Purpose
DESCRIPTION: Provides concise definitions for core Manim classes related to text rendering and object transformations.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_7

LANGUAGE: APIDOC
CODE:
```
Tex:
  description: Uses LaTeX to create mathematical formulas.
TexText:
  description: Uses LaTeX to create text.
TransformMatchingTeX:
  description: Automatically transforms sub-objects according to the similarities and differences of tex in Tex.
TransformMatchingShapes:
  description: Automatically transform sub-objects directly based on the similarities and differences of the object point sets.
```

----------------------------------------

TITLE: Manim: Comprehensive Graph Plotting and Animation
DESCRIPTION: This extensive example showcases how to initialize `Axes`, plot various mathematical functions (sine, ReLU, step) with custom properties like `use_smoothing` and `discontinuities`, and add labels using both LaTeX and `Text` mobjects. It further demonstrates animating transitions between different graphs and using `ValueTracker` with `axes.i2gp` to animate a `Dot` moving along a parabola.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_13

LANGUAGE: Python
CODE:
```
class GraphExample(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        relu_graph = axes.get_graph(
            lambda x: max(x, 0),
            use_smoothing=False,
            color=YELLOW,
        )
        # For discontinuous functions, you can specify the point of
        # discontinuity so that it does not try to draw over the gap.
        step_graph = axes.get_graph(
            lambda x: 2.0 if x > 3 else 1.0,
            discontinuities=[3],
            color=GREEN,
        )

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            FadeTransform(sin_label, relu_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(relu_graph, step_graph),
            FadeTransform(relu_label, step_label),
        )
        self.wait()

        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
            FadeOut(step_graph),
            FadeOut(step_label),
            ShowCreation(parabola)
        )
        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()
```

----------------------------------------

TITLE: Manim Core Mobject Utility Functions and Concepts
DESCRIPTION: This section documents key Manim functions and classes for mobject manipulation and animation. It explains the purpose and usage of `always_redraw` for creating dynamically updated mobjects, `DecimalNumber` for animated numerical displays, and various positioning and updating methods like `.to_edge()`, `.center()`, `.set_y()`, `always()`, `f_always()`, and `.add_updater()`.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_10

LANGUAGE: APIDOC
CODE:
```
always_redraw(func: Callable[[], Mobject])
  Description: Creates a new mobject every frame. The function should return a Mobject.

DecimalNumber
  Description: A variable number mobject. Speed it up by breaking it into Text characters.

.to_edge(edge: Union[np.ndarray, Sequence[float]])
  Description: Places the object on the specified edge of the screen.

.center()
  Description: Places the object in the center of the screen.

always(f: Callable, x: Any)
  Description: Executes a certain function `f(x)` every frame.

f_always(f: Callable, g: Callable[[], Any])
  Description: Similar to `always`, executes `f(g())` every frame.

.set_y(y_coord: float)
  Description: Sets the y-coordinate (ordinate) of the object on the screen.

.add_updater(updater_func: Callable[[Mobject, Optional[float]], None])
  Description: Sets an update function for the object. The function should take in either one argument (the mobject) or two arguments (the mobject and time since last frame). Example: `mob1.add_updater(lambda mob: mob.next_to(mob2))` means `mob1.next_to(mob2)` is executed every frame.
```

----------------------------------------

TITLE: Dynamic Object Updates with Manim Updaters
DESCRIPTION: Demonstrates how to use Manim's updater functions (`always_redraw`, `always`, `f_always`) to create dynamically updating mobjects. This example shows a brace that continuously redraws itself to follow a square, and a decimal number that updates to display the square's width.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_8

LANGUAGE: Python
CODE:
```
class UpdatersExample(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE_E, 1)

        # On all all frames, the constructor Brace(square, UP) will
        # be called, and the mobject brace will set its data to match
        # that of the newly constructed object
        brace = always_redraw(Brace, square, UP)

        text, number = label = VGroup(
            Text("Width = "),
            DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=2,
                include_sign=True,
            )
        )
        label.arrange(RIGHT)

        # This ensures that the method deicmal.next_to(square)
        # is called on every frame
        always(label.next_to, brace, UP)
        # You could also write the following equivalent line
        # label.add_updater(lambda m: m.next_to(brace, UP))

        # If the argument itself might change, you can use f_always,
        # for which the arguments following the initial Mobject method
        # should be functions returning arguments to that method.
        # The following line ensures that decimal.set_value(square.get_y())
        # is called every frame
        f_always(number.set_value, square.get_width)
        # You could also write the following equivalent line
```

----------------------------------------

TITLE: Transforming Shapes with TransformMatchingShapes in Manim
DESCRIPTION: Illustrates `TransformMatchingShapes` for animating transformations between objects based on their visual shapes, regardless of their internal structure. It shows how to morph one `Text` object into another by matching their visual components.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_6

LANGUAGE: Python
CODE:
```
source = Text("the morse code", height=1)
target = Text("here come dots", height=1)

self.play(Write(source))
self.wait()
kw = {"run_time": 3, "path_arc": PI / 2}
self.play(TransformMatchingShapes(source, target, **kw))
self.wait()
self.play(TransformMatchingShapes(target, source, **kw))
self.wait()
```

----------------------------------------

TITLE: Manim Coordinate System and Point Mapping
DESCRIPTION: This example demonstrates how to create and configure `Axes` (a coordinate system) in Manim, specifying ranges, dimensions, and styling. It shows how to add coordinate labels and how to map between coordinates and screen points using `axes.c2p` (coords_to_point) and `axes.p2c` (point_to_coords). The snippet also illustrates using `always_redraw` to dynamically display lines tracking a moving point's coordinates.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_11

LANGUAGE: Python
CODE:
```
class CoordinateSystemExample(Scene):
    def construct(self):
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-1, 10),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-2, 2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            height=6,
            width=10,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        self.add(axes)

        # Axes descends from the CoordinateSystem class, meaning
        # you can call call axes.coords_to_point, abbreviated to
        # axes.c2p, to associate a set of coordinates with a point,
        # like so:
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        self.wait()

        # Similarly, you can call axes.point_to_coords, or axes.p2c
        # print(axes.p2c(dot.get_center()))

        # We can draw lines from the axes to better mark the coordinates
        # of a given point.
        # Here, the always_redraw command means that on each new frame
        # the lines will be redrawn
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()
```

----------------------------------------

TITLE: Manim LaTeX Transformation with OldTex and TransformMatchingTex
DESCRIPTION: Illustrates the use of `OldTex` for rendering LaTeX expressions, including isolating specific parts of the expression. It also demonstrates `TransformMatchingTex` for animating transformations between LaTeX equations by matching corresponding parts.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_4

LANGUAGE: python
CODE:
```
class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # Passing in muliple arguments to Tex will result
            # in the same expression as if those arguments had
            # been joined together, except that the submobject
            # hierarchy of the resulting mobject ensure that the
            # Tex mobject has a subject corresponding to
            # each of these strings.  For example, the Tex mobject
            # below will have 5 subjects, corresponding to the
            # expressions [A^2, +, B^2, =, C^2]
            OldTex("A^2", "+", "B^2", "=", "C^2"),
            # Likewise here
            OldTex("A^2", "=", "C^2", "-", "B^2"),
            # Alternatively, you can pass in the keyword argument
            # "isolate" with a list of strings that should be out as
            # their own submobject.  So the line below is equivalent
            # to the commented out line below it.
            OldTex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
            # OldTex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
            OldTex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
            })

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEG,
            ),
            **play_kw
        )
        self.wait()
```

----------------------------------------

TITLE: Manim: Dynamic Dot Movement Relative to Axes
DESCRIPTION: This snippet demonstrates how to use `f_always` to bind a `Dot`'s position to a specific coordinate on dynamically transforming `Axes`, ensuring the dot moves correctly with the coordinate system. It also includes animating the axes' scaling and position.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_12

LANGUAGE: Python
CODE:
```
f_always(dot.move_to, lambda: axes.c2p(1, 1))
self.play(
    axes.animate.scale(0.75).to_corner(UL),
    run_time=2,
)
self.wait()
self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))
```

----------------------------------------

TITLE: Manim Scene: Linear and Complex Plane Transformations
DESCRIPTION: This Manim scene, `OpeningManimExample`, illustrates fundamental mathematical concepts through animation. It demonstrates how to visualize linear transformations using a `NumberPlane` and how to apply complex functions (e.g., z -> z^2) to a `ComplexPlane`.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/example_scenes.rst#_snippet_16

LANGUAGE: python
CODE:
```
    class OpeningManimExample(Scene):
        def construct(self):
            intro_words = Text("""
                The original motivation for manim was to
                better illustrate mathematical functions
                as transformations.
            """)
            intro_words.to_edge(UP)

            self.play(Write(intro_words))
            self.wait(2)

            # Linear transform
            grid = NumberPlane((-10, 10), (-5, 5))
            matrix = [[1, 1], [0, 1]]
            linear_transform_words = VGroup(
                Text("This is what the matrix"),
                IntegerMatrix(matrix, include_background_rectangle=True),
                Text("looks like")
            )
            linear_transform_words.arrange(RIGHT)
            linear_transform_words.to_edge(UP)
            linear_transform_words.set_stroke(BLACK, 10, background=True)

            self.play(
                ShowCreation(grid),
                FadeTransform(intro_words, linear_transform_words)
            )
            self.wait()
            self.play(grid.animate.apply_matrix(matrix), run_time=3)
            self.wait()

            # Complex map
            c_grid = ComplexPlane()
            moving_c_grid = c_grid.copy()
            moving_c_grid.prepare_for_nonlinear_transform()
            c_grid.set_stroke(BLUE_E, 1)
            c_grid.add_coordinate_labels(font_size=24)
            complex_map_words = TexText("""
                Or thinking of the plane as $\\mathds{C}$,\\\\
                this is the map $z \\rightarrow z^2$
            """)
            complex_map_words.to_corner(UR)
            complex_map_words.set_stroke(BLACK, 5, background=True)

            self.play(
                FadeOut(grid),
                Write(c_grid, run_time=3),
                FadeIn(moving_c_grid),
                FadeTransform(linear_transform_words, complex_map_words)
            )
            self.wait()
            self.play(
                moving_c_grid.animate.apply_complex_function(lambda z: z**2),
```

----------------------------------------

TITLE: Manim Coordinate System API Updates
DESCRIPTION: Details changes to Manim's coordinate system classes (`Axes`, `ThreeDAxes`, `NumberPlane`, `ComplexPlane`), focusing on range definition and new utility functions for graph interaction.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/whatsnew.rst#_snippet_4

LANGUAGE: APIDOC
CODE:
```
Coordinate System Classes (Axes, ThreeDAxes, NumberPlane, ComplexPlane):
  Range Definition Change:
    Old: x_min, x_max, y_min, y_max
    New:
      x_range (np.array([Minimum, maximum, step size]))
      y_range (np.array([Minimum, maximum, step size]))
  New Utility Functions:
    .i2gp(x, graph) (abbreviation for .input_to_graph_point(x, graph))
    .get_v_line(point, line_func=DashedLine)
    .get_h_line(point, line_func=DashedLine)
    .get_graph_label(graph, label, x, direction, buff, color)
```

----------------------------------------

TITLE: Manim Camera and CameraFrame API Updates
DESCRIPTION: Outlines significant changes to Manim's camera system, including the removal of older camera classes, the introduction of `CameraFrame` as a `Mobject`, and new light source capabilities.
SOURCE: https://github.com/3b1b/manim/blob/master/docs/source/getting_started/whatsnew.rst#_snippet_1

LANGUAGE: APIDOC
CODE:
```
Camera:
  Removed Classes:
    - MappingCamera
    - MovingCamera
    - MultiCamera
    - All functions in ThreeDCamera
  New Features:
    light_source (Point): Accessible via self.camera.light_source. Default position (-10, 10, 10)

CameraFrame (Mobject):
  Access: self.camera.frame (in Scene)
  Inherited Methods:
    - .shift()
    - .scale()
  Specific Methods:
    .to_default_state()
    .set_euler_angles(theta, phi, gamma)
    .set_theta(theta)
    .set_phi(phi)
    .set_gamma(gamma)
    .increment_theta(dtheta)
    .increment_phi(dphi)
    .increment_gamma(gamma)
  Usage Example:
    self.camera.frame.add_updater(lambda mob, dt: mob.increment_theta(0.1 * dt))
```