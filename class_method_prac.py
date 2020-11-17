class A(object):
    num_of_emp = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
        A.num_of_emp += 1

    @classmethod
    def from_string(cls, string):
        first, last = string.split('-')
        return cls(first, last)

obj = A('vivek', 'anand')
print obj.num_of_emp
print obj.first

new_obj = A.from_string('iniyan-v')
print new_obj.num_of_emp
print new_obj.first