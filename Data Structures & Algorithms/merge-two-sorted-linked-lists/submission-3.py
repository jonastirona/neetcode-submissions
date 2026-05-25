# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        if not list1 and not list2: return None
        if not list1 or (list2 and list1.val > list2.val):
            merged = list2
            list2 = list2.next
        else:
            merged = list1
            list1 = list1.next
        
        currMerged = merged
        curr1 = list1
        curr2 = list2

        while curr1 or curr2:
            if not curr1 or (curr2 and curr1.val > curr2.val):
                currMerged.next = curr2
                curr2 = curr2.next
            else:
                currMerged.next = curr1
                curr1 = curr1.next
            currMerged = currMerged.next

        return merged

