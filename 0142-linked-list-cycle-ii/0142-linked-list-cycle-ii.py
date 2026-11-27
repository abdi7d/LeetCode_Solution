# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        # Phase 1: Determine if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
            
        # Phase 2: Find the entrance to the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
