# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def get_path(sum1,targetsum,root,path):
            if not root:
                return
            if not root.left and not root.right:
                if root.val + sum1 == targetsum:
                    path.append(root.val)
                    res.append([i for i in path])
                    path.pop(-1)
                    return
            path.append(root.val)
            get_path(root.val+sum1,targetsum,root.left,path)
            get_path(root.val+sum1,targetsum,root.right,path)
            path.pop(-1)        
        get_path(0,targetSum,root,[])
        return res
            
        
        