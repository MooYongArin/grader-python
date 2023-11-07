import numpy as np
# A is a 2-d array
def get_column_from_bottom_to_top( A, c ):
    return A[::-1,c]
def get_odd_rows( A ):
    return A[1::2]
def get_even_column_last_row( A ):
    return A[len(A)-1,::2]
def get_diagonal1( A ): # A is a square matrix
    lst = []
    for i in range(len(A)):
        lst.append(A[i,i])
    return  np.array(lst)
    # from top-left corner down to bottom-right corner
def get_diagonal2( A ): # A is a square matrix
    lst = []
    for i in range(len(A)):
        lst.append(A[i,len(A)-i-1])
    return  np.array(lst)
    # from top-right corner down to bottom-left corner
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
