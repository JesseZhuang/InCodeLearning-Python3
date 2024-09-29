"""
find all occurrences of the pattern inside the text.
O(n) time, O(1) space not considering result Z array.

For a string str[0..n-1], Z array is of same length as string. An element Z[i] of Z array stores length of the longest
 substring starting from str[i] which is also a prefix of str[0..n-1]. The first entry of Z
 array is meaning less as complete string is always prefix of itself.
"""
