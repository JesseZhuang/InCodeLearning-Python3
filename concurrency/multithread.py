'''
https://docs.python.org/3/library/threading.html
python multithreading
CPython implementation detail: In CPython, due to the Global Interpreter Lock, 
only one thread can execute Python code at once (even though certain performance-oriented 
libraries might overcome this limitation). If you want your application to make better use of 
the computational resources of multi-core machines, you are advised to use multiprocessing or 
concurrent.futures.ProcessPoolExecutor. However, threading is still an appropriate model 
if you want to run multiple I/O-bound tasks simultaneously.
'''
import threading
import time


def print_cube(num):
    '''function to print cube of given num'''
    print('active number of threads:', threading.active_count(), f'. Sleeping 2s in {threading.current_thread().name}')
    time.sleep(2)
    print(f"Cube: {num*num*num}")


def print_square(num):
    '''function to print square of given num'''
    time.sleep(3)
    print(f'Slept 3s in {threading.current_thread().name}', 'active number of threads: ', threading.active_count())
    print(f"Square: {num*num}")


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    t1.start()  # start a new thread, then run the target function with args
    t2.start()
    print(f'in {threading.current_thread().name}', 'active number of threads: ', threading.active_count())
    # wait for finishing
    t1.join()
    t2.join()
    # both threads completely executed
    print("Done!")
