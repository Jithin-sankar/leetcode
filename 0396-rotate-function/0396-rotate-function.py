class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        total = sum(nums)

        f = 0
        for i in range(n):
            f += i * nums[i]

        result = f

        for i in range(n - 1, 0, -1):

            f = f + total - n * nums[i]

            result = max(result, f)

        return result