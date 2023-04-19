# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile(coordinate_x, coordinate_y, color):
    point = sd.get_point(coordinate_x, coordinate_y)
    left_coordinate_x = coordinate_x - 20
    left_coordinate_y = coordinate_y + 15
    right_coordinate_x = coordinate_x + 20
    right_coordinate_y = coordinate_y + 15
    right_point = sd.get_point(right_coordinate_x, right_coordinate_y)
    left_point = sd.get_point(left_coordinate_x, left_coordinate_y)
    mouth_coordinate_x = coordinate_x
    mouth_coordinate_y = coordinate_y - 20
    mouth_point = sd.get_point(mouth_coordinate_x, mouth_coordinate_y)
    sd.circle(center_position=mouth_point, radius=15, color=color, width=3)
    sd.circle(center_position=right_point, radius=5,color=color, width=3)
    sd.circle(center_position=left_point, radius=5,color=color, width=3)
    sd.circle(center_position=point, radius=50,color=color, width=3)

smile(50, 50, sd.COLOR_DARK_ORANGE)




sd.pause()
