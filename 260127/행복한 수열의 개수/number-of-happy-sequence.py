n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
num_list = []
for i in range(n):
    tmp_list1 = []
    tmp_list2 = []
    for j in range(n):
        tmp_list1.append(grid[i][j])
        tmp_list2.append(grid[j][i])
    num_list.append(tmp_list1)
    num_list.append(tmp_list2)
num_cnt = 0
for i in range(len(num_list)):
    tmp_list = num_list[i]
    tmp_val = 1
    for j in range(len(tmp_list)-1):
        if tmp_list[j] == tmp_list[j+1]:
            tmp_val += 1
    if tmp_val >= m:
        num_cnt += 1
print(num_cnt)

    