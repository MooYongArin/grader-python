import string
def text2keys( text ):
    dct = {" ":"0"}
    starter = 2
    repeat = 1
    count = 0
    for letter in string.ascii_lowercase:
        count += 1
        # จบที่ r
        if count == 19:
            break
        if repeat == 4:
            repeat = 1
            starter += 1
        dct[letter] = str(starter)*repeat
        repeat += 1
    dct.update({'s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999'})

    text = text.lower()
    key = ""
    for item in text:
        if item in dct:
            key += dct[item] + " "
    key = key.strip()
    return key
def keys2text( keys ):
    dct = {" ":"0"}
    starter = 2
    repeat = 1
    count = 0
    for letter in string.ascii_lowercase:
        count += 1
        # จบที่ r
        if count == 19:
            break
        if repeat == 4:
            repeat = 1
            starter += 1
        dct[letter] = str(starter)*repeat
        repeat += 1
    dct.update({'s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999'})
    
    keys = keys.split()
    inv_dct = {v: k for k, v in dct.items()}
    text = ""
    for item in keys:
        if item in inv_dct:
            text += inv_dct[item]
    return text


exec(input().strip())