# # # OOPs : 
# # qw = [2, 3, 12, 90, 67, 1, 200, 45]

# # minn = qw[0]  # 2, 1
# # maxx = qw[0]  # 2, 3, 12

# # for i in qw:
# #     # 2 > 1
# #     if minn > i:  
# #         minn = i
        
# #         2 < 12
# #     elif maxx < i:
# #         maxx = i
    
# # print(minn)
# # print(maxx)

# # OOps = object oriented programmin

# # class
# # objects


# 1) class
# 2) object
# 3) self
# 4) constructer
# 5) methods
# 6) abttributes
# 7) Inharitance
#     1) single inharitance
#     2) multipal inharitance
#     3) multilevel inhritance
#     4) hirarical inharitance
#     5) hibrid inharitance

# 8) abstraction
#     abstract class
#     interfaces
#     abstract methods

# 9) Encapsulation
#     access spacifires
#         1) public mambers
#         2) private mambers
#         3) protected mambers

# 10) Polymorphisum:
#     1) Duck Typing
#     2) mehtod overloading
#     3) mehtod overriding
#     4) operator overloading
    



# Class : class is bluprint of an object

# objects : instance of a class

# self = use for ranfrenceing 

# class xyz:
#     def car(self):
#         print("i am a car")
    
#     def bus(self):
#         print("i am a bus")

# obj = xyz()
# obj.bus()

# obj1 = xyz()






# cunstucter : __init__(), it class automatically while we create an objects



# constructer is useed to initlize attrebutes

# class sumthis:
#     def __init__(self):
#         print("heloo i am cnstructer..")
    
#     def xyz(self, a, b):
#         c = a + b
#         print("the sum is : ", c)

#     def bus(self):
#         print("i am bus", a)

# obj = sumthis()
# obj.xyz(12, 10)

# obj.bus()


# class mycls:
#     def __init__(self, a, b):
#         self.name = a
#         self.age = b
    
#     def sumthis(self):
#         print("i am sum", self.name)

#     def car(self):
#         print(f"{self.name} have {self.age} age")

# obj = mycls("kriss", 20)
# ob1 = mycls("ayush", 21)

# ob1.car()


# Inharitance : to get some properties from anther class we use inharitance


# # 1) single inharitance

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2")
        
# obj = cls2()
# obj.mthd1()



# obj = cls1()
# obj1 = cls2()
# obj1.mthd3()






# # multipal inharitance:

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2:
#     def mthd3(self):
#         print("i am from class 2")

# class cls3(cls1, cls2):
#     def mthd4(self):
#         print("i am from class 3")
        
# obj = cls3()
# obj.mthd3()





# # multilevel inharitance:

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2")

# class cls3(cls2):
#     def mthd4(self):
#         print("i am from class 3")
        
# obj = cls3()
# obj.mthd1()





# # hirical inharitance:

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2")

# class cls3(cls1):
#     def mthd4(self):
#         print("i am from class 3")
        
# obj = cls3()
# obj.mthd1()







# hybrid inharitance:

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2")

# class cls3(cls2):
#     def mthd4(self):
#         print("i am from class 3")

# class cls4(cls2, cls3):
#     def mthd5(self):
#         print("i am from class 4")
        
# obj = cls3()
# obj.mthd1()



# 2) abstraction : data hiding

# abstract classes
# abstract method
# interfaces

# abc = abstract base class

# from abc import ABC, abstractmethod

# class cls1(ABC):
#     @abstractmethod
#     def car(self):
#         pass
    
#     @abstractmethod
#     def train(self):
#         print("i am train")

# class cls2(cls1):
#     def bus(self):
#         print("i am bus")
    
#     def car(self):
#         print("i am car")
    
#     def train(self):
#         print("i am train")
        
# obj = cls2()
# obj.car()




















































































