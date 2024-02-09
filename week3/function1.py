#task1
def convert_grams_to_ounces(grams):
    return 28.3495231 * grams

grams = int(input('Enter grams: '))
print(convert_grams_to_ounces(grams))


#task2
def centigrade_temperature(F):
    F -= 32
    return (5 / 9) * F
    
F = float(input('Enter Fahrenheit temperature: '))
print(f'Centigrade temperature: {centigrade_temperature(F)}')


#task3
def solve(numheads, numlegs):
    a = numheads * 2
    rabbits = numlegs - a
    rabbits /= 2
    chickens = numheads - rabbits
    print(f'chickens: {chickens}\nrabbits: {rabbits}')

legs = int(input('Enter legs: '))
heads = int(input('Enter heads: '))
solve(heads, legs)


#task4
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = [int(x) for x in input("Enter numbers:").split()]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)


#task5
from itertools import permutations
def print_permutations(input_string):
    perms = permutations(input_string)
    for perm in perms:
        print(''.join(perm))

user_input = input("Enter string: ")
print("All string permutations:")
print_permutations(user_input)


#task6
def reverse_sentence(input_string):
    words = input_string.split()    
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

user_input = input("Enter sentence: ")
reversed_sentence = reverse_sentence(user_input)
print("Sentence with inverted words", reversed_sentence)


#task7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
        
print(has_33([1, 3, 3]))     
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3]))     
