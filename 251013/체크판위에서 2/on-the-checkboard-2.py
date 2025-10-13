import sys

# 재귀 깊이 제한을 풀어주는 것이 좋음 (문제의 R, C가 작아서 필수는 아님)
# sys.setrecursionlimit(10**6) 

def solve():
    R, C = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().split()) for _ in range(R)]

    # (r, c) 위치에서 jump_count 만큼 점프해서 도달했을 때,
    # 앞으로 도착지까지 갈 수 있는 경로의 수를 반환하는 함수
    def dfs(r, c, jump_count):
        # 기저 사례: 점프 3번을 완료했을 때
        if jump_count == 3:
            # 도착점에 정확히 도달했다면 성공(1), 아니면 실패(0)
            if r == R - 1 and c == C - 1:
                return 1
            else:
                return 0

        # 재귀 단계: 다음 점프 위치를 탐색
        path_count = 0
        current_color = grid[r][c]

        # 현재 위치 (r, c)보다 아래쪽, 오른쪽에 있는 모든 칸을 탐색
        for nr in range(r + 1, R):
            for nc in range(c + 1, C):
                # 점프 조건: 색깔이 달라야 함
                if grid[nr][nc] != current_color:
                    # 다음 위치에서부터 탐색을 계속하고, 거기서 찾은 경로의 수를 더함
                    path_count += dfs(nr, nc, jump_count + 1)
        
        return path_count

    # 시작점 (0, 0)에서 점프 0번으로 시작
    # 시작점의 색깔은 'W' 또는 'B' 중 하나이므로, grid[0][0]과 다른 색깔을 가진 곳으로만 첫 점프가 가능
    # 하지만 첫 점프는 색깔만 다르면 되므로 로직은 동일
    answer = dfs(0, 0, 0)
    print(answer)

# 입력을 빠르게 받기 위해 stdin.readline 사용 권장
# 만약 터미널에서 직접 실행하신다면 input()을 사용하셔도 됩니다.
if __name__ == "__main__":
    solve()