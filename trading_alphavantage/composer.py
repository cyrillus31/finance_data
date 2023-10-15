import os

def find_csv_files_in_current_dir() -> dict:
    result = {}
    root, dirs, files = next(os.walk(os.getcwd()))
    files.sort()
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension != ".csv":
            continue
        try:
            ticker, date = filename.split("_")
        except ValueError:
            continue
        if ticker not in result:
            result[ticker] = [(file, date)]
        else:
            result[ticker].append((file, date))

    return result



def main():
    print("Убедитесь, что в папке, откуда запускается программа, лежает csv файл с именами следующего вида: 'тикер_год-месяц.csv'")
    input("И нажмите 'Enter'\n")

    csv_files = find_csv_files_in_current_dir()
    
    for ticker in csv_files:
        files = csv_files[ticker]
        start_date = files[0][1]
        end_date = files[-1][1]
        composed_file_name = f"{ticker}_{start_date}_-_{end_date}.csv"
        with open(composed_file_name, "a") as compound_file:
            for file_tuple in files:
                file, date = file_tuple
                with open(file, "r") as sub_file:
                    compound_file.write(sub_file.read())
        print(f"Файл, содержащий данные по тикеру {ticker} c {start_date} по {end_date}, был создан:")
        print(composed_file_name, "\n")

    input("Все данные по предоставленным тикерам были собраны в соответствующие файлы. Нажмите 'Enter'")

if __name__ == "__main__":
    main()















# print(csv_files)


        


