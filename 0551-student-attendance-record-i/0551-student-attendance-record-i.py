class Solution(object):
    def checkRecord(self, s):
        absent = 0
        late = 0

        for ch in s:
            if ch == 'A':
                absent += 1
                if absent >= 2:
                    return False
                late = 0

            elif ch == 'L':
                late += 1
                if late >= 3:
                    return False

            else:  # 'P'
                late = 0

        return True
        

        
        