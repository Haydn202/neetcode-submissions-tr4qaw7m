# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maxAve = 0

        def dfs(node):
            nonlocal maxAve

            if not node:
                return 0, 0  # sum, count

            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)

            total = leftSum + rightSum + node.val
            count = leftCount + rightCount + 1

            ave = total / count
            maxAve = max(maxAve, ave)

            return total, count

        dfs(root)

        return maxAve