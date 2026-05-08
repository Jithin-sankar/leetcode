class Solution(object):
    def findLucky(self, arr):
        ans = -1

        for i in arr:
            if arr.count(i) == i:
                ans = max(ans, i)

        return ans
      
        