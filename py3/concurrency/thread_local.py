"""
thread local
"""

import threading
from time import sleep


def task(value):
    """store value and sleep for that duration"""
    local = threading.local()
    local.value = value
    sleep(value)
    print(f'Stored value: {local.value}')


# threads can share same variable name, value are different
threading.Thread(target=task, args=(1,)).start()
sleep(0.5)
threading.Thread(target=task, args=(2,)).start()
# Stored value: 1
# Stored value: 2
