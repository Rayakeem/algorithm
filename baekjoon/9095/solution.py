import sys
input = sys.stdin.readline

#갯수 입력
N = int(input())

#Top-dowm
memo = {}

def dfs(K) :
  #base case
  if K == 1 : return 1
  if K == 2 : return 2
  if K == 3 : return 4

  #memo out
  if K in memo:
    return memo[K]

  #memoization
  if K not in memo:
    memo[K] = dfs(K-1) + dfs(K-2) + dfs(K-3)
    return memo[K]
  
for _ in range(N):
  K = int(input())
  print(dfs(K))


#bottom-up

#갯수 입력
N = int(input())

#배열
dp = [0] * 11

#초기식
dp[1] = 1
dp[2] = 2
dp[3] = 4

#점화식 - 미리 다 계산
for i in range(4, 11) :
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(N) :
  k = int(input())
  print(dp[k])