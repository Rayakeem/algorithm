import sys
input = sys.stdin.readline

T = int(input())

# 최대 n이 10이니까 미리 다 구해놓기
dp = [0] * 11

dp[1] = 1  # 1
dp[2] = 2  # 1+1, 2
dp[3] = 4  # 1+1+1, 1+2, 2+1, 3

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])