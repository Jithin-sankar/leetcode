class Solution(object):
    def isGood(self, nums):

        nums.sort()

        n = len(nums) - 1

        expected = list(range(1, n + 1)) + [n]

        return nums == expected