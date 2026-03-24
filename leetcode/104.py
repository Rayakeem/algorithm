from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#BFS - Level order
class Solution:
    def maxDepth(self, root):
        max_d = 0
        if root is None :
            return max_d

        q = deque()
        q.append((root, 1))

        while q:
            cur_n, cur_d = q.popleft()
            max_d = max(cur_d, max_d)

            if cur_n.left:
                q.append((cur_n.left, cur_d +1))
            if cur_n.right:
                q.append((cur_n.right, cur_d +1))

        return max_d
        

#DFS - post odrder
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        l_d = self.maxDepth(root.left)
        r_d = self.maxDepth(root.right)

        return max(l_d, r_d) + 1   

