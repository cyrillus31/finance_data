import csv
from utils import convert_date_time, float_format

import logging
logging.basicConfig(level=logging.DEBUG)


with open("aapl.us.txt", "r", encoding="UTF-8") as input:
    fieldnames = ["ticker", "per", "date", "time", "open", "high", "low", "close", "vol", "openint"]
    reader = csv.DictReader(input, fieldnames=fieldnames)


    # create a new file
    with open("new.csv", "w", encoding="UTF-8") as output:
        writer = csv.writer(output)
        next(reader) #bypass the headers here
        for row in reader:
            date, time = row["date"], row["time"]

            # converting time from CET to US/Eastern
            date, time = convert_date_time(date, time)
            row_data = [date, time]
            row_data.extend(list(map(float_format, [row["open"], row["high"], row["low"], row["close"]])))
            writer.writerow(row_data)

