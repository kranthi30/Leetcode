class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        while(len(nums)>2 and nums[0] >= nums[1] + nums[2]):
            nums.pop(0)
        if len(nums) < 3:
            return 0
        return sum(nums[:3])
        