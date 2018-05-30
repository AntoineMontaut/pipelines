from multiprocessing import Pool
from time import sleep, clock, time

def slow_function(e):
    sleep(2)
    print("Finished",e)
    return e*10

def main():
    # without
    print('Normal loop')
    elements = range(8)
    time1 = time()
    processed_elements = list(map(slow_function, elements))
    time2 = time()
    print('Took %0.3f s' % (time2-time1))
    print(processed_elements)

    # with
    print('Fast loop')
    pool = Pool(8)
    elements = range(8)
    time1 = time()
    processed_elements = pool.map(slow_function, elements)
    time2 = time()
    print('Took %0.3f s' % (time2-time1))
    pool.close()
    print(processed_elements)

if __name__ == '__main__':
    main()
