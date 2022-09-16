# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        s1 = ''
        s2 = ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2+= str(l2.val)
            l2 = l2.next
        s1 = s1[::-1]
        s2 = s2[::-1]
        a = int(s1)+int(s2)
        a = str(a)
        a = a[::-1]
        ans = final = ListNode()
        for i in a:
            ans.next = ListNode(i)
            ans = ans.next
        return final.next
        