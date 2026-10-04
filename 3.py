import time

frames = [
    "[o      ]",
    "[  o    ]",
    "[    o  ]",
    "[      o]"
]

for i in range(5):
    for frame in frames:
        print("\033[1;1H")
        print(frame)
        time.sleep(0.3)

