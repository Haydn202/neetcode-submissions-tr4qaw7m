# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        commonDescendant = None

        def dfs(node) -> TreeNode:
            if not node:
                return None
            
            if p.val >= node.val >= q.val or p.val <= node.val <= q.val:
                return node
            
            if p.val > node.val and q.val > node.val:
                right = dfs(node.right)
                if right:
                    return right

            if p.val < node.val and  q.val < node.val:
                left = dfs(node.left)
                if left:
                    return left   

            return None

        
        return dfs(root)
        