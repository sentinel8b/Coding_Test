m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name_of_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day_total = d2 - d1
if m1 <= m2:
    month_total = num_of_days[m1:m2]
    days_total = 0
    for i in month_total:
        days_total += i

    days_total += day_total
    print(name_of_days[days_total % 7])
else:
    month_total = num_of_days[m2:m1]
    days_total = 0
    for i in month_total:
        days_total -= i

    days_total -= day_total
    print(name_of_days[days_total % 7 - 7])
