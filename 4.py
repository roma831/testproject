file = open('sequence.txt', 'r')
chet = 0
nechet = 0
count = 0
blue = "\u001b[44m"
red = "\u001b[41m"
reset = "\u001b[0m"

for line in file:
    count += 1
    if count % 2 == 0:
        chet += abs(float(line))
    else:
        nechet += abs(float(line))

file.close()

print(f'{blue}{' ' * int(chet // 10)}{reset} {((chet / (chet + nechet)) * 100):.2f}%')
print(f'{red}{' ' * int(nechet // 10)}{reset} {((nechet / (chet + nechet)) * 100):.2f}%')
