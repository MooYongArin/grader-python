x = input()
test = ""

for item in x:
    if item == '(':
        item = item.replace('(','[')
    elif item == '[':
        item = item.replace('[','(')
    elif item == ')':
        item = item.replace(')',']')
    elif item == ']':
        item = item.replace(']',')')
    test += item
print(test)