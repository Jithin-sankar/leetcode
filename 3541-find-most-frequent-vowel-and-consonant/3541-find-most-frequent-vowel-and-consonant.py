class Solution(object):
    def maxFreqSum(self, s):
        se = set(s)
        v=0
        c = 0
        for i in se:
            if i in "aeiou":
                v = max(v,s.count(i))
            else:
                c= max(c,s.count(i))
        return v+c