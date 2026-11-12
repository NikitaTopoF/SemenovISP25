n = int(input("Аппараты"))
for i in range(1, n + 1):
    seconds = i - 1
    while seconds >= 0:
        print(f"Осталось секунд: {seconds}")
        seconds -= 1
    print(f"Пуск {i}")
