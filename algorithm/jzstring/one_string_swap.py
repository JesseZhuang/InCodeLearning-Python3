"""leet 1790, easy"""


class Solution:
    """todo editorial"""

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_index_diff = 0
        second_index_diff = 0
        num_diffs = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diffs += 1
                # num_diffs is more than 2, one string swap will not make two strings equal
                if num_diffs > 2:
                    return False
                elif num_diffs == 1:
                    # store the index of first difference
                    first_index_diff = i
                else:
                    # store the index of second difference
                    second_index_diff = i
        # check if swap is possible
        return (
                s1[first_index_diff] == s2[second_index_diff]
                and s1[second_index_diff] == s2[first_index_diff]
        )
