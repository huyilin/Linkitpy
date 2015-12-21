__author__ = 'Yilin'

from multiprocessing import Pool

def f(x):
    return x * x
if __name__ == '__main__':

    pool = Pool(processes = 10)
    results = pool.map(f, range(1000000))
    print results

    print "hello"