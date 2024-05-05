from collections import defaultdict


# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = defaultdict(lambda: 0)
        dict_t = defaultdict(lambda: 0)
        for c in s:
            dict_s[c] += 1
        for c in t:
            dict_t[c] += 1
        return dict_s == dict_t
