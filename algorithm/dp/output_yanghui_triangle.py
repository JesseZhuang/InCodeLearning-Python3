'''lint code 2348, easy'''

# read data from console
n = int(input())
l = [[1]]

while len(l) < n:
    l1 = [0] + l[len(l) - 1]
    l2 = l[len(l) - 1] + [0]
    l.append([x + y for x, y in (zip(l1, l2))])

# output the answer to the console according to the requirements of the question

for i in range(n):
    print(*l[i])
