n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cur_cnt = 1
max_cnt = 1

for i in range(1, n):
    if arr[i] > arr[i-1]:
        cur_cnt += 1
    else:
        cur_cnt = 1

    max_cnt = max(cur_cnt, max_cnt)

print(max_cnt)