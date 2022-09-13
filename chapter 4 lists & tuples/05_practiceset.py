#  #q1 Write a program to store seven fruits in a list entered by the user.

# fruitno1 = input("enter 1 fruit")
# fruitno2 = input("enter 2 fruit")
# fruitno3 = input("enter 3 fruit")
# fruitno4 = input("enter 4 fruit")
# fruitno5 = input("enter 5 fruit")
# fruitno6 = input("enter 6 fruit")
# fruitno7 = input("enter 7 fruit")


# fruits = [fruitno1,fruitno2,fruitno3,fruitno4,fruitno5,fruitno6,fruitno7]
# print(fruits)


#q2 Write a program to accept the marks of 6 students and display them in a sorted manner.t

# s1 = int(input("enter marks :"))   #IMPNOTE str me se int me karna na bhule
# s2 = int(input("enter marks :"))
# s3 = int(input("enter marks :"))
# s4 = int(input("enter marks :"))
# s5 = int(input("enter marks :"))
# s6 = int(input("enter marks :"))

# studentsmarks = [s1,s2,s3,s4,s5,s6]
# print(studentsmarks)
# studentsmarks.sort() #IMPNOTE - ek baar sort ho jaye fir uss variable print karna ho ta hai 
# print(studentsmarks)


# #q3 check that a tuple cannot be changed in python

# t1 = (1, "harrywithhair",98.78,True)
# t1[0] = 45  # this is how you can add anything at any index of  a tuple 
# error shows, that means you cant change any tuple 





#q4 Write a program to sum a list with 4 numbers.

# a = [23,-45,65,45]
# print(a[0]+a[1]+a[2]+a[3])





# #q5 Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)   
print(a.count(1))
print(a)
print(a.count(0))



