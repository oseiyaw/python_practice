#!/usr/bin/env python3

import re
import csv

with open("csv_data.csv") as file:
    csv_line = csv.reader(file, delimiter=',')
    for line in csv_line:
        print(line)

#def import_csv(File):
    

#def main():
    

#main()