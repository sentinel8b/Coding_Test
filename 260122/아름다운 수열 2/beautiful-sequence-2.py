N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
result = 0
for i in range(N-M+1):
    tmp_val = 0
    for j in range(i, i+M):
        if A[j] in B:
            tmp_val += 1
    if tmp_val == M:
        result += 1
print(result)