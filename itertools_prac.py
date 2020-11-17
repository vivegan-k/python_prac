import itertools

days = ['sun','mon','tue']

cycle1 = itertools.cycle(days)

print next(cycle1)
print next(cycle1)
print next(cycle1)
print next(cycle1)

countr = itertools.count(100,10)

print next(countr)
print next(countr)
print next(countr)

print list(itertools.chain('1234','ABCD'))

def test_function(x):
    return x <40

vals = [10, 20, 30, 40, 30, 50]

print list(itertools.dropwhile(test_function, vals))
print list(itertools.takewhile(test_function, vals))