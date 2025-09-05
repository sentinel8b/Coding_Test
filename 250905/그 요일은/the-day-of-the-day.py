m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
def guess_dayname_repeat(m1, d1, m2, d2, A):
    day_of_month = [0, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    day_idx = day_name.index(A)
    def cal_num_days(m, d):
        day = 0 
        for month in range(m):
            day += day_of_month[month]
        day += d
        return day

    total_day1 = cal_num_days(m1, d1)
    total_day2 = cal_num_days(m2, d2)

    day_diff = total_day2 - total_day1
    return day_diff // day_idx

ans = guess_dayname_repeat(m1, d1, m2, d2, A) -1
print(ans)