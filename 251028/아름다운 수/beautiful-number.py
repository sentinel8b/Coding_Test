n = int(input())

cnt = 0

def make_sequence(curr_len):
    global cnt
    if curr_len == n:
        cnt += 1
        return
    if curr_len > n:
        return

    for block in ['1', '22', '333', '4444']:
        make_sequence(curr_len+len(block))

make_sequence(0)

print(cnt)