import pandas as pd
from map import data, dest, temp

pd.options.display.max_rows = 9999


data_read = pd.read_csv(data)
dest_read = pd.read_csv(dest)
temp_read = pd.read_csv(temp)