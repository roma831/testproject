import os
import time

frames = [
    "[o      ]",
    "[  o    ]",
    "[    o  ]",
    "[      o]"
]


for repeat in range(5):
    for frame in frames:
        # Возвращаем курсор на строку 3, столбец 5,
        # стираем строку и выводим новый кадр
        print('\033[H', end='', flush=True)
        print(frame)
        time.sleep(0.3)