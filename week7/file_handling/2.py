import os

def check_path_access(path):
    if not os.path.exists(path):
        print(f"The path {path} does not exist.")
        return

    if not os.access(path, os.R_OK):
        print(f"No read access to the path {path}.")
    else:
        print(f"Read access to the path {path} is available.")

    if not os.access(path, os.W_OK):
        print(f"No write access to the path {path}.")
    else:
        print(f"Write access to the path {path} is available.")

    if os.path.isdir(path):
        if not os.access(path, os.X_OK):
            print(f"No execute access to the path {path}.")
        else:
            print(f"Execute access to the path {path} is available.")
    else:
        print(f"{path} is not a directory.")

path_to_check = input("Enter the path to check access: ")
check_path_access(path_to_check)
