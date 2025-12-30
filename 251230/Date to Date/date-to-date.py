m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d_start = d2 - d1 + 1

num_of_days_tmp = num_of_days[m1:m2]

m_tmp = 0
for i in num_of_days_tmp:
    m_tmp += i

print(m_tmp+d_start)