# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxval):

            if not root:
                return 0
            
            result = 1 if root.val >= maxval else 0
            maxval = max(maxval, root.val)

            result += dfs(root.left, maxval)
            result += dfs(root.right, maxval)
            return result
        
        return dfs(root, -101)

        
        