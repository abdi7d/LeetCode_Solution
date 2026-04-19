# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        while head:
            # detect duplicates
            if head.next and head.val == head.next.val:
                
                # skip all nodes with this value
                while head.next and head.val == head.next.val:
                    head = head.next
                
                prev.next = head.next  # remove duplicates
            
            else:
                prev = prev.next  # move prev only if no duplicate
            
            head = head.next
        
        return dummy.next