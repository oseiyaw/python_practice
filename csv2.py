#!/usr/bin/env python3

import csv
import re

searching = re.search(r'^A\w*', 'Amelia')
print(searching[0])

dict = {}

with open('csv_data.csv', mode='r') as file:
    csv_read =csv.reader(file)
    
    next(csv_read)
    for line in csv_read:
        searc = re.search(r'A\w*', line[0])
        if searc != None:
            print(searc)
            dict[searc[0]] = "The age is: " + line[1]
    print (dict)

print(dict.keys())
print(dict.values())

namey = [keys for keys in dict.keys()]
sentence = [val for val in dict.values()]


f = ['name', 'sentence']
with open("csv_data2.csv", mode='w') as file:
    csv_write=csv.DictWriter(file, fieldnames=f)
    csv_write.writeheader()
    
    csv_write.writerow({'name': namey[0], 'sentence':sentence[0]})


with open('csv_data2.csv', mode='r') as file:
    reader = csv.DictReader(file)

    for line in reader:
        print(line)