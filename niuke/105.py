def j(x):
    tmp = 1
    for i in range(1,x+1):
        tmp *= i
    return tmp
x = int(raw_input().strip())
print(j(x))