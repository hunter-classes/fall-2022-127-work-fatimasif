# Project-03-data / Working Solo 
# Assignment: Downoad a single data source, read it in using the Python CSV module and perform some basic analysis on the data (average of some field, extract some meaningful subset etc.) and report on the results.

import csv

# opening the csv file containing data about coffee
file = open('coffee.csv')
type(file)
csvreader = csv.reader(file)

# this code will analyze each country and the amount of coffee bags it produced in a specific year
with open('coffee.csv') as input:
    csv_reader = csv.reader(input, delimiter=',') # each value(whether part of header or a data record) is separated by a comma. This separator character is called a Delimiter. A CSV file may use other delimiters other than comma.
    line_count = 0 # first row is the header so it begins at 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Header row - {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} produced {row[10]} bags of coffee in the year {row[5]}, and the owner of the coffee is {row[6]}.')
            line_count += 1
    print(f'Total: {line_count} lines')

  
# Extra 1 : Use multiple aspects of a single data source in your analysis

import pandas as pd

# reading the file and getting the columns 
df = pd.read_csv('coffee.csv')
df.columns

# counts the amount of times a country is associated with the production of coffee and gives the information as a list
coffee_counts= df['Location.Country'].value_counts() 
print ("Below is a list of each country and how much coffee was produced: \n") 
print(coffee_counts) 

# this will compare the number of times each country is mentioned
# it will print the country that produced coffee the most times (lead producer)
max_country= coffee_counts.idxmax() 
max_coffee= coffee_counts.max() 
print("The country where the most coffee produced is", max_country, ". Produced " + str(max_coffee) + " times.\n")


# Extra 2: Use Matplotlib or another Python graphing/plotting library to visualize part or all of your analysis.

import matplotlib.pyplot as plt

# plotting the countries
# x-axis shows the countries
# y-axis shows the number of coffee production
coffee_counts.plot(kind='bar')
plt.show() 
