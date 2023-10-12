def peaks(x):
    lst = []
    for i in range(1,len(x)-1):
        if x[i-1] < x[i] and x[i+1] < x[i]:
            lst.append(i)
    return lst
exec(input()) 
