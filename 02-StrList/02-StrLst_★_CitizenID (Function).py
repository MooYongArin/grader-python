def check_digit(n):
    n_12 = (11 - ((int(n[0])*13 + int(n[1])*12 + int(n[2])*11 + int(n[3])*10 +int(n[4])*9+int(n[5])*8+int(n[6])*7+int(n[7])*6+int(n[8])*5+int(n[9])*4+int(n[10])*3+int(n[11])*2) % 11)) % 10
    return n_12
exec(input()) 