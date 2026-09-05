class Solution(object):
    def isValid(self, s):
        stack=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        empty=[]
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack==empty:
                    return False
                if stack[-1]!=pairs[ch]:
                    return False
                stack.pop()
        return len(stack)==0