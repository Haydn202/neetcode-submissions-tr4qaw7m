# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy

        listLength = 1
        current = head

        while current.next:
            current = current.next
            listLength += 1
        
        target = listLength - n

        temp = dummy
        for _ in range(target):
            temp = temp.next

        temp.next = temp.next.next

        return dummy.next


