n = int(input("n"))
o = 1
g = 1
while o <= n:
    for i in range(g):
        if o>n:
            break
        print(o, end=" ")
        o+=1
    print()
    g+=1