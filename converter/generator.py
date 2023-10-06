import csv
import os
from utils import convert_date_time, float_format

import logging
logging.basicConfig(level=logging.DEBUG)





def generator(input_name: str, output_name: str = "new"):
    if not os.path.exists("results/"):
        os.mkdir("results")

    with open(input_name, "r", encoding="UTF-8") as input:
        fieldnames = ["ticker", "per", "date", "time", "open", "high", "low", "close", "vol", "openint"]
        reader = csv.DictReader(input, fieldnames=fieldnames)


        # create a new file
        with open("results/"+output_name, "w", encoding="UTF-8") as output:
            writer = csv.writer(output)
            next(reader) #bypass the headers here
            for index, row in enumerate(reader):
                date, time = row["date"], row["time"]

                # converting time from CET to US/Eastern
                date, time = convert_date_time(date, time)

                # get the first date in the file
                if index == 0:
                    date = ":".join([p.zfill(2) for p in date.split("/")[::-1]])
                    start = "_".join([date, time])
                    title = row["ticker"]
                    new_output_name = f"{title}.csv"

                row_data = [date, time]
                row_data.extend(list(map(float_format, [row["open"], row["high"], row["low"], row["close"]])))
                writer.writerow(row_data)

        # get the last date in the file
        date = ":".join([p.zfill(2) for p in date.split("/")[::-1]])
        finish = "_".join([date, time])

        os.rename("results/"+output_name, f"results/{start.replace('/', '')}_-_{finish.replace('/','')}_{new_output_name}")


generator("aapl.us.txt", "new.csv")
