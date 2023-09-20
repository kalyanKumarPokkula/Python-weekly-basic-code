import csv

with open("names.csv", "r") as file:
    list = csv.reader(file)
    for row in list:
        print(f"student name is {row[0]} and age is {row[1]}")
