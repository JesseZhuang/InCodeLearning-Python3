from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        self.sl = SortedList()
        self.counts = defaultdict(int)
        self.res = []


def process(query: List[str], s: Solution):
    op, v = query
    v = int(v)
    counts, sl, res = s.counts, s.sl, s.res
    match op:
        case "ADD":
            counts[v] += 1
            sl.add(v)
            res.append(str(len(sl)))
        case "DELETE":
            if v not in counts:
                res.append("false")
                return
            sl.remove(v)
            counts[v] -= 1
            if counts[v] == 0: del counts[v]
            res.append("true")
    s.counts, s.sl, s.res = counts, sl, res


def solution(queries):
    s = Solution()
    for query in queries:
        if len(query) == 2:  # add or delete
            process(query, s)
        elif len(query) == 1:  # get median
            cnt = len(s.sl)
            if cnt == 0:
                s.res.append("")
            else:
                id = cnt // 2
                if cnt % 2 == 0: id -= 1
                s.res.append(str(s.sl[id]))
    return s.res


"""
Your task is to implement a simple container of integer numbers. Plan your design according to the level specifications below:

Level 1: Container should support adding and removing numbers.

Expand to see level 1 details.
Level 2: Container should support getting the median of the numbers stored in it.

To move to the next level, you need to pass all the tests at this level.

Note

You will receive a list of queries to the system, and the final output should be an array of strings representing the returned values of all queries. Each query will only call one operation.

Level 1
Implement two operations for adding and removing numbers from the container. Initially, the container is empty.

ADD <value> — should add the specified integer value to the container and return a string representing the number of integers in the container after the addition.

DELETE <value> — should attempt to remove the specified integer value from the container. If the value is present in the container, remove it and return "true", otherwise, return "false".

Examples
The example below shows how these operations should work (the section is scrollable to the right):

Queries	Explanations
queries = [
  ["ADD", "5"],
  ["ADD", "10"],
  ["ADD", "5"],
  ["DELETE", "10"],
  ["DELETE", "1"],
  ["ADD", "1"]
]

returns "1"; container state: [5]
returns "2"; container state: [5, 10]
returns "3"; container state: [5, 10, 5]
returns "true"; container state: [5, 5]
returns "false"; container state: [5, 5]
returns "3"; container state: [5, 5, 1]

the output should be ["1", "2", "3", "true", "false", "3"].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.string queries

An array of queries to the system. It is guaranteed that all the queries parameters are valid: each query calls one of the operations described in the description, all operation parameters are given in the correct format, and all conditions required for each operation are satisfied.

Guaranteed constraints:
1 ≤ queries.length ≤ 500.

[output] array.string

An array of strings representing the returned values of queries.

Level 2
Container should support calculating the median of the numbers stored in it.

GET_MEDIAN  — should return a string representing the median integer - the integer in the middle of the sequence after all integers stored in the container are sorted in ascending order. If the length of the sequence is even, the leftmost integer from the two middle integers should be returned. If the container is empty, this method should return an empty string.
Examples
The example below shows how these operations should work (the section is scrollable to the right):

Queries	Explanations
queries = [
  ["GET_MEDIAN"],
  ["ADD", "5"],
  ["ADD", "10"],
  ["ADD", "1"],
  ["GET_MEDIAN"],
  ["ADD", "4"],
  ["GET_MEDIAN"],
  ["DELETE", "1"],
  ["GET_MEDIAN"]
]

returns ""; container state: []
returns "1"; container state: [5]
returns "2"; container state: [5, 10]
returns "3"; container state: [5, 10, 1]
returns "5"; sorted sequence of container numbers is: [1, 5, 10]
returns "4"; container state: [5, 10, 1, 4]
returns "4"; sorted sequence of container numbers is: [1, 4, 5, 10]
returns "true"; container state: [5, 10, 4]
returns "5"; sorted sequence of container numbers is: [4, 5, 10]

the output should be ["", "1", "2", "3", "5", "4", "4", "true", "5"].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.string queries

An array of queries to the system. It is guaranteed that all the queries parameters are valid: each query calls one of the operations described in the description, all operation parameters are given in the correct format, and all conditions required for each operation are satisfied.

Guaranteed constraints:
1 ≤ queries.length ≤ 500.

[output] array.string

An array of strings representing the returned values of queries.
"""
