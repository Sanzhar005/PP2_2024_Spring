def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            contents = source.read()
            destination.write(contents)
        print("File copied successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = "source.txt"  
destination_file = "destination.txt"  
copy_file(source_file, destination_file)