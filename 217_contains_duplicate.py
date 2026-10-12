class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if num in freq:
                freq[num] > 1
                return True
        return False

solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
