# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:  
        length = 0 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length += 2
        
        def reveres(node):
            prev = None
            current = node
            following = None

            while current:
                following = current.next
                current.next = prev
                prev = current
                current = following
            
            return prev

        mid = slow.next
        slow.next = None

        rev = reveres(mid)
        
        p1, p2 = head, rev

        while p2:
            tmp1, tmp2 = p1.next, p2.next
            p1.next = p2
            p2.next = tmp1
            p1, p2 = tmp1, tmp2
        




