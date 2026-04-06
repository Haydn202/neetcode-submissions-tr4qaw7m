# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()

        if root:
            queue.append(root)

        level = 0
        result = []

        while len(queue) > 0:
            levelItems = []
            for i in range(len(queue)):
                current = queue.popleft()
                levelItems.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
            
            result.append(levelItems)
            level += 1
                
        return result 
                    
                    