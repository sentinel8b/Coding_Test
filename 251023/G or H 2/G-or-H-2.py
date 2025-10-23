n = int(input())
arr = [None] * (100 + 1) 

for _ in range(n):
    pos_str, char = input().split()
    arr[int(pos_str)] = char

max_size = 0

for start_idx in range(101):
    for end_idx in range(start_idx, 101):
        
        cnt_g = 0
        cnt_h = 0
        pos_first = -1 
        pos_last = -1 
        
        for idx in range(start_idx, end_idx + 1):
            if arr[idx] is not None:
                pos_last = idx 
                
                if pos_first == -1:
                    pos_first = idx
                
                if arr[idx] == 'G':
                    cnt_g += 1
                elif arr[idx] == 'H':
                    cnt_h += 1
        
        if pos_first == -1:
            continue
        is_valid = False
        
        if cnt_g > 0 and cnt_h == 0:
            is_valid = True
        elif cnt_h > 0 and cnt_g == 0:
            is_valid = True
        elif cnt_g > 0 and cnt_g == cnt_h:
            is_valid = True

        if is_valid:
            current_size = pos_last - pos_first
            max_size = max(max_size, current_size)

print(max_size)