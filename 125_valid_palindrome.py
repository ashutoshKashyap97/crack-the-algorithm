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
