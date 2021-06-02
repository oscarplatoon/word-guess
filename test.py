import random 
import string 
import csv


easy = []
med  = []
hard = [] 

with open('sample.csv', 'r', newline='') as sample_file:
    csv_reader = csv.reader(sample_file, delimiter=',')
    easy = next(csv_reader)  
    med = next(csv_reader)
    hard = next(csv_reader)

    # for row in sample_file:
    #     print(row)