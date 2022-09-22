class Solution:
    def reverseWords(self, s: str) -> str:
        l1 = s.split()
        s1 = ''
        for i in range (0,len(l1)):
            s1 += l1[i][::-1]
            if(i != len(l1)-1):
                s1 += ' '
        return s1
        