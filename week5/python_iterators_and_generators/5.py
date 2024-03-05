def generator(n):
    while 0 <= n:
        yield n
        n = n - 1

n = int(input())
reverse = generator(n)
for x in reverse:
    print(x)