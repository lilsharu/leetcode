class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        output = []
        left = 0
        right = 0
        cur_len = -1
        while left < len(words):
            while (
                right + 1 <= len(words) and cur_len + 1 + len(words[right]) <= maxWidth
            ):
                cur_len += len(words[right]) + 1
                right += 1
            extra_spaces = maxWidth - cur_len
            num_gaps = right - left - 1
            extra_gap = extra_spaces // (num_gaps) + 1 if num_gaps > 0 else 0
            num_with_extra = extra_spaces % num_gaps if num_gaps > 0 else 0
            extra_end = 0 if num_gaps > 0 else extra_spaces
            if right != len(words):
                output += [
                    (" " * (extra_gap + 1)).join(
                        words[left : left + num_with_extra] + [""]
                        if num_with_extra > 0
                        else []
                    )
                    + (" " * extra_gap).join(words[left + num_with_extra : right])
                    + " " * extra_end
                ]
            else:
                output += [" ".join(words[left:right]) + " " * (extra_spaces)]
            left = right
            right = left
            cur_len = -1
        return output
