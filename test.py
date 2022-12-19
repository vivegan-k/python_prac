from ctypes.wintypes import PMSG
from unicodedata import name
from unittest import result
from urllib3 import Retry


def swap(a, b):
    a,b = b,a
    return a,b

li = [1,1,2,2,3,3,5,5,6,7,7]

def odd_and_single_occurence(li):
    d = {}
    for val in li:
        if val not in d:
            d[val] = 1
        else:
            d[val] += 1
    print(d)

    res = []
    for key in d.keys():
        if d[key] == 1 and key % 2 != 0:
            res.append(key)
    return res

print(odd_and_single_occurence(li))

li1 = [1,2,3]
li2 = [4,5,6]

def sum_of_squares(a, b):
    result = []
    for x,y in zip(a,b):
        result.append(x**2 + y**2)
    return result

print(sum_of_squares(li1,li2))

def fibonacci(n):
    a, b = 0,1
    for i in range(n):
        yield a
        a, b = b, a+b

def square(func):
    def wrapper(n):
        return func(n) ** 2
    return wrapper

@square
def get_number(n):
    return n

class Arithmetic(object):
    def __init__(self, a, b):
       self.a = a
       self.b = b

    def add_values(self):
        return self.a + self.b

obj = Arithmetic(2,3)
print(obj.add_values())

list1 = [2,3,4,5]
print(list(map(lambda x : x**2, list1)))

Employee table - eid name doj 
Accounts table - aid salary eid 

SELECT name,eid, doj 
FROM Employee
WHERE Employee.eid == Accounts.eid
AND Accounts.salary > 15000

1. Test needs to be executed exactly at 3 PM
2. Listener script needs to be be idle and executed at 3 PM
3. If retured log is smaller in size which can be taken backup, it should be taken backup




