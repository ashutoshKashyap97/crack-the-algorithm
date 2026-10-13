class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []
        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[i + n])
        return shuffled

solution = Solution()
print(solution.shuffle([2, 5, 1, 3, 4, 7], 3))  # Output: [2, 3, 5, 4, 1, 7]
print(solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))  # Output: [1, 4, 2, 3, 3, 2, 4, 1]