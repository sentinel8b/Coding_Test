m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.m1, d1, m2, d2 = map(int, input().split())


def guess_day(m1, d1, m2, d2):
    day_name = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    max_date_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def get_day_of_yr(m, d):
        total_days = 0
        for month in range(1, m):
            total_days += max_date_per_month[month]
        total_days += d
        return total_days

    day1_of_year = get_day_of_yr(m1, d1)
    day2_of_year = get_day_of_yr(m2, d2)
    
    # 두 날짜 간의 차이 계산 (m2, d2가 m1, d1보다 빠르면 음수)
    diff_days = day2_of_year - day1_of_year
    
    # '월요일'을 0으로 하는 요일 인덱스
    start_day_index = 0
    
    # 최종 요일 인덱스 계산 (음수 처리 포함)
    result_index = (start_day_index + diff_days) % 7
    if result_index < 0:
        result_index += 7
    
    return day_name[result_index]

ans = guess_day(m1, d1, m2, d2)
print(ans)