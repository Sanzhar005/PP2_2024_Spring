def write_list_to_file(filename, my_list):
    try:
        with open(filename, 'w') as file:
            for item in my_list:
                file.write(str(item) + '\n')
        print(f"List has been written to '{filename}' successfully.")
    except IOError:
        print(f"Error writing to file '{filename}'.")

my_list = ['apple', 'banana', 'orange', 'grape']
filename = "output.txt"  
write_list_to_file(filename, my_list)