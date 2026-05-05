class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence))==26
        """
        :type sentence: str
        :rtype: bool
        """

        