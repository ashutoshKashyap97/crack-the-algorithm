class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        freq = {}
        for num in nums:
            if num in freq:
                count+= freq[num]
            freq[num] = freq.get(num , 0) + 1
        return count

solution = Solution()
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))