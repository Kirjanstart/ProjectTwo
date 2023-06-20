# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код

def polygon_shape(point, angle, length):
    shapes = {0: 3,
             1: 4,
             2: 5,
             3: 6,
             }

    # print('0 : красный', '1 : оранжевый', '2 : желтый', '3 : зеленый', '4 : голубой', '5 : синий', '6 : фиолетовый', sep='\n')
    # print('Пожалуйста выберите цвет')
    print('Возможные фигуры:')
    print('0 : треугольник', '1 : квадрат', '2 : пятиугольник', '3 : шестиугольник', sep='\n')
    print('Пожалуйста выберите желаемую фигуру')
    poly_shape = int(input())

    while poly_shape not in range(0, 4):
        print('Вы ввели неверное значение!')
        print('Пожалуйста выберите желаемую фигуру!')
        poly_shape = int(input())

    else:
        n = shapes[poly_shape]
        delta = (360 / n)
        while n > 0:

            v = sd.get_vector(start_point=point, angle=angle - n * delta, length=length, width=3)
            v.draw()
            n -= 1
            point = v.end_point


point_1 = sd.get_point(300, 100)


polygon_shape(point=point_1, angle=0, length=100)



sd.pause()
