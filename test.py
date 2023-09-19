def approximate_log10(a, epsilon=1e-10):
    L = 0.0 
    U = a   
    x = (L + U) / 2 

    while abs(10**x - a) > epsilon:
        if 10**x < a:
            L = x
        else:
            U = x
        x = (L + U) / 2

    return x

a = int(input())
result = approximate_log10(a)
print(round(result,6))
