a, b, c, d = [int(i) for i in input("").split()]
h1 = a * 60
time1 = h1+b
h2 = c * 60
time2 = h2+d
total_time = time2 - time1

if time1 <= time2 and 7 <= a < 23 and 7 <= c < 23 and 0 <= b < 60 and 0 <= d < 60:
    if total_time <= 15:
        price = 0
    elif total_time <= 180:
        if total_time % 60 == 0:
            price = (total_time // 60) * 10
        else:
            price = ((total_time // 60) + 1) * 10
    elif total_time <= 300:
        if total_time % 60 == 0:
            price = (total_time - 180// 60) * 20 + 30 
        else:
            price = ((total_time - 180) // 60 + 1) * 20 + 30
    else:
        price = 200

    print(price)
else:
    print('Error')


