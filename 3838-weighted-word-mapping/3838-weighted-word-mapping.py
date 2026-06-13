class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = []

        for word in words:
            s = 0
            for ch in word:
                s += weights[ord(ch) - ord('a')]

            ans.append(ascii_lowercase[25 - (s % 26)])

        return "".join(ans)