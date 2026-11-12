side = float(input("Введите сторону квадрата: "))
speed = float(input("Введите скорость жука: "))
turns = 0
while True:
    if side <= speed or abs(side - speed) <= 0.01:
        break
    side = side * (2 ** 0.5) / 2
    turns = turns + 1
    if abs(side - speed) <= 0.01:
        turns = turns + 1
print(turns)