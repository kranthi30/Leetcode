# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        while head:
            list1.append(head.val)
            head = head.next
        list1.pop(len(list1) // 2)
        res = final = ListNode()
        for i in list1:
            res.next = ListNode(i)
            res = res.next
        return final.next
        