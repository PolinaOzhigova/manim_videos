from manim import *

config.background_color = "#2B3F57"

class lp(Scene):
    def construct(self):
        
        # Ось
        axes = Axes(
            x_range=[0, 50, 10],
            y_range=[0, 50, 10],
            x_length=6,
            y_length=6
        )
        
        # Целевая функция (пример с минимумом)
        objective = axes.plot_line_graph(
            x_values = [0, 40],
            y_values = [40, 0],
            line_color=YELLOW
        )
        func_label = MathTex("x_1 + x_2 = 40").next_to(objective, UP)
        
        # Ограничение
        constraint = axes.plot_line_graph(
            x_values = [0, 40],
            y_values = [20, 20],
            line_color=RED
        )
        constr_label = MathTex("x_2 < 20").next_to(constraint, RIGHT)

        vertices = [
            axes.coords_to_point(0, 0),
            axes.coords_to_point(0, 20),
            axes.coords_to_point(20, 20),
            axes.coords_to_point(40, 0)
        ]
        polygon = Polygon(*vertices, color=RED, fill_opacity=0.3)

        self.play(Create(axes))
        self.play(Create(objective), Write(func_label), run_time=1.5)
        self.play(Create(constraint), Write(constr_label), run_time=1)
        self.play(DrawBorderThenFill(polygon), run_time=1)
        self.wait(1)
        
        # Стираем график
        self.play(
            FadeOut(objective),
            FadeOut(func_label),
            FadeOut(constraint),
            FadeOut(constr_label),
            FadeOut(axes),
            FadeOut(polygon)
        )
        
        # Шаг 3: Формула максимизации
        obj_func = MathTex("50x_1 + 40x_2 \\rightarrow \\max").scale(1.5)
        self.play(Write(obj_func), run_time=4)
        self.wait(4)
        self.play(FadeOut(obj_func))
        
        # Шаг 4: Система ограничений
        constraints = VGroup(
            MathTex(r"x_1 + 3x_2 \leq 120"),
            MathTex(r"2x_1 + x_2 \leq 100"),
            MathTex(r"x_2 - x_1 \leq 20"),
            MathTex(r"x_2 \leq 32")
        ).arrange(DOWN, buff=0.5).shift(UP)
        
        for constr in constraints:
            self.play(Create(constr), run_time=3)
            self.wait(2)
        
        self.wait(2)
        self.play(FadeOut(constraints))


        axes = Axes(
            x_range=[0, 60, 10],
            y_range=[0, 60, 10],
            x_length=9,
            y_length=6,
            axis_config={"color": WHITE},
        ).add_coordinates()
        axes_labels = axes.get_axis_labels(x_label="x_1", y_label="x_2")
        
        # Line 1: x1 + 3x2 = 120
        line1 = axes.plot(lambda x: (120 - x)/3, x_range=[0, 70], color=BLUE)
        line1_label = MathTex(r"x_1 + 3x_2 \leq 120").next_to(axes.c2p(50, 25), RIGHT, buff=0.05).scale(0.6)

        vertices1 = [
            axes.coords_to_point(0, 0),
            axes.coords_to_point(0, 40),
            axes.coords_to_point(50, 70/3),
            axes.coords_to_point(50, 0)
        ]
        polygon1 = Polygon(*vertices1, color=BLUE, fill_opacity=0.3)
        
        # Line 2: 2x1 + x2 = 100
        line2 = axes.plot(lambda x: 100 - 2*x, x_range=[20, 50], color=GREEN)
        line2_label = MathTex(r"2x_1 + x_2 \leq 100").next_to(axes.c2p(55, 5), UP, buff=0.05).scale(0.6)
        
        vertices2 = [
            axes.coords_to_point(0, 0),
            axes.coords_to_point(0, 40),
            axes.coords_to_point(36, 28),
            axes.coords_to_point(50, 0)
        ]
        polygon2 = Polygon(*vertices2, color=GREEN, fill_opacity=0.3)
        
        # Line 3: x2 - x1 = 20 
        line3 = axes.plot(lambda x: x + 20, x_range=[0, 30], color=YELLOW)
        line3_label = MathTex(r"x_2 - x_1 \leq 20").next_to(axes.c2p(30, 50), RIGHT, buff=0.05).scale(0.6)
        
        vertices3 = [
            axes.coords_to_point(0, 0),
            axes.coords_to_point(0, 20),
            axes.coords_to_point(15,35),
            axes.coords_to_point(36, 28),
            axes.coords_to_point(50, 0)
        ]
        polygon3 = Polygon(*vertices3, color=YELLOW, fill_opacity=0.3)
        
        # Line 4: x2 = 40
        line4 = axes.plot(lambda x: 32, x_range=[0, 60], color=PURPLE)
        line4_label = MathTex(r"x_2 \leq 32").next_to(axes.c2p(60, 32), RIGHT, buff=0.05).scale(0.6)

        vertices4 = [
            axes.coords_to_point(0, 20),
            axes.coords_to_point(12, 32),
            axes.coords_to_point(24, 32),
            axes.coords_to_point(36, 28),
            axes.coords_to_point(50, 0),   
            axes.coords_to_point(0, 0)     
        ]
        polygon4 = Polygon(*vertices4, color=PURPLE, fill_opacity=0.3)

        # Line 5: Z
        line5 = axes.plot(lambda x: 5*x / 4, x_range=[0, 70], color=WHITE)
        line5_label = MathTex("grad, c(50, 40)").next_to(axes.c2p(23, 15), UP, buff=0.05).scale(0.6).set_color(WHITE)

        perpendicular_lines = VGroup()
        for x in [0, 10, 15, 20, 25, 30, 32]:
            perp_line = axes.plot(lambda x_val, x0=x, y0=x: (-1) * (x_val - x0) + y0,
                                 color=WHITE, stroke_width=0.6)
            perpendicular_lines.add(perp_line)

        dot1 = Dot(point=axes.c2p(36, 28), color=WHITE, radius=0.1)
        dot1_label = MathTex("A (36, 28)").next_to(axes.c2p(36, 28), RIGHT, buff=0.1).scale(0.6).set_color(WHITE)

        line6 = axes.plot_line_graph(x_values = [36, 36], y_values = [0, 28], line_color=LIGHT_GREY, stroke_width=1)
        line7 = axes.plot_line_graph(x_values = [0, 36], y_values = [28, 28], line_color=LIGHT_GREY, stroke_width=1)

        
        # Отображение с верными таймерами

        self.play(Create(axes), Write(axes_labels))
        self.wait(2)

        self.play(Create(line1), Write(line1_label), run_time=2)
        self.wait(2)
        self.play(DrawBorderThenFill(polygon1), run_time=2)
        self.wait(3)

        self.play(Create(line2), Write(line2_label))
        self.wait(1)
        self.play(ReplacementTransform(polygon1, polygon2))
        self.wait(2)


        self.play(Create(line3), Write(line3_label))
        self.wait(1)
        self.play(ReplacementTransform(polygon2, polygon3))
        self.wait(1)

        self.play(Create(line4), Write(line4_label))
        self.wait(1)
        self.play(ReplacementTransform(polygon3, polygon4))
        self.wait(1)

        

        self.play(Create(line5), Write(line5_label), run_time=2)
        self.wait(1)

        
        self.play(Uncreate(VGroup(line1, line2, line3, line4, line1_label, line2_label, line3_label, line4_label)))
        self.wait(2)

        self.play(ShowIncreasingSubsets(perpendicular_lines), run_time=3)
        self.wait(1)
        self.play(FadeOut(perpendicular_lines))
        self.wait(1)
        self.play(GrowFromCenter(perpendicular_lines[-1]))
        self.wait(1)

        self.play(GrowFromCenter(dot1))
        self.wait(1)
        self.play(Indicate(dot1))
        self.wait(2)


        self.play(Create(line6))
        self.play(Create(line7))
        self.play(AddTextLetterByLetter(dot1_label))
        self.wait(8)