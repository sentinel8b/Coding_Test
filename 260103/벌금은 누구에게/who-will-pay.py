N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

stdt_list = [0 for _ in range(N+1)]
result = -1
for i in range(len(student)):
    idx = student[i]
    stdt_list[idx] += 1
    if stdt_list[idx] >= K:
        result = idx
        break
print(result)