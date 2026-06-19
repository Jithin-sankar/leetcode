class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = [0]
        for i in range(1, len(gain)+1):
            alt.append(gain[i-1] + alt[i-1])
        
        return max(alt)

        