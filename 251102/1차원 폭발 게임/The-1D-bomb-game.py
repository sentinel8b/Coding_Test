n, m = map(int, input().split())
bombs = []
for _ in range(n):
    bombs.append(int(input()))

while True:
    exploded = False
    
    new_bombs = []
    
    i = 0
    while i < len(bombs):
        current_num = bombs[i]
        
        j = i
        while j < len(bombs) and bombs[j] == current_num:
            j += 1
        
        count = j - i
        
        if count >= m:
            exploded = True 
        
        else:
            new_bombs.extend(bombs[i:j])
            
        i = j 
        

    if not exploded:
        break  
        
    bombs = new_bombs
    
    if not bombs:
        break

print(len(bombs))
for b in bombs:
    print(b)