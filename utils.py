import datetime
import pytz


utc = pytz.utc
warsawtz = pytz.timezone("CET")
nytz = pytz.timezone("US/Eastern")

# formats strings and floats into strings with 4 digits after the decimal dot
def float_format(number: str) -> str:
    return "{:.4f}".format(float(number))

def convert_date_time(date: str, time: str) -> tuple[str]:
    # date format: 20230131 -> 31/01/2023
    # time format: 153000 -> 15:30 +5 minutes 

    # first parse the arguments
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])

    hours = int(time[:2])
    minutes = int(time[2:4])

    warsaw = datetime.datetime(year, month, day, hours, minutes, 0, tzinfo=warsawtz) + datetime.timedelta(minutes=5)
    ny = warsaw.astimezone(nytz)
    # print(ny.time())
    # print(datetime.time(9, 36))
    if ny.time() < datetime.time(9, 35):
        raise Exception("Starting time goes below 9:35am")
    return ny.strftime("%#d%#m%Y"), ny.strftime("%#H:%M")