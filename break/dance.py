n = int(input("Введите запас терпения учителя: "))
index = 1
correct = 0
mistakes = 0
while mistakes < n:
    word = input("Введите отсчёт: ")
    if (index == 1 and word == "раз") or (index == 2 and word == "два") or (index == 3 and word == "три") or (index == 4 and word == "четыре"):
        correct = correct + 1
        index = index + 1
        if index == 5:
            index = 1
    else:
        mistakes = mistakes + 1
        if mistakes < n:
            print("Правильных отсчётов было", correct, "но теперь вы ошиблись.")
            correct = 0
            index = 1
        else:
            print("На сегодня хватит.")