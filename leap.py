

def is_leap(year:int)-> bool:
    if year % 400 == 0:
        Leap_year = True
    elif year % 100 == 0:
        Leap_year = False
    elif year % 4 == 0:
        Leap_year = True
    else:
        Leap_year = False
    return Leap_year

year = int(input("enter the value: "))
result = is_leap(year)
print(result)
