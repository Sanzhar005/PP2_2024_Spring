def generator(a, b):
    for i in range(a, b):
        yield i**2

a = int(input())
b = int(input())
square = generator(a, b)
for x in square:
    print(x) 