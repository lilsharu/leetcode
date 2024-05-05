# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        for i in range(1, len(arr) + 1):
            val = arr[-i]
            arr[-i] = current_max
            current_max = max(val, current_max)
        return arr
