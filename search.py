from func import fn, ln, ui

c = int(input('Enter search priority \n1.Search By FirstName\n2.Search By LastName\n3.Search By UserId\n\n'))


if c == 1 :
    print('Selected Search by FirstName')
    f = input('Enter the FirstName to be searched --> ')
    fn(f)

elif c == 2:
    print('Selected Search by LastName')
    l = input('Enter the LastName to be searched --> ')
    ln(l)

elif c == 3:
    print('Selected search by UserId')
    u = input('Enter the UserId to be searched --> ')
    ui(u)

if c > 3 or c <= 0: 
    print('wrong Option ' )
    print('\n\nEnter search priority \n1.Search By FirstName\n2.Search By LastName\n3.Search By UserId\n\n')

    
