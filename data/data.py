# Project-03-data / Working Solo 
# Assignment: Downoad a single data source, read it in using the Python CSV module and perform some basic analysis on the data (average of some field, extract some meaningful subset etc.) and report on the results.

# import pandas as pd 
# cledf = pd.read_csv('squirrel.csv')

import csv

# using DictReader and list comprehensions
reader = csv.DictReader(open("squirrel.csv"))
# reader = csv.reader(open("squirrel.csv"))

key_word1 = 'Gray'
counter = 0
with open('squirrel.csv',encoding='UTF-8') as a:
  for line in a:
    if (key_word1) in line:
      counter = counter + 1
print(counter)

# data = [x for x in reader]

# get all the gray squirrels
# gray = [int(x['Gray']) for x in data] 

# gray_squirrel = [ x for x in data if int(x['gray'])>7]