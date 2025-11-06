from collections import deque

n = int(input())

MAX_SIZE = 2000001 
visited = [False] * MAX_SIZE

bfs_q = deque()
bfs_q.append((n, 0))
visited[n] = True  

while bfs_q:
    curr_num, step = bfs_q.popleft()

    if curr_num == 1:
        print(step)
        break

    next_num = curr_num - 1
    if next_num > 0 and not visited[next_num]:
        visited[next_num] = True
        bfs_q.append((next_num, step + 1))

    next_num = curr_num + 1
    if next_num < MAX_SIZE and not visited[next_num]:
        visited[next_num] = True
        bfs_q.append((next_num, step + 1))

    if curr_num % 2 == 0:
        next_num = curr_num // 2
        if not visited[next_num]:
            visited[next_num] = True
            bfs_q.append((next_num, step + 1))

    if curr_num % 3 == 0:
        next_num = curr_num // 3
        if not visited[next_num]:
            visited[next_num] = True
            bfs_q.append((next_num, step + 1))