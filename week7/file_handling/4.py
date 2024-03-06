def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1

filename = "example.txt"  
num_lines = count_lines(filename)
if num_lines != -1:
    print(f"The file '{filename}' contains {num_lines} lines.")