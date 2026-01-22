N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
result = 0
for i in range(N-M+1):
    if sorted(A[i:i+M]) == sorted(B):
        result += 1
print(result)