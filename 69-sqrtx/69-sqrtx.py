class Solution:
    def mySqrt(self, x: int) -> int:
        a = 1
        if x == 0:
            return 0
        sqrt = 1
        while(a <= x/2):
            target = a*a
            if target == x:
                return a
            if target < x:
                sqrt = a
            elif target > x:
                return sqrt
            a += 1
        return sqrt
            
        