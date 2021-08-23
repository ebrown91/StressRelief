##request user input for size, cr%, and heat number
##search list for match, if match suggest SR time and temp
##if no match add MTR data then predict SR time and temp

import csv

with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)