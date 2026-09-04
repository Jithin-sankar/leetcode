class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            maxi = max(nums[:i+1])
            mini =  min(nums[i:])
            diff = maxi - mini
            if diff<=k:
                return i
        return -1