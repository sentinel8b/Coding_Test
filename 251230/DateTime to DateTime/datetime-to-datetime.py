a, b, c = map(int, input().split())

# Please write your code here.

if a < 11:
    print(-1)
else:
    total_day = a - 11
    total_hour = b - 11
    total_min = c - 11

    print(total_day * 24 * 60 + total_hour * 60 + total_min)