# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxPrev) -> int:
            result = 0

            if not node:
                return result

            if node.val >= maxPrev:
                result += 1        
            
            current_max = max(maxPrev, node.val)
            left = dfs(node.left, current_max)
            right = dfs(node.right, current_max)

            result = result + left + right

            return result
        
        return dfs(root, float('-inf'))

