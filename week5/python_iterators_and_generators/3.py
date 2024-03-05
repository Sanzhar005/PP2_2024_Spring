def generator(n):
    for i in range(n):
        if i%4 == 0 and i%3 == 0:
            yield i

n = int(input())
divisible = generator(n)
for x in divisible:
    print(x)