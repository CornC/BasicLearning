'''
@Description: 多进程和多线程编程
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-08-13 15:15:35
@LastEditors: CornC.fcx
@LastEditTime: 2019-08-13 16:59:57
'''

# 单进程
from random import randint
from time import sleep, time
from multiprocessing import Process  # 注意 代码提示中的 process 是无法作为函数调用的 要引入的是 Process
from threading import Thread, Lock
from os import getpid


def download_file(filename):
    print('开始下载>>>>>>> 进程号[%d]' % getpid())
    download_time = randint(5, 10)
    sleep(download_time)
    print(' %s 下载耗时 %d' % (filename, download_time))


def sample_ex():
    start = time()
    download_file('abc.pdf')
    download_file('def.pdf')
    end = time()
    print('共耗时 %d' % (end - start))


# 多进程


def multi_ex():
    start = time()
    p1 = Process(target=download_file, args=('abc.pdf', ))
    p1.start()
    p2 = Process(target=download_file, args=('def.pdf', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('共耗时 %d' % (end - start))


# 多线程


def multi_thread():
    start = time()
    t1 = Thread(target=download_file, args=('abc.pdf', ))
    t1.start()
    t2 = Thread(target=download_file, args=('def.pdf', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时 %d' % (end - start))


# 自定义线程（ 继承 Thread 重写其 Run 方法 ）


class DownloadThread(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载>>>>>>> 进程号[%d]' % getpid())
        download_time = randint(5, 10)
        sleep(download_time)
        print(' %s 下载耗时 %d' % (self._filename, download_time))

def my_thread():
    start = time()
    t1 = DownloadThread('abc.pdf')
    t1.start()
    t2 = DownloadThread('def.pdf')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时 %d' % (end - start))

# 线程锁

class Account(object):

    def __init__(self):
        self._money = 0
        self._lock = Lock() # 保证每个进程可以有序的对该属性进行修改

    def update_account(self, money):
        self._lock.acquire()
        try:
            new_money = self._money + money
            sleep(0.01)
            self._money = new_money
        finally:
            self._lock.release()

    @property
    def money(self):
        return self._money

class AccountThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.update_account(self._money)

def thread_lock():
    account = Account()
    threads = []
    for _ in range(100):
        t = AccountThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.money)


if __name__ == "__main__":
    # sample_ex()
    # multi_ex()
    # multi_thread()
    #　my_thread()
    thread_lock()
