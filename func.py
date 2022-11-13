from map import dest
from read import dest_read

def fn(f):
    fname = dest_read.loc[dest_read['FirstName'] == f.capitalize()]
    print(fname)


def ln(l):
    lname = dest_read.loc[dest_read['LastName'] == l.capitalize()]
    print(lname)

def ui(u):
    uid = dest_read.loc[dest_read['Username'] == u.capitalize()]
    print(uid)