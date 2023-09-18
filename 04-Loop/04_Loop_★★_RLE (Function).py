def RLE(t):
    t += " "
    str2RLE_ans = ""
    count = 0
    big_lst = []
    lst = []
    for i in range(1,len(t)):
        count += 1
        if t[i] != t[i-1]:
            lst.append(str(t[i-1]))
            lst.append(count)
            big_lst.append(lst)
            count = 0
            lst = []
    return big_lst
exec(input()) # DON'T remove this line