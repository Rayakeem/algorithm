class Solution:
    def uniquePaths(self, m, n) :
        
        #dfs 이중리스트
        memo = [ [-1] * n for _ in range(m)]

        def dfs ( r , c):
            
            unique_paths = 0

            #base case
            if r == 0 and c == 0 :
                memo[r][c] = 1

            #memo
            if memo[r][c] == -1 :
                #위 이동
                if r-1 >=0 :
                    unique_paths += dfs (r-1, c)
                #왼쪽 이동
                if c-1 >= 0:
                    unique_paths += dfs (r, c-1)
                  
                memo[r][c] = unique_paths

            return memo[r][c]
        
        return dfs(m-1,n-1)