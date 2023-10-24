def factor(N): # N เป็ นจ ำนวนเต็มบวกมำกกว่ำ 1
    lst= []
    for k in range(2,N+1):
        power = 0
        while True:
            if N % k == 0:
                power += 1
                N /= k
            else:
                if power!=0:
                    lst.append([k,power])
                break
    return lst
exec(input().strip()) 