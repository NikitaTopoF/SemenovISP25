n = int(input("Число"))
total_sum = 0
for i in range(1, n + 1):
    power = 0
    for j in range(1, i + 1):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            power += j
    total_sum += i ** power
print(total_sum)
