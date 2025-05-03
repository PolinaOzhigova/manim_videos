from manim import *
import math

config.background_color = "#2B3F57"

class BisectionSquare2(Scene):
    def construct(self):
        def parabola(x):
            return 2 * math.sin(2*x) + x**2
        
        axes = Axes(
            x_range=[-3, 5, 1],
            y_range=[-2, 6, 1],
            axis_config={"color": WHITE}
        )
        
        parabola_graph = axes.plot(parabola, color=BLUE)
        
        a, b = -2, 4
        epsilon = 0.0005
        delta = 0.0005
        max_iter = 7

        # Фиксированные параметры высоты (вычисляем один раз)
        y_start, y_end = -5, 9
        bottom_left = axes.coords_to_point(a, y_start)  # Начальная левая граница
        top_left = axes.coords_to_point(a, y_end)
        bottom_right = axes.coords_to_point(b, y_start)
        top_right = axes.coords_to_point(b, y_end)
        l1 = Line(bottom_left, top_left, color=GREEN)
        line1_label = MathTex("a").next_to(axes.c2p(-2.5, 3), RIGHT, buff=0.05).scale(1)
        l2 = Line(bottom_right, top_right, color=GREEN)
        line2_label = MathTex("b").next_to(axes.c2p(4.5, 3), LEFT, buff=0.05).scale(1)
        fixed_height = top_left[1] - bottom_left[1]     # Фиксированная высота
        center_y = (bottom_left[1] + top_left[1]) / 2   # Фиксированная Y-координата центра

        # Создаем прямоугольник с изначальной шириной
        initial_width = axes.coords_to_point(b, y_start)[0] - bottom_left[0]
        rect = Rectangle(
            width=initial_width,
            height=fixed_height,
            color=GREEN, 
            fill_opacity=0.2
        ).move_to([(bottom_left[0] + axes.coords_to_point(b, y_start)[0])/2, center_y, 0])

        self.play(Create(parabola_graph), Create(axes))
        self.play(Create(l1), Write(line1_label))
        self.play(Create(l2), Write(line2_label))
        self.play(Create(rect))
        self.play(Uncreate(VGroup(l1, l2)))
        self.wait(1)
        self.play(Unwrite(VGroup(line1_label, line2_label)))
        
        for i in range(max_iter):
            mid = (a + b) / 2
            x1 = mid - delta
            x2 = mid + delta
            
            f1 = parabola(x1)
            f2 = parabola(x2)

            dot1 = Dot(axes.coords_to_point(x1-0.1, parabola(x1-0.1) ), color=ORANGE )
            dot2 = Dot(axes.coords_to_point(x2+0.1, parabola(x1+0.1) ), color=PINK )

            if i < 3:
                self.play(Create(VGroup(dot1, dot2)))
                self.wait(2)
                if i == 0:
                    self.wait(10)

            if f1 < f2:
                b = x2
            else:
                a = x1
            
            # Новая ширина и X-координата центра
            new_left = axes.coords_to_point(a+0.1, y_start)[0]
            new_right = axes.coords_to_point(b-0.1, y_start)[0]
            if i >= 3:
                new_left = axes.coords_to_point(a, y_start)[0]
                new_right = axes.coords_to_point(b, y_start)[0]
            new_width = new_right - new_left
            new_center_x = (new_left + new_right)/2

            # Анимируем ТОЛЬКО ширину и позицию по X
            self.play(
                rect.animate.stretch_to_fit_width(new_width).move_to([new_center_x, center_y, 0]),
                run_time=0.5
            )
            self.wait(1)

            if i < 3:
                self.play(Uncreate(VGroup(dot1, dot2)))
                self.wait(2)
            
            if abs(b - a) < epsilon:
                break
        
        vertex_dot = Dot(axes.c2p((a+b)/2, parabola((a+b)/2)), color=GREEN)
        self.play(FadeOut(rect), FadeIn(vertex_dot))
        self.play(Indicate(vertex_dot))
        self.wait(3)