class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s
        i = 0
        while i < len(s) - 1:
            if s[i] != s[i + 1] and s[i].lower() == s[i + 1].lower():
                s = s[:i] + s[i + 2:]
                if i > 0:
                    i -= 1
            else:
                i += 1

        return s


if __name__ == "__main__":
    solution = Solution()
    s = "abBAcC"
    print(solution.makeGood(s))