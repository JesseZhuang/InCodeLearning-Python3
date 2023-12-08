# priority queue
import heapq
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

q = Q.PriorityQueue()
q.put((10, 'ten'))  # first item in the tuple should be comparable, same for heapq
q.put((1, 'one'))
q.put((5, 'five'))
while not q.empty():
    print(q.get())

# (1, 'one')
# (5, 'five')
# (10, 'ten')

# heapq, heap[k] <= heap[2*k+1] and heap[2*k+2], 0 based
# if 1 based, heap[2*k] and heap[2*k+1]


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def heapsort(iterable):
    heapq.heapify(iterable)  # Transform list x into a heap, in-place, in linear time.
    print(iterable[0])
    heapq.heappop(iterable)  # take out the min element
    return [heapq.heappop(iterable) for i in range(len(iterable))]


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
# 0
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
