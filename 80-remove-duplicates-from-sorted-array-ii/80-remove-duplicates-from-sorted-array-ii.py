class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict1 = {}
        for i in range(len(nums)):
            if dict1.get(nums[i]) == None:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] += 1
        for key,value in dict1.items():
            if value > 2:
                for i in range(value - 2):
                    nums.remove(int(key))
        return len(nums)
                