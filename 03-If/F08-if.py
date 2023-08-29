def day_of_year(d, m, y):
    _BC = y - 543
    if (_BC % 4 == 0 and _BC % 100 != 0) or (_BC % 4 == 0 and _BC % 100 == 0 and _BC % 400 == 0):
        if m == 1:
            return d
        elif m == 2:
            return 31+int(d)
        elif m == 3:
            return 31+29+int(d)
        elif m == 4:
            return 31+29+31+int(d)    
        elif m == 5:
            return 31+29+31+30+int(d)   
        elif m == 6:
            return 31+29+31+30+31+int(d)   
        elif m == 7:
            return 31+29+31+30+31+30+int(d)   
        elif m == 8:
            return 31+29+31+30+31+30+31+int(d)   
        elif m == 9:
            return 31+29+31+30+31+30+31+31+int(d)   
        elif m == 10:
            return 31+29+31+30+31+30+31+31+30+int(d)   
        elif m == 11:
            return 31+29+31+30+31+30+31+31+30+31+int(d)   
        elif m == 12:
            return 31+29+31+30+31+30+31+31+30+31+30+int(d)   
    else:
        if m == 1: 
            return d
        elif m == 2:
            return 31+int(d)
        elif m == 3:
            return 31+28+int(d)
        elif m == 4:
            return 31+28+31+int(d)    
        elif m == 5:
            return 31+28+31+30+int(d)   
        elif m == 6:
            return 31+28+31+30+31+int(d)   
        elif m == 7:
            return 31+28+31+30+31+30+int(d)   
        elif m == 8:
            return 31+28+31+30+31+30+31+int(d)   
        elif m == 9:
            return 31+28+31+30+31+30+31+31+int(d)   
        elif m == 10:
            return 31+28+31+30+31+30+31+31+30+int(d)   
        elif m == 11:
            return 31+28+31+30+31+30+31+31+30+31+int(d)   
        elif m == 12:
            return 31+28+31+30+31+30+31+31+30+31+30+int(d)   
exec(input())

