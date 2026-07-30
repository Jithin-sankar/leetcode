class Solution(object):
    def minimumPushes(self, word):
        a=len(word)
        ans=0
        i=1
        while a>0:
            if a>=8:
                ans+=8*i
                i+=1
                a-=8
            else:
                ans+=a*i
                a=0
                i+=1
        return ans