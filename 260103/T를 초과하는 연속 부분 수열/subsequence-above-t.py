n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

result = 0
dup_num = 0
for i in range(n):
    if arr[i] > t:
        dup_num += 1
    else:
        dup_num = 0
    if dup_num > result:
        result = dup_num

print(result)