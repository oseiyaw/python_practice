#!/usr/bin/env python3

import csv
import re

'''
Testing that my regular expression was workinging
searching = re.search(r'^A\w*', 'Amelia')
print(searching[0])
'''


#create a new dictionary to store data from CSV
dict = {}

#open the CSV file to be read in read mode
with open('csv_data.csv', mode='r') as file:
    #create the new CSV reader for the file
    csv_read =csv.reader(file)
    #skip the headings and read the data only
    next(csv_read)
    #for loop to go through the csv reader
    for line in csv_read:
        #regular expression to extract names that begin with an A
        searc = re.search(r'A\w*', line[0])
        #only add the results found to dictionary and discard any other results
        if searc != None:
            #add result to a new dictionary
            dict[searc[0]] = "The age is: " + line[1]
            #print the dictionary
    print (dict)

'''
Obsolete - do not use
print(dict.keys())
print(dict.values())
'''

#lists to store the names and values from the dictionaries 
namey = [keys for keys in dict.keys()]
sentence = [val for val in dict.values()]


f = ['name', 'sentence'] #Field Names for new CSV file
#Open a new CSV in write mode, will be overwritten with every run
with open("csv_data2.csv", mode='w') as file:
    #Creates a new Dict writer object for CSV file
    csv_write=csv.DictWriter(file, fieldnames=f)
    #Writes the new headers for the csv files
    csv_write.writeheader()
    #write the rows with the namey and sentence lists
    csv_write.writerow({'name': namey[0], 'sentence':sentence[0]})

#Test that the new CSV file has the write information by opening the file
with open('csv_data2.csv', mode='r') as file:
    #create a new reader to read the dictionaryy file
    reader = csv.DictReader(file)
    #Prints the lines in the new file
    for line in reader:
        print(line)