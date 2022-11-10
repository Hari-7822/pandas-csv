import os
from csv import DictWriter 
import pandas as pd

pd.options.display.max_rows = 9999
head = ['id', 'FirstName', 'LastName', 'Username', 'Email', 'Avatar', 'Gender', 'DoB', 'Address']

base = os.path.abspath(os.path.dirname('/home/hari/Documents/python/intern-task/'))


data = os.path.join(base, 'src/in.csv')
dest = os.path.join(base, 'src/random.csv')

pr = pd.read_csv(data)
shuffle = pr.sample()
con = shuffle.to_csv()

with open(dest, 'w') as wr:
    ins = DictWriter(wr, fieldnames=head)
    ins.writerow(con)


print(pr.sample())


# print(pr.dropna())