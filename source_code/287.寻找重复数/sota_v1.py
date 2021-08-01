from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # 实现do  while
        # slow = 0
        # fast = 0
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow != fast:
        #         break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    print(solution.findDuplicate(nums))