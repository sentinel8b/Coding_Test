n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
result = 1
for i in range(n):
    if n == 0:
        dup_num = 1
    else:
        if arr[i] > arr[i-1]:
            dup_num += 1
        else:
            dup_num = 1
        if result < dup_num:
            result = dup_num
print(result)            