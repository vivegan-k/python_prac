import multiprocessing

def add(a,b):
    print 'sum:', a+b

def sub(a,b):
    print 'minus:', a-b


if __name__ == '__main__':

    p1 = multiprocessing.Process(target=add, args=(10,3))

    p2 = multiprocessing.Process(target=sub, args=(10,3))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
