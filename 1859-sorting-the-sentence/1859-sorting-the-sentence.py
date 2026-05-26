class Solution(object):
    def sortSentence(self, s):
        s=sorted(s.split(),key=lambda word: word[-1])
        s=[word[:-1] for word in s]
        return ' '.join(s)
        