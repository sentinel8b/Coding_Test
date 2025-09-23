n = int(input())
arr = [int(input()) for _ in range(n)]


max_cnt = 0
# Please write your code here.
cur_cnt = 1
for i in range(len(arr)):
    if i == 0:
        continue
    elif arr[i] == arr[i-1]:
        cur_cnt += 1
    elif arr[i] != arr[i-1]:
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt
            cur_cnt = 1

print(max_cnt)