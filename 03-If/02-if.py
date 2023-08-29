stid,gpax,com_prog,calI,calII = input().split()
stid2,gpax2,com_prog2,calI2,calII2 = input().split()

def GradeToNum(x):
    if x == 'A':
        return 4
    if x == 'B':
        return 3
    if x == 'C':
        return 2
    if x == 'D':
        return 1

if (com_prog == 'A' and calI != 'D' and calI != 'F' and calII != 'D' and calII != 'F' and (com_prog2 != 'A' or calI2 == 'D' or calI2 == 'F' or calII2 == 'D' or calII2 == 'F' )) :
    print(stid)
elif (com_prog2 == 'A' and calI2 != 'D' and calI2 != 'F' and calII2 != 'D' and calII2 != 'F' and (com_prog != 'A' or calI == 'D' or calI == 'F' or calII == 'D' or calII == 'F' )) :
    print(stid2)    
elif (com_prog2 == 'A' and calI2 != 'D' and calI2 != 'F' and calII2 != 'D' and calII2 != 'F' and com_prog == 'A' and calI != 'D' and calI != 'F' and calII != 'D' and calII != 'DF' ):
    if gpax > gpax2:
        print(stid)
    elif gpax2 > gpax:
        print(stid2)
    elif gpax2 == gpax:
        if GradeToNum(calI) > GradeToNum(calI2):
            print(stid)
        elif GradeToNum(calI2) > GradeToNum(calI):
            print(stid2)
        elif GradeToNum(calI) == GradeToNum(calI2):
            if GradeToNum(calII) > GradeToNum(calII2):
                print(stid)
            elif GradeToNum(calII2) > GradeToNum(calII):
                print(stid2)
            elif GradeToNum(calII) == GradeToNum(calII2): 
                print('Both')
else :
    print('None')
