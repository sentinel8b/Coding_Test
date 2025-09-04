n = int(input())

# Please write your code here.

def pinrt_nums_n_by_n(n :int):
    j = 1
    for i in range(n):
        for _ in range(n):
            print(j, end = " ")
            j += 1
            if j == 10:
                j = 1
        print()

pinrt_nums_n_by_n(n)