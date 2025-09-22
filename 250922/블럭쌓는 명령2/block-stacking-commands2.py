n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
stack_list = [0] * n
for i in range(k):
    start_idx, end_idx = commands[i]
    for j in range(start_idx-1, end_idx):
        stack_list[j] += 1

print(max(stack_list))