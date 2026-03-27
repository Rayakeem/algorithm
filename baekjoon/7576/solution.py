# 좌표랑 같이 day를 저장함
# 한번에 큐에 넣기: 그리드를 이중 포문으로 돌면서 1인 것들을 다 넣어 , day는 0으로
# 큐 한번에 돌리기
# 팝하고 좌표 이동, 범위 안이고 그리드 좌표값이 0이면 인큐, 방문처리 1 하고, day를 + 1 함
# max_day를 구하는 법: 동시에 큐가 퍼지니까 가장 늦게 도착한 큐를 찾아야 최종적으로 토마토가 다 익은 것임. 그래서 max()사용
# max_day = 0 해놓고, 큐를 pop했을 때 max_day와 현재 팝한 좌표의 day를 비교해서 저장
# 출력에서 다시 이중 포문 돌면서 남은 0이 있나 확인 -> 있으면 -1 프린트, exit(), 포문 안에서는 break안된다
# 0이 없으면 max_day 출력


# 1이 두 개 인 경우는 어떻게 처리..? -> 한번에 큐에 넣고 다중 bfs
#M 가로 N 세로, 사방으로만 움직임

#day를 튜플로 같이 저장하는 방식

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
grid = []
q = deque()

for _ in range(N):
  grid.append(list(map(int, input().split())))

dir = [ (1,0), (0,1), (-1,0), (0,-1)]

# 처음에 1을 전부 queue에 넣어
for i in range(N) :
  for j in range(M):
    if grid[i][j] == 1:
      q.append((i,j,0))

max_day = 0

#BFS
while q:
  x, y, d = q.popleft()

  max_day = max(max_day, d)

  for ax, ay in dir :
    nx = ax + x
    ny = ay + y

    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0 :
      q.append((nx, ny, d + 1))
      grid[nx][ny] = 1 #방문 익음 처리

#출력
for row in grid:
  if 0 in row :
    print(-1)
    exit()

print(max_day)
    
# --------------------------------------------------
# day를 좌표 값으로 입력하는 방법
# 1인 곳은 이미 익음(0일) -> 다음으로 익는 곳은 이전 곳의 + 1 (2일) -> ... 즉, 출력할 때는 일 수를 -1 해주어야 한다

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
grid = []
q = deque()

for _ in range(N):
  grid.append(list(map(int, input().split())))

dir = [ (1,0), (0,1), (-1,0), (0,-1)]

for i in range(N) :
  for j in range(M) :
    if grid[i][j] == 1 :
      q.append((i,j))

#bfs
while q:
  x, y = q.popleft()

  for ax, ay in dir :
    nx = ax + x
    ny = ay + y

    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0 :
      q.append((nx, ny))
      grid[nx][ny] = grid[x][y] + 1

#출력
max_day = 0

for r in range(N) :
  for v in range(M):
    if grid[r][v] == 0 :
      print(-1)
      exit()

    max_day = max(max_day, grid[r][v])
  
print(max_day-1)