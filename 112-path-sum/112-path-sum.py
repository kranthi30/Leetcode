# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        list1 = []
        def dfs(root,target):
            if not root:
                return None
            target += root.val
            if target == targetSum and not root.left and not root.right:
                list1.append(target)
            if root.left:
                dfs(root.left,target)
            if root.right:
                dfs(root.right,target)
        dfs(root,0)
        if len(list1) != 0:
            return True
        return False
            



        