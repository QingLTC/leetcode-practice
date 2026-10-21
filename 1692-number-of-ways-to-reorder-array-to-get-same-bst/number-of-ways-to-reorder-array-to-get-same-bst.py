import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            l_len = len(left)
            r_len = len(right)
            
            comb = math.comb(l_len + r_len, l_len)
            
            return (comb * dfs(left) * dfs(right)) % MOD
        
        return (dfs(nums) - 1) % MOD