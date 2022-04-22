with open("file.txt") as f:
    line = f.readline()
    while line:
        print(line)
        print(f.tell())
        line = f.readline()

f = open("file.txt", "r")
offset = 0
line = f.__next__()
while line:
    offset = f.seek(len(line) + offset)
    print(line)
    print(offset)
    try:
        line = f.__next__()
    except:
        break
