N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here
max_cnt = 1
cur_cnt = 1

for i in range(1, N):
    if arr[i] > 0: # P
        if arr[i-1] > 0: # P
            cur_cnt+=1
        else:
            cur_cnt= 1
    else: # N
        if arr[i-1] > 0: # P
            cur_cnt = 1
        else:
            cur_cnt +=1
    max_cnt = max(max_cnt, cur_cnt)

print(max_cnt)
