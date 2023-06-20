# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код

def polygon_color(n, point, angle, length):
    colors = {0: sd.COLOR_RED,
             1: sd.COLOR_ORANGE,
             2: sd.COLOR_YELLOW,
             3: sd.COLOR_GREEN,
             4: sd.COLOR_CYAN,
             5: sd.COLOR_BLUE,
             6: sd.COLOR_PURPLE}
    delta = (360 / n)
    print('0 : красный', '1 : оранжевый', '2 : желтый', '3 : зеленый', '4 : голубой', '5 : синий', '6 : фиолетовый', sep='\n')
    print('Пожалуйста выберите цвет')
    poly_color = int(input())

    while poly_color not in range(0, 7):
        print('Вы ввели неверное значение!')
        print('Пожалуйста выберите цвет!')
        poly_color = int(input())

    else:
        while n > 0:
            v = sd.get_vector(start_point=point, angle=angle - n * delta, length=length, width=3)
            v.draw(color=colors[poly_color])
            n -= 1
            point = v.end_point


point_1 = sd.get_point(300, 100)


polygon_color(n = 12, point=point_1, angle=0, length=100)




sd.pause()
