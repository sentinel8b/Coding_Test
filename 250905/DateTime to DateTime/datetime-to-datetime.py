a, b, c = map(int, input().split())

# Please write your code here.
def cal_elapsed_mins(a, b, c):
    cur_day, cur_hour, cur_min = 11, 11, 11
    # initial break cond
    if a < cur_day:
        return -1
        if b < cur_hour:
            return -1
            if c < cur_min:
                return -1

    elapsed_mins = 0
    while True:
        if a == cur_day and b == cur_hour and c == cur_min:
            return elapsed_mins
        
        elapsed_mins += 1
        cur_min += 1
        if cur_min > 59:
            cur_min = 0
            cur_hour += 1
            if cur_hour > 23:
                cur_hour = 0
                cur_day += 1

ans = cal_elapsed_mins(a, b, c)
print(ans)
        
