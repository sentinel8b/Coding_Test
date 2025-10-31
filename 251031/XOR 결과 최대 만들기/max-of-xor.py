import copy
n, m = map(int,input().split())
num_list = list(map(int, input().split()))

max_val = 0
choosen_nums = []

def calc_xor(num_list):
    result = 0 
    for num in num_list:
        result = result ^ num
    return result


def pick(idx, cnt):
    global choosen_nums
    global max_val

    #base cond
    if cnt == m:
        choosen_nums_copy = copy.deepcopy(choosen_nums)
        case_xor_dec = calc_xor(choosen_nums_copy)
        max_val = max(max_val, case_xor_dec)
        return

    if idx == n:
        return

    # pick
    choosen_nums.append(num_list[idx])
    pick(idx+1, cnt + 1)
    choosen_nums.pop()

    #pass
    pick(idx+1, cnt)

pick(0,0)
print(max_val)