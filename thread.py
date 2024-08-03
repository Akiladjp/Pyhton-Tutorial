from time import sleep;
from threading import *;

# def func1():
#     for i in range(5):
#         print('Good')
#         sleep(1)
    
# def func2():
#     for i in range(5):
#         print('bye')
    
# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)

# t1.start()
# sleep(0.2)
# t2.start()


class A(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)

class B(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5):
            print('Welcome')
            sleep(1)

obj1 = A()
obj2 = B()

obj1.start()
sleep(0.2)
obj2.start()

obj1.join()
obj2.join()


