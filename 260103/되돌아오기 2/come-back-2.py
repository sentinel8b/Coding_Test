commands = input()

# Please write your code here.
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

init_dir = 3
init_loc = [0,0]
result = -1
for i in range(len(commands)):
    if commands[i] == 'F':
        init_loc[0] += dx[init_dir]
        init_loc[1] += dy[init_dir]
    elif commands[i] == "R":
        init_dir = (init_dir + 1) % 4
    elif commands[i] == "L":
        init_dir = (init_dir - 1 + 4) % 4
    if init_loc[0] == 0 and init_loc[1] == 0:
        result = i + 1
        break
print(result)