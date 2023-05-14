import csv
import datetime
import pytz


utc = pytz.utc
print(utc)
# print(pytz.all_timezones)
warsawtz = pytz.timezone("Europe/Warsaw")
print(warsawtz)

def convert_date_time(date: str, time: str) -> tuple[str]:
    # date format: 20230131 -> 31/01/2023
    # time format: 153000 -> 15:30 +5 minutes + convert the timezone from Warsaw to NYC (from UTC+2 to UTC-4)
    # first parse the results
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])

    hours = int(time[:2])
    minutes = int(time[2:4])

    warsaw = datetime.datetime(year, month, day, hours, minutes, 0, warsawtz) 
    print(warsaw)


with open("aapl.us.txt", "r", encoding="UTF-8") as input:
    fieldnames = ["ticker", "per", "date", "time", "open", "high", "low", "close", "vol", "openint"]
    reader = csv.reader(input)
    # reader = csv.DictReader(input, fieldnames=fieldnames)
    next(reader) #bypass the headers here
    date, time = next(reader)[2:4]
    print(date, time)
    convert_date_time(date, time)

