import numpy as np

print 'Create np array'

li = [1,2,3]
arr = np.array(li)
print arr # one dimensional

li1 = [[1,2,3],[4,5,6],[7,8,9]]
arr1 = np.array(li1)
print arr1

print 'np arange'

print np.arange(0,10)
print np.arange(0,11,2)

print np.zeros(3)
print np.zeros((2,3))
print np.ones((3,4))

print np.linspace(0,5,100) #Takes 3rd argument as no of points we want in given range

print 'Identity matrix'

np.eye(4)

print 'Random values'

print np.random.rand(5) #random samples from a uniform distribution over 0 to 1.
print np.random.rand(5,5)

print np.random.randn(5) # standard normal distribution or a Gaussian distribution
print np.random.randn(5,5) # standard normal distribution or a Gaussian distribution

print np.random.randint(1,100,10)
arr2 = np.arange(25)
print 'arr2', arr2

print 'arr2.reshape(5,5)', arr2.reshape(5,5)
reshaped_array = arr2.reshape(5,5)

print reshaped_array.shape
print arr2.max()

print arr2.min()

print arr2.argmin()
print arr2.argmax()
print arr2.shape
