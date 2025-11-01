n, m, q = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def push(r, d):
    if d == 'R':
        temp = building[r][0]
        for i in range(m-1):
            building[r][i] = building[r][i+1]
        building[r][-1] = temp
    else: # L
        temp = building[r][-1]
        for i in range(m-1, 0, -1):
            building[r][i] = building[r][i-1]
        building[r][0] = temp

def in_range(r):
    return 0<=r<n

for r_init, d_init in winds:
    r_init -= 1 # 0-based 인덱싱
    
    prop_stack = [(r_init, d_init)]
    visited = set() 

    while prop_stack:
        r, d = prop_stack.pop()

        if r in visited:
            continue
            
        push(r, d)
        visited.add(r) 

        new_dir = 'L' if d == 'R' else 'R'
        pivot_row = building[r] 

        for offset in [-1, 1]:
            next_r = r + offset

            if not in_range(next_r) or next_r in visited:
                continue

            offset_row = building[next_r]
            has_match = False
            for i in range(m):
                if pivot_row[i] == offset_row[i]:
                    has_match = True
                    break

            if has_match:
                prop_stack.append((next_r, new_dir))

for row in building:
    print(*row) 