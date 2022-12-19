from ast import arg
from multiprocessing import set_forkserver_preload


class Calculator(object):
    cost = 1000
    def __init__(self, brand,model='123',man_year='2022'):
        self.brand = brand
        self.model = model
        self.man_year = man_year

    def __repr__(self):
        return '{} {}'.format(self.brand, self.model)

    def __str__(self) -> str:
        return 'Calculator class for {} {}'.format(self.brand, self.model)

    def __call__(self, *args, **kwds):
        return args

    @staticmethod
    def get_number(num):
        return 'Received number: %s' % str(num)
    
    @classmethod
    def change_cost(cls, cost):
        cls.cost = cost
    
    @classmethod
    def change_brand(cls, brand):
        return cls(brand)
    
    def get_brand(self):
        return self.brand
    
    def get_cost(self):
        return self.cost

    def add(self, *args):
        self.sum1 = 0
        print(args)
        for val in args:
            self.sum1 += val
        return self.sum1

    def sub(self, val1, val2):
        self.diff = val1 - val2
        return self.diff

    @property
    def year(self):
        '''
        Manufactured year
        '''
        return self.man_year

    @year.setter
    def year(self, man_year):
        print('Year is set as {}'.format(man_year))
        self.man_year = man_year
        return self.man_year
    
    @year.deleter
    def year(self):
        print('Year is deleted')
        self.man_year = None

        

class Calculator1(Calculator):
    def __init__(self, brand):
        super(Calculator1, self).__init__(brand)
    
    def get_brand_name(self):
        return self.brand

class Calculator2(Calculator):
    pass

class Calculator3(Calculator1, Calculator2):
    pass


calc = Calculator(brand='casio')
print(calc.add(1,2,3,4,5))
print(calc.sub(7,1))
print(calc.get_number(5))
Calculator.get_number(2)
Calculator.change_cost(2000)
print(calc.get_cost())
print(calc.get_brand())
new_calc = Calculator.change_brand('citizen')
print(new_calc.get_brand())
new_calc.change_cost(3000)
print(new_calc.get_cost())
calci = Calculator(brand='ti')
print(calci.get_cost())
#print(help(Calculator3)) # Prints MRO order
calc1 = Calculator1('test')
print(calc1.get_brand_name())
print(calc)
print(repr(calc))
print(str(calc))
print(calc(1,2,3))
print(calc.year)
calc.year = '2000'
print(calc.year)
del calc.year
print(calc.year)
