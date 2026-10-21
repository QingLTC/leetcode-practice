class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        obtain = num
        while obtain != 0:
            if obtain % 2 == 0:
                obtain = obtain / 2
                step += 1
            else:
                obtain = obtain - 1
                step += 1
        return step