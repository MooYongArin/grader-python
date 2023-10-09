def R_operater(x):
    new_x = ""
    for i in range(len(x)):
        if x[i] == 'A' or x[i] == 'a':
            new_x += 'T'
        elif x[i] == 'T' or x[i] == 't':
            new_x += 'A'
        elif x[i] == 'C' or x[i] == 'c':
            new_x += 'G'
        elif x[i] == 'G' or x[i] == 'g':
            new_x += 'C'
    reverse_new_x = new_x[::-1]
    return reverse_new_x
def F_operater(x):
    lst = ['A',0,'T',0,'G',0,'C',0,]
    for item in x:
        if item in ['A','a']:
            lst[1] += 1
        elif item in ['T','t']:
            lst[3] += 1
        elif item in ['G','g']:
            lst[5] += 1
        elif item in ['C','c']:
            lst[7] += 1
    return 'A' + "=" + str(lst[1])+ ', '+ "T" + "=" + str(lst[3])+ ', '+ 'G' + "=" + str(lst[5])+ ', '+'C'+ "=" + str(lst[7])
_str = input().strip()
check = True
for item in _str:
    if item not in ['A','T','C','G','a','t','c','g'] :
        print('Invalid DNA')
        check = False
        break
if check == True:
    operater = input()
    if operater == 'R':
        print(R_operater(_str))
    if operater == 'F':
        print(F_operater(_str))
    if operater == 'D':
        target = input()
        count_D = 0
        _str = _str.upper()
        for i in range(len(_str)):
            if _str[i:i+2] == target:
                count_D += 1
        print(count_D)
