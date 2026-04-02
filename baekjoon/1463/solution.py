import sys
input = sys.stdin.readline

N = int(input())

# # dp[i] = i를 1로 만드는 최소 연산 횟수
# dp = [0] * (N + 1)

# for i in range(2, N + 1):
#     # 1 빼기
#     dp[i] = dp[i - 1] + 1

#     # 2로 나누어 떨어지면
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)

#     # 3으로 나누어 떨어지면
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)

# print(dp[N])

# Top-Down
memo = {}

def dfs(n):
    # base case
    if n == 1:
        return 0

    # memo
    if n in memo:
        return memo[n]

    # 계산
    res = dfs(n - 1) + 1

    if n % 2 == 0:
        res = min(res, dfs(n // 2) + 1)

    if n % 3 == 0:
        res = min(res, dfs(n // 3) + 1)

    memo[n] = res
    return res

print(dfs(N))