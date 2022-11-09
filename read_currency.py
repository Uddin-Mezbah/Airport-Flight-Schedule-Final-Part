import csv

with open('./data/currencyrates.csv','r') as file:
    lines = csv.reader(file)
    for line in lines:
        if 'Egyptian' in line[0]: #change country name
            print(line)
