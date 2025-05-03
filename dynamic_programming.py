from manim import *

config.background_color = "#2B3F57"

class DynamicProgramming(Scene):
    def construct(self):
        # Формула целевой функции
        target_func = MathTex(
            r"F(u_1, \ldots, u_n) = \sum_{j=1}^n c_j u_j \to \max",
            font_size=36
        )
        self.play(Write(target_func))
        self.wait(12)
        self.play(FadeOut(target_func))

        # Формула ограничения
        constraint = MathTex(
            r"\sum_{j=1}^n a_j u_j \leq b",
            font_size=36
        )
        self.play(Write(constraint))
        self.wait(11)
        self.play(FadeOut(constraint))

        # Уравнение состояния
        state_eq = MathTex(
            r"x_{j+1} = x_j - a_j u_j,\quad j = 1, 2, \ldots, n",
            font_size=36
        )
        initial_cond = MathTex(
            r"x_1 = b",
            font_size=36
        )
        initial_cond.next_to(state_eq, DOWN, buff=0.5)
        
        self.play(Write(state_eq))
        self.play(Write(initial_cond))
        self.wait(30)
        self.play(FadeOut(state_eq), FadeOut(initial_cond))

        # Ограничения на управление
        control_limits = MathTex(
            r"u_j \geq 0,\quad a_j u_j \leq x_j",
            font_size=36
        )
        self.play(Write(control_limits))
        self.wait(5)
        self.play(FadeOut(control_limits))

        # Рекуррентные соотношения (позиционируем выше центра)
        rec_relation = MathTex(
            r"f_j(x) = \max_{u_j} \{c_j u_j + f_{j-1}(x - a_j u_j)\}",
            font_size=36
        ).shift(UP*1.5)  # Сдвигаем вверх на 0.5 единицы
        
        rec_range = MathTex(
            r"j = n, n-1, \ldots, 1",
            font_size=36
        ).next_to(rec_relation, DOWN, buff=0.5)
        
        self.play(Write(rec_relation))
        self.play(Write(rec_range))
        self.wait(2)

        # Условия для u_j
        u_conditions = MathTex(
            r"u_j = 0, 1, 2, \ldots, \left\lfloor\frac{x}{a_j}\right\rfloor",
            font_size=36
        ).next_to(rec_range, DOWN, buff=0.5)
        self.play(Write(u_conditions))
        self.wait(2)

        # Формула для последнего этапа
        final_step = MathTex(
            r"f_n(x) = \max c_n u_n,\quad a_n u_n \leq x",
            font_size=36
        ).next_to(u_conditions, DOWN, buff=0.5)
        self.play(Write(final_step))
        self.wait(55)
        self.play(*[FadeOut(mob) for mob in self.mobjects])