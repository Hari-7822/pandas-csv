from read import dest_read

list = ['FirstName', 'LastName', 'Username', 'Email']

# dest_read.loc[dest_read.duplicated(subset=list), :]
dest_read.drop_duplicates(subset=list, inplace=True, keep = False)
