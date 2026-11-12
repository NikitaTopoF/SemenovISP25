prev = int(input("Введите цену акции: "))
buy_price = 0
sell_price = 0
bought = False
sold = False
while prev != 0:
    price = int(input("Введите цену акции: "))
    if price == 0:
        break
    if not bought:
        if price > prev:
            buy_price = prev
            bought = True
    elif not sold:
        if price < prev:
            sell_price = prev
            sold = True
    prev = price

print(buy_price, sell_price, sell_price - buy_price)