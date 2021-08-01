from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            i = len(nums) - 2
            while i != -1:
                if nums[i] == 0:
                    j = i + 1
                    while j < len(nums) and nums[j] != 0:
                        nums[j - 1] = nums[j]
                        j += 1
                    if j - 1 != i:
                        nums[j - 1] = 0
                i -= 1


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 1]
    solution.moveZeroes(nums)
    print(nums)