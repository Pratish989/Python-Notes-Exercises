# q1 Write a program to print the multiplication table of a given number using for loop.
# i = 1
# x = int(input("enter your no."))
# for i in range(10): 
#     i = i + 1
#     print(x * i)

# q2 Write a program to greet all the person names stored in a list l1 and which starts with S.

# l1 = ["shalini", "raghav", "pratish", "shailesh", "kushangi"]
# for items in l1:
#     print("hello " + items)

# x = items.startswith("s")
# # for x in l1:
# #     print("hello " + )

# if x == True:
    # print("hello " + x)


# q3 Attempt question 1 using a while loop
# i = 1
# x = int(input("enter your no."))
# while i in range(10):
#     i = i + 1
#     print(x * i)

# q4 Write a program to find whether a given number is prime or not.
# x =  int (input("enter the number"))
# if x%2 == 0:
#     print("it is not a prime number")
# elif x%3 == 0:
#     print("this is not prime number")
# else:
#     print("it is a prime number")

# q5 Write a program to find the sum of first n natural numbers using a while loop.
i = 1
while i < 10:
    print(str(i))
    x = (i+1)/2
    i = (i * x)
