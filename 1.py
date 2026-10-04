width = 30
height = 4

white = "\u001b[47m"
blue = "\u001b[44m"
red = "\u001b[41m"
reset = "\u001b[0m"

for i in range(height):
    print(red + " " * width + reset)

for i in range(height):
    print(white + " " * width + reset)

for i in range(height):
    print(blue + " " * width + reset)
