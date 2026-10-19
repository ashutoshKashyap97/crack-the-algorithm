class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        last_index = len(s) - 1
        left = 0
        while left < last_index:
            s[left] , s[last_index] = s[last_index] , s[left]
            last_index -= 1
            left += 1

solution = Solution()
s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)