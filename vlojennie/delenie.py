a = int(input("Колонки"))
b = int(input("Строки"))
for r in range(1, b + 1):
    for c in range(1, a + 1):
        print(c / r, end=" ")
    print()
