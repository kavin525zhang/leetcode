from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[nums[i] % n - 1] > n - 1:
                return nums[i] % n
            nums[nums[i] % n - 1] += n


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    print(solution.findDuplicate(nums))