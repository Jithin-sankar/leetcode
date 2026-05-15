class Solution(object):
    def recoverOrder(self, order, friends):
        friend_set = set(friends)
        result = []

        for person in order:
            if person in friend_set:
                result.append(person)

        return result
       
        