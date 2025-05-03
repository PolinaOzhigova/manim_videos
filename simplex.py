from manim import *
import numpy as np

config.background_color = "#2B3F57"

class simplex(ThreeDScene):
    def construct(self):

        constraints = VGroup(
            Tex("Linear programming problem"),
            MathTex(r"F = 5x_1+6x_2 + 10x_3 \rightarrow max"),
            MathTex(r"6x_1 + 3x_2 \leq 100"),
            MathTex(r"x_1 + 4x_2 + x_3 \leq 50"),
        ).arrange(DOWN, buff=0.5).shift(UP)
        
        self.play(Write(constraints), run_time=1)
        self.wait(2)
        self.play(FadeOut(constraints))

        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Золотое сечение
        phi = (1 + np.sqrt(5)) / 2
        
        # Вершины икосаэдра (увеличенные в 2 раза)
        scale = 2
        vertices = np.array([
            [-1, phi, 0], [1, phi, 0], [-1, -phi, 0], [1, -phi, 0],
            [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
            [phi, 0, -1], [phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
        ]) / np.linalg.norm([-1, phi, 0]) * scale
        
        # Грани икосаэдра (списки индексов вершин)
        faces = [
            [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
            [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
            [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
            [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
        ]
        
        # Отображение граней икосаэдра
        for face in faces:
            polygon = Polygon(*[vertices[i] for i in face], color=BLUE, fill_color=BLUE, fill_opacity=0.5,  stroke_width=1.5)
            self.add(polygon)

        # for i, vertex in enumerate(vertices):
        #     label = Text(f"{np.round(vertex, 2)}", font_size=24).move_to(vertex + np.array([0, 0, 0.3]))
        #     self.add(label)
        
        # Выделение трех вершин по очереди (используем 3D точки)
        highlight_color = YELLOW
        for i in [8, 9, 4]:
            sphere = Dot3D(vertices[i], radius=0.15, color=highlight_color)
            self.add(sphere)
            self.wait(1.5)
            self.play(FadeOut(sphere), run_time=0.5)
        
        self.wait(1.5)
        
        
