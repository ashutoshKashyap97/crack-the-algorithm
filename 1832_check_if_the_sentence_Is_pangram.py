class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence_set = set(sentence)
        return len(sentence_set) == 26

solution = Solution()
print(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(solution.checkIfPangram("leetcode"))