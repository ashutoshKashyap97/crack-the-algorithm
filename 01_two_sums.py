class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in freq:
                return [freq[complement], i]
            freq[nums[i]] = i
        return []

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
