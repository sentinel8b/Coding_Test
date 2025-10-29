import sys
input_str = input()

char_cnt = 0
op_list = []
for char in input_str:
    if char.isalpha():
        char_cnt += 1
    else:
        op_list.append(char)

max_val = -sys.maxsize
num_list = []

def calc_eq(num_list):
    # 첫 번째 숫자를 초기 결과값으로 설정
    result = num_list[0]
    
    # op_list를 순회하면서 연산을 차례대로 적용
    # i는 0부터 op_list의 길이 - 1 까지
    for i in range(len(op_list)):
        op = op_list[i]
        next_num = num_list[i+1] # 연산할 다음 숫자
        
        if op == '+':
            result += next_num
        elif op == '-':
            result -= next_num
        elif op == '*':
            result *= next_num
            
    return result

def backtrack_max_val(idx):
    global max_val
    global num_list

    if idx == char_cnt:
        case_val = calc_eq(num_list)
        max_val = max(max_val, case_val)
        return

    for i in range(1,4+1):
        num_list.append(i)
        backtrack_max_val(idx + 1)
        num_list.pop()

backtrack_max_val(0)

print(max_val)