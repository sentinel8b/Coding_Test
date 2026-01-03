n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

result = 0
for i in range(n):
    if i == 0:
        dup_num = 0
    else:
        if arr[i] > t and arr[i-1] > t:
            dup_num += 1
        else:
            dup_num = 0
    if result < dup_num:
        result = dup_num
if result == 0:
    print(result)
else:
    print(result + 1)