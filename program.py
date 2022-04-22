#!/usr/bin/python3

import csv
from io import StringIO
import time
import traceback

INDEX_FILE = "index.csv"
TEMP_FILE = "temp.txt"
IS_DEV = True


def printError(message, err):
    if IS_DEV:
        print(traceback.format_exc())
    else:
        print(message, err)


def measure_and_print(func, file, key, value, offset):
    t1 = time.time()
    row = {}
    message_time = ""
    isPrint = False
    if func == find_without_index:
        message_time = "WITHOUT INDEX RESULTS: "
        row = func(file, key, value)
        isPrint = True
    if func == find_with_index:
        message_time = "WITH INDEX RESULTS: "
        row = func(file, key, value, offset)
        isPrint = True
    if func == build_and_get_index:
        message_time = "BUILD TIME: "
        row = func(file, key)
        isPrint = False
    t2 = time.time()
    t = t2 - t1
    message_time = message_time + "passed as " + str(t) + " seconds too far"
    print(message_time)
    print("===========================================================================")
    if isPrint:
        print(str(row))
    print()
    return row


def build_and_get_index(file, key):
    index = {}
    try:
        index[key] = "offset"
        index = {key: "offset"}
        with open(INDEX_FILE, "w") as f:
            writer = csv.writer(f)
            writer.writerow([key, "offset"])

            with open(file) as f:
                reader = csv.reader(f)
                headers = next(reader)
                offset = 0
                for row in reader:
                    line = ",".join(row)
                    value = row[headers.index(key)]
                    writer.writerow([value, offset])
                    if not value in index.keys():
                        index[value] = offset
                    offset += len(line.encode('utf-8'))
    except Exception as error:
        printError("Ошибка при построении индекса: ", error)
    return index


def find_offset(key, value):
    try:
        with open(INDEX_FILE) as f:
            reader = csv.reader(f)
            headers = next(reader)
            for row in reader:
                if row[headers.index(key)] == value:
                    return row[headers.index("offset")]
    except Exception as error:
        printError("Ошибка при поиске оффсета: ", error)


def find_with_index(file, key, value, offset):
    try:
        with open(file) as f:
            reader = csv.reader(f)
            headers = next(reader)
            f.seek(int(offset))
            for row in reader:
                if row[headers.index(key)] == value:
                    return row
    except Exception as error:
        printError("Ошибка при поиске информации из csv: ", error)


def find_without_index(file, key, value):
    return find_with_index(file, key, value, 0)


def testing(file, key, value, isBuild):
    offset = "0"
    if isBuild:
        index = measure_and_print(build_and_get_index, file, key, "", 0)
        offset = index[value]
    else:
        offset = find_offset(key, value)
    print("offset: " + str(offset) + "\n")
    measure_and_print(find_without_index, file, key, value, 0)
    measure_and_print(find_with_index, file, key, value, offset)


if __name__ == "__main__":
    testing('test.csv', 'hostname', 'sw1', True)

    # value = "1234-very-hungry-games"
    # value = "2767052-the-hunger-games"
    # value = "18730321-paris"
    # value = "2.Harry_Potter_and_the_Order_of_the_Phoenix"
    # testing("books.csv", "bookId", value, True)
