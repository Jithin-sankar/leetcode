class Solution(object):
    def validDigit(self, n, x):
        s=str(n)
        x=str(x)
        return x in s and s[0]!= x
        
        