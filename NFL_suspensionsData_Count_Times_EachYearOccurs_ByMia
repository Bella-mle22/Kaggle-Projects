#NFL_suspensionsData_Count_Times_EachYearOccurs_ByMia
#Download Data From Here: https://github.com/fivethirtyeight/data/blob/master/nfl-suspensions/nfl-suspensions-data.csv

#Instructions
#Read the dataset into a list of lists.
#Import the csv module.
#Create a File handler for nfl_suspensions_data.csv.
#Use the csv.reader and list methods to read the file into a list named nfl_suspensions.
#Remove the first list in nfl_suspensions, which contains the header row of the CSV file.
#Select all lists in nfl_suspensions, except the for the one at index 0.
#Assign the resulting list of lists back to the variable nfl_suspensions.
#Count the number of times each value in the year column occurs.
#Create an empty dictionary called years.
#Use a for loop to iterate over the list in nfl_suspensions representing the year column:
#Extract that row's value for the year column and assign to row_year.
#If row_year is already a key in years, add 1 to the value associated with that key.
#If row_year isn't already a key in years, set the value associated with the key to 1.
#Use the print function to display the dictionary years.

import csv
f = open("nfl_suspensions_data.csv")
nfl_suspensions =  list(csv.reader(f))
nfl_suspensions = nfl_suspensions[1:]

years_column = nfl_suspensions[5]
years = {}

for suspension in nfl_suspensions:
    row_year = suspension[5]
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else:
        years[row_year] = 1

print(years)
