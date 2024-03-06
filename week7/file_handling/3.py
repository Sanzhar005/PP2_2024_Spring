import os

def check_path_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    
    if not os.access(path, os.R_OK):
        print(f"The path '{path}' is not readable.")
    else:
        print(f"The path '{path}' is readable.")
    
    if not os.access(path, os.W_OK):
        print(f"The path '{path}' is not writable.")
    else:
        print(f"The path '{path}' is writable.")
    
    if not os.access(path, os.X_OK):
        print(f"The path '{path}' is not executable.")
    else:
        print(f"The path '{path}' is executable.")

path_to_check = "C:/Users/Username/Documents"
check_path_access(path_to_check)