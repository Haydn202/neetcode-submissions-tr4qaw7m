# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        def dfs(node):
            if not node:
                return 0, 0, 0

            leftSum, leftCount, leftBest = dfs(node.left)
            rightSum, rightCount, rightBest = dfs(node.right)

            total = leftSum + rightSum + node.val
            count = leftCount + rightCount + 1

            ave = total / count

            best = max(ave, leftBest, rightBest)

            return total, count, best

        _, _, maxAve = dfs(root)

        return maxAve