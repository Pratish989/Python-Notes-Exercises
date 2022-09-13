# Write a program to find the greatest of four numbers entered by the user

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a > b):
#     print("a is greater than b")
# elif(a > c):
#     print("a is greater than c")
# elif(b > c):
#     print("b is greater than c")
# elif(d>c):
#     print("d is greater than c")
# elif(c > a):
#     print()    

# x = max(a,b,c,d) #shortcut method
# print(x)


#q2 Write a program to find out whether a student is pass or fail if it requires a total of 40%
#  and at least 33% in each subject to pass.
#  Assume 3 subjects and take marks as an input from the user.


# maths = int(input())
# if (maths>33):
#     print("you have passed the math exam")
# else:
#     print("you have failed the math exam ")

# hindi = int(input())
# if (hindi>33):
#     print("you have passed the hindi exam")  
# else:
#     print("you have failed hindi exam  ") 


# science = int(input())     
# if (science>33):
#     print("you have passed the science exam")
# else:
#     print("you have failed the science exam")

# if (science>33 and maths> 33 and hindi):
#     print("you are eligible to pass the semester ")
# else:
#     print(x = (science + maths + hindi)/3)

#     if (x >40):
#         print("pass")
#     else:
#         print("fail")
#     )

#correct answer 

# sub1 = int(input("enter your marks "))
# sub2 = int(input("enter your marks "))
# sub3 = int(input("enter your marks "))

# if ( sub1<33 or sub2 < 33 or sub3< 33):
#     print("you have failed this exam bexause of less marks in one of the subjects")
# elif(sub1 +sub2 + sub3)/3 < 40:
#     print("you have failed the exam because you have less average than 40 ")
# else:
#     print("you have now passed the exam ")


#q3 A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# text  = input("enter your text")
# if (" make a lot of money " in text ):
#     print("this is spam comment")
# elif("buy now" in text):
#     print("this is spam comment")
# elif("click this" in text):
#     print("this is spam comment")
# elif("subscribe this " in text):
#     print("this is spam comment")
# else:
#     print("nothing")


#q4 Write a program to find whether a given username contains less than 10 characters or not.

# username = input("enter your username")
# if (len(username) > 10):
#     print("length is greater than 10") 
# else:
#     print("no it is not greater than 10")


#q5 Write a program that finds out whether a given name is present in a list or not.


# listofnames = ["kavya", "pratish", "khushi", "namra", "aaditya", "smit", "maharshi"]

# x = input("enter your name")
# if (x in listofnames):
#     print("your name is in the list")
# else:
#     print("your name is not in the list")

#q6 Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100	Ex
# 80-90	A
# 70-80	B
# 60-70	C
# 50-60	D
# <50	F


# marks = int(input("enter your marks"))
# if ( 100<marks or marks>90 ):
#     print("your grade is A")
# elif( 90<marks or marks>80):
#     print("your grade is  B")
# elif(80<marks or marks>70):
#     print("your grade is C")
# elif(70<marks or marks>60):
#     print("your grade is D")
# elif(60<marks or marks>50):
#     print("your grade is E")
# else:
#     print("your grade is F")


#q7 Write a program to find out whether a given post is talking about “Harry” or not

post = input("enter the post")

if "harry" in post:
    print("yes")
else:
    print("no")