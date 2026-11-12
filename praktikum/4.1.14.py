A = float(input("Стипендия A: "))
B = float(input("Расходы B: "))
nuzhno = 0
for mesyac in range(10):
    deficit = B - A
    nuzhno = nuzhno + deficit
    B = B * 1.03

print("Нужно попросить:", nuzhno)
