class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (get_digit_sum(x), x))
        target_pos = {val: i for i, val in enumerate(sorted_nums)}
        visited = [False] * n
        num_cycles = 0

        for i in range(n):
            if visited[i]:
                continue
            num_cycles += 1
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = target_pos[nums[curr]]
        return n - num_cycles