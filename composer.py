import os
import csv
import time

from generator import generator

cwd = os.getcwd()

root, folders, files = next(os.walk(cwd))

def generate_all_files(files=files):
    for file in files:
        if file[-1:-5:-1] == "txt.":
            generator(file)

def generate_compound_file():
    root, folders, files = next(os.walk(os.path.join(cwd, "results")))
    temp_hash = set() 

    with open(os.path.join("results","compound.csv"), "w", encoding="UTF-8") as file:
        writer = csv.writer(file)
        files.sort()
        for file in files:
            if file == "compound.csv":
                pass

            with open(os.path.join(root, file), "r", encoding="UTF-8") as input:
                reader = csv.reader(input)
                for row in reader:
                    if ''.join(row) in temp_hash:
                        continue
                    temp_hash.add(''.join(row))
                    writer.writerow(row)


if __name__ == "__main__":
    input("""В папку с программой положите txt файлы которыe хотите отформатировать.
Когда будете готовы нажмите Enter\n""")
    generate_all_files()
    answer = input("""В папке с программой была создана папка results. 
Файлы были переформатированы и помещены в папку results.
Хотите их объединить? y/n:  """)
    if answer.lower()[0] == "y":
        generate_compound_file()
        input("\nФайлы объеденены в файл compound.csv, который находится в папке results")
        print("Работа программы будет прекращена")
        time.sleep(2)
        exit()
    else:
        print("\nРабота программы будет прекращена")
        time.sleep(2)
        exit()


                

