# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Rewire pointers
            prev.next = second
            first.next = second.next
            second.next = first

            # Move prev to the end of the swapped pair
            prev = first

        return dummy.next
