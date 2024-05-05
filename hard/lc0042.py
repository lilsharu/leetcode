from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        N = len(nums)
        nums += [-1]
        while i < N:
            if nums[i] > N or nums[i] < 0:
                i += 1
                continue
            val = nums[i]
            if nums[val] == val:
                i += 1
                continue
            temp = nums[val]
            nums[val] = val
            nums[i] = temp
        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
        return len(nums) + 1
