import os

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            if os.access(file_path, os.R_OK | os.W_OK):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"No permission to delete '{file_path}'.")
        else:
            print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_to_delete = "example.txt"  
delete_file(file_to_delete)