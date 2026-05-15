class Solution(object):
    def recoverOrder(self, order, friends):
        friend = set(friends)
        result = []

        for person in order:
            if person in friend:
                result.append(person)

        return result
       
        