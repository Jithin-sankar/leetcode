class Solution(object):
    def arrayRankTransform(self, arr):
        # Get unique elements and sort them
        sorted_arr = sorted(set(arr))

        # Assign rank to each unique element
        rank = {}
        for i, num in enumerate(sorted_arr):
            rank[num] = i + 1

        # Replace each element with its rank
        return [rank[num] for num in arr]