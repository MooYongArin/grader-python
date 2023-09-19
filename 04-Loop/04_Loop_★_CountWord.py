target = input()
sentence = input().split()
count = 0

for item in sentence:
    x = len(item)
    item = item.replace('.',' ')
    item = item.strip('"')
    item = item.strip('/')
    item = item.strip('(')
    item = item.strip(')')
    item = item.strip(',')
    item = item.strip('.')
    item = item.strip("'")

    if len(item) != x:
        item = item.strip('"')
        item = item.strip('/')
        item = item.strip('(')
        item = item.strip(')')
        item = item.strip(',')
        item = item.strip('.')
        item = item.strip("'")
    item = item.split()
    for word in item:
        print(word)
        if word == target:
            count += 1
print(count)