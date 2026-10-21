from typing import List

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.MOD = 1_000_000_007
        self.sum_sq = [0] * (4 * n)
        self.sum_val = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _apply(self, node: int, l: int, r: int, val: int):
        length = r - l + 1
        # (d + v)^2 = d^2 + 2*v*d + v^2
        self.sum_sq[node] = (
            self.sum_sq[node] 
            + 2 * val * self.sum_val[node] 
            + val * val * length
        ) % self.MOD
        self.sum_val[node] = (self.sum_val[node] + val * length) % self.MOD
        self.lazy[node] = (self.lazy[node] + val) % self.MOD

    def _push_down(self, node: int, l: int, r: int):
        if self.lazy[node] != 0:
            mid = (l + r) // 2
            self._apply(2 * node, l, mid, self.lazy[node])
            self._apply(2 * node + 1, mid + 1, r, self.lazy[node])
            self.lazy[node] = 0

    def _push_up(self, node: int):
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.MOD
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % self.MOD

    def update(self, node: int, l: int, r: int, ql: int, qr: int, val: int):
        if ql <= l and r <= qr:
            self._apply(node, l, r, val)
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr, val)
        self._push_up(node)


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 1_000_000_007
        tree = SegmentTree(n)
        last_pos = {}  
        total_ans = 0

        for j, num in enumerate(nums):
            prev = last_pos.get(num, -1)
            tree.update(1, 0, n - 1, prev + 1, j, 1)
            total_ans = (total_ans + tree.sum_sq[1]) % MOD
            last_pos[num] = j

        return total_ans
        