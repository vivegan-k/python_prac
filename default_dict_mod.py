from collections import defaultdict

d = defaultdict(int)

d[1]

print d[1]
print d.keys()

d1 = defaultdict(lambda: 0)

d1['zero']
d1['one']
d1['two'] = 2
print d1

d1['three'] = 'three'

print d1
print d1.keys(), d1.values()
