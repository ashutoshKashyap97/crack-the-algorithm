class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""

        for char in s:
            if char.isalnum():
                s1 += char.lower()
        return s1 == s1[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True  
print(solution.isPalindrome("race a car"))  # False

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1

#         while left < right:
#             if not s[left].isalnum():
#                 left += 1
#             elif not s[right].isalnum():
#                 right -= 1
#             elif s[left].lower() != s[right].lower():
#                 return False
#             else:
#                 left += 1
#                 right -= 1

#         return True