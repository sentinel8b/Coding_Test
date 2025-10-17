from itertools import permutations

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
cnt = 0

sorted_B = sorted(B)

for i in range(len(A) - M + 1):
    if sorted(A[i:i+M]) == sorted_B:
        cnt += 1

print(cnt)