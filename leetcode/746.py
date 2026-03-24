class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {}

        def dfs(i):
            #1. base case
            if i <= 1 :
                return 0
            
            #2. memo check
            if i in memo:
                return memo[i]
            
            #3. 계산
            memo[i] = min(
              dfs(i-1) + cost[i-1],
              dfs(i-2) + cost[i-2]
            )
            return memo[i]


        return dfs(n)

# 실행
sol = Solution()
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))