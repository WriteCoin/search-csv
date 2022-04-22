#!/usr/bin/python3

import csv

# f = open('file.txt', 'r')
# offset = 0
# line = f.__next__()
# while line:
#   offset = f.seek(len(line) + offset)
#   print(line)
#   print(offset)
#   try:
#     line = f.__next__()
#   except:
#     break

print()

# f = open('file.txt', 'r')
# offset = 0
# for line in f:
#   print(f.tell())

with open("test.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        print(reader.__sizeof__())


# with open('test.csv') as f:
#   reader = csv.DictReader(f)
#   rows = list(reader)
#   i = 0
#   # row = reader[i]
#   line = f.readline()
#   while line:
#     print(line)
#     print(f.tell())
#     i += 1
#     line = f.readline()

# with open('test.csv') as f:
#   line = f.readline()
#   while line:
#     print(line)
#     print(f.tell())
#     values = line.split(',')
#     print("list: ", values)

#     line = f.readline()

# with open('test.csv') as f:
#   reader = csv.DictReader(f)
#   row = next(reader)
#   headers = list(row.keys())
#   print("Headers: ", headers)
#   print(row)
#   while row:
#     print(f.tell())
# try:
# row = next(reader)
# except:
# break
# print(row)
# for row in reader:
#   values = list(row.values())
#   line = ','.join(values)
#   print(line)
#   print(f.tell())

# i = 0
# for row in reader:
#   print(row)
#   print(repr(row))
#   i += 1

# my_dict = {'a': 1, 'b': 2, 'c': 3}
