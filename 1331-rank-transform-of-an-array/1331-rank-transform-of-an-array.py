class Solution(object):
    def arrayRankTransform(self, arr):
        temp=set(arr)
        sorted_nums=sorted(list(temp))
        n=len(arr)
        for i in range(n):
            arr[i] = bisect_left(sorted_nums, arr[i]) + 1
        return arr