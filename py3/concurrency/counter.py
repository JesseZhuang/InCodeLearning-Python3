"""
python 3 lock
"""

import logging
import threading
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format='(%(threadName)-9s) %(message)s', )  # printf field width 9

OP_CNT = 100_000


class Counter(ABC):
    """counter ABC"""

    def __init__(self, value=0):
        self.value = value

    @abstractmethod
    def increment(self):
        pass

    @abstractmethod
    def decrement(self):
        pass


class NCounter(Counter):
    """not thread-safe"""

    def __init__(self, value: int = 0):
        super().__init__(value)

    # https://stackoverflow.com/questions/77096404/cant-create-race-condition-in-python-3-11-using-multiple-threads
    def increment(self):
        self.value += int(1)

    def decrement(self):
        self.value -= int(1)


class LCounter(Counter):
    """using lock"""

    def __init__(self, value: int = 0):
        super().__init__(value)
        self.lock = threading.Lock()

    def increment(self):
        self.lock.acquire()
        logging.debug('Acquired a lock')
        try:
            logging.debug('incrementing')
            self.value = self.value + int(1)
        finally:
            logging.debug('Releasing a lock')
            self.lock.release()

    def decrement(self):
        with self.lock:
            logging.debug('Acquired lock, decrementing')
            self.value -= int(1)


def inc_worker(c: Counter):
    """workers using counter"""

    for _ in range(OP_CNT):
        c.increment()


def dec_worker(c: Counter):
    """workers using counter"""

    for _ in range(OP_CNT):
        c.decrement()


class CCounter(Counter):
    """using Condition RLock, re-entrant lock"""

    def __init__(self, value=0):
        super().__init__(value)
        self.condition = threading.Condition()

    def increment(self):
        with self.condition:
            self.value += int(1)

    def decrement(self):
        with self.condition:
            self.value -= int(1)


if __name__ == '__main__':
    counter = Counter()
    for i in range(2):
        t = threading.Thread(target=inc_worker, args=(counter,))
        t.start()

    logging.debug('Waiting for worker threads')
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('Counter: %d', counter.value)
