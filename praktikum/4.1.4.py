import math
k = float(input("Длина палки: "))
h = float(input("Шаг: "))
y = 2
while y <= 3:
    cos_a = y / k
    rad = math.acos(cos_a)
    gradus = round(math.degrees(rad), 1) 
    print("При y =", y, "угол =", gradus)
    y = y + h
