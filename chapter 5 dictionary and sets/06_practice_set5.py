#q1 Write a program to create a dictionary of Hindi words with values as their English translation.
# Provide the user with an option to look it up


# hindi =  {
# "nahana" : "bathing ",
# "paadna" : "farting",
# "khodna" : "dumping"
# }

# print("enter the word for the translation"  )

# print(hindi["khodna"])
# print(hindi.get(("nahana"))) 

# a =input("enter the name \n") # here we took input from user
# print("the meaning of your word is  " + hindi[a]) # idhar a input hai, woh hindi decitionary ke koi bhi input me se hoga
# print("the meaning of your word is  " + hindi.get(a)) #this wont show any error instead if we will enter any 
# key which is not present in dictionary, it will show None


#q2 Write a program to input eight numbers from the user and display all the unique numbers (once)
# (jab bhi 'unique'word aaye tab set ka use hoga (mostly))


# set = set()

# a = input("enter no")
# b = input("enter no")
# c = input("enter no")
# d = input("enter no")
# e = input("enter no")
# f = input("enter no")
# g = input("enter no")
# h = input("enter no")
# default is string,so we have to convert ito int. so we'll use typecasting
# a = int(input())
# set.add(a)

# b = int(input())
# set.add(b)

# c = int(input())
# set.add(c)

# d = int(input())
# set.add(d)

# e = int(input())
# set.add(e)

# f = int(input())
# set.add(f)

# g = int(input())
# set.add(g)

# h = int(input())
# set.add(h)

# print(set)

# q3 Can we have a set with 18(int) and “18”(str) as a value in it?

# set1 = (18,"18")
# print(set1)

# q4 What will be the length of the following set S:

# S = set()

# S.add(20)

# S.add(20.0) 

# S.add("20")

# print(S)
# print(len(S))
# 20 and 20.0 will be count as one only. 


# q5 Create an empty dictionary. Allow 4 friends to enter their favorite language as values 
# and use keys as their names. Assume that the names are unique


# dict = {}

# a = input()
# b = input()
# c  = input()
# d  = input()
# e = input()
# f = input()
# g = input()
# h = input()

# dict.update({a : b})
# dict.update({c : d})
# dict.update({e : f})
# dict.update({g : h})

# print(dict)

# q6 If the names of 2 friends are the same; what will happen to the program in Program 6?

# dict = {}

# a = input()
# b = input()
# c  = input()
# d  = input()
# e = input()
# f = input()
# g = input()
# h = input()

# dict.update({a : b})
# dict.update({c : d})
# dict.update({e : f})
# dict.update({g : h})

# print(dict)

# answer - only the last oneexecuted will be shown in the output 


# q7 If the languages of two friends are the same; what will happen to the program in Program 6?

dict = {}

a = input()
b = input()
c  = input()
d  = input()
e = input()
f = input()
g = input()
h = input()

dict.update({a : b})
dict.update({c : d})
dict.update({e : f})
dict.update({g : h})

print(dict)

# answer - now the values are same, but still it is shown in the output with diff keys and same values

# IMPNOTE - keys unique honi chaiye, values chalega








