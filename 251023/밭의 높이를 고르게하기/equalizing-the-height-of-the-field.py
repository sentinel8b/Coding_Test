import sys

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize

# Please write your code here.
for i in range(N-T+1):
    diff = 0
    for j in range(i, i+T):
        diff += abs(H-arr[j])
    ans = min(ans, diff)

print(ans)