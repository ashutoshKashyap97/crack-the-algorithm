#Boyer–Moore Voting Algorithm

# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         candidate = None
#         count = 0

#         for num in nums:
#             if count == 0:
#                 candidate = num

#             if num == candidate:
#                 count += 1
#             else:
#                 count -= 1

#         return candidate

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        majority_count = len(nums)//2
        for num in nums:
            freq[num] = freq.get(num , 0) + 1
            if num in freq and freq[num] > majority_count:
                return num

solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # Output: 3
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2