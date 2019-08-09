import random
import time

start_time = time.time
class Cat:
    def __init__(self,new_name):
        print("这是一个初始化方法")
        self.name = new_name
    def eat(self):
        print("%s爱吃鱼"%self.name)


laji = Cat("垃圾")
laji.eat()
i = random.randint(1, 10)
print(i)
end_time = time.time
print("时间为：%f" % (end_time - start_time))




