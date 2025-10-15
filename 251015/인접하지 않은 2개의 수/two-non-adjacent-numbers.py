n = int(input())
numbers = list(map(int, input().split()))

max_val = 0
# Please write your code here.
for i in range(n):
    for j in range(i+2, n):
        local_sum = numbers[i] + numbers[j]
        max_val = max(local_sum, max_val)

print(max_val)