#그래프 문제
# 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력
# BSF, 큐
# 시작이 0,0에서 그리드의 범위 이내, 방문하지 않은 1이면 큐에 넣어, cnt +=1 <- 집 갯수 
# 큐에서 빼서 사방으로 좌표 넘긴다음 마찬가지로 범위 이내, 방문하지 않은 1이면 인큐 + 0으로 바꿔 (방문 표시)
# 큐가 비면 단지 1개 완성 단지 변수에 넣어. 단지 += 1; 집갯수 리스트에 cnt 넣어.
# 큐가 다 비었고, 그리드 끝에 다다르면 (n.n) 방문 끝
# 단지 출력, 집갯수 리스트 오름차순 한 다음 출력 <- 오름차순 시간복잡도 있을 수 있으니 다른 방법으로 해도 좋을 것 같음

#이중 for문으로 0,0부터 방문 시작 -> 좌표값이 1이면 bfs/dfs 넣어
#cnt =1 , 방문 표시 0으로 해
#좌표 상하좌우 옮겨놓고 좌표값 1이고 범위 안이면 bfs/dfs. , 방문 표시
#sort() 하고 길이로 단지 출력

#bfs
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

result = []
graph = []
dir = [ (-1,0), (1,0), (0,1), (0,-1)]

#그래프 입력받기
for _ in range(N):
    graph.append(list(map(int, input().strip())))

def bfs (graph, a, b ): 

  q = deque()
  q.append((a, b))
  graph[a][b] = 0
  count = 1 #들어오면서 첫번째 집 a,b 를 방문했기 때문에 count값을 1로 시작한다.

  while q: 
    x, y = q.popleft()

    for ax, ay in dir :
      nx = ax + x
      ny = ay + y

      if 0 <= nx < N and 0<= ny <N and graph[nx][ny] == 1 :
        q.append((nx, ny))
        graph[nx][ny] = 0
        count += 1 #좌표 옮기고 새로운 좌표에서 카운트

  return count

for i in range(N):
  for j in range(N) :
    if graph[i][j] == 1 :
      result.append(bfs(graph, i, j))

result.sort()

print(len(result))
for home in result:
  print(home)


#dfs
import sys
input = sys.stdin.readline

N = int(input())
graph = []
result = []

for _ in range(N) :
  graph.append(list(map(int, input().strip())))

dir = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs (a, b):
  graph[a][b] = 0
  count = 1

  for x, y in dir :
    nx = x + a
    ny = y + b

    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 :
      count += dfs(nx, ny)

  return count

for i in range(N) :
  for j in range(N) :
    if graph[i][j] == 1 :
      result.append(dfs(i,j))

result.sort()
print(len(result))
for k in result :
  print(k)