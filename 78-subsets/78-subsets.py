class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        list1 = [[]]
        for i in range(1,len(nums)+1):
            a = itertools.combinations(nums,i)
            list1.extend(a)
        return list1
        