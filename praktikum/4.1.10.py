for x in range(29):
    chislo = 2 * (x ** 2) + 29
    is_prostoye = True
    for delitel in range(2, chislo):
        if chislo % delitel == 0:
            is_prostoye = False
            break
    if is_prostoye:
        print("x =", x, "Число:", chislo)
