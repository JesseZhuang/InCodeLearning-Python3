# defaultdict is a subclass of dict

# usage of defaultdict and & in sets

from collections import defaultdict

a = [[1, 2], [3, 4], [3, 6]]
b = [[1, 2], [2, 3], [3, 5]]

dict_a = defaultdict(list)
dict_b = defaultdict(list)

print("two empty defaultdicts:\n  dict_a is", dict_a)
print("  dict_b should be same", dict_b)

for item in a:
    dict_a[item[0]].append(item)

for item in b:
    dict_b[item[0]].append(item)

dict_a[1].append([1, 2, 3, 4])  # can add arbitrary key value pairs
dict_a[10].append((2, 3))  # add a tuple into the list

print("after adding elements\n ", dict_a)

print("a normal dict\n ", {1: [1, 2], 3: [3, 4]})
# get common first element in each list
common_keys = set(dict_a.keys()) & set(dict_b.keys())
print("common keys")
for key in common_keys:
    print("  key: {0}, dict a: {1}, dict b: {2}".
          format(key, dict_a[key], dict_b[key]))
print("constant factory with lambda")


# constant function factory with lambda function
def constant_factory(value):
    return lambda: value
d = defaultdict(constant_factory('missing'))
print(' ', d)  # still empty
d.update(name='John', action='ran')
d['name'] = 'Jesse'
print('  %(name)s %(action)s to %(object)s' % d)
print(' ', d)
print('  %(name)s %(action)s to %(unexisting)s' % d)
print(' ', d)
