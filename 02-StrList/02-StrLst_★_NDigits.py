m = int(input())
n = int(input())

if n > len(str(m)):
    print( '0'*(n-len(str(m))) + str(m))
else:
    print(m)
