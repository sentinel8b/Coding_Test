from collections import deque

n = int(input())

# type 0 : -1
# type 1 : +1
# type 2 : if n%2 == 0 -> n // 2
# type 3 : if n%3 == 0 -> n // 3

def can_go(op_type, curr_num):
    if op_type == 2:
        if curr_num%2 != 0:
            return False
    if op_type == 3:
        if curr_num%3 != 0:
            return False

    return True

def excute_op(op_type, curr_num):
    if op_type == 0:
        return curr_num - 1
    if op_type == 1:
        return curr_num + 1
    if op_type == 2:
        return curr_num//2
    if op_type == 3:
        return curr_num//3


bfs_q = deque()
for op_idx in range(4):
    if can_go(op_idx, n):
        bfs_q.append((op_idx, n, 0))

while bfs_q:
    op_idx, curr_num, step = bfs_q.popleft()

    if curr_num == 1:
        print(step)
        break

    new_num = excute_op(op_idx, curr_num)
    for op_idx in range(4):
        if can_go(op_idx, new_num):
            bfs_q.append((op_idx, new_num, step+1))



        