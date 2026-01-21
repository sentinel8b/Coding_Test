n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
result = 0
for i in range(n):
    for j in range(i, n):
        tmp_val = 0
        for comp in arr[i:j+1]:
            tmp_val += comp
        tmp_val /= (j+1-i)
        if tmp_val in arr[i:j+1]:
            result += 1

print(result)