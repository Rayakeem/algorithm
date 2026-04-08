import sys
input = sys.stdin.readline

N = int(input())

# [0] + cost_list를 받아서 층 수를 맞춰준다.
# 1층과 2층은 베이스케이스로 구해놓는다
# 3층부터 N층까지 반복문을 돌면서 구한다.
# N층을 출력.

# 중요: 시작점을 제외한 계단을 연속으로 한 칸씩 총 두칸을 연속으로 오를 수 없으니, 점화식은 max( (N-2) , (N-3) + cost[N-1] ) + cost[N]

# bottom-up

cost = [0] + [ int(input()) for _ in range(N) ]
# 이렇게 하면 [0, 1,2,3,4,5] 인덱스가 실제 층수와 동일 (0층을 없애기 위함)

memo = [0] * (N+1)

if N < 2 : print(cost[N])
else :
  memo[1] = cost[1]
  memo[2] = cost[2] + memo[1]

  for i in range(3, N+1) :
    memo[i] =max(
        memo[i-2], memo[N-3] + cost[i-1]
      ) + cost[i]
  
  print(memo[N])