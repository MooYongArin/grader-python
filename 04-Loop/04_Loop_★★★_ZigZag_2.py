zig_min = int()
zig_max = int()
zag_min = int()
zag_max = int()
n = 0
while True:
    x = input().split()
    # n = บรรทัดที่
    n = n + 1
    if x == ["Zig-Zag"]:
        print(zig_min,zig_max)
        break
    if x == ["Zag-Zig"]:
        print(zag_min,zag_max)
        break
    else:
        _x = int(x[0])
        _y = int(x[1])
        if n % 2 == 0:
            # Zig-Zag cases!!
            if _y < zig_min or zig_min == "":
                zig_min = _y
            if _x > zig_max or zig_max == "":
                zig_max = _x

            # Zag-Zig cases!!
            if _x < zag_min or zag_min == "":
                zag_min = _x
            if _y > zag_max or zag_max == "":
                zag_max = _y

        if n % 2 != 0:
            # Zig-Zag cases!!
            if _x < zig_min or zig_min == "":
                zig_min = _x
            if _y > zig_max or zig_max == "":
                zig_max = _y

            # Zag-Zig cases!!
            if _y < zag_min or zag_min == "":
                zag_min = _y
            if _x > zag_max or zag_max == "":
                zag_max = _x
