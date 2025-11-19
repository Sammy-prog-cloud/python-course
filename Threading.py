import threading
import time
import random


# def execute_thread():
#     print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
# Note that strftime mean string formatted time
#     rand_sleep_time = random.randint(1, 4)
#     time.sleep(rand_sleep_time)
#     print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
#
#
# for i in range(10):
#     thread = threading.Thread(target=execute_thread)
#     thread.start()
#     print("Active Threads : ", threading.active_count())
#     print("Thread Objects : ", threading.enumerate())

class CustThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        get_time(self.name)
        print("Thread", self.name, "Execution Ends")


def get_time(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep_time = random.randint(1, 4)
    time.sleep(rand_sleep_time)


thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()


