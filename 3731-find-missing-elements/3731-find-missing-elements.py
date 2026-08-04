class Solution(object):
    def findMissingElements(self, nums):
        n=max(nums)
        m=min(nums)

        res=[]
        for i in range(m,n):
            if i not in nums:
                res.append(i)
        return res
