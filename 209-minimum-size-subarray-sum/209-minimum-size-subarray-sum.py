class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_value = float('inf')
        max_value = min_value
        i = 0
        j = 0
        sum1 = 0
        while(i < len(nums)):
            sum1 += nums[i]
            if(sum1 >= target):
                while(sum1 >= target):
                    min_value = min(min_value,i-j+1)
                    sum1 -= nums[j]
                    j += 1
            i += 1
        return 0 if min_value == max_value else min_value
        
            

            
        