import pandas as pd
from map import data, dest , temp
from read import data_read , dest_read, temp_read 


shuffle = data_read.sample()

add = pd.concat([shuffle, dest_read], ignore_index = True)
format = add.to_csv(dest)


dest_read.loc[:, ~dest_read.columns.str.match("Unnamed")].to_csv(dest)
list = dest_read.columns.tolist()

dest_read.sort_values("FirstName", ascending =True, inplace = True, na_position = 'first') #sorting in acsending manner in Csv


dest_read.drop_duplicates()

print(list)
print(dest_read)