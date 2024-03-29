# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код



def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()



def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw()

def pentagram(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    v5.draw()

def hexagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 30, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 60, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 90, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 120, length=length, width=3)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 150, length=length, width=3)
    v6.draw()

    v7 = sd.get_vector(start_point=v6.end_point, angle=angle + 180, length=length, width=3)
    v7.draw()

    v8 = sd.get_vector(start_point=v7.end_point, angle=angle + 210, length=length, width=3)
    v8.draw()

    v9 = sd.get_vector(start_point=v8.end_point, angle=angle + 240, length=length, width=3)
    v9.draw()

    v10 = sd.get_vector(start_point=v9.end_point, angle=angle + 270, length=length, width=3)
    v10.draw()

    v11 = sd.get_vector(start_point=v10.end_point, angle=angle + 300, length=length, width=3)
    v11.draw()

    v12 = sd.get_vector(start_point=v11.end_point, angle=angle + 330, length=length, width=3)
    v12.draw()

def polygon(n, point, angle, length):
    delta = (360 / n)
    # sumangle = (n-2) * 180
    # delta = sumangle//n
    while n > 0:
        v = sd.get_vector(start_point=point, angle=angle - n * delta, length=length, width=3)
        v.draw()
        n -= 1
        point = v.end_point




point_1 = sd.get_point(300, 100)


# triangle(point=point_1, angle=0, length=300)
# square(point=point_1, angle=0, length=300)
# pentagram(point=point_1, angle=0, length=300)
# hexagon(point=point_1, angle=0, length=100)
polygon(n = 12, point=point_1, angle=0, length=100)
# for i in range(1, 60):
#     polygon(n = i, point=point_1, angle=0, length=100)





# Часть 1-бис.
# Попробуйте прикинуть объем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы, чтобы внести изменения в код? Выгода на лицо. :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
