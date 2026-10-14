class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        unique_sum = 0
        for num, count in freq.items():
            if count == 1:
                unique_sum += num

        return unique_sum

solution = Solution()
print(solution.sumOfUnique([1, 2, 3, 4, 5]))  # Output: 15
print(solution.sumOfUnique([1, 2, 3, 2, 4, 5, 4]))  # Output: 9