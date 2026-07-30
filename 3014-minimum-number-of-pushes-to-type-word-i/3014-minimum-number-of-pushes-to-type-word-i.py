from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        freq = Counter(word)

        # Sort frequencies in descending order
        counts = sorted(freq.values(), reverse=True)

        pushes = 0
        for i, count in enumerate(counts):
            pushes += count * (i // 8 + 1)

        return pushes