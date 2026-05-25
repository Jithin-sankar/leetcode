class Solution(object):
    def findPeaks(self, m):
        l = []
        for i in range(1,len(m)-1):
            if m[i] >m[i-1] and m[i] > m[i+1]: l.append(i)
        return l