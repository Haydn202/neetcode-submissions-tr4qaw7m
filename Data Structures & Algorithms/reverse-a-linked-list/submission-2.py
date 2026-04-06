# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
            
        return self.recursive(head, None)

    def iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous
    
    def recursive(self, current: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if current.next:
            result = self.recursive(current.next, current)
        else:
            result = current

        current.next = prev
        return result
    