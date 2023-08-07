import time,datetime
import random
class Animal:
    def __init__(self,name,age):
        animal="a living organism that feeds on organic matter"
        self.name=name
        self.age=age
    def __repr__(self):
        return(f'animal defination:{self.name}')
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name,age=14)
        self.lucky_num=random.randint(10,15)
    #def __str__(self):
     #   return("number lucky is:",self.lucky_num)

goodi=Dog("hi")
print(goodi.lucky_num)
print(goodi.name)
