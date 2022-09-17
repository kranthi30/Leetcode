# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list1[left-1:right] = list1[left-1:right][::-1]
        res = final = ListNode()
        for i in range(len(list1)):
            res.next = ListNode(list1[i])
            res = res.next
        return final.next
            
        