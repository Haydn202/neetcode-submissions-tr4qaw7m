# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        sum = targetSum - root.val

        isLeaf = not root.left and not root.right

        if sum == 0 and isLeaf:
            return True
        
        if root.left:
            if self.hasPathSum(root.left, sum):
                return True
        
        if root.right:
            if self.hasPathSum(root.right, sum):
                return True
        
        return False