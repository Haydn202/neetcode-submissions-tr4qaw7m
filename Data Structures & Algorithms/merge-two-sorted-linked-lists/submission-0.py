# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head1 = list1
        head2 = list2
        current = dummy

        while head1 and head2:
            if head1.val < head2.val:
                current.next = head1
                current = head1
                head1 = head1.next
            else:
                current.next = head2
                current = head2
                head2 = head2.next
        if head1:
            current.next = head1
        elif head2:
            current.next = head2

        return dummy.next