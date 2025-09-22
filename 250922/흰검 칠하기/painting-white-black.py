n = int(input())
cur_idx = 0
tiles = {}

for i in range(n):
    dx, dir_str = input().split()
    dx = int(dx)
    if dir_str == 'L':
        for i in range(cur_idx, cur_idx-dx, -1):
            tile_info = tiles.get(i, {'W' : 0, 'B' : 0, 'last_color' : None})
            if tile_info['last_color'] == 'G':
                continue
            else:
                tile_info['W'] += 1
                tile_info['last_color'] = 'W'
                if tile_info['W'] >= 2 and tile_info['B'] >= 2:
                    tile_info['last_color'] = 'G'
                tiles[i] = tile_info
        cur_idx -= dx
        cur_idx += 1
    else:
        for i in range(cur_idx, cur_idx + dx):
            tile_info = tiles.get(i, {'W' : 0, 'B' : 0, 'last_color' : None})
            if tile_info['last_color'] == 'G':
                continue
            else:
                tile_info['B'] += 1
                tile_info['last_color'] ='B'
                if tile_info['W'] >= 2 and tile_info['B'] >= 2:
                    tile_info['last_color'] = 'G'
                tiles[i] = tile_info
        cur_idx += dx
        cur_idx -= 1
blk = 0
white = 0
gray = 0

for i in tiles.keys():
    tile_info = tiles.get(i, None)
    if tile_info:
        color = tile_info['last_color']
        if color == 'B':
            blk +=1
        elif color == 'W':
            white += 1
        elif color == 'G':
            gray += 1

print(white, blk, gray)
