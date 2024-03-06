import os

def list_directories_files(path):
    try:
        items = os.listdir(path)
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print("Directory:", full_path)
                list_directories_files(full_path)
            else:
                print("File:", full_path)
    except Exception as e:
        print("An error occurred:", e)

path_to_explore = "/path/to/your/directory"
list_directories_files(path_to_explore)
