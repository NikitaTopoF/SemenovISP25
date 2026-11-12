while True:
    a = int(input("Введите первое число: "))
    op = input("Введите операцию: ")
    if op == "x":
        print(a)
        break
    if op == "!":
        if a < 0:
            continue
        result = 1
        for i in range(1, a + 1):
            result = result * i
        print(result)
    else:
        b = int(input("Введите второе число: "))
        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            if b == 0:
                continue
            print(a // b)
        elif op == "%":
            if b == 0:
                continue
            print(a % b)