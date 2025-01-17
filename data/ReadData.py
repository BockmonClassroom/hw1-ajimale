"""
Name: Abdikarim Jimale
Date to code: 01/12/2025

"""

import csv

# Ask the user for the file path
file_path = input("Please enter the path of the file: ")

# open the CSV file
try:
    with open (file_path, mode ='r', newline='') as file:
        #Create a CSV reader object
        csv_reader = csv.reader(file)

        #Iterate through each row and print
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print(f"The file at {file_path} was not found. Please check the path and try again.")
