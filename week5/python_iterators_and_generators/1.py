a = int(input())
num = (x**2 for x in range(1,a))
i = 0
while i < a:
    print(next(num))
    i+1