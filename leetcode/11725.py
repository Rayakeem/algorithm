from collections import deque
import sys

#인접그래프(리스트) 생성
N = int(input())
tree = [ [] for _ in range(N+1)] #노드 갯수를 tree안에서 인덱스로 사용

#그래프 연결
for _ in range(N-1):
  a,b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

#부모노드 리스트 만들기
parent = [0] * (N+1)
parent[1] = -1           # 루트 방문 처리
q = deque([1])

#BFS 순회하면서 부모리스트에 넣기
while q:
  cur = q.popleft()

  for nxt in tree[cur]:
    if parent[nxt] == 0:
      parent[nxt] = cur

      q.append(nxt)

#부모리스트를 인덱스 2번부터 N+1개까지 출력 
for i in range(2, N+1):
  print(parent[i])