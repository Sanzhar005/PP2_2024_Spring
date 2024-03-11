def square_numbers(a):
    for x in range(1, a):
        yield x ** 2

a = int(input())
num = square_numbers(a)
i = 0
while i < a:
    print(next(num))
    i += 1  