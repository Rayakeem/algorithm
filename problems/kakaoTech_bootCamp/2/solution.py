#달팽이 채우기

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# 격자 초기화 (-1로 채움)
grid = [[-1] * M for _ in range(N)]

# 방향: 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0  # 시작 위치
dir = 0      # 방향 인덱스

for i in range(K):
    grid[x][y] = arr[i]

    nx = x + dx[dir]
    ny = y + dy[dir]

    # 방향 전환 조건
    if nx < 0 or nx >= N or ny < 0 or ny >= M or grid[nx][ny] != -1:
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]

    x, y = nx, ny

# 출력
for row in grid:
    print(*row)