n = int(input())

tiles = {}
cur_idx = 0
# Please write your code here.
for i in range(n):
    dx, dir_str = input().split()
    dx = int(dx)
    if dir_str == 'R':
        start_idx = cur_idx
        end_idx = cur_idx + dx
        for j in range(start_idx, end_idx):
            tile_info = tiles.get(j, {'color' : None})
            tile_info['color'] = 'B'
            tiles[j] = tile_info
        cur_idx = end_idx - 1
    else:
        start_idx = cur_idx
        end_idx = cur_idx - dx
        for j in range(start_idx, end_idx, -1):
            tile_info = tiles.get(j, {'color' : None})
            tile_info['color'] = 'W'
            tiles[j] = tile_info
        cur_idx = end_idx + 1

blk = 0
white = 0

for tile_info in tiles.values():
    color = tile_info['color']
    if color == 'B':
        blk += 1
    elif color == 'W':
        white += 1

print(white, blk)

