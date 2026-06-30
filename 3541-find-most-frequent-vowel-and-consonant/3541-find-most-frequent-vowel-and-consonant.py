class Solution(object):
    def maxFreqSum(self, s):
        se = set(s)
        vcount=0
        ccount = 0
        for i in se:
            if i in "aeiou":
                vcount = max(vcount,s.count(i))
            else:
                ccount = max(ccount,s.count(i))
        return vcount+ccount