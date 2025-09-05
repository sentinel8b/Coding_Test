m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

elapsed_day = 0

while True:
    if m1 == m2 and d1 == d2:
        print(elapsed_day)
        break
    d1 += 1
    elapsed_day += 1
    if d1 > days_per_month[m1]:
        m1 += 1
        d1 = 0
    
    
