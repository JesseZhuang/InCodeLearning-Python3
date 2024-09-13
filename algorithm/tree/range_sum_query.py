"""
leet code 307, medium, tags: array, design, binary indexed tree, segment tree.

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices
left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
"""

# pylint: disable=invalid-name

from typing import Optional


class Node:
    """
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval. All of the leaves will store
    elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n). Space: O(n).
    3379 ms, 49.1 Mb.
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class NumArray:
    '''leet code 307'''

    def __init__(self, nums: list[int]):
        def createTree(nums: list[int], l: int, r: int) -> Node:
            '''helper function to create the tree from input array'''
            if l == r:  # leaf node
                n = Node(l, r)
                n.total = nums[l]
                return n

            mid = (l + r) // 2
            root = Node(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)
            root.total = root.left.total + root.right.total
            return root

        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        '''update index with val, i.e., array[index] = val'''

        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)

            root.total = root.left.total + root.right.total
            return root.total

        updateVal(self.root, index, val)

    def sumRange(self, left: int, right: int):
        """sum of elements nums[i..j], inclusive."""

        def rangeSum(root, i, j):
            '''Helper function to calculate range sum'''
            if root.start == i and root.end == j:
                return root.total
            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, left, right)
