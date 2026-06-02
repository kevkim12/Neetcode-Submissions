# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val < list2.val:
            ans = list1
            list1 = list1.next
        else:
            ans = list2
            list2 = list2.next
        ansRoot = ans

        while list1 != None or list2 != None:
            # If list1 or list 2 has no more values
            if list1 == None:
                ans.next = list2
                list2 = list2.next
            elif list2 == None:
                ans.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                ans.next = list2
                list2 = list2.next
            else:
                ans.next = list1
                list1 = list1.next
            
            ans = ans.next

        return ansRoot