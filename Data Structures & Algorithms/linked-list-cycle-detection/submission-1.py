# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        cycleIndex = -1
        index = 0

        visited = {}
        current = head

        while current.next and cycleIndex == -1:
            if current.val in visited:
                cycleIndex = index
                break
            
            visited[current.val] = index
            current = current.next
            index += 1
        
        return cycleIndex != -1