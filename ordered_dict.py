import collections

print 'Normal dictionary:'

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

print 'OrderedDict:'
# OrderedDict inserts value based on order we are inserting
d = collections.OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['f'] = 'F'
d['e'] = 'E'

for k, v in d.items():
    print k, v
