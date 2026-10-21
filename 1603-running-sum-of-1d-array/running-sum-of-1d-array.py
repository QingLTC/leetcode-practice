class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0
        for i in nums:
            total = total + i
            result.append(total)
        return result

nums = [1,2,3,4]
solution = Solution()
solution.runningSum(nums)