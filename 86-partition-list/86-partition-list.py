# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1 = []
        list2 = []
        while head:
            list1.append(head.val)
            head = head.next
        i = 0
        j = 0
        while(i < len(list1)):
            if list1[i] < x:
                list1.insert(j,list1.pop(i))
                j += 1
                i += 1
            else:
                i += 1
        ans = final = ListNode()
        for i in list1:
            ans.next = ListNode(i)
            ans = ans.next
        return final.next
        