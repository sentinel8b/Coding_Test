n = int(input())

seq_list = []

def print_seq(seq_list):
    for num in seq_list:
        print(num, end = '')

def is_valid(seq_list):
    L = len(seq_list)
    max_k = L // 2

    for k in range(1, max_k+1):
        if seq_list[L-k:L] == seq_list[L-2*k:L-k]:
            return False
    
    return True

    

def make_seq(idx):
    global seq_list
    if idx == n:
        if is_valid(seq_list):
            print_seq(seq_list)
            exit()

    for i in range(4,6+1):
        seq_list.append(i)
        if is_valid(seq_list):
            make_seq(idx+1)
        seq_list.pop()

make_seq(0)            