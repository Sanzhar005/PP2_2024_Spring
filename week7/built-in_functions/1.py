import math

def multiply_list(numbers):
    result = math.prod(numbers)
    return result

numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Result:", result)