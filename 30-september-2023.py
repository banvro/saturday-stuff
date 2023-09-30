# Excaption handeling : 

# 1) complite time error (syntex error)
# 2) logical error
# 3) time error


# a  10
# b = 20
# c = a + b

# if 10 ==10
#     print("hello")



# logical error

# a = 10
# b = 0

# c = a /b 

# print(c)

# runt time errror 

# age = int(input("Enter your age : "))


# print("user enterd :", age)

# try : 
#     # diutable code

# except Exception:
#     #handel errors here...

# else:
#     # it execute for while your try is not genrate any error
# finally:
#     # it just idecate your excaption handeled






# a = 10
# b = 2

# try:
#     age = int(input("Enter your age : "))

# except Exception:
#     print("here is an error")

# else:
#     print("user age is : ", age)

# finally:
#     print("i am done..")

# print("sbjahsvdj")


# import re 

# text = """Python was conceived in the late 1980s[43] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[45] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life", a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[46] In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[47][48]

# Python 2.0 was released on 16 October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 3.0, released on 3 December 2008, with many of its major features backported to Python 2.6.x[50] and 2.7.x. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[51]

# Python 2.7's end-of-life was initially set for 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[52][53] No further security patches or other improvements will be released for it.[54][55] Currently only 3.8 and later are supported (2023 security issues were fixed in e.g. 3.7.17, the final 3.7.x release[56]). In 2021, Python 3.9.2 and 3.8.8 were expedited[57] as all versions of Python (including 2.7[58]) had security issues leading to possible remote code execution[59] and web cache poisoning.[60]

# In 2022, Python 3.10.4 and 3.9.12 were expedited[61] and 3.8.13, because of many security issues.[62] When Python 3.9.13 was released in May 2022, it was announced that the 3.9 series (joining the older series 3.8 and 3.7) would only receive security fixes in the future.[63] On September 7, 2022, four new releases were made due to a potential denial-of-service attack: 3.10.7, 3.9.14, 3.8.14, and 3.7.14.[64][65]

# As of November 2022, Python 3.11 is the stable release. Notable changes from 3.10 include increased program execution speed and improved error reporting.[66]

# Since 27 June 2023, Python 3.8 is the oldest supported version of Python (albeit in the 'security support' phase), due to Python 3.7 reaching end-of-life.[67]

# The first release candidate of Python 3.12 was offered on 6 August 2023.

# """




# ptrn = "\d\d\d\d"

# match = re.findall(ptrn, text)

# print(match)
# # for i in match:
# #     print(i)



# import re

# txt = """Python was conceived in the late 1980s[43] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[45] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" abc@gmail.com from his responsibilities as Python's "benevolent dictator for life", a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[46] In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[47][48]

# Python 2.0 was released on 16 abc123@gmail.com October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 3.0, released on 3 December 2008, with many of its major features backported to Python 2.6.x[50] and 2.7.x. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[51]

# Python 2.7's end-of-life was initially set for 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[52][53] No further security patches or other improvements will be released for it.[54][55] Currently only abc123@yahho.com 3.8 and later are supported (2023 security issues were fixed in e.g. 3.7.17, the final 3.7.x release[56]). In 2021, Python 3.9.2 and 3.8.8 were expedited[57] Abc1abc@gmail.in as all versions of Python (including 2.7[58]) had security issues leading to possible remote code execution[59] and web cache poisoning.[60]

# In 2022, Python 3.10.4 and 3.9.12 were expedited[61] and 3.8.13, because of many security issues.[62] When Python 3.9.13 was released in May 2022, it was announced that the 3.9 series (joining the older series 3.8 and 3.7) would only receive security fixes in the future.[63] On September 7, 2022, four new releases were made due to a potential denial-of-service attack: 3.10.7, 3.9.14, 3.8.14, and 3.7.14.[64][65]

# As of November 2022, Python 3.11 is the stable release. Notable changes from 3.10 include increased program execution speed and improved error reporting.[66]

# Since 27 June 2023, Python 3.8 is the oldest supported version of Python (albeit in the 'security support' phase), due to Python 3.7 reaching end-of-life.[67]

# The first release candidate of Python 3.12 was offered on 6 August 2023.

# """

# [9876]\d{9}
# ptrn = "[a-zA-z][a-z]+\d*[a-z]*[@][a-z]+[.][a-z]{2,3}"



# match = re.findall(ptrn, txt)

# print(match)


# Multithreading : 


# Multithreading 

# a = 10

# b = 20

# c = a + b

# print("hellowww")

# print("imporetnet")

# print("done")



# import threading

# def fun1():
#     for i in range(100):
#         print("heyyyyyyyyy")
    
# def fun2():
#     for i in range(500):
#         print("noooooooooo")

# print("code start...")

# fun1()

# fun2()

# th1 = threading.Thread(target = fun1)
# th2 = threading.Thread(target = fun2)

# th1.start()
# th2.start()

# print("important code")

# print("helloooo")

# print("goooooo")

# print("done")



import mysql.connector



con = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "saturday")

courser = con.cursor()

courser.execute("insert into saturdayclass values('Python', '823485542', 'python@gmail.com')")
con.commit()














