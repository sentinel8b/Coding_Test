
N, M, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

max_total_value = 0

def get_max_value_from_block(items):
    max_value_for_block = 0  

    def find_best_subset(index, current_weight, current_value):
        nonlocal max_value_for_block

        if index == M:
            max_value_for_block = max(max_value_for_block, current_value)
            return

        find_best_subset(index + 1, current_weight, current_value)

        item_weight = items[index]
        if current_weight + item_weight <= C:
            find_best_subset(index + 1, current_weight + item_weight, current_value + item_weight**2)

    find_best_subset(0, 0, 0)
    return max_value_for_block


max_values_grid = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N - M + 1):
        block = grid[r][c : c + M]
        max_values_grid[r][c] = get_max_value_from_block(block)


for r1 in range(N):
    for c1 in range(N - M + 1):
        value1 = max_values_grid[r1][c1]

        for c2 in range(c1 + M, N - M + 1):
            value2 = max_values_grid[r1][c2]
            max_total_value = max(max_total_value, value1 + value2)

        for r2 in range(r1 + 1, N):
            for c2 in range(N - M + 1):
                value2 = max_values_grid[r2][c2]
                max_total_value = max(max_total_value, value1 + value2)

print(max_total_value)