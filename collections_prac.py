import collections

Point = collections.namedtuple("Point", "x y")
p1 = Point(10,20)
p2 = Point(30,40)

print p1
print p2

p1 = p1._replace(x=100)

print p1

d = collections.defaultdict(int)

fruits = ['apple', 'banana', 'papaya', 'banana', 'orange', 'pineapple', 'mango']
fruits1 = ['mango','kiwi', 'avocado']

for fruit in fruits:
    d[fruit] += 1

print d

counter = collections.Counter(fruits)
print counter
print sum(counter.values())

counter.update(fruits1)
print counter
print sum(counter.values())

print counter.most_common(2)

print  counter
counter.subtract(fruits1)
print counter

deq = collections.deque('abcde')

print len(deq)
deq.append('f')

print deq

deq.appendleft('z')

print deq

deq.pop()

print deq

deq.popleft()

print deq