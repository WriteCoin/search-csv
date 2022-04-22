#!/usr/bin/python3

import time

# import numpy as np
import pandas as pd


def measure_and_print(func, **args):
    message_time = args["message_time"]
    isPrint = args["isPrint"]
    f = args["f"]

    t1 = time.time()
    res = func(**args)
    t2 = time.time()
    t = t2 - t1
    message_time = message_time + " passed as " + str(t) + " seconds too far"

    if isPrint:
        print(message_time)
        print("===================================================================")
        print(str(res))
        print()
    if f:
        f(message_time=message_time, t=t, **args)
    return res


def find_records(**args):
    res = None
    try:
        file = args["file"]
        cond = args["cond"]
        offset = args["offset"]
        csv = pd.read_csv(file)
        res = csv[cond(csv)]
    except Exception as error:
        print("Ошибка при поиске информации из csv: ", error)
    return res


if __name__ == "__main__":
    # find_records(file='books.csv', cond=lambda csv: csv.bookId == "2767052-the-hunger-games", offset=0)
    measure_and_print(
        find_records,
        file="books.csv",
        cond=lambda csv: csv.bookId == "2767052-the-hunger-games",
        offset=0,
        message_time="RESULT WITHOUT INDEX:",
        isPrint=True,
        f=None,
    )
