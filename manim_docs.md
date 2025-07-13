TITLE: NumPy Style Function Docstring with Parameters, Returns, and Examples
DESCRIPTION: Provides a comprehensive example of a Python function docstring adhering to the NumPy format, including sections for 'Parameters' (with details on varargs and kwargs), 'Returns', and 'Examples' to guide users on function usage.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/docs/docstrings.rst#_snippet_2

LANGUAGE: python
CODE:
```
def my_function(
    thing: int,
    other: np.ndarray,
    name: str,
    *,
    d: "SomeClassFromFarAway",
    test: Optional[int] = 45
) -> "EpicClassInThisFile":  # typings are optional for now
    """My cool function. Builds and modifies an :class:`EpicClassInThisFile` instance with the given
        parameters.

    Parameters
    ----------
    thing
        Specifies the index of life.
    other
        Specifies something cool.
    name

```

----------------------------------------

TITLE: Manim Example Gallery and Installation Documentation Updates
DESCRIPTION: Summarizes various updates to Manim's example gallery and installation documentation. This includes additions of new examples for a wide range of geometric `Mobjects` (e.g., `Ellipse`, `Polygon`, `Arrow`, `Square`, `Circle`), removal of outdated examples (`BezierSpline`, `SmallDot`), and the inclusion of a new guide for installing Manim on Google Colab. Also covers adding new SVG files for documentation and examples.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.5.0-changelog.rst#_snippet_12

LANGUAGE: APIDOC
CODE:
```
Manim Example Gallery and Installation:

Example Additions:
  - New examples added for:
    - Ellipse, Polygon, RegularPolygon, Triangle, RoundedRectangle
    - DashedLine, TangentLine, Elbow, Arrow, Vector, DoubleArrow
    - Square, Dot, Circle, Rectangle
    - SurroundingRectangle
    - Rotation examples
    - Sounds examples

Example Removals:
  - Removed BezierSpline from the example gallery.
  - Removed SmallDot from examples.

Installation Guides:
  - Added: Documentation for installing Manim on Google Colab.

Documentation Assets:
  - Added: New SVG files for use in documentation and examples.
```

----------------------------------------

TITLE: General Documentation Improvements and Examples
DESCRIPTION: Various updates to the Manim documentation, including copyediting of existing guides (e.g., `troubleshooting.rst`, `configurations.rst`), adding new examples (`PolygonOnAxes`, `arrange_in_grid`), re-adding missing documentation (`value_tracker`), fixing typos, and updating copyright information. This also includes adding documentation and type hints for `utils/iterables.py` and instructions for installing extra dependencies with Poetry.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.15.2-changelog.rst#_snippet_19

LANGUAGE: APIDOC
CODE:
```
# Documentation Updates:
# - Copyediting: troubleshooting.rst, tutorials/configurations.rst, general documentation.
# - New Examples: Added examples for PolygonOnAxes and improved arrange_in_grid example
```

----------------------------------------

TITLE: Import Manim Library
DESCRIPTION: This snippet imports all necessary components from the Manim library, making them available for use in any Manim scene or animation script. It's a standard starting point for Manim projects.
SOURCE: https://github.com/manimcommunity/manim/blob/main/example_scenes/manim_jupyter_example.ipynb#_snippet_0

LANGUAGE: python
CODE:
```
from manim import *
```

----------------------------------------

TITLE: Manim Text and LaTeX Classes API Reference
DESCRIPTION: Comprehensive API documentation for Manim's text rendering classes: Text, MarkupText, Tex, and MathTex, detailing their constructors, parameters, and primary functionalities.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/using_text.rst#_snippet_17

LANGUAGE: APIDOC
CODE:
```
Text Class for Manim:
  __init__(text: str, gradient: tuple = None, t2g: dict = None, line_spacing: float = 1, disable_ligatures: bool = False, **kwargs)
    - text: The string content of the text object.
    - gradient: A tuple of colors (e.g., (RED, BLUE, GREEN)) to apply a gradient across the entire text.
    - t2g: A dictionary mapping string slices or words to color tuples, applying gradients to specific parts of the text. Example: {'[1:-1]': (RED, GREEN), 'World': (RED, BLUE)}.
    - line_spacing: A float value controlling the vertical spacing between lines of text. Default is 1.
    - disable_ligatures: A boolean. If True, disables ligatures, ensuring a one-to-one mapping between characters and submobjects. Useful for precise character manipulation but may affect text rendering for languages heavily relying on ligatures (e.g., Arabic).
  Behavior:
    - Behaves like VGroups, allowing slicing and indexing for individual character manipulation (e.g., `for letter in text: letter.set_color(...)`).

MarkupText Class for Manim:
  __init__(text: str, **kwargs)
    - text: The string content, which must be valid PangoMarkup (similar to HTML).
  Description:
    - Renders text that accepts and processes PangoMarkup for rich text formatting, unlike the plain text rendering of the Text class.

Tex Class for Manim (LaTeX Rendering):
  __init__(latex_string: str, **kwargs)
    - latex_string: The LaTeX code to render. Must be a raw string (e.g., r"\LaTeX") to correctly handle backslashes and other special LaTeX characters.
  Description:
    - Used to insert general LaTeX expressions into Manim scenes.
    - Can render mathematical formulas by enclosing them in '$' symbols (e.g., Tex(r"$\xrightarrow{x^6y^8}$")).

MathTex Class for Manim (Mathematical LaTeX Rendering):
  __init__(latex_math_string: str, **kwargs)
    - latex_math_string: The LaTeX code for a mathematical expression.
  Description:
    - Specifically designed for rendering mathematical expressions.
    - All content passed to MathTex is processed within an 'align*' environment by default, simplifying the rendering of multi-line equations and alignments.
    - Offers a more streamlined approach for math compared to enclosing expressions in '$' with the Tex class.
```

----------------------------------------

TITLE: Install Manim Plugin Template for Development
DESCRIPTION: Installs the `manim-plugintemplate` package, which serves as an in-depth tutorial and a starting point for creating new Manim plugins. It provides a structured example for plugin development.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/plugins.rst#_snippet_4

LANGUAGE: bash
CODE:
```
pip install manim-plugintemplate
```

----------------------------------------

TITLE: Deprecated and Removed APIs in Manim v0.11.0
DESCRIPTION: Lists classes, methods, and parameters that have been deprecated or removed in this release, advising users to update their code to use the new alternatives or remove references to the obsolete APIs.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.11.0-changelog.rst#_snippet_2

LANGUAGE: APIDOC
CODE:
```
ThreeDScene.distance (parameter)
ThreeDCamera.distance (parameter)
  - Renamed to 'focal_distance'.

SampleSpaceScene (class)
ReconfigurableScene (class)
  - These classes have been deprecated.

Surface.u_min (parameter)
Surface.u_max (parameter)
Surface.v_min (parameter)
Surface.v_max (parameter)
  - These parameters have been removed (previously deprecated).

Mobject.rotate_in_place()
Mobject.scale_in_place()
Mobject.scale_about_point()
  - These methods have been deprecated as they are redundant.

VMobject.get_points()
  - This method has been deprecated.
```

----------------------------------------

TITLE: Manim v0.13.0 API Enhancements
DESCRIPTION: This section details enhancements made to existing API methods in Manim version 0.13.0, improving their flexibility and usability.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.13.0-changelog.rst#_snippet_2

LANGUAGE: APIDOC
CODE:
```
API Enhancements in Manim v0.13.0:

Table:
  add_highlighted_cell
    - Added missing `**kwargs` parameter to allow for more flexible customization when highlighting cells.
```

----------------------------------------

TITLE: Manim Scene: Text, Transformations, and Grid Animations
DESCRIPTION: This Manim scene demonstrates various animation techniques. It shows how to render LaTeX text, arrange objects, perform `Write` and `FadeIn` animations, and apply `Transform` animations. It also includes an example of creating a `NumberPlane` grid and applying a non-linear function to it using `apply_function`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_29

LANGUAGE: Python
CODE:
```
class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid", font_size=72)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                          + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()
```

----------------------------------------

TITLE: reStructuredText Syntax for Embedding Python Code Examples
DESCRIPTION: Illustrates the reStructuredText (RST) syntax used to embed literal code blocks, specifically for Python examples, within documentation files.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/docs/docstrings.rst#_snippet_3

LANGUAGE: rst
CODE:
```
::

       # python code here
```

----------------------------------------

TITLE: Deprecated and Removed Manim API in v0.9.0
DESCRIPTION: Details changes to deprecated parameters and removed classes/functions in Manim v0.9.0, guiding users to their replacements and indicating removed utility functions.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.9.0-changelog.rst#_snippet_0

LANGUAGE: APIDOC
CODE:
```
Deprecated classes and functions:

- DashedLine and DashedVMobject parameters:
  - dash_spacing: Unused parameter.
  - positive_space_ratio: Replaced with dashed_ratio.

- Removed classes and functions (deprecated until v0.7.0 and v0.8.0):
  - FadeInFrom, FadeOutAndShift, FadeOutToPoint, FadeInFromPoint, FadeInFromLarge, VFadeIn, VFadeOut, VFadeInThenOut: Use FadeIn or FadeOut with appropriate keyword arguments.
  - CircleIndicate, ShowCreationThenDestruction, AnimationOnSurroundingRectangle, ShowPassingFlashAround, ShowCreationThenDestructionAround, ShowCreationThenFadeAround, WiggleOutThenIn, TurnInsideOut: Use Circumscribe, ShowPassingFlash, or Wiggle instead.
  - OpenGLTexMobject, OpenGLTextMobject: Use MathTex and Tex instead.
  - VMobjectFromSVGPathstring: Use SVGPathMobject instead.

- Removed utility functions:
  - get_norm, cross: Use corresponding Numpy methods instead.
  - angle_between: Replaced with angle_between_vectors.

- ParametricSurface parameters:
  - u_min, u_max: Replaced by u_range.
  - v_min, v_max: Replaced by v_range.
```

----------------------------------------

TITLE: Manim Toy Example Scene Definition
DESCRIPTION: Defines a basic Manim scene demonstrating object creation, transformations, updaters, and animations. This example initializes a square and a circle, transforms the square into the circle, adds a dot with an updater that follows the circle's movement, and concludes by fading out all mobjects.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_0

LANGUAGE: python
CODE:
```
from manim import *

class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))
```

----------------------------------------

TITLE: Manim v0.13.0 API Deprecations and Removals
DESCRIPTION: This section details the API elements that have been deprecated or removed in Manim version 0.13.0, along with their replacements where applicable. These changes aim to streamline the API and remove outdated functionalities.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.13.0-changelog.rst#_snippet_0

LANGUAGE: APIDOC
CODE:
```
Deprecated/Removed API Elements in Manim v0.13.0:

ThreeDCamera:
  - Removed parameter: `distance`
  - Replacement: `focal_distance`

TracedPath:
  - Removed parameter: `min_distance_to_new_point`

DashedVMobject:
  - Removed parameters: `positive_space_ratio`, `dash_spacing`

mobject module:
  - Removed methods: All `<method>_in_place` methods

ReconfigurableScene:
  - Removed class

SampleSpaceScene:
  - Removed class
```

----------------------------------------

TITLE: Manim Internal Rendering API Reference
DESCRIPTION: Comprehensive documentation for key methods and classes involved in Manim's internal animation processing and frame rendering pipeline, detailing their purpose and interaction.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_24

LANGUAGE: APIDOC
CODE:
```
Animation.interpolate()
  - Purpose: Updates the state of an animation based on the current time progression.

Scene.play_internal()
  - Purpose: The core internal render loop entry point. It handles the time progression, ensures updater functions run, and coordinates frame rendering, even if frames are skipped.
  - Details: Iterates over time progression, updates internal state of all mobjects, and ensures consistency even when frames are not rendered.

CairoRenderer.render(moving_mobjects)
  - Purpose: Renders an image by processing a list of moving mobjects. Static mobjects are assumed to be pre-painted to the background.
  - Parameters:
    - moving_mobjects (list of Mobjects): Mobjects that are actively changing and need to be rendered.

CairoRenderer.update_frame()
  - Purpose: Updates the renderer's current frame. This involves preparing the camera and initiating the capture process.
  - Details: Checks for a `static_image` to set as background via `Camera.set_frame_to_background` or resets the camera via `Camera.reset`.

Camera.set_frame_to_background()
  - Purpose: Sets a stored static image as the background of the camera.

Camera.reset()
  - Purpose: Resets the camera to its default state.

Camera.capture_mobjects()
  - Purpose: Captures the scene by processing mobjects and converting them into a NumPy array stored in the camera's `pixel_array` attribute.
  - Process:
    1. Creates a flat list of mobjects (submobjects extracted from parents).
    2. Processes mobjects in batches by type (e.g., vectorized, image).
    3. Uses dedicated display functions to convert Python Mobject objects to NumPy arrays.

Camera.display_multiple_vectorized_mobjects()
  - Purpose: A dedicated display function for converting a batch of vectorized mobjects into pixel data.
  - Details: Gets the current Cairo context and calls `Camera.display_vectorized` for each mobject in the batch.

Camera.display_multiple_non_background_colored_vmobjects()
  - Purpose: A more particular display function for vectorized mobjects that do not have a background image.

Camera.display_vectorized()
  - Purpose: Draws the actual background stroke, fill, and then stroke of a vectorized mobject onto the Cairo context.
  - Details: Interacts with Cairo at a low level, calling `Camera.apply_stroke` and `Camera.set_cairo_context_color`.

Camera.apply_stroke()
  - Purpose: Applies stroke properties to a mobject within the Cairo context.

Camera.set_cairo_context_color()
  - Purpose: Sets the color in the Cairo context. This is where low-level drawing of Bézier curves (determined by mobject points) happens.

SceneFileWriter (Class)
  - Purpose: Receives the NumPy array (image representation of the scene) from the renderer after the camera has captured the scene, concluding one iteration of the render loop.
```

----------------------------------------

TITLE: Manim Command Line Interface Arguments
DESCRIPTION: Documentation for various command-line arguments used with the `manim` executable to control rendering behavior, output quality, and animation playback. These flags provide fine-grained control over the animation generation process.
SOURCE: https://github.com/manimcommunity/manim/blob/main/README.md#_snippet_2

LANGUAGE: APIDOC
CODE:
```
manim [flags] <file.py> <SceneName>
  -p: Preview the video file automatically when rendering is complete.
  -ql: Render at a lower quality for faster processing.
  -s: Skip to the end and just show the final frame of the animation.
  -n <number>: Skip ahead to the Nth animation of a scene.
  -f: Show the generated file in the file browser.
```

----------------------------------------

TITLE: Python Manim Import Statement
DESCRIPTION: A standard Python import statement used to bring the Manim library into a Python script, enabling access to its functionalities. This is a basic example for starting a Manim project.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_11

LANGUAGE: python
CODE:
```
import manim
```

----------------------------------------

TITLE: Annotate Lines with Braces in Manim
DESCRIPTION: This example shows how to use the `Brace` Mobject to annotate a line segment. It demonstrates creating a line between two dots and then adding both horizontal and rotated braces with custom text annotations, showcasing text positioning relative to the brace.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_1

LANGUAGE: Python
CODE:
```
class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.add(line, dot, dot2, b1, b2, b1text, b2text)
```

----------------------------------------

TITLE: Animate Square to Circle Transformation with Dynamic Properties
DESCRIPTION: Demonstrates how to create a square, rotate it, and transform it into a circle using Manim's `.animate` property for dynamic property changes like rotation and fill color. This method interpolates between start and end states, showing the animation of property changes.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_11

LANGUAGE: python
CODE:
```
class AnimatedSquareToCircle2(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(square.animate.set_fill(PINK, opacity=0.5))  # color the circle on screen
```

----------------------------------------

TITLE: Breaking API Changes in Manim v0.11.0
DESCRIPTION: This section details significant API changes that may require code updates, including modifications to coordinate system methods and polar coordinate conventions to align with mathematical standards.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.11.0-changelog.rst#_snippet_0

LANGUAGE: APIDOC
CODE:
```
CoordinateSystem.get_area()
  - Implementation changed to work without Riemann rectangles.
  - To mimic old behavior, use CoordinateSystem.get_riemann_rectangles(dx) with a small 'dx' value.

cartesian_to_spherical(x, y, z, phi, theta)
spherical_to_cartesian(r, phi, theta)
  - Parameter names 'phi' and 'theta' have been switched to align with standard mathematical conventions for spherical coordinates.
```

----------------------------------------

TITLE: Manim Scene Class API Reference
DESCRIPTION: Comprehensive documentation for the `Scene` class in Manim, detailing its role as the central component for displaying mobjects, playing animations, and managing time. It outlines key methods like `add`, `remove`, `play`, `wait`, and the `construct` method.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_25

LANGUAGE: APIDOC
CODE:
```
Scene Class:
  Description: The connective tissue of manim. Every mobject has to be added to a scene to be displayed, or removed from it to cease being displayed. Every animation has to be played by a scene, and every time interval where no animation occurs is determined by a call to wait. All of the code of your video must be contained in the construct method of a class that derives from Scene. Finally, a single file may contain multiple Scene subclasses if multiple scenes are to be rendered at the same time.
  Methods:
    - add(mobject):
      Description: Adds a mobject to the scene to be displayed.
      Parameters:
        - mobject: The mobject to add to the scene.
    - remove(mobject):
      Description: Removes a mobject from the scene, causing it to cease being displayed.
      Parameters:
        - mobject: The mobject to remove from the scene.
    - play(animation, ...):
      Description: Plays one or more animations.
      Parameters:
        - animation: One or more animation objects to play.
    - wait(duration):
      Description: Pauses the scene for a specified duration.
      Parameters:
        - duration: The time in seconds to wait.
    - construct():
      Description: Abstract method where all video code must be contained. This method is automatically called when the scene is rendered.
```

----------------------------------------

TITLE: Positioning Manim Mobjects Relative to Each Other
DESCRIPTION: This example illustrates how to position Manim Mobjects relative to each other using the `next_to` method. It shows how to specify a reference Mobject, a direction (e.g., `RIGHT`), and a buffer distance to precisely arrange objects on the screen.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_8

LANGUAGE: python
CODE:
```
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen
```

LANGUAGE: bash
CODE:
```
manim -pql scene.py SquareAndCircle
```

----------------------------------------

TITLE: Manim Deprecated and Removed API Elements (v0.6.0)
DESCRIPTION: Lists classes and functions that have been deprecated or fully removed in this release, with guidance on replacements.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.6.0-changelog.rst#_snippet_3

LANGUAGE: APIDOC
CODE:
```
Removed Classes:
  - TexMobject
  - TextMobject
  - Replacement: Use Tex or MathTex instead. (Deprecated for a while, now fully removed).

Deprecated Functions:
  - angle_between (in space_ops.py)
  - Note: Refactored functions in space_ops.py.
```

----------------------------------------

TITLE: Animate Ambient 3D Camera Rotation in Manim
DESCRIPTION: This Manim 3D scene demonstrates continuous ambient rotation of the camera around a 3D scene. It shows how to start and stop the rotation, and then manually move the camera.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_25

LANGUAGE: Python
CODE:
```
    class ThreeDCameraRotation(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            circle=Circle()
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(circle,axes)
            self.begin_ambient_camera_rotation(rate=0.1)
            self.wait()
            self.stop_ambient_camera_rotation()
            self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
            self.wait()
```

----------------------------------------

TITLE: Define and Render a Complete Manim Scene Example
DESCRIPTION: Presents a full Manim scene definition, `ToyExample`, showcasing various animation methods like `ReplacementTransform`, `Create`, `add_updater`, and `animate.shift`. The snippet also includes the necessary programmatic call to render the defined scene using `tempconfig`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_4

LANGUAGE: python
CODE:
```
from manim import *

class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))

with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = ToyExample()
    scene.render()
```

----------------------------------------

TITLE: Manim v0.13.0 New API Features
DESCRIPTION: This section outlines the new methods and keyword arguments introduced in Manim version 0.13.0 to extend functionality, particularly for scene control and plotting capabilities.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.13.0-changelog.rst#_snippet_1

LANGUAGE: APIDOC
CODE:
```
New API Features in Manim v0.13.0:

Scene:
  add_subcaption
    - New method for adding subcaptions to the scene.

Scene.play:
  - New keyword arguments:
    - `subcaption`: Used to specify a subcaption during animation playback.
    - `subcaption_duration`: Controls the display duration of the subcaption.
    - `subcaption_offset`: Adjusts the position offset of the subcaption.

CoordinateSystem:
  plot_antiderivative_graph
    - New method for plotting the antiderivative graph of a given function.
```

----------------------------------------

TITLE: Create and Style a Manim Mobject
DESCRIPTION: This code demonstrates how to instantiate a `Circle` object, which is a type of `Mobject` in Manim. It then applies visual styling by setting the fill color to pink and adjusting its opacity.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_5

LANGUAGE: python
CODE:
```
circle = Circle()  # create a circle
circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
```

----------------------------------------

TITLE: Manim v0.13.0 API Behavior Fixes
DESCRIPTION: This section outlines bug fixes related to the behavior of specific Manim API classes and methods in version 0.13.0, addressing issues with rendering, positioning, and data handling.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.13.0-changelog.rst#_snippet_3

LANGUAGE: APIDOC
CODE:
```
API Behavior Fixes in Manim v0.13.0:

ThreeDAxes:
  - Fixed bug with alignment of the z-axis.

PointCloud:
  - Fixed bug related to camera zooming interaction.

Table:
  get_cell
    - Fixed bug causing incorrect cell coordinates after scaling the table.

DecimalNumber:
  - Fixed bug affecting color consistency when the number of displayed digits changes.

Flash:
  - Fixed positioning bug.
```

----------------------------------------

TITLE: RotationUpdater Example in Manim
DESCRIPTION: This Manim scene demonstrates how to use updaters to control the rotation of a Mobject. It shows a line rotating in one direction, then reversing its rotation using `add_updater` and `remove_updater` methods.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_12

LANGUAGE: python
CODE:
```
class RotationUpdater(Scene):
    def construct(self):
        def updater_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt)
        line_reference = Line(ORIGIN, LEFT).set_color(WHITE)
        line_moving = Line(ORIGIN, LEFT).set_color(YELLOW)
        line_moving.add_updater(updater_forth)
        self.add(line_reference, line_moving)
        self.wait(2)
        line_moving.remove_updater(updater_forth)
        line_moving.add_updater(updater_back)
        self.wait(2)
        line_moving.remove_updater(updater_back)
        self.wait(0.5)
```

----------------------------------------

TITLE: Manim Mobject and Geometry API Updates
DESCRIPTION: This section details significant updates to Manim's Mobject and geometric primitive APIs, including deprecations, new 3D objects, enhanced property handling, and improved rendering capabilities for various Mobject types.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.4.0-changelog.rst#_snippet_0

LANGUAGE: APIDOC
CODE:
```
SVGPathMobject (replaces VMobjectFromSVGPathstring):
  - Description: New SVG engine capable of handling wider variations of SVG files, retaining fill and stroke properties.
  - Breaking Change: VMobjectFromSVGPathstring is deprecated and renamed to SVGPathMobject.

New 3D Mobjects:
  - Classes: Cone, Cylinder, Line3D, Arrow3D, Torus
  - Description: Added new classes for creating various 3D geometric shapes.

Matrix Class:
  - Description: Enhanced documentation and examples for the Matrix class.

Mobject.set(property_name, value):
  - Description: Generic method to set Mobject properties, providing a compatibility layer between properties and get_*/set_* methods.

MarkupText Coloring:
  - Description: Replaced <color> syntax with Pango's <span foreground> for coloring parts of MarkupText. Allows using colors for underline, overline, and strikethrough.

Cross Mobject Stroke:
  - Description: Ensures user-supplied stroke color and width are correctly applied to the Cross Mobject.

VMobject Stroke Attributes:
  - Description: Corrections for setting stroke-related attributes on VMobject.

CubicBezier Class:
  - Description: Now explicitly accepts four points for defining the curve. Documentation includes new examples.

FunctionGraph Arguments:
  - Description: Redundancy in FunctionGraph arguments has been removed.

Mobject Properties (width, height, depth):
  - Description: These attributes have been migrated to properties for better consistency and control.

VMobject.set_color(colors: list):
  - Description: Fixed setting Mobject color to a gradient by passing a list of colors.
```

----------------------------------------

TITLE: Manim API Enhancements in v0.9.0
DESCRIPTION: Describes various improvements and optimizations made to existing Manim classes and functionalities in v0.9.0, including OpenGL compatibility, rendering updates, and refined mobject behaviors.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.9.0-changelog.rst#_snippet_2

LANGUAGE: APIDOC
CODE:
```
Enhancements:

- OpenGL compatibility:
  - Added OpenGL compatibility for :class:`~.VDict`, :meth:`~.Axes.get_line_graph` and :class:`~.FocusOn`.

- Window size flag:
  - Added ``window_size`` flag to manually adjust the size of the OpenGL window.
  - Accepts a tuple in the form: ``x,y``.

- DashedVMobject rework:
  - Reworked :class:`~.DashedVMobject`.
  - Rewritten the logic to generate dashes.

- OpenGL renderer updates:
  - Adds model matrices to all OpenGLVMobjects.
  - Improved performance on vectorized mobject shaders.
  - Added updaters that are part of the scene rather than a mobject.

- DecimalNumber color:
  - Made :class:`~.DecimalNumber` apply color to the ellipsis when `show_ellipsis` is set to true.

- Create animation:
  - Let :class:`~.Create` work on :class:`~.OpenGLSurface`.

- Hashing warning:
  - Added warning when there is a large number of items to hash.

- Write animation:
  - Add the ``reverse`` parameter to :class:`~.Write`.
```

----------------------------------------

TITLE: Manim: ThreeDScene Camera Zoom with `move_camera`
DESCRIPTION: Introduces the new `zoom` parameter for `ThreeDScene.move_camera`, allowing direct control over camera zoom. Includes a Python usage example and the API signature.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.10.0-changelog.rst#_snippet_0

LANGUAGE: python
CODE:
```
self.move_camera(zoom=2)
```

LANGUAGE: APIDOC
CODE:
```
ThreeDScene.move_camera(zoom: float = 1.0, **kwargs)
  Description: Adjusts the camera's position and orientation in a 3D scene.
  Parameters:
    zoom (float): The zoom factor to apply. A value greater than 1 zooms in, less than 1 zooms out. Defaults to 1.0 (no zoom change).
```

----------------------------------------

TITLE: Animate Point Moving on Shapes in Manim
DESCRIPTION: This example showcases various animation types for a `Dot` object. It demonstrates growing a `Circle` from its center, transforming one dot into another, moving a dot along a circular path, and rotating a dot around a specified point.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_6

LANGUAGE: Python
CODE:
```
class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()
```

----------------------------------------

TITLE: Create Gradient Image from NumPy Array in Manim
DESCRIPTION: This example demonstrates generating an `ImageMobject` from a NumPy array to create a simple grayscale gradient image. It scales the image and adds a `SurroundingRectangle` for visual emphasis, showcasing how to integrate array-based images.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_3

LANGUAGE: Python
CODE:
```
class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        imageArray = np.uint8(
            [[i * 256 / n for i in range(0, n)] for _ in range(0, n)]
        )
        image = ImageMobject(imageArray).scale(2)
        image.background_rectangle = SurroundingRectangle(image, color=GREEN)
        self.add(image, image.background_rectangle)
```

----------------------------------------

TITLE: Type Hinting Callables
DESCRIPTION: Provides an example of type hinting a callable object, specifying its input and output types using `Callable[[input_type], output_type]` for clarity and type safety.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/docs/typings.rst#_snippet_2

LANGUAGE: python
CODE:
```
rate_func: Callable[[float], float] = lambda t: smooth(1 - t)
```

----------------------------------------

TITLE: Animate Difference of Ellipses in Manim
DESCRIPTION: This snippet demonstrates how to create a 'Difference' mobject from two ellipses, apply color and fill opacity, and then animate its scaling and positioning relative to other objects. It also shows how to add and fade in accompanying text.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_5

LANGUAGE: Python
CODE:
```
d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
difference_text = Text("Difference", font_size=23)
self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
difference_text.next_to(d, UP)
self.play(FadeIn(difference_text))
```

----------------------------------------

TITLE: Manim Camera Following Graph
DESCRIPTION: This example illustrates how to implement a camera that dynamically follows a moving object along a graph in Manim. It utilizes `MovingCameraScene` and `add_updater` to ensure the camera's frame continuously centers on a `moving_dot`. The `MoveAlongPath` animation is used to move the dot along a plotted sine wave, demonstrating advanced camera control for focused views.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_20

LANGUAGE: Python
CODE:
```
class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
```

----------------------------------------

TITLE: Manim Scene and Animation Rendering Pipeline API
DESCRIPTION: This section describes key methods and classes involved in Manim's animation playback and rendering pipeline, from initial setup to frame generation. It covers how animations are prepared, mobjects are managed, and the time progression is handled during the rendering process.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_23

LANGUAGE: APIDOC
CODE:
```
Class: .ReplacementTransform
  - Description: An animation class that populates its relevant animation attributes (e.g., compatible copies of start and target mobjects) to enable safe interpolation between them during an animation.

Method: .CairoRenderer.save_static_frame_data()
  - Description: Checks if there are any static mobjects in the scene. If so, it updates the frame with only these static mobjects and saves a NumPy array representing the rendered frame to the `static_image` attribute. If no static mobjects exist, `static_image` is set to `None`.
  - Parameters: None explicitly mentioned; operates on the current scene's state.
  - Returns: Modifies the `static_image` attribute of the renderer (NumPy array or None).
  - Related Attribute: `static_image` (attribute of `CairoRenderer`, stores the rendered static frame data).

Method: .Scene.play_internal()
  - Description: The integral part of the Manim render loop. This method steps through the time progression of the animation and renders the corresponding frames.
  - Parameters: None explicitly mentioned; operates on the scene's current animations.
  - Internal Steps:
    1. Determines the total run time of the animations by calling `.Scene.get_run_time()`.
    2. Constructs the time progression via the internal method `.Scene._get_animation_time_progression()` (which wraps `.Scene.get_time_progression()`).
    3. Iterates over the generated time progression: for each time stamp `t`, it calls `.Scene.update_to_time(t)`.

Method: .Scene.get_run_time()
  - Description: Calculates the total run time for the current set of animations being played.
  - Parameters: None explicitly mentioned.
  - Returns: The maximum `run_time` attribute found among all animations passed to the `.Scene.play()` call.

Method: .Scene._get_animation_time_progression()
  - Description: An internal method that wraps `.Scene.get_time_progression()` to construct the time progression for the animation. It generates an iterator over time stamps for rendering.
  - Parameters: None explicitly mentioned.
  - Returns: A `tqdm` progress bar object for an iterator over `np.arange(0, run_time, 1 / config.frame_rate)`, representing the time stamps for frame rendering.

Method: .Scene.get_time_progression()
  - Description: Generates the sequence of time stamps that define when new animation frames should be rendered. These timestamps are relative to the current animation's start.
  - Parameters: None explicitly mentioned.
  - Returns: An iterator providing time stamps (relative to the current animation, starting at 0 and ending at the total animation run time, with the step size determined by the render frame rate).

Method: .Scene.update_to_time(t: float)
  - Description: Updates the scene state to a specific time stamp `t` during the render loop, preparing mobjects for rendering at that moment.
  - Parameters:
    - t (float): The current time stamp in the animation's timeline.
  - Internal Steps:
    1. Computes `dt`, the time passed since the last update (which might be 0 for the initial call).
    2. Calls `.Animation.update_mobjects()` for all updater functions attached to the respective animation, excluding the "main mobject" of the animation.
    3. Computes `alpha` (the relative time progression for the current animation: `t / animation.run_time`).

Method: .Animation.update_mobjects()
  - Description: Triggers all updater functions that are attached to the respective animation's mobjects. This method is crucial for animating changes over time.
  - Parameters: None explicitly mentioned; operates on the animation's associated mobjects.
  - Note: This method typically does not update the "main mobject" of the animation itself, but rather its sub-mobjects or related components.

Method: .Animation.get_all_mobjects_to_update()
  - Description: Provides details on which mobjects are targeted for updates by an animation. For example, for a `Transform` animation, it might refer to the unmodified copies of the start and target mobjects.
  - Parameters: None explicitly mentioned.
  - Returns: Information about the mobjects that will have their updater functions called.

Method: .Scene.compile_animation_data()
  - Description: (Referenced) A method involved in determining if an animation is considered a "frozen frame" animation (e.g., if only a static `.Wait` animation is played).
  - Parameters: Not detailed in the provided text.

Method: .Scene.should_update_mobjects()
  - Description: (Referenced) A method involved in determining if an animation is considered a "frozen frame" animation, influencing whether moving mobjects need to be repainted in every frame.
  - Parameters: Not detailed in the provided text.
```

----------------------------------------

TITLE: Example Usage of my_function in Manim
DESCRIPTION: Demonstrates a typical invocation of 'my_function' with various argument types, including numerical, NumPy array, string, and custom class instances, along with keyword arguments for 'd' and 'test'. This snippet illustrates how to call the function with diverse inputs.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/docs/docstrings.rst#_snippet_4

LANGUAGE: python
CODE:
```
my_function(5, np.array([1, 2, 3]), "Chelovek", d=SomeClassFromFarAway(cool=True), test=5)
```

----------------------------------------

TITLE: New Manim API Features in v0.9.0
DESCRIPTION: Introduces new mobjects, methods, and functions added in Manim v0.9.0, enhancing capabilities for creating animations with new table support, improved coordinate system labeling, and animation types.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.9.0-changelog.rst#_snippet_1

LANGUAGE: APIDOC
CODE:
```
New features:

- Table mobject:
  - New :class:`~.Table` mobject for easy-to-use and customizable tables.
  - Examples available at the module documentation page <.mobject.table> and its subpages.

- NumberLine and Axes non-numerical values:
  - NumberLine.add_labels: New method for :class:`~.NumberLine` accepting a dictionary of positions/values.
  - CoordinateSystem.add_coordinates: Now accepts a dictionary too.

- Broadcast animation:
  - Added a :class:`~.Broadcast` animation.

- Circle.from_three_points:
  - Added a static method :meth:`.Circle.from_three_points` for defining a circle from three points.
  - Added a new :func:`~.perpendicular_bisector` function in ``space_ops.py``.

- ParametricSurface.set_fill_by_value:
  - Enables a color gradient to be applied to a :class:`~.ParametricSurface`.
  - Includes ability to define at which points the colors should be centered.
```

----------------------------------------

TITLE: Animate a Group of Mobjects to a Destination in Manim
DESCRIPTION: This example illustrates how to move an entire `VGroup` of mobjects to a specific destination point. It calculates the necessary shift based on the position of one of the group's elements and applies the animation to the whole group.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_10

LANGUAGE: Python
CODE:
```
class MovingGroupToDestination(Scene):
    def construct(self):
        group = VGroup(Dot(LEFT), Dot(ORIGIN), Dot(RIGHT, color=RED), Dot(2 * RIGHT)).scale(1.4)
        dest = Dot([4, 3, 0], color=YELLOW)
        self.add(group, dest)
        self.play(group.animate.shift(dest.get_center() - group[2].get_center()))
        self.wait(0.5)
```

----------------------------------------

TITLE: Get Global uv Tool Directory
DESCRIPTION: Command to retrieve the base directory where `uv` stores its globally installed tools. This is useful for configuring IDEs to properly locate and resolve Manim's environment when installed as a global tool.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_13

LANGUAGE: bash
CODE:
```
uv tool dir
```

----------------------------------------

TITLE: Basic Manim Scene with Circle
DESCRIPTION: This example defines a simple Manim scene named `Example1` that adds a `Circle` object to the display. It utilizes Manim's Jupyter magic command (`%%manim`) for quick rendering with specific output settings like warning suppression and quality.
SOURCE: https://github.com/manimcommunity/manim/blob/main/example_scenes/manim_jupyter_example.ipynb#_snippet_1

LANGUAGE: python
CODE:
```
%%manim -v WARNING --disable_caching -ql -s Example1

class Example1(Scene):
    def construct(self):
        self.add(Circle())
```

----------------------------------------

TITLE: Deprecated Manim API in v0.17.3
DESCRIPTION: This section lists functions and methods that have been removed or deprecated in Manim v0.17.3, advising users to update their code to avoid compatibility issues.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.17.3-changelog.rst#_snippet_0

LANGUAGE: APIDOC
CODE:
```
Removed:
- OpenGLSurface.set_fill_by_value: Removed deprecated function.
```