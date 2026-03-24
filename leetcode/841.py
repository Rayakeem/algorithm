#DFS

def sol(rooms):

  visited = set()

  def dfs(cur_r):
    visited.add(cur_r)
    for k in rooms[cur_r]:
      if k not in visited :
        dfs(k)

  dfs(0)

  if len(visited) == len(rooms) :
    return print(True)
  else :
    return print(False)
    
sol(rooms = [[0,1],[2,0],[3],[]])