class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        num = n
        for i in range (n+1):
            if num in nums:
                num -=1
            else:
                return num