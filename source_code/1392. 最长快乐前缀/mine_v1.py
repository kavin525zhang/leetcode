class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return ""

        max_str = ""
        for i in range(n - 1):
            if s[i] == s[-1]:
                if s[:i + 1] == s[-(i + 1):]:
                    max_str = s[:i + 1]

        return max_str


if __name__ == "__main__":
    solution = Solution()
    s = "ababab"
    print(solution.longestPrefix(s))