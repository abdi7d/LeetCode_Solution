# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)
        
        before_curr = before
        after_curr = after
        
        while head:
            if head.val < x:
                before_curr.next = head
                before_curr = before_curr.next
            else:
                after_curr.next = head
                after_curr = after_curr.next
            
            head = head.next
        
        # important: end after list
        after_curr.next = None
        
        # connect lists
        before_curr.next = after.next
        
        return before.next