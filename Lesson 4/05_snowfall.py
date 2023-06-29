# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

snowflakes = []
N = 20
while N > 0:
    i = sd.random_number(10, 100)
    snowflakes.append(i)
    N -= 1

print(snowflakes)



# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

# point_0 = sd.get_point(sd.random_number(0,1000), sd.random_number(500, 600))

# sd.snowflake(center=point_0, length=200, factor_a=0.5)


y = sd.random_number(500, 600)
x = sd.random_number(0,1000)

y2 = sd.random_number(500, 600)
x2 = sd.random_number(0,1000)
sd.start_drawing()
for length in snowflakes:

    y = sd.random_number(500, 600)
    x = sd.random_number(0, 1000)
    while y > 10:
        # sd.clear_screen()
        delta_x = sd.random_number(-7, 7)
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length)
        # sd.sleep(0.01)
        # y -= 1
        sd.snowflake(center=point, length=length, color=sd.background_color)
        y -= 1
        if y <=10:
            sd.snowflake(center=point, length=length)
            break
        x += delta_x
        sd.finish_drawing()
        # sd.sleep(0.01)
        if sd.user_want_exit():
            break




# while True:
#     sd.clear_screen()
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=50)
#     y -= 10
#     if y < 5:
#        break
#     x = x + 10
#
#     point2 = sd.get_point(x2, y2)
#     sd.snowflake(center=point2, length=30)
#     y2 -= 10
#     if y2 < 5:
#        break
#     x2 = x2 + 20
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугроб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


