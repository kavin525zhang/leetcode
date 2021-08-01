from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        if len(nums) > 1:
            i = 0
            while i < len(nums):
                if nums[i] == 0:
                    count += 1
                    nums.remove(0)
                else:
                    i += 1
        nums.extend([0] * count)


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 1]
    solution.moveZeroes(nums)
    print(nums)