#q1.1
# name = input("enter your name :")
# age = input("enter your age:")
# age = int(age)
# import datetime
# date = datetime.datetime.now() #here, the first datetime is class and second one is function.
# temp = 100 - age 
# u_date = temp + date.year
# print(u_date)
# print(date)

#q1.2
# a= input("enter any number :")
# a = int(a)
# if(a%2==0):
#  print(" this number is even")
# else:
#  print("this number is odd")


#q identify whether the user given number is multiple of 4 or not.
# a= input("enter any number :")
# a = int(a)
# if (a%4==0):
#     print("it is a multiple of 4")
# else:
#     print("it is not a multiple of 4")


#q check whether the user-input number is +,-,0

# a = int(input("enter any  number"))
# if (a>0):
#     print("positive")
# elif(a==0):
#     print("zero") 
# else:
#     print("negative")


#q2.1 Write a program as mentioned below:
# Take a list, a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], and write a program that print out 
# all the elements of the list that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in  range(len(a)):
#   if(a[i]<5):
#        print(a[i])


# to get th output in single line 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in  range(len(a)):
#   if(a[i]<5):
#        print(a[i],end =" ")

# another method to get the output in single line
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]      
# ans = []
# for i in range(len(a)):
#     if (a[i]<5):
#         ans.append(a[i])
# print(ans)



#q check whether the user-entered year is leap year or not.

y  = int(input("enter year"))
if (y%4 == 0):
    print("leap year")
else:
    print(" {0} is not a leap year".format(y))



    


