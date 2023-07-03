# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код

from room_1 import folks as f_1
from room_2 import folks as f_2
print('В комнате room_1 живут:', *f_1)
print('В комнате room_2 живут:', *f_2)
