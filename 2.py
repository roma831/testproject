BLACK = "\033[40m"
RESET = "\033[0m"
height = 9
width = height

for y in range(height):
    line = ""
    for x in range(width):
        if x == y or x == height - 1 - y:
            line += BLACK + "  " + RESET
        else:
            line += "  "
    print(line)

