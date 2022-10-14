# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sortedcontainers import SortedList
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = SortedList()
        if not head:
            return None
        while head:
            a.add(head.val)
            head = head.next
        ans = final = ListNode()
        for i in a:
            if a.count(i) > 1:
                continue
            ans.next = ListNode(i)
            ans = ans.next
        return final.next
        