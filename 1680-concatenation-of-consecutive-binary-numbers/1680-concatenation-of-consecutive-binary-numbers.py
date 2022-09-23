class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s1 = ''
        i = 1
        while(i <= n):
            s1 += bin(i)[2:]
            i += 1
        return int(s1,2)%(10**9+7)
        