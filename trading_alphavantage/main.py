import time
import requests
import io
from datetime import datetime

from api_key import api_key

intervals =  {
   1: "1min",
   5: "5min",
   15: "15min",
   30: "30min",
   60: "60min",
   }

symbol = None
interval = "1min" 
month = None
outputsize = None
extended_hours = "true"

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&adjusted={}&symbol={}&interval={}&month={}&outputsize=full&extended_hours={}&apikey={}&datatype=csv"

def row_reformat(row: str) -> str:
    date_and_time, rest = row.split(",", maxsplit=1)
    dt = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S")
    new_string = dt.strftime("%#d/%#m/%Y,%#H:%M")
    return (new_string + "," + rest.strip() + "\n")

# row_example = "2023-09-29 01:16:00,172.2300,172.3050,172.2300,172.2350,45487"
# test = row_reformat(row_example)
# print(test)
# exit()

def generate_params() -> dict:
    symbols = input("Напишите интересующие вас биржевые тикеры, разделяя их пробелами: ").split()

    while True:
        year_start, month_start = map(int, input("Укажите год и месяц, начиная с которого вы хотели бы получить данные (в формате 2023-09): ").split("-"))
        year_end, month_end = map(int, input("Укажите последний год и мясяц, зканчивая которым вы хотели бы получить данные (в формате 2023-12): ").split("-"))
        if year_start <= year_end:
            break
        if year_start == year_end and month_start == month_end:
            break
        else:
            print("Вы неправильно указали даты. Попробуйте еще раз...\n")

    total_months = ((int(year_end) - int(year_start)) * 12 + (int(month_end) - int(month_start))) + 1
    print(total_months)
    months = []
    for _ in range(total_months):
        while year_start <= year_end:
            if month_start > month_end and year_start == year_end:
                break
            m = f"{year_start}-{str(month_start).zfill(2)}"
            months.append(m)
            month_start += 1
            if month_start > 12:
                year_start += 1
                month_start = 1
        
    params = {
            "months": months,
            "interval": interval,
            "symbols": symbols,
            "adjusted": "false",
            }

    print(params)
    return params




def send_requests(params):
    count = 0
    adjusted = params["adjusted"]
    for symbol in params["symbols"]:
        for month in params["months"]:
            count += 1
            # print(symbol, params["interval"], month, api_key)
            fails = 0
            while True:
                if fails >= 3:
                    print("Было произведено 3 неудачные попытки скачать данные. Скорее всего у вас закончилось количество запросов на сегодня.")
                    print("Работа программы будет завершена.")
                    time.sleep(2)
                    exit()
                r = requests.get(url.format(adjusted, symbol, params["interval"], month, extended_hours, api_key))
                try:
                    note = r.json()["Note"]

                except:
                   break 

                else:
                    fails += 1
                    print(note)
                    print("В связи с ограничением на количество запросов по вашему API ключу программа подождет 60 секунд и попробует продолжить работу.")
                    time.sleep(30)
                    print("30 секунд осталось до возобновления работы программы.")
                    time.sleep(31)



            filename = f"{symbol.upper()}_{month}.csv"
            csv_file = [line for line in io.StringIO(r.content.decode("utf-8"))][:1:-1]
            # csv_file = r.content.decode("utf-8")
            # csv_reader = csv.reader(csv_file)
                
            with open(filename, "w+") as file:
                for line in csv_file:
                    file.write(row_reformat(line))
                    
                print(f'Файл{filename} создан. {count} из {len(params["symbols"]) * len(params["months"])}')

if __name__ == "__main__":
    params = generate_params()
    send_requests(params)
    print("Работа программы завершена")
    time.sleep(2)



