subsidy = int(input("Введите размер субсидии (в тыс. рублей): "))
total_heads = int(input("Введите количество голов скота: "))
for bulls in range(subsidy // 20 + 1):
    remaining_after_bulls = subsidy - bulls * 20
    for cows in range(remaining_after_bulls // 10 + 1):
        remaining_after_cows = remaining_after_bulls - cows * 10
        calves = remaining_after_cows // 5
        if bulls + cows + calves == total_heads and bulls > 0:
            print(bulls, cows, calves)