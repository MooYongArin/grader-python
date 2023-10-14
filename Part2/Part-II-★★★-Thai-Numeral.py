def to_Thai( N ):
    N = int(N)
    check = False
    out = ""
    if N >= 1000 and N//1000 != 0 :
        out += dct[(N//1000)] + ' pun '
        N %= 1000
        check = True
    if N >= 100 and N//100 != 0: 
        out += dct[(N//100)] + ' roi '
        N %= 100
        check = True
    if N > 10 and N//10 != 0: 
        if N//10 != 2 and N//10 != 1 :
            out += dct[(N//10)] + ' sip '
        elif N//10 == 2:
            out +=  'yi' + ' sip '
        elif N//10 == 1:
            out += 'sip '
        N %= 10
        check = True
    if check and N == 0:
        return out
    if check and N == 1:
        out += 'et'
    else:
        out += dct[N]
        
    return out
reverse_dct = {
    'soon' : 0,
    'neung': 1,
    'song' : 2,
    'sam': 3,
    'si' : 4,
    'ha': 5,
    'hok' : 6,
    'chet': 7,
    'paet' : 8,
    'kao': 9,
    'sip' : 10,
}
dct = {}
for item in reverse_dct:
    dct.update({reverse_dct[item]:item})
exec(input().strip()) 