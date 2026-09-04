class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # right[i] = min(nums[i:])  -- built back-to-front
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        # walk front-to-back, tracking running max so far
        left = float('-inf')
        for i in range(n):
            left = max(left, nums[i])
            if left - right[i] <= k:
                return i

        return -1