N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
result = 0

for i in range(N):
    a = A[i]
    for j in range(i+1, N):
        b = A[j]
        for w in range(j+1, N):
            c = A[w]
            if a <= b and b <= c:
                result += 1
print(result)