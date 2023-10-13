def sqrt_n_times(x, n):
    for i in range(n):
        x = x**0.5
    return x
 
def cube_root(y):
    y = y**( (1/(2**2))*(1+(1/(2**2)))*(1+(1/(2**4)))*(1+(1/(2**8)))*(1+(1/(2**16)))*(1+(1/(2**32))) )
    return y
def main():
    q = float(input())
    print(cube_root(q))

exec(input()) # DON'T remove this line