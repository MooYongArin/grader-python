main_text = input()
main_text = main_text.lower()
dct = {}
for item in main_text:
    if 'a'<=item<='z':
        if item in dct:
            dct[item] += 1
        else:
            dct[item] = 1
lst = []
for item in dct:
    lst.append([-dct[item],item])
lst = sorted(lst)
for item in lst:
    print(item[1], '->',-int(item[0]))