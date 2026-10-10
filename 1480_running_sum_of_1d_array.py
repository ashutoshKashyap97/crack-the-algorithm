class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        result = []
        for num in nums:
            total+= num
            result.append(total)
        return result

solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))