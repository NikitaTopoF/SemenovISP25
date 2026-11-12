for a in range(1, 10000):
    sum_a = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a = sum_a + i
    b = sum_a
    sum_b = 0
    for i in range(1, b):
        if b % i == 0:
            sum_b = sum_b + i
    if sum_b == a and a < b:
        print(a, b)