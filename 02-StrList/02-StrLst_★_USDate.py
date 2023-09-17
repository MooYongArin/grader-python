x = input().split('/')

def NumberToMonth(x):
    if x == '1':
        return 'January'
    if x == '2':
        return 'February'
    if x == '3':
        return 'March'
    if x == '4':
        return 'April'
    if x == '5':
        return 'May'
    if x == '6':
        return 'June'
    if x == '7':
        return 'July'
    if x == '8':
        return 'August'
    if x == '9':
        return 'September'
    if x == '10':
        return 'October'
    if x == '11':
        return 'November'
    if x == '12':
        return 'December'

print(NumberToMonth(x[1]) + " " + x[0] + ', ' + x[2])
