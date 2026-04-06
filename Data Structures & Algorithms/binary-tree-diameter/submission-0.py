# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def nodeHeight(node: Optional[TreeNode]):
            if not node:
                return 0
            
            leftHeight = nodeHeight(node.left)
            rightHeight = nodeHeight(node.right)

            currentDiameter = leftHeight + rightHeight

            if currentDiameter > self.diameter:
                self.diameter = currentDiameter
                
            return 1 + max(leftHeight, rightHeight)
        
        nodeHeight(root)
        
        return self.diameter
