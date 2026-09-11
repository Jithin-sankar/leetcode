class Solution(object):
    def generateParenthesis(self, n):
        total = 0
        result = []
        ind = 0
        num = [""] * (n * 2)

        def solve(ind, total):
            if ind == len(num):
                if total == 0:
                    result.append("".join(num))
                return

            if total > len(num) // 2:
                return

            if total < 0:
                return

            num[ind] = "("
            solve(ind + 1, total + 1)

            num[ind] = ")"
            solve(ind + 1, total - 1)

        solve(ind, total)
        return result