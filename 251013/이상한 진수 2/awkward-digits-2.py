a = list(input())

def change_idx(bin_num_list, idx):
    temp_list = bin_num_list.copy()
    if temp_list[idx] == '1':
        temp_list[idx] = '0'
    else:
        temp_list[idx] = '1'

    return "".join(temp_list)

max_val = 0

for i in range(len(a)):
    possible_binary_str = change_idx(a, i)
    
    possible_val = int(possible_binary_str, 2)
    max_val = max(max_val, possible_val)

print(max_val)