from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if not grid:
            return -1
        
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        def bfs(ax, ay, ad):
          
          dir = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1),(-1,1), (1,-1), (1,1)]
          
          q = deque([(ax,ay,ad)])
          grid[0][0] = 1

          while q:
              x, y, d= q.popleft()
              if x == n-1 and y == n-1:
                  return d 

              for ax, ay in dir:
                  nx = x+ax
                  ny = y+ay

                  if 0<= nx <n and 0<= ny <n and grid[nx][ny] == 0:
                      nd = d + 1
                      q.append((nx, ny, nd))
                      grid[nx][ny] = 1
          return -1 #큐가 빌 때까지 0을 못 찾으면 끝 (중간에 길이 끊김)
        
        result = bfs(ax = 0, ay = 0, ad = 1 )
        return result

    
        
grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 0, 0]
    ]

sol = Solution()
result = sol.shortestPathBinaryMatrix(grid)
print("RESULT:", result)