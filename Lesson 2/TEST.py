# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

snowflakes = []
n = 20
while n > 0:
    i = sd.random_number(10, 100)
    snowflakes.append(i)
    n -= 1
print(snowflakes)