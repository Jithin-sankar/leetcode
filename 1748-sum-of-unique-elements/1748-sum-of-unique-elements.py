class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in nums:
            if nums.count(i)==1:
                l.append(i)
        return sum(l)