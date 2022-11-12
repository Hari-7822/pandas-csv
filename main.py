import os
import pandas as pd
from csv import writer

pd.options.display.max_rows = 9999

base = os.path.abspath(os.path.dirname('/home/hari/Documents/python/intern-task/'))


data = os.path.join(base, 'src/in.csv')
dest = os.path.join(base, 'src/random.csv')


data_read = pd.read_csv(data)
dest_read = pd.read_csv(dest)

shuffle = data_read.sample()

add = pd.concat([shuffle, dest_read], ignore_index = True)
format = add.to_csv(dest)

non = dest_read.loc[:, ~dest_read.columns.str.match("Unnamed")].to_csv(dest)

dest_read.drop_duplicates(inplace = True)

print(dest_read)