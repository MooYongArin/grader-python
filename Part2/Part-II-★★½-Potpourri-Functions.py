def convex_polygon_area(p):
    p.append(p[0])
    sum_left = 0
    sum_right = 0
    for i in range(len(p)-1):
        sum_left += p[i][0]*p[i+1][1]
        sum_right += p[i][1]*p[i+1][0]
        
    ans = abs(0.5*(sum_left-sum_right))
    return ans
def is_heterogram(s):
    s = s.lower()
    dct = {}
    for item in s:
        if 'a'<= item <='z':
            if item not in dct:
                dct[item] = 1
            else:
                return False
    return True
def replace_ignorecase(s, a, b):
    ans = ""
    a = a.lower()
    i = 0
    while i < len(s):
        if s[i:i+len(a)].lower() == a:
            ans += b
            i += len(a)
        else:
            ans += s[i]
            i += 1
    return ans
def top3(votes):
    all_sort = sorted(votes.items(), key=lambda item: (-item[1], item[0]))
    i = 0
    top_3 = []
    for item in all_sort:
        i+=1
        top_3.append(item[0])
        if i ==3:
            return top_3
 
for k in range(2):
 exec(input().strip())
