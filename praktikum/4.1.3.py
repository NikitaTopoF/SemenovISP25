n = int(input("Введите количество часов:"))
ameb = 1
for i in range(1, n + 1, 3):
    ameb *= 2
print(f"Количество амеб через n часов:", ameb)    
