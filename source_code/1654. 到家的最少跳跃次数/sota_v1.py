from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        self.key = -1

        def dfs(num, cnt, back):
            if self.key < 0 and 0 <= num <= 6000:  # # 6000是往右探索的最大值，x最大为2000
                if num == x:  # 第一次遍历到 x时的次数即为结果，暂存结果，不再递归
                    self.key = cnt
                    return
                if num + a not in forbidden:
                    forbidden.add(num + a)  # 防止无限递归，比如 a = b 时，不加限制，就会出现无限递归
                    dfs(num + a, cnt + 1, 0)
                if num - b not in forbidden and back != 1:  # 若back为1说明上次就是往后跳的
                    dfs(num - b, cnt + 1, 1)

        dfs(0, 0, 0)
        return self.key


if __name__ == "__main__":
    solution = Solution()
    forbidden = [8, 3, 16, 6, 12, 20]
    a = 15
    b = 13
    x = 11
    print(solution.minimumJumps(forbidden, a, b, x))