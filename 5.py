RESET = '\u001b[0m'
BLUE = '\u001b[44m'
x_max = 10
y_max = x_max

lines = []
for y in range(y_max, -1, -1):
    line = ""
    for x in range(x_max + 1):
        if x == y:
            line += f'{BLUE} {RESET}'
        else:
            line += " "
    lines.append(line)

print("\n".join(lines))