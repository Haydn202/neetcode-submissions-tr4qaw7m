# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        validRange = (-99999, 99999)

        def dfs(node, validRange) -> bool:
            if not node:
                return True

            minVal, maxVal = validRange

            if node.val >= maxVal or minVal >= node.val:
                return False

            left = dfs(node.left, (minVal, node.val))
            right = dfs(node.right, (node.val, maxVal))

            return left and right


        return dfs(root, validRange)