class Solution(object):
    def findGCD(self, nums):
        small = min(nums)
        large = max(nums)
        while large:
            small,large = large,small%large
        return small