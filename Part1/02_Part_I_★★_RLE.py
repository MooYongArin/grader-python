Type = input()

if Type == 'str2RLE':
    print("1")
    Text_STR = input()
elif Type == 'RLE2str':
    print("2")
    Text_RLE,Num_RLE = input().split()
else :
    print("Error")