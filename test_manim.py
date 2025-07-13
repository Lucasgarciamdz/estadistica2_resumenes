from manim import *

class TestScene(Scene):
    def construct(self):
        self.add(Tex("Hello World"))
        self.wait(1)
