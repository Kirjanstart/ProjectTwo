# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
point = sd.get_point(400, 400)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, color=(255, 255, 255), width=3)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=3)


# point = sd.get_point(100, 100)
# bubble(point=point, step=10)


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 200)
#     bubble(point=point, step=5)


# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
# for y in range(100, 301, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5)



# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point=point, step=step)



sd.pause()

