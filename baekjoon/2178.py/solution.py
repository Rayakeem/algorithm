# from collections import deque
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# #grid
# grid = []

# for _ in range(N) :
#   grid.append(list(map(int, input().strip()))) #공백없는 입력은 strip

# #최단거리 - bfs
# #시작위치부터 dist 1, 1로만 지나다녀야 하고 상하좌우 움직일 수 있음
# #1,1부터 시작해서 (N(세로 y),M(가로 x))에서 break
# #예외: 시작부터 0인경우- 0?
# # 좌표와 거리를 함께 저장하여 넘겨, 좌표 이동할때 거리 + 1

# dir = [(1,0), (0,1), (0, -1), (-1, 0)]

# def bfs(a, b, dist) :
#   q = deque()
#   q.append((a,b,dist))
#   grid[a][b] = 0

#   while q:
#     a, b, dist = q.popleft()

#     # 도달
#     if a == N-1 and b == M-1:
#       return dist

#     for x, y in dir :
#       nx = a + x
#       ny = b + y

#       if nx >= 0 and nx < N and ny >= 0 and ny < M and grid[nx][ny] == 1:
#         q.append((nx, ny, dist + 1))
#         grid[nx][ny] = 0

#   return dist

# result = bfs(0,0,1)
# print(result)



from collections import deque
import sys
input = sys.stdin.readline


# N 세로, M 가로 x가 N , y가 M
# 끝에 도달하면 리턴, 도달 안하면 0? 
# 좌표랑 거리를 함께 저장하고, 리턴할 때 거리 반환
# 방문했으면 표시로 0으로 바꿔줘


N, M = map(int, input().split())
grid = []

dir = [ (1,0), (0,1), (-1,0), (0,-1) ]

for _ in range(N) :
  grid.append(list(map(int, input().strip())))

def bfs(a, b, d, grid) :
  if not grid:
    return 0
  
  if grid[a][b] == 0 :
    return 0
  
  q = deque()
  q.append((a,b,d))
  grid[a][b] = 0

  while q: 
    x, y, dist = q.popleft()

    #escape
    if x == N -1 and y == M -1 :
      return dist

    for ax, ay in dir :
      nx = ax + x
      ny = ay + y

      if 0 <= nx and nx < N and 0 <= ny and ny < M and grid[nx][ny] == 1 :
        q.append((nx, ny , dist + 1))
        grid[nx][ny] = 0

  return 0

print(bfs(0,0,1, grid))