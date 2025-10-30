n, m = map(int, input().split())

choosen_num_list = []

def print_ans():
    for num in choosen_num_list:
        print(num, end = " ")
    print()

def choose(idx, cnt):
    global choosen_num_list
    if cnt == m:
        print_ans()
        return
        
    if idx ==n:
        return
    
    # pick cur_num
    choosen_num_list.append(idx+1)
    choose(idx+1, cnt +1)
    choosen_num_list.pop()
    # pass
    choose(idx+1, cnt)

choose(0,0)
    
