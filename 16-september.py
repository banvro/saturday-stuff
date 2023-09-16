# range(start, end, increament)

# default :
#     start = 0
#     end = n - 1
#     increament = 1


# range(3, 1)

# for i in range(1, 11):
#     print("2 x ", i, "=", 2 * i)
#     print()




# a = 20

# print("akjsbdkasd a", a, "aksjdbkasjd", a)

# data types : 

# 1) Integer
# 2) Float
# 3) String 
# 4) Boolean
# 5) complex
    # 6) Lsit
    # 7) Set 
    # 8) tuple
    # 9) DIctionry


# a = (12, 20, 90, 78, "helo", "100.8")

# print(type(a))


# list    : ordered, allow duplicate values, mutable
# tuple   : ordered, allow duplicate values, imutable
# set      : unordered, do not allow duplicasy, mutable
# dictionry : ordered, do not allow dupliasy, mutable

# lst = [12, 100, 78, "hello", "ok", "nice", 200]
# print(lst, type(lst))
# print(lst[-2])


# slicing :

# lst = [12, 100, 78, "hello", "ok", "nice", 200]

# print(lst[2 : 6])
# print(lst[4 : ])
# print(lst[ : : 2])

# lst = [12, 100, 78, "hello", "ok", "nice", 200]

# 1) append()
# 2) insert()

# lst.append(1000)
# lst.insert(2, 1000)

# print(lst)

# lst = [12, 100, 78, "hello", "ok", "nice", 200]

# to delete data 
# 1) pop()
# 2) remove()

# lst.pop()
# lst.remove(lst[4])

# clear()

# lst.clear()

# print(lst)
# lst = []


# for i in range(10):
#     lst.append(i)

# print(lst)
# for i in range(5):
#     print(i)
#     print("hello wordls")
#     print(i, i, i ,i)
#     print("ok")

# print("yyyyyyyyyyyyyy")




# a = [12, 2, 23, 34, 12, 2, 10, 1]
# b = 0

# for i in a:
#     b = b + i

# print(b)



# tuple   : ordered, allow duplicate values, imutable


# tpl = (10, 90, 100, "hello", 100.8, 100)

# print(tpl, type(tpl))


# set      : unordered, do not allow duplicasy, mutable

# st = {12, 100, "hello", 900, 100, 12}

# st.add(1000)
# st.pop()
# st.remove(100)

# print(st)



# dictionry : ordered, do not allow dupliasy, mutable

# {key : value} 
# dict = {"name" : "kriss", "age" : 20, "number" : 9236498}

# dict["Adderesss"] = "this is my address"
# dict.pop("age")

# print(dict.values())
# print(dict.keys())

# dic = {
#     1 : {
#         "name" : "ayush",
#         "age" : 20
#     },
#     2 : {
#         "name" : "kriss",
#         "age" : 20
#     }
# }

# print(dic[2]["age"])

# lst = ["name", "age", "number"]

# tpl = ("Kriss", 20, 9836487234)

# dict = {}

# for i in range(3):
#     dict[lst[i]] = tpl[i]

# print(dict)
# ouput :
#  
# {"name" : "kriss", "age" : 20, "number" : 982342346}


# functions : 

# xyz()

# 1) userdefine function 

# 2) built in function
# print()
# input()
# len()
# type()
# int()


# a = 10
# b = 20
# c = a + b
# print(c)



# z = 10
# y = 40
# s = z + y
# print(s)


# def xyz():
#     print("Hello world")


# xyz()


# xyz()

# xyz()


# perameters
# arguments



# #perameters
# def sumthis(a, b):
#     c = a + b
#     print(c)


# #arguments
# sumthis(12, 10)

# sumthis(100, 2000)


# sumthis()/


# def xyz(x, y):
#     print(f"usernam eis : {x} user age is : {y}")


# xyz(y = 30, x = "kriss")


# xyz("moris", 89)


# def sum(a = 100, b = 200):
#     c = a + b

#     print(c)


# sum(10, 1)


# 1) *args = arbitrary positanl argumnts
# 2) **kwargs  = keyword posinal argumnets

# def cal(*args):
#     z = 0
#     for i in args:
#         z = z + i
#     print(z)

# cal(12, 10, 100, 89, 67, 1)

# ()

# {}

# def myinfo(**r):
#     print(r)

# # myinfo(12, 2,3, 34, 5)
# myinfo(name = "kriss", age = 30)

# return
# def ui(a, u):
#     x = a + u
#     # print(x)
#     return x

# yu =  ui(12, 10)


# y = 100 + yu

# print(y)


# code optimization





# table(89)

# 2 x 1 = 2
# 2 x 2 = 4
# .
# .
# .

# .
# .
# 2 x 10 = 20
# def tbl(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)

# while True:
#     choc = input("Press q for quit and t for print table : ")

#     if choc == "q":
#         break

#     elif choc == "t":
#         zx = int(input("Enter table number : "))
#         tbl(zx)
#     else:
#         print("Please enter smehting vaild..")



# for i in range()

# lst = ["hlo", 1, 2, 3, 78, 100]


# age = 18

# # 18 < 20
# while age < 20:
#     age = age + 1
#     print("helloooooo")




# def tbl(n):
#     # for i in range(1, 11):
#     #     print(n, "x", i, "=", n * i)
#     x = 1
#     while x <= 10:
#         print(n, "x", x, "=", n * x)
#         x = x + 1


# tbl(12)


# a = 10

# zx = a + a + a + a + a + a + a + a + a + a

# b = (a + a + a + a + a + a + a + a)/a

# s = int(b)

# print(zx + s)




# print(b)


# z = True + True

# print(b - z)
# print(b - len("ui"))












# Excaption Handeling :

# 1) compile Time Error 
# 2) Logical Error   
# 3) Run Time error


# if 10 == 10
#     print("helloooo")

# a = 
# v 10


# 2) logical error :

# a = 10
# b = 0

# c = a/b

# print(c)


# 3) run time error 

# age = int(input("Enter your age : "))

# print(age)


# try:
#     # doutable code.....

# except Exception:
#     # error handel here

# else:
#     # work if try not create any error

# finally:
#     # excecutte to tell ty exxaeption block working

a = 10
b = 8

# age = int(input("Ente your age : "))

try:
    c = a / b
    age = int(input("Ente your age : "))

except ZeroDivisionError:
    print("you never devide any degiit by 0")

except ValueError:
    print("Enter vaid age...")

except Exception as e:
    print(e)

else:
    print(c, age)

finally:
    print("i am done....")


print("kjasdjaasjdhvjsahd")












