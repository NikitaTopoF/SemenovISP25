a = int(input("nach"))
b = int(input("koch"))
f = int(input("shag"))
for i in range(a, b + 1, f):
    for j in range(a, b + 1, f):
        print(i, "+", j, "=", i + j, end = "\t")
    print()    