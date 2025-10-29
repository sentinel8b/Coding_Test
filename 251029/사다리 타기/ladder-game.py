n, m = map(int, input().split())
ladder_to_use = [list(map(int, input().split())) for _ in range(m)]
min_cnt = 15
selected_line = []

def calculate_result(N, ladder_to_use):
    sorted_ladders = sorted(ladder_to_use, key = lambda x : x[1])
    locations = list(range(1, N+1))
    result = [0] * (N + 1)
    for a, b in sorted_ladders:
        a_idx = a - 1
        temp = locations[a_idx + 1]
        locations[a_idx + 1] = locations[a_idx]
        locations[a_idx] = temp
    
    for i, val in enumerate(locations):
        result[val] = i+1

    return result


def is_valid(selected_line):
    global target_results
    result = calculate_result(n, selected_line)
    if target_results == result:
        return True
    else:
        return False

def select_line(line_idx):
    global selected_line
    global min_cnt

    if line_idx == m:
        if is_valid(selected_line):
            min_cnt = min(min_cnt, len(selected_line))
            return
        else:
            return
    
    # move on to next line
    select_line(line_idx+1)

    # select this line
    selected_line.append(ladder_to_use[line_idx])
    select_line(line_idx+1)
    selected_line.pop()

target_results = calculate_result(n, ladder_to_use)

select_line(0)

print(min_cnt)