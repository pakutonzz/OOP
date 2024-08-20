def is_leap(year) :
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_years(day, month, year) :

    day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    if is_leap(year) :
        day_in_month[1] = 29
    
    for i in range(month-1) : 
        day += day_in_month[i]
    
    return day

print(day_of_years(1, 12, 2023))