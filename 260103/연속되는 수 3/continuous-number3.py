N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

result = 1
for n in range(N):
    if n == 0:
        dup_num = 1
    else:
        if arr[n] < 0 and arr[n-1] < 0:
            dup_num += 1
        elif arr[n] > 0 and arr[n-1] > 0:
            dup_num += 1
        else:
            dup_num = 1
        if result < dup_num:
            result = dup_num
print(result)