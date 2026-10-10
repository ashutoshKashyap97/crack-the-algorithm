class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        # for account in accounts:
        #     wealth = sum(account)
        #     if wealth > max_wealth:
        #         max_wealth = wealth
        for account in accounts:
            wealth = 0
            for money in account:
                wealth += money
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
        

solution = Solution()
print(solution.maximumWealth([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))