class Solution(object):
    def countEven(self, num):
        
        o=0
        for i in range(2, num+1):
            d=list(map(int, str(i)))
            if sum(d)%2==0:
                o+=1
        return o