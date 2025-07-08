#!/usr/bin/env python3

import csv

dict = {}

with open('csv_data.csv', mode='r') as file:
    csv_read =csv.reader(file)
    next(csv_read)
    for line in csv_read:
        dict[line[0]] = "The age is: " + line[1]
    print (dict)