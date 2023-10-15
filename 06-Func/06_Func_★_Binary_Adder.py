str1,str2 = [ int(e,2) for e in input().split()]
print(bin(str1+str2)[2:])