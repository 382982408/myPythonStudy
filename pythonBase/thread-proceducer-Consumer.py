#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/2
'''
假设有一群生产者和一群消费者，他们通过一个市场来交换产品，生产者的策略是如果市场上剩余的产品少于1000个，
那么久生产100个产品投放到市场上，而消费者的策略是如果市场上剩余的产品多余100个的时候，那么久生产3个商品
'''
import threading
import time

#定义生产者
class Producer(threading.Thread):
    def run(self):
        global count

        while True:
            #判断全局变量是否被上锁
            if con.acquire():
                #生产者已经满足市场条件
                if count > 1000:
                    con.wait()
                else:
                    #继续生产商品
                    count += 100
                    msg = self.name + "生产者已经生产了100个商品了，总数量为:" + str(count)
                    print(msg)
                #释放锁
                con.release()
            time.sleep(1)
#定义消费者
class Consumer(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 100:
                    con.wait()
                else:
                    count -= 3
                    msg = self.name + "消费者消费了3个产品，总数量为:" + str(count)
                    print(msg)
                    con.notify()
                con.release()
            time.sleep(1)

if __name__ == '__main__':
    #定义一个全局变量，表示商品数量
    count = 500
    #创建条件变量
    con = threading.Condition()
    #创建两个生产者线程
    for i in range(2):
        p = Producer()
        p.start()
    #创建5个消费者
    for i in range(5):
        c = Consumer()
        c.start()

