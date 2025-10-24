n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]

def in_range(x, y):
    return x>=0 and x < n and y>=0 and y<n

max_val = 0

for x in range(n):
    for y in range(n):
        for k in range(1,n): # R
            for l in range(1,n): # L
                p1 = (x,y) #start
                p2 = (x-k, y+k) #move1
                p3 = (x-k-l, y+k-l) #move2
                p4 = (x-l, y-l) #move3
                
                if in_range(p2[0], p2[1]) and in_range(p3[0], p3[1]) and in_range(p4[0], p4[1]):
                    current_sum = 0
                    for dir_idx, repeat in enumerate([k,l,k,l]):
                        for _ in range(repeat):
                            dx, dy = dxs[dir_idx], dys[dir_idx]
                            x = x+dx
                            y = y+dy
                            current_sum += grid[x][y]
                    max_val = max(max_val, current_sum)

print(max_val)



