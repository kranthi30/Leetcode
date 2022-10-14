# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        b = len(list1)
        if(b != k):
            for i in range(k%b):
                a = list1.pop(b-1)
                list1.insert(0,a)
        ans = final = ListNode()
        for i in list1:
            ans.next = ListNode(i)
            ans = ans.next
        return final.next
            