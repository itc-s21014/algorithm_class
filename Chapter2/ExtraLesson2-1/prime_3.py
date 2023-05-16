p = [True]*82
p[0] = False
p[1] = False
n = 2

def hyou():
    s = ""
    for i in range(82):
        if p[i] == True:
            s += "{:2d}, ".format(i)
        else:
            s += "/, "
        if i%10 == 9:
            s += "\n"
    print(s)

def furui():
    global n
    for i in range(n+n, 82, n):
        p[i] = False
    print(n, "の倍数を篩い落としました")
    hyou()
    while n<82:
        n = n + 1
        if p[n] == True:
            break

hyou()
while n<9:
    input("Enterキーを押してください")
    furui()