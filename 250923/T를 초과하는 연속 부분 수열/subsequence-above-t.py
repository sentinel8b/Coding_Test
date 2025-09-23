n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cur_cnt = 0
max_cnt = 0

for i in range(0,n):
    if arr[i] > t:
        cur_cnt += 1
    else:
        cur_cnt = 0
    
    max_cnt = max(max_cnt, cur_cnt)

print(max_cnt)