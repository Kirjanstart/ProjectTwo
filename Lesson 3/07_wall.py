# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
x1 = 0
x2 = 100
y1 = 0
y2 = 50
for y1 in range(0, 1201, 100):
    for x1 in range(0, 1200, 100):
        bottom = sd.get_point(x1, y1)
        top = sd.get_point(x2, y2)
        sd.rectangle(bottom, top, width=1)
        x2 += 100
    y2 += 100
y2 = 100
for y1 in range(50, 1201, 100):
    for x1 in range(-50, 1200, 100):
        bottom = sd.get_point(x1, y1)
        top = sd.get_point(x2, y2)
        sd.rectangle(bottom, top, width=1)
        x2 += 100
    y2 += 100







sd.pause()
