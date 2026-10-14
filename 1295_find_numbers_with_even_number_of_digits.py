class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

solution = Solution()
print(solution.findNumbers([12, 345, 2, 6, 7896]))  # Output: 2
print(solution.findNumbers([555, 901, 482, 1771]))  # Output: 1