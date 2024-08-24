import os

def list_files(directory):
    files = os.listdir(directory)
    print("Files in", directory, ":")
    for file in files:
        print(file)

list_files("/path/to/directory")
