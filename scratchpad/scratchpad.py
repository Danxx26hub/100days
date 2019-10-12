from collections import namedtuple
from collections import Counter
import requests 
import csv

counting = []
Contacts = namedtuple('Contacts', ['id','first_name', 'last_name', 'email'])
file = 'MOCK_DATA.csv'

with open(file, 'r') as csv_f:
    reader = csv.reader(csv_f)

    for row in map(Contacts._make, reader):
        #print(row)
        counting.append(row.email)
        
        #print(row.first_name, ' : ', row.email)
counted = []
for email in counting:
    if email.endswith('.com'):

        counted.append(email.split('.')[1])
    elif email.endswith('.org'):

        counted.append(email.split('.')[1])
    elif email.endswith('.edu'):

        counted.append(email.split('.')[1])
        
num = Counter(counted)
print(num)
print(f'there are {num["com"]} .com email addresses')

        