import multiprocessing

def square_list(ip_list, q):

    for i in ip_list:
        q.put(i ** 2)

def extract_queue(q):
    while not q.empty():
        print q.get()
    print 'Queue is now empty'

if __name__ == '__main__':

    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=square_list, args=([1,2,3,4], q))
    p2 = multiprocessing.Process(target=extract_queue, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
