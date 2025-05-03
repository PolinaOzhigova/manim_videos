from manim import *
import math

config.background_color = "#2B3F57"

class GoldenSectionSearch(Scene):
    def construct(self):
        def parabola(x):
            return 2 * math.sin(2*x) + x**2
        
        axes = Axes(
            x_range=[-3, 5, 1],
            y_range=[-2, 6, 1],
            axis_config={"color": WHITE}
        )
        
        parabola_graph = axes.plot(parabola, color=BLUE)
        
        l, r = -2, 4
        epsilon = 0.0005
        max_iter = 10
        resphi = 0.618
        
        # Параметры для визуализации
        y_start, y_end = -5, 9
        bottom_left = axes.c2p(l, y_start)
        top_left = axes.c2p(l, y_end)
        fixed_height = top_left[1] - bottom_left[1]
        center_y = (bottom_left[1] + top_left[1]) / 2
        
        bottom_right = axes.coords_to_point(r, y_start)
        top_right = axes.coords_to_point(r, y_end)
        l1 = Line(bottom_left, top_left, color=GREEN)
        line1_label = MathTex("a").next_to(axes.c2p(-2.5, 3), RIGHT, buff=0.05).scale(1)
        l2 = Line(bottom_right, top_right, color=GREEN)
        line2_label = MathTex("b").next_to(axes.c2p(4.5, 3), LEFT, buff=0.05).scale(1)
        
        # Создаем прямоугольник
        initial_width = axes.c2p(r, y_start)[0] - bottom_left[0]
        rect = Rectangle(
            width=initial_width,
            height=fixed_height,
            color=GREEN,
            fill_opacity=0.2
        ).move_to([(bottom_left[0] + axes.c2p(r, y_start)[0])/2, center_y, 0])
        
        
        self.play(Create(parabola_graph), Create(axes))
        self.play(Create(l1), Write(line1_label))
        self.play(Create(l2), Write(line2_label))
        self.play(Create(rect))
        self.play(Uncreate(VGroup(l1, l2)))
        self.wait(1)
        self.play(Unwrite(VGroup(line1_label, line2_label)))
        
        
        x1 = l + (1 - resphi) * (r - l)
        x2 = l +  resphi * (r - l)
        f1 = parabola(x1)
        f2 = parabola(x2)

        x1_d = Dot(axes.c2p(x1, f1), color=YELLOW )
        x2_d = Dot(axes.c2p(x2, f2), color=YELLOW )

        ld1 = MathTex("x1").next_to(x1_d, RIGHT, buff=0.05).scale(0.6)
        ld2 = MathTex("x2").next_to(x2_d, UP, buff=0.05).scale(0.6)

        self.play(Create(VGroup(x1_d, x2_d)))
        self.play(Write(VGroup(ld1, ld2)))
        self.wait(5)

        self.play(Unwrite(VGroup(ld1, ld2)))
        ld2 = MathTex("x2").next_to(x1_d, RIGHT, buff=0.05).scale(0.6)
        self.play(Write(VGroup(ld2)))
        self.wait(2)
        self.play(Unwrite(VGroup(ld2)))

        dot_left = False
        delete = 0

        # Логика золотого сечения
        for i in range(max_iter):

            if f1 < f2:
                r = x2

                x2 = x1
                f2 = f1

                x1 = l + (1 - resphi) * (r - l)
                f1 = parabola(x1)

                delete = x2_d
                x2_d = x1_d
                x1_d = Dot(axes.c2p(x1, f1), color=YELLOW )

                dot_left = True

            else:
                l = x1

                x1 = x2
                f1 = f2

                x2 = l + resphi * (r - l)
                f2 = parabola(x2)

                delete = x1_d
                x1_d = x2_d
                x2_d = Dot(axes.c2p(x2, f2), color=YELLOW )

                dot_left = False
            
            # Новые координаты для визуализации
            new_left = axes.c2p(l, y_start)[0]
            new_right = axes.c2p(r, y_start)[0]
            new_width = new_right - new_left
            new_center_x = (new_left + new_right) / 2
            
            # Анимация изменений
            self.play(
                rect.animate.stretch_to_fit_width(new_width).move_to([new_center_x, center_y, 0]),
                run_time=0.5
            )
            self.wait(1)

            if i < 3:
                if dot_left:
                    self.play(Uncreate(delete))
                    self.wait(1)
                    self.play(Create(x1_d))
                else:
                    self.play(Uncreate(delete))
                    self.wait(1)
                    self.play(Create(x2_d))
            
            if i == 3:
                self.play(Uncreate(VGroup(delete, x2_d)))
        
            
            if abs(r - l) < epsilon:
                break
        
        # Отображение результата
        vertex_dot = Dot(axes.c2p((l + r)/2, parabola((l + r)/2)), color=GREEN, radius=0.1)
        self.play(FadeOut(rect), FadeOut(x1_d), FadeOut(x2_d), FadeIn(vertex_dot))
        self.play(Indicate(vertex_dot))
        self.wait(2)