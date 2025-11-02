from copy import deepcopy

n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

temp = deepcopy(blocks)

s1 -= 1
e1 -= 1
s2 -= 1
e2 -= 1

del temp[s1:e1+1]


del temp[s2:e2+1]

print(len(temp))


for block_num in temp:
    print(block_num)
