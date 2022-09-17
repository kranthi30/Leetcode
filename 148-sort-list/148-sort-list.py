# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list1.sort()
        ans = final = ListNode()
        for i in list1:
            ans.next = ListNode(i)
            ans = ans.next
        return final.next
        