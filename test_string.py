from io import StringIO
import csv

scsv = """text,with,Polish,non-Latin,letters
1,2,3,4,5,6
a,b,c,d,e,f
gęś,zółty,wąż,idzie,wąską,dróżką,
"""

f = StringIO(scsv)
reader = csv.reader(f, delimiter=',')
for row in reader:
    print('\t'.join(row))