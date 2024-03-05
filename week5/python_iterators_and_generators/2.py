n = int(input())
a = (i%2 == 0 for i in range(0, n + 1))
x = 0
b = 0
while x <= n:
    if next(a) == True:
        print(b)
        b = b + 2

    x = x + 1