m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.m1, d1, m2, d2 = map(int, input().split())


def guess_day(m1, d1, m2, d2):
    day_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    max_date_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def get_day_of_yr(m, d):
        day = 0
        for month in range(m):
            day += max_date_per_month[month]
        day+= d
        return day

    day_1 = get_day_of_yr(m1, d1)
    day_2 = get_day_of_yr(m2, d2)

    diff = day_2 - day_1
    idx = diff % 7
    return day_name[idx]

ans = guess_day(m1, d1, m2, d2)
print(ans)

