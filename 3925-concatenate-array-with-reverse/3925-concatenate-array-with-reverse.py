class Solution(object):
    def concatWithReverse(self, nums):
        n=len(nums)
        ans=nums[:]+nums[::-1]
        return ans
      
       