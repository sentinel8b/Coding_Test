n = int(input())
A = list(map(int, input().split()))

# Please write your code here
max_val = 1e6
for i in range(n):
    val_per_case = 0
    for j in range(n):
        if j == i:
            val_per_case += 0 
        else:
            val_per_case += A[j] * abs(i-j)
    if val_per_case < max_val:
        max_val = val_per_case

print(max_val)

