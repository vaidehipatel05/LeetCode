# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = []
        beg = head
        end = head

        while end and end.next:
            beg = beg.next
            end = end.next.next
        
        mid = beg
        
        new_list = ListNode(0)
        current = new_list

        while mid is not None:
            current.next = ListNode(mid.val)
            current = current.next
            mid = mid.next

        return new_list.next