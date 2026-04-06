# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        
        if len(lists) > 1:
            mid = len(lists) // 2
            left = self.mergeKLists(lists[mid:])
            right = self.mergeKLists(lists[:mid])
            return self.merge(left, right)
                    
        
        return lists[0]

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        if left is None:
            return right
        elif right is None:
            return left

        dummy = ListNode()

        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
                current = current.next
            else:
                current.next = right
                right = right.next
                current = current.next
        
        current.next = left or right
        
        return dummy.next
