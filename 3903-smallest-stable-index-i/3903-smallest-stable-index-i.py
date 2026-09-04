class Solution(object):
    def firstStableIndex(self, nums, k):
        ans=-1
        for i in range(len(nums)):
            mini=max(nums[:i+1])-min(nums[i:])
            print(mini)
            if mini<=k:
                return i
        return ans