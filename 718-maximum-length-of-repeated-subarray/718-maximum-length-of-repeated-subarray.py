class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 =''.join([chr(i) for i in nums2])
        strmax = ''
        ans = 0
        for i in nums1:
            strmax += chr(i)
            if strmax in nums2:
                ans = max(ans,len(strmax))
            else:
                strmax = strmax[1:]
        return ans
       
        