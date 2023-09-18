def GradeToNum(x):
    if x == 'A':
        return 4
    if x == 'B':
        return 3
    if x == 'C':
        return 2
    if x == 'D':
        return 1

def choose(stu1, stu2):
    stid = stu1[0]
    stid2 = stu2[0]
    gpax = stu1[1]
    gpax2 = stu2[1]
    com_prog = stu1[2]
    com_prog2 = stu2[2]
    calI = stu1[3]
    calI2 = stu2[3]
    calII = stu1[4]
    calII2 = stu2[4]
    ans = []
    if (com_prog == 'A' and calI != 'D' and calI != 'F' and calII != 'D' and calII != 'F' and (com_prog2 != 'A' or calI2 == 'D' or calI2 == 'F' or calII2 == 'D' or calII2 == 'F' )) :
        ans.append(stid)
    elif (com_prog2 == 'A' and calI2 != 'D' and calI2 != 'F' and calII2 != 'D' and calII2 != 'F' and (com_prog != 'A' or calI == 'D' or calI == 'F' or calII == 'D' or calII == 'F' )) :
        ans.append(stid2)    
    elif (com_prog2 == 'A' and calI2 != 'D' and calI2 != 'F' and calII2 != 'D' and calII2 != 'F' and com_prog == 'A' and calI != 'D' and calI != 'F' and calII != 'D' and calII != 'DF' ):
        if gpax > gpax2:
            ans.append(stid)
        elif gpax2 > gpax:
            ans.append(stid2)
        elif gpax2 == gpax:
            if GradeToNum(calI) > GradeToNum(calI2):
                ans.append(stid)
            elif GradeToNum(calI2) > GradeToNum(calI):
                ans.append(stid2)
            elif GradeToNum(calI) == GradeToNum(calI2):
                if GradeToNum(calII) > GradeToNum(calII2):
                    ans.append(stid)
                elif GradeToNum(calII2) > GradeToNum(calII):
                    ans.append(stid2)
                elif GradeToNum(calII) == GradeToNum(calII2): 
                    ans.append(stid)
                    ans.append(stid2)
    return ans
exec(input()) 
