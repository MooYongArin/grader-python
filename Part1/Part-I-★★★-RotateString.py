rotation = input()
n = int(input())
all_str = ""
check_invalid = []
rotation_str = ""
rotation_180 = []
valid = ""

for i in range(n):
    x = input().strip()
    len_main = len(x)
    check_invalid.append(x)
    all_str += x

for item in check_invalid:
    if len(item) != len_main:
        print("Invalid size")
        valid = "invalid"
        break

if rotation == '90':
    if valid != "invalid":
        for i in range(len_main):
            test = len(all_str) - len_main
            rotation_str = ""
            for j in range(n):
                rotation_str += all_str[test+i - len_main*j]
            print(rotation_str)

elif rotation == 'flip':
    if valid != "invalid":
        keep_str = all_str
        for i in range(n):
            j = len_main - i
            rotation_str = ""
            for j in range(len_main-1,-1,-1):
                rotation_str += all_str[j + i*len_main]
            print(rotation_str)

elif rotation == '180':
    if valid != "invalid":
        for i in range(len_main):
            test = len(all_str) - len_main
            rotation_str = ""
            for j in range(n):
                rotation_str += all_str[test+i - len_main*j]
            rotation_180.append(rotation_str)
        for item in rotation_180:
            all_str += item
        len_main = n
        n = len(rotation_180)
        for i in range(len_main):
            test = len(all_str) - len_main
            rotation_str = ""
            for j in range(n):
                rotation_str += all_str[test+i - len_main*j]
            print(rotation_str)
    
