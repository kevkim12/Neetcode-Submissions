# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        d = {}
        idx = 1

        while curr:
            d[idx] = curr
            idx += 1
            curr = curr.next

        if len(d) - n != 0:

            # There is a node before
            if len(d) - n - 1 in d:
                d[len(d) - n - 1].next = d[len(d) - n]

            # There is a node after
            if len(d) - n + 1 in d:
                d[len(d) - n].next = d[len(d) - n + 1].next

            return head
        else:

            return head.next