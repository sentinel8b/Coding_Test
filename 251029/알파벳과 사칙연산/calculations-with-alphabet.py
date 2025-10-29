import sys
input_str = input()

unique_chars_set = set()
op_list = []
for char in input_str:
    if char.isalpha():
        unique_chars_set.add(char)
    else:
        op_list.append(char)

unique_chars_list = list(unique_chars_set)
num_unique_chars = len(unique_chars_list)

max_val = -sys.maxsize

value_map = {} 

def calc_eq(num_list):
    result = num_list[0]
    for i in range(len(op_list)):
        op = op_list[i]
        next_num = num_list[i+1]
        
        if op == '+':
            result += next_num
        elif op == '-':
            result -= next_num
        elif op == '*':
            result *= next_num
            
    return result

def backtrack_max_val(idx):
    global max_val
    global value_map

    if idx == num_unique_chars:
        
        num_list = []
        for char in input_str:
            if char.isalpha():
                num_list.append(value_map[char]) 
        
        # 5. 생성된 num_list로 식 계산
        case_val = calc_eq(num_list)
        max_val = max(max_val, case_val)
        return

    current_char = unique_chars_list[idx]
    for i in range(1, 4 + 1):
        value_map[current_char] = i    
        backtrack_max_val(idx + 1)     

backtrack_max_val(0)

print(max_val)