# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = {}

        idx = 0
        while head:
            if head.val not in visited:
                visited[head.val] = idx
            else:
                return True
            head = head.next
            idx = idx + 1

        return False