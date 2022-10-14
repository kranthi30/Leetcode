# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sortedcontainers import SortedList
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a = SortedList()
        for i in lists:
            while i:
                a.add(i.val)
                i = i.next
        ans = final = ListNode()
        for i in a:
            ans.next = ListNode(i)
            ans = ans.next
        return final.next
        