import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if bool(re.fullmatch(p,s)):
            return True
        return False
        