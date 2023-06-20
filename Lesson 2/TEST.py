# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100



# sd.snowflake(center=point_0, length=200, factor_a=0.5, factor_b=0.1)
y = 500
x = 100

x2 = 150
y2 = 450
while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=50)
    y -= 10
    if y<50:
        break
    x = x * 1.05


    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=50)
    y2 -= 10
    if y<50:
        break
    x2 = x2 * 1.05
    sd.sleep(0.1)
    if sd.user_want_exit():
        break






sd.pause()