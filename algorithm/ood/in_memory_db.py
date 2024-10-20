"""
code signal in memory database

Level 1
The basic level of the in-memory database contains records.
Each record can be accessed with a unique identifier key, which is of string type. A record contains several
field - value pairs, with field as string type and value as integer type. All operations have a timestamp parameter
 - a stringified timestamp in milliseconds. It is guaranteed that all timestamps are unique and are in a range
  from 1 to 10^9 . Operations will be given in order of strictly increasing timestamps. Timestamps will be needed
   starting from Level 3.

• set(self, timestamp: int, key: str, field: str, value: int) -> None
- should insert a field - value pair to the record associated with key. If the field in the record already exists,
 replace the existing value with the specified value. If the record does not exist, a new one is created.

• compare_and_set (self, timestamp: int, key: str, field: str, expected_value: int, new_value: int) -› bool
 - should update the value of field in the record associated with key to new_value if the current value equals
  expected value. If expected value does not not match the current value, or either key or field does not exist,
   this operation is ignored. This operation should return True if the field was updated and False otherwise.

- compare_and delete (self, timetamp: int, key: str, field: str, expected value: int) -> bool — Should remove the
 field field in the record associated with key if the previous value equals expected_value. If expected_value does not
 match the current value, or either key or field does not exist, this operation is ignored.
 This operation should return True if the field was removed and False otherwise.

• get (self, timestamp: int, key: sti, field: str) -> int | None — should return the value contained within
field of the record associated with key. If the record or the field does not exist, should return None.

other notes

1. implement set, get, delete
2. implement with timestamp: set, get, delete, set_with_ttl，cannot get if ttl expires.
3. implement scan and scan_with_prefix
4. 实现 backup and restore，backup就是take snapshot，restore就是把指定时间的snapshot给恢复了。
题目不难，90分钟的题，65分钟搞定，得到600满分。
需要注意的点：
1. 搞snapshot的时候要用copy.deepcopy，把class里的所有的状态无脑copy一份存了。
2. 不用花时间优化，能brute force就不要写binary search，能过test case 就行。
3. 有的set不带ttl，那就把过期时间设为 float('inf')，后期的处理能省不少事儿

Level 2: In-memory database should support displaying a specific record's fields based on a filter
 "SCAN <key>" (by alphabetic order), "SCAN_BY_PREFIX <key> <prefix>" (field with prefix, by alphabetic order)
我的思路是将field map变成TreeMap (java 选手...)，scan by prefix用regex匹配搜索
Level 3: In-memory database should support TTL (Time-To-Live) configurations on database records 需要实现的操作有：
"SET_AT <key> <field> <value> <timestamp>", "SET_AT_WITH_TTL <key> <field> <value> <timestamp> <ttl>",  "
GET_AT <key> <field> <timestamp>", "DELETE_AT <key> <field> <timestamp>", "SCAN_AT <key> <timestamp>",
"SCAN_BY_PREFIX_AT <key> <prefix> <timestamp>"
我在这里花了最多时间以至于没来得及写下一题，主要是没理解题目要求 "SET_AT" 是指带上了timestamp，但是没有expire time，
如果之前对同一个<key>+<field>设置过 "SET_AT_WITH_TTL"，则再次调用"SET_AT" 时需要将expire time设为永久
我的思路是field map的value变成一对值 (value, expireTime)，expireTime为永久的搞个 null 啥的
Level 4: back up from time to time 需要实现的操作有："BACKUP <timestamp>", "RESTORE <timestamp> <timestampToRestore>"
"""


class InMemoryDB:
    pass


def solution(queries):
    res = []
    for q in queries:
        match (q[0]):
            case "1":
                res.append(q[1])
    return res
