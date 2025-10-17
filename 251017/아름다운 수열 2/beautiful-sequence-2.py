from itertools import permutations

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
cnt = 0

def get_possible_sequence(seq_list):
    return set(permutations(seq_list, M))

possible_seq = get_possible_sequence(B)

for seq in possible_seq:
    for i in range(len(A) - M + 1):
        if A[i:i+M] == list(seq).copy():
            cnt += 1

print(cnt)