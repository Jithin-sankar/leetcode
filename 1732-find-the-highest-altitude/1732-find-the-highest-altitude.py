class Solution(object):
    def largestAltitude(self, gains):
        curr_alt = 0 
        max_alt = curr_alt 

        for n in gains:
            curr_alt += n 
            max_alt = max(max_alt, curr_alt)

        return max_alt

        