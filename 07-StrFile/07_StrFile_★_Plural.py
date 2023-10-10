def s_x_ch(x):
    return x + "es"
def y_no_vovel(x):
    x = x[:len(x)-1]
    return x + "ies"
def no_cases(x):
    return x + "s"

word = input().strip()
if word[len(word)-1] in ['s','x'] or word[len(word)-2:len(word)] == 'ch':
    print(s_x_ch(word))
elif word[len(word)-1] == 'y' and word[len(word)-2] not in ['a','e','i','o','u']:
    print(y_no_vovel(word))
else:
    print(no_cases(word))
