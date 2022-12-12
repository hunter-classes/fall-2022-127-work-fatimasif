# Project-03-data / Working Solo 
# Assignment: Downoad a single data source, read it in using the Python CSV module and perform some basic analysis on the data (average of some field, extract some meaningful subset etc.) and report on the results.

import csv

reader = csv.DictReader(open("death.csv"))

key_word1 = 'Male'
counter = 0
with open('death.csv',encoding='UTF-8') as a:
  for line in a:
    if (key_word1) in line:
      counter = counter + 1
print(counter)

# Example using csv module into a list
#reader = csv.reader(open("death.csv"))
#for line in reader:
  #print(line)

# using a csv.reader on a dataset
# where the first line are the field/column names
reader = csv.reader(open("death.csv"))
full_data = [x for x in reader]
field_names = full_data[0]
data = full_data[1:]

#