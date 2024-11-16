#!usr/bin/python
# coding:utf8

# how to avoid tedious conditionals or loops using dictionary method.

dict_data = {
    "A2": 3,
    "A3": 0,
    "B1": 4,
    "C3": 4,
    "C1": 2,
    "C4": 6,
    "D1": 5,
    "D2": 1
}

'''
target = [
    {
        "class" : "A",
        "elements" : [{"name":"A2", "value":3}, {"name":"A3", "value":0}]
    },
    {
        "class" : "B",
        "elements" : [{"name":"B1", "value":4}]
    },
    {
        "class" : "C",
        "elements" : [{"name":"C3", "value":4}, {"name":"C1", "value":2},
        {"name":"C4", "value":6}]
    },
    {
        "class" : "D",
        "elements" : [{"name":"D1", "value":5}, {"name":"D2", "value":1}]
    }
]
'''

# with tedious conditionals

tempA = {"class": "A", "elements": []}
tempB = {"class": "B", "elements": []}
tempC = {"class": "C", "elements": []}
tempD = {"class": "D", "elements": []}

for e in dict_data.keys():
    if e[0] == tempA["class"]:
        tempA["elements"].append({"name": e, "value": dict_data[e]})
    elif e[0] == tempB["class"]:
        tempB["elements"].append({"name": e, "value": dict_data[e]})
    elif e[0] == tempC["class"]:
        tempC["elements"].append({"name": e, "value": dict_data[e]})
    elif e[0] == tempD["class"]:
        tempD["elements"].append({"name": e, "value": dict_data[e]})

target = [tempA, tempB, tempC, tempD]
print(target)

# with dictionary

result = {
    "A": {"class": "A", "elements": []},
    "B": {"class": "B", "elements": []},
    "C": {"class": "C", "elements": []},
    "D": {"class": "D", "elements": []}
}

# todo note printed maybe a dict_values() object, not a list?
for e in dict_data.keys():
    result[e[0]]["elements"].append({"name": e, "value": dict_data[e]})

print(result.values())
print(result.values() == target)
