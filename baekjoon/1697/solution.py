#최단거리 찾기
#초는 움직인 수 카운트?
#K에 도달할 수 있는 방법 중 가장 빨리 도착하는 것을 찾으면 됨
#17에 도달하는 방법: 1.K-1 2.K+1 3.K/2
# 간선 루프 돌 수 있으니 방문 리스트를 만들어 표시해
# 탐색 범위가 0 ≤ N ≤ 100,000 이므로 방문리스트의 크기는 100,001개

#BFS
#수빈과 동생 위치 입력받고
# 방문 리스트 만들어
#이동위치 N+1, N-1 , N*2 
#큐에 수빈 위치 넣어. + 카운트(시간)도 / 시작 위치 방문했으니 큐 넣을 때에 true
#큐 빌동안 팝, 카운트 1 하고, 이동위치로 이동해봐. 
#팝 했을 때 K랑 동일하면 out, 카운트 리턴
#예외? N,K 위치가 같은 경우 -> 0, K의 위치가 0인 경우..?

from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int, input().split())

visited = [False] * 100001

def bfs (N,K) :
  q = deque()
  visited[N] = True
  q.append((N, 0))

  while q: 
    x, time  = q.popleft()

    if x == K : 
      return time

    for nx in (x-1, x+1, x*2) :
      if 0<= nx <= 100000 and not visited[nx] :
        visited[nx] = True
        q.append((nx, time +1))

print(bfs(N,K))