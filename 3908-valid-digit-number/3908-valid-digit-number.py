class Solution(object):
    def validDigit(self, n, x):
       s = str(n)
       return str(x) in s and s[0] != str(x)
        
        