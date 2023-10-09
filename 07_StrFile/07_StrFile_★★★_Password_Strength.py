def no_lowercase(t): # return True if no lowercase, otherwise return False
    for item in t:
        if 'a' <= item <= 'z':
            return False
    return True
def no_uppercase(t):
    for item in t:
        if 'A' <= item <= 'Z':
            return False
    return True
def no_number(t):
    for item in t:
        if '0' <= item <= '9':
            return False
    return True
def no_symbol(t):
    symbols = '[!@#\$%^&\*()_+]"'
    for i in t:
        if i in symbols:
            return False
    return True
def character_repetition(t):
    for i in range(len(t)-3):
        if len(t) >= 4:
            if t[i:i+4] == 4*t[i]:
                return True
    return False
def number_sequence(t):
    all_num = '1234567890'
    addition_cases = ['0123']
    for j in range(len(all_num)-3):
        for i in range(len(t)-3):
            if t[i:i+4] == all_num[j:j+4] or t[i:i+4] == all_num[j+4:j:-1] or t[i:i+4] == all_num[3::-1] or t[i:i+4] in addition_cases :
                return True
    return False
def letter_sequence(t):
    t = t.lower()
    a_z = "abcdefghijklmnopqrstuvwxyz"
    for j in range(len(a_z)-3):
        for i in range(len(t)-3):
            if t[i:i+4] == a_z[j:j+4] or t[i:i+4] == a_z[j+4:j:-1] or t[i:i+4] == a_z[3::-1] :
                return True
    return False
def keyboard_pattern(t):
    pattern = ["1234567890-=", "qwertyuiop", "asdfghjkl", "zxcvbnm","!@#$%^&*()_+"]
    t = t.lower()
    for item_test in pattern:
        for i in range(len(t)-3):
            for j in range(len(item_test)-3):
                if item_test[j:j+4] == t[i:i+4] or item_test[j+4:j:-1] == t[i:i+4] or item_test[3::-1] == t[i:i+4]:
                    return True
    return False 
#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw):
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append("No numbers")
if no_symbol(passw):
    errors.append("No symbols")
if character_repetition(passw):
    errors.append("Character repetition")
if number_sequence(passw):
    errors.append("Number sequence")
if letter_sequence(passw):
    errors.append("Letter sequence")
if keyboard_pattern(passw):
    errors.append("Keyboard pattern")
if len(errors) == 0:
    print("OK")
else:
    for item in errors:
        print(item)