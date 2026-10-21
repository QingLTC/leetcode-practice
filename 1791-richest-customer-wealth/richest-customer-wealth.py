class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        result = 0
        for customer in accounts:
            wealth = 0
            for money in customer:
                wealth += money 
            if wealth > result:
                result = wealth
        return result