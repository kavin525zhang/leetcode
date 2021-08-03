from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sort = sorted(arr)
        num_index = {}
        for num in arr_sort:
            if num not in num_index:
                num_index[num] = len(num_index) + 1
        results = []
        for num in arr:
            results.append(num_index[num])

        return results


if __name__ == "__main__":
    solution = Solution()
    arr = [4, 1, 2, 3]
    print(solution.arrayRankTransform(arr))