import numpy as np
def mult_table(nrows, ncols):
    arr_rows = np.arange(1,nrows+1)
    arr_cols = np.arange(1,ncols+1).reshape((1,ncols))
    return arr_rows*arr_cols
    # คืนอาเรย์ที่มี shape เป็น (nrow, ncols) ภายในเก็บตารางสูตรคูณ (ดูตัวอย่างข ้างล่าง)
exec(input().strip()) # ตอ้ งมคี าสงั่ นี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
