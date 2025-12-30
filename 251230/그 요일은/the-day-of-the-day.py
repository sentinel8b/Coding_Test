m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_idx = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4, 'Sat':5, 'Sun':6}

month_total = num_of_days[m1:m2]
day_total = d2 - d1

days_total = 0

for i in month_total:
    days_total += i

days_total += day_total

if days_total % 7 < day_idx[A]:
    print(days_total // 7)
else:
    print(days_total // 7 + 1)