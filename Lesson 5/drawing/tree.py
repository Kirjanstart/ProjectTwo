# -*- coding: utf-8 -*-

import simple_draw as sd

# sd.resolution = (1200, 600)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код


def branch(point, angle, length):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()
    v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v2.draw()
    next_point_1 = v1.end_point
    next_point_2 = v2.end_point
    div_angle_1 = sd.random_number(-40, 40) / 100
    div_angle_2 = sd.random_number(-40, 40) / 100
    div_length = sd.random_number(-20, 20) / 100
    next_angle_1 = angle - 30 - (30 * div_angle_1)
    next_angle_2 = angle + 30 + (30 * div_angle_2)
    next_length_1 = length * (0.75 + div_length * 0.75)
    branch(point=next_point_1, angle=next_angle_1, length=next_length_1)
    branch(point=next_point_2, angle=next_angle_2, length=next_length_1)

# point_0 = sd.get_point(300, -100)

# branch(point=point_0, angle=90, length=150)


# for delta in range(0, 51, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)







# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()




