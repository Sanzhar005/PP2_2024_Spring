def snake_to_camel(snake_case):
    return ''.join(word.capitalize() for word in snake_case.split('_'))

snake_case_string = "this_is_a_snake_case_string"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)