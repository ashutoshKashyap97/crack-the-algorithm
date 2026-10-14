class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        num_count = {}
        result = []
        for i, num in enumerate(sorted_nums):
            if num not in num_count:
                num_count[num] = i

        for num in nums:
            result.append(num_count[num])

        return result

solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(solution.smallerNumbersThanCurrent([6, 5, 4, 8]))
print(solution.smallerNumbersThanCurrent([7, 7, 7, 7]))