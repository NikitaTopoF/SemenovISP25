x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))
x1 = 0
y1 = 0
moves = 0
while True:
    direction = input("Введите направление: ")
    if direction == "стоп":
        break
    steps = int(input("Введите количество шагов: "))
    if direction == "север":
        y1 = y1 + steps
    elif direction == "юг":
        y1 = y1 - steps
    elif direction == "восток":
        x1 = x1 + steps
    elif direction == "запад":
        x1 = x1 - steps
    moves = moves + 1
    if x == x1 and y == y1:
        moves1 = moves
print(moves1)