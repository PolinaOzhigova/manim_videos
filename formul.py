from manim import *

# Изменение цвета фона видео
config.background_color = "#2B3F57"

class formula(Scene):
    def construct(self):
        # Формула
        rec_relation = MathTex(
            r"F(u_1 = 2, u_2 = 1) = 23",
            font_size=36
        )
        
        # Отображение, таймер до конца видео - 12 секунд
        self.play(Write(rec_relation))
        self.wait(12)

