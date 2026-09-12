class Solution(object):
    def countCommas(self, n):
        count = 0 
        if n <=999:
            return 0
        else:
            for i in range(1000,n):
                count+=1
            return count+1
        
