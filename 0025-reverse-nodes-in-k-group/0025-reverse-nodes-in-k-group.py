# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        
        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # reverse group
            prev = groupNext
            curr = groupPrev.next
            
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # reconnect
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next