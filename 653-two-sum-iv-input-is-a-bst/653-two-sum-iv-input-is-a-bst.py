# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return
        def inorder(root):
            l1 = []
            if root:
                if(root.left):
                    l1 += inorder(root.left)
                l1.append(root.val)
                if(root.right):
                    l1 += inorder(root.right)
            return l1
        a = inorder(root)
        for i in range (len(a)):
            if(k - a[i] in a[i+1:]):
                return True
            
            
            
            
        