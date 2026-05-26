class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        result = [None] * len(words)

        for w in words:
            index = int(w[-1]) - 1
            result[index] = w[:-1]

        return " ".join(result)
      
        