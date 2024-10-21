"""
code signal in memory database

Level 1
The basic level of the in-memory database contains records.
Each record can be accessed with a unique identifier key, which is of string type. A record contains several
field - value pairs, with field as string type and value as integer type. All operations have a timestamp parameter
 - a string field timestamp in milliseconds. It is guaranteed that all timestamps are unique and are in a range
  from 1 to 10^9 . Operations will be given in order of strictly increasing timestamps. Timestamps will be needed
   starting from Level 3.

• set(self, timestamp: int, key: str, field: str, value: int) -> None
- should insert a field - value pair to the record associated with key. If the field in the record already exists,
 replace the existing value with the specified value. If the record does not exist, a new one is created.

• compare_and_set (self, timestamp: int, key: str, field: str, expected_value: int, new_value: int) -› bool
 - should update the value of field in the record associated with key to new_value if the current value equals
  expected value. If expected value does not match the current value, or either key or field does not exist,
   this operation is ignored. This operation should return True if the field was updated and False otherwise.

- compare_and_delete (self, timestamp: int, key: str, field: str, expected value: int) -> bool
— Should remove the field in the record associated with key if the previous value equals expected_value.
If expected_value does not match the current value, or either key or field does not exist, this operation is ignored.
 This operation should return True if the field was removed and False otherwise.

• get (self, timestamp: int, key: sti, field: str) -> int | None — should return the value contained within
field of the record associated with key. If the record or the field does not exist, should return None.

other notes

2. implement with timestamp: set, get, delete, set_with_ttl，cannot get if ttl expires.
3. implement scan and scan_with_prefix
4. 实现 backup and restore，backup就是take snapshot，restore就是把指定时间的snapshot给恢复了。
题目不难，90分钟的题，65分钟搞定，得到600满分。(Holly!)
需要注意的点：
1. 搞snapshot的时候要用copy.deepcopy，把class里的所有的状态无脑copy一份存了。
2. 不用花时间优化，能brute force就不要写binary search，能过test case 就行。
3. 有的set不带ttl，那就把过期时间设为 float('inf')，后期的处理能省不少事儿

Level 2
The database should support displaying data based on filters.
Introduce an operation to support printing some fields of a record.

• scan (self, timestamp: int, key: str) -> list[str]
— should return a list of strings representing the fields of the record associated with key. The returned list should
be in the following format ["‹field_1>(<value_1>)", " <field_2>(‹value_2>)", ...] , where fields are sorted
 lexicographically. If the specified record does not exist, returns an empty list.

• scan_by_prefix(self, timestamp: int, key: str, prefix: str) -> list[str] - should return a list of
strings representing some fields of the record associated with key. Specifically, only fields that start with prefix
 should be included. The returned list should be in the same format as in the scan operation with fields sorted in
 lexicographical order.

我的思路是将field map变成TreeMap (java 选手...)，scan by prefix用regex匹配搜索

Level 3
Support the TTL (Time-To-Live) settings for records and fields.
For each field - value pair in the database, the TTL determines how long that value will persist before being removed.

Note: All relevant operations defined in previous levels are assumed to have an infinite TTL.
• set_with_ttl (self, timestamp: int, key: str, field: str, value: int, ttl: int) -> None
 - should insert the specified value and set its Time-To-Live starting at timestamp. If the field in the record
 already exists, then update its value and TTL. The ttl parameter represents the number of time units that this field
  - value pair should exist in the database, meaning it will be available during this interval:
  [timestamp, timestamp + ttl) . It is guaranteed that ttl is greater than 0.

• compare_and_set_with_ttl (self, timestamp: int, key: str, field: str,
expected_value: int, new_value: int, ttl: int) -> bool
 - the same as compare_and_set, but should also update TTL of the new_value. This operation should return True
 if the field was updated and False otherwise. It is guaranteed that ttl is greater than 0.

我在这里花了最多时间以至于没来得及写下一题，主要是没理解题目要求 "SET_AT" 是指带上了timestamp，但是没有expire time，
如果之前对同一个<key>+<field>设置过 "SET_AT_WITH_TTL"，则再次调用"SET_AT" 时需要将expire time设为永久
我的思路是field map的value变成一对值 (value, expireTime)，expireTime为永久的搞个 null 啥的

Level 4

The database should be backed up from time to time. Introduce operations to support backing up and restoring the
 database state based on timestamps. When restoring, ttl expiration times should be recalculated accordingly.

• BACKUP ‹timestamp> — should save the database state at the specified timestamp, including the remaining ttl
 for all records and fields. Remaining ttl is the difference between their initial ttl and their current lifespan
  (the duration between the timestamp of this operation and their initial timestamp). Returns a string representing
   the number of non-empty non-expired records in the database.
• RESTORE ‹timestamps «timestampToRestore›
— should restore the database from the latest backup before or at timestampToRestore. It's guaranteed that a backup
 before or at timestampToRestore will exist. Expiration

Assumption: delete_at, set_at, set_at_with_ttl, .etc. should not affect existing backups.

"""
import copy
from collections import defaultdict

from sortedcontainers import SortedDict


class Value:
    def __init__(self, value: int, last_set_at: int, ttl=None):
        self.value: int = value
        self.ttl: None | int = ttl
        self.last_set_at: int = last_set_at  # timestamp that this value most recently was set

    def is_expired(self, timestamp: int) -> bool:
        # must use is not None, ttl 0 is valid
        return self.ttl is not None and self.ttl + self.last_set_at <= timestamp


class Record:
    def __init__(self):
        self.data: SortedDict[str, Value] = SortedDict()  # field->value


class InMemoryDB:

    def __init__(self):
        self.records: defaultdict[str, Record] = defaultdict(lambda: Record())
        self.backups: SortedDict[int, dict[str, Record]] = SortedDict()  # timestamp -> records

    # unclear what happens if set history after backup, for example, set_at (... at timestamp 4) after backup at 5
    # maybe guaranteed timestamp should always increase
    def set_at(self, key: str, field: str, value: int, timestampToSet: int) -> None:
        self.records[key].data[field] = Value(value, timestampToSet)  # no ttl

    def set(self, timestamp: int, key: str, field: str, value: int) -> None:
        self.records[key].data[field] = Value(value, timestamp)

    def set_with_ttl(self, timestamp: int, key: str, field: str, value: int, ttl: int) -> None:
        self.records[key].data[field] = Value(value, timestamp, ttl)

    def set_at_with_ttl(self, key: str, field: str, value: int, timestampToSet: int, ttl: int) -> None:
        self.records[key].data[field] = Value(value, timestampToSet, ttl)

    def compare_and_set(self, timestamp: int, key: str, field: str, expected_value: int, new_value: int) -> bool:
        if key in self.records and self.records[key].data[field].value == expected_value:
            self.records[key].data[field] = Value(new_value, timestamp)
            return True
        return False

    def compare_and_set_with_ttl(self, timestamp: int, key: str, field: str,
                                 expected_value: int, new_value: int, ttl: int) -> bool:
        if key in self.records and self.records[key].data[field].value == expected_value:
            self.records[key].data[field] = Value(new_value, timestamp, ttl)
            return True
        return False

    def delete_at(self, key: str, field: str, timestampToDelete: int) -> bool:
        if key in self.records and field in self.records[key].data:
            v = self.records[key].data[field]
            v.last_set_at, v.ttl = timestampToDelete, 0
            # value expires at timestampToDelete, before that still live
            return True
        return False

    def compare_and_delete(self, timestamp: int, key: str, field: str, expected_value: int) -> bool:
        if (key in self.records and field in self.records[key].data and
                self.records[key].data[field].value == expected_value):
            self.records[key].data[field] = Value(expected_value, timestamp, 0)  # set to expire at timestamp
            return True
        return False

    def get(self, timestamp: int, key: str, field: str) -> int | None:
        if key not in self.records or field not in self.records[key].data:
            return None
        v = self.records[key].data[field]
        if v.is_expired(timestamp):  # expired
            return None
        return v.value

    def scan_at(self, key: str, at_timestamp: int) -> list[str]:
        return [f"{k}({v.value})" for k, v in self.records[key].data.items() if not v.is_expired(at_timestamp)]

    def scan(self, timestamp: int, key: str) -> list[str]:
        return [f"{k}({v.value})" for k, v in self.records[key].data.items() if not v.is_expired(timestamp)]

    def scan_by_prefix(self, timestamp: int, key: str, prefix: str) -> list[str]:
        res = list()
        for k, v in self.records[key].data.items():
            if k.startswith(prefix):
                if not v.is_expired(timestamp):
                    res.append(f"{k}({v.value})")
            else:
                break
        return res

    def backup(self, timestamp: int) -> int:
        cnt = 0
        c = copy.deepcopy(self.records)
        for _, r in c.items():
            non_empty = False
            for v in r.data.values():
                if not v.is_expired(timestamp):
                    non_empty = True
                    if v.ttl is not None:
                        v.ttl -= timestamp - v.last_set_at
            if non_empty:
                cnt += 1
        self.backups[timestamp] = c
        return cnt

    def restore(self, timestamp: int, timestampToRestore: int) -> None:
        idx = self.backups.bisect_right(timestampToRestore) - 1
        if idx > 0:
            c = copy.deepcopy(self.backups.peekitem(idx))[1]
            for _, r in c.items():
                for v in r.data.values():
                    v.last_set_at = timestamp
            self.records = c


def solution(queries):
    res = []
    db = InMemoryDB()
    for q in queries:
        match (q[0]):
            case "SET":
                res.append(db.set(q[1], q[2], q[3], q[4]))
            case "SET_AT":
                res.append(db.set_at(q[1], q[2], q[3], q[4]))
            case "SET_WITH_TTL":
                res.append(db.set_with_ttl(q[1], q[2], q[3], q[4], q[5]))
            case "SET_AT_WITH_TTL":
                res.append(db.set_at_with_ttl(q[1], q[2], q[3], q[4], q[5]))
            case "GET":
                res.append(db.get(q[1], q[2], q[3]))
            case "COMPARE_AND_SET":
                res.append(db.compare_and_set(q[1], q[2], q[3], q[4], q[5]))
            case "COMPARE_AND_SET_WITH_TTL":
                res.append(db.compare_and_set_with_ttl(q[1], q[2], q[3], q[4], q[5], q[6]))
            case "COMPARE_AND_DELETE":
                res.append(db.compare_and_delete(q[1], q[2], q[3], q[4]))
            case "DELETE_AT":
                res.append(db.delete_at(q[1], q[2], q[3]))
            case "SCAN":
                res.append(db.scan(q[1], q[2]))
            case "SCAN_AT":
                res.append(db.scan_at(q[1], q[2]))
            case "SCAN_BY_PREFIX":
                res.append(db.scan_by_prefix(q[1], q[2], q[3]))
            case "BACKUP":
                res.append(db.backup(q[1]))
            case "RESTORE":
                res.append(db.restore(q[1], q[2]))

            case _:
                res.append("unsupported")
    return res
