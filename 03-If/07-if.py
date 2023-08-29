number = int(input())

if number < 1000:
    print(number)
elif number == 1000:
    print('1K')
elif number > 1000 and number < 10000:
    print(str(round((number/1000),1)) + 'K')
elif number >= 10000 and number < 1000000:
    print(str(int(round((number/1000),0))) + 'K')    
elif number >= 1000000 and number < 10000000:
    print(str(round((number/1000000),1)) + 'M')
elif number >= 10000000 and number < 1000000000:
    print(str(int(round((number/1000000),0))) + 'M')
elif number >= 1000000000 and number < 10000000000:
    print(str(round((number/1000000000),1)) + 'B')
elif number >= 10000000000:
    print(str(int(round((number/1000000000),0))) + 'B')