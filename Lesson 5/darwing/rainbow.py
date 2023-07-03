# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
sd.resolution = (1200, 600)
x = 50
y = 350
for color in rainbow_colors:
    st_point = sd.get_point(x, 50)
    fn_point = sd.get_point(y, 450)
    x+=5
    y+=5
    sd.line(st_point, fn_point, color=color,  width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
radius = 300
for color in rainbow_colors:
    point = sd.get_point(600, 0)
    radius -= 20
    sd.circle(point, radius, color=color, width=20)

sd.pause()
