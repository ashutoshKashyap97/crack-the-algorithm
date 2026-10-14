class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        result = []
        for kid in candies:
            if kid + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result

solution = Solution()
print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))

# class Solution:
#     def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
#         max_candies = max(candies)

#         result = []

#         for candy in candies:
#             result.append(candy + extraCandies >= max_candies)

#         return result