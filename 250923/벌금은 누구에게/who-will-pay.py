N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
penality_list = [0] * (N + 1)

for target in student:
    penality_list[target] += 1
    if penality_list[target] == K:
        print(target)
        break