d = int(input())
m = int(input())
y = int(input())

_BC = y - 543
if (_BC % 4 == 0 and _BC % 100 != 0) or (_BC % 4 == 0 and _BC % 100 == 0 and _BC % 400 == 0):
    if m == 1:
        print (d)
    elif m == 2:
        print (31+int(d))
    elif m == 3:
        print (31+29+int(d))
    elif m == 4:
        print (31+29+31+int(d) )   
    elif m == 5:
        print (31+29+31+30+int(d)   )
    elif m == 6:
        print (31+29+31+30+31+int(d) )  
    elif m == 7:
        print (31+29+31+30+31+30+int(d)   )
    elif m == 8:
        print (31+29+31+30+31+30+31+int(d))   
    elif m == 9:
        print (31+29+31+30+31+30+31+31+int(d) )  
    elif m == 10:
        print (31+29+31+30+31+30+31+31+30+int(d))   
    elif m == 11:
        print (31+29+31+30+31+30+31+31+30+31+int(d)  ) 
    elif m == 12:
        print (31+29+31+30+31+30+31+31+30+31+30+int(d)   )
else:
    if m == 1: 
        print (d)
    elif m == 2:
        print (31+int(d))
    elif m == 3:
        print (31+28+int(d))
    elif m == 4:
        print (31+28+31+int(d) )   
    elif m == 5:
        print (31+28+31+30+int(d)   )
    elif m == 6:
        print (31+28+31+30+31+int(d))   
    elif m == 7:
        print (31+28+31+30+31+30+int(d) )  
    elif m == 8:
        print (31+28+31+30+31+30+31+int(d)   )
    elif m == 9:
        print (31+28+31+30+31+30+31+31+int(d))   
    elif m == 10:
        print (31+28+31+30+31+30+31+31+30+int(d))   
    elif m == 11:
        print (31+28+31+30+31+30+31+31+30+31+int(d)   )
    elif m == 12:
        print (31+28+31+30+31+30+31+31+30+31+30+int(d) )  