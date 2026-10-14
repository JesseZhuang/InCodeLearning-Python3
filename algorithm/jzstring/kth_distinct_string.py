class Solution:
    def kthDistinct(self, arr, k):
        # The frequency pass is O(n) expected time and O(n) space.
        frequencies = {}
        for value in arr:
            frequencies[value] = frequencies.get(value, 0) + 1

        # The ordered scan is O(n) expected time and preserves input order.
        for value in arr:
            if frequencies[value] == 1:
                k -= 1
                if k == 0:
                    return value

        return ""
