def is_mobile_number(number):
    if len(number) == 10:
        if number[0:2] == '06' or number[0:2] == '08' or number[0:2] == '09':
            return True 
        else:
            return False
    else:
        return False
exec(input())
