n = int(input("Введите число N: "))
for c in range(1, n + 1):
    for a in range(1, c):
        for b in range(a + 1, c):
            if a * a + b * b == c * c:
                d = 2
                podhodit = True
                while d <= a:
                    if a % d == 0 and b % d == 0 and c % d == 0:
                        podhodit = False
                        break
                    d = d + 1
                if podhodit == True:
                    print(a, b, c)