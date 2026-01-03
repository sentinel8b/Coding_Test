n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

result = 0
dup_num = 0
for i in range(n-1):
    if arr[i] > t and arr[i+1] > t:
        dup_num += 1
        if result < dup_num:
            result = dup_num
    elif arr[i] > t and arr[i+1] <= t:
        dup_num += 1
        if result < dup_num:
            result = dup_num
        dup_num = 0


print(result)