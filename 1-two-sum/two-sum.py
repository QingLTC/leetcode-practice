class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # 字典备忘录: {数字: 它的下标}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i