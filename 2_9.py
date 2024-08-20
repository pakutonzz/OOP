def is_leap(year) :
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_in_year(year) :
    return 366 if is_leap(year) else 365

def day_of_years(day, month, year) :

    day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    if is_leap(year) :
        day_in_month[1] = 29
    
    for i in range(month-1) : 
        day += day_in_month[i]
    
    return day

def date_diff(date1, date2) :

    d1, m1 ,y1 = date1.split('-')
    d2, m2, y2 = date2.split('-')

    day_in_month1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    day_in_month2 = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(int(y1)) :
        day_in_month1[1] = 29
    if is_leap(int(y2)) :
        day_in_month2[1] = 29
    
    if 0 <= int(m1) <= 12 and 0 <= int(m2) <= 12 and 0 <= int(y1) and 0 <= int(y2) :
        if 0 <= int(d1) <= day_in_month1[int(m1)-1] and 0 <= int(d2) <= day_in_month2[int(m2)-1] :
            days = 0

            for year in range(int(y1), int(y2)) :
                days += day_in_year(year)
            
            days += day_of_years(int(d2), int(m2), int(y2)) - day_of_years(int(d1), int(m1), int(y1)) + 1
            
            return days
        else : 
            return -1
    else :
        return -1

print(date_diff('25-12-1999', '9-13-2020'))