from collections import namedtuple
from collections import Counter
import requests 
import csv

counting = []
Contacts = namedtuple('Contacts', ['id','first_name', 'last_name', 'email'])
file = 'MOCK_DATA.csv'

with open(file, 'r') as csv_f:
    reader = csv.reader(csv_f, delimiter=",")
    items_dict = { (lineid, fname, lnam, email) for (lineid, fname, lnam, email) in reader}

    for row in map(Contacts._make, reader):
        if row.email.endswith('.com'):
            print(row)
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


for v in items_dict:
    print(v[1])




        