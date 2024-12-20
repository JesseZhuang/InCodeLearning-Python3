import time
from threading import Thread
from unittest import TestCase

from py3.concurrency.counter import NCounter, LCounter, inc_worker, OP_CNT, dec_worker, CCounter

THREAD_CNT = 10


class TestCounter(TestCase):

    def setUp(self):
        self.tbt1 = NCounter()
        self.tbt2 = LCounter()
        self.tbt3 = CCounter()

    def test_unsafe_counter(self):
        threads = [Thread(target=inc_worker, args=(self.tbt1,)) for _ in range(THREAD_CNT)]
        for t in threads: t.start()
        for t in threads: t.join()
        self.assertNotEqual(self.tbt1.value, THREAD_CNT * OP_CNT)

        threads = [Thread(target=dec_worker, args=(self.tbt1,)) for _ in range(THREAD_CNT)]
        for t in threads: t.start()
        for t in threads: t.join()
        self.assertNotEqual(self.tbt1.value, - THREAD_CNT * OP_CNT)

    def test_safe_counters(self):
        threads = [Thread(target=inc_worker, args=(c,)) for _ in range(THREAD_CNT)
                   for c in [self.tbt2, self.tbt3]]
        for t in threads: t.start()
        for t in threads: t.join()
        self.assertEqual(self.tbt2.value, THREAD_CNT * OP_CNT)
        self.assertEqual(self.tbt3.value, THREAD_CNT * OP_CNT)

    def test_rlock_vs_lock_timing(self):
        """python 3.12 Rlock faster 0.3 s < 0.39 s"""
        start = time.time()
        threads = [Thread(target=dec_worker, args=(self.tbt2,)) for _ in range(THREAD_CNT)]
        for t in threads: t.start()
        for t in threads: t.join()
        self.assertEqual(self.tbt2.value, -THREAD_CNT * OP_CNT)
        end = time.time()
        print(end - start)

        start = time.time()
        threads = [Thread(target=dec_worker, args=(self.tbt3,)) for _ in range(THREAD_CNT)]
        for t in threads: t.start()
        for t in threads: t.join()
        self.assertEqual(self.tbt3.value, - THREAD_CNT * OP_CNT)
        end = time.time()
        print(end - start)
