class Solution(object):
    def findMissingElements(self, nums):
        mn = min(nums)
        mx = max(nums)

        s = set(nums)
        result = []

        for i in range(mn + 1, mx):
            if i not in s:
                result.append(i)

        return result