import os

from generator import generator

cwd = os.getcwd()

root, folders, files = next(os.walk(cwd))

def generate_all_files(files=files):
    for file in files:
        if file[-1:-5:-1] == "txt.":
            generator(file)


generate_all_files()
