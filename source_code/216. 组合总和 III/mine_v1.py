from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45 or k > 9:
            return []

        if n > sum(list(range(9 - k + 1, 10))) or n < sum(list(range(1, k + 1))):
            return []

        results = []

        def f(k, i, ans):
            if k < 0 or sum(ans) > n or i > 10:
                return
            if k == 0 and sum(ans) == n:
                results.append(ans)
                return
            if i <= 9:
                f(k - 1, i + 1, ans + [i])
                f(k, i + 1, ans)

        f(k, 1, [])
        return results


if __name__ == "__main__":
    solution = Solution()
    k = 9
    n = 45
    print(solution.combinationSum3(k, n))