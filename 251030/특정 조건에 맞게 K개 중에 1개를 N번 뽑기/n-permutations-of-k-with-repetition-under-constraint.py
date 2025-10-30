k, n = map(int, input().split())

num_seq = []

def print_num():
    global num_seq
    for num in num_seq:
        print(num, end = ' ')
    print()

def is_valid():
    global num_seq
    if len(num_seq) >= 3:
        if num_seq[-1] == num_seq[-2] and num_seq[-2] == num_seq[-3]:
            return False
        else:
            return True
    else:
        return True

def choose_num(idx):
    global num_seq
    if idx == n:
        if is_valid():
            print_num()
        return
    
    if not is_valid():
        return


    for i in range(1,k+1):
        num_seq.append(i)
        choose_num(idx+1)
        num_seq.pop()


choose_num(0)