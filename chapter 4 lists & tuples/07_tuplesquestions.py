# q1 Unpack the tuple into 4 variables
t1 = (56, 36 , "tuples", False)
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])

# q2 Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)

(tuple1,tuple2) = (tuple2,tuple1)

print(tuple1)
print(tuple2)

#q3 Copy specific elements from one tuple to a new tuple
tuple3 = (11, 22, 33, 44, 55, 66)
tuple4 = tuple3 [3 : -1]
print (tuple4)

# q4 Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
tuple5 = (11, [22, 33], 44, 55)
tuple5 [1] [0] = 222
print(tuple5)


# CONCEPT - LIST KE ANDAR WALI LIST ME CHANGES KRNE KE LIYE
# STEP1 -  INDEXINIG STEP2 = ASSIGNMENT OPERATOR SE VALUE ASSIGN KARDENE KI 

# q5 Sort a tuple of tuples by 2nd item
tuple6 = (('a', 23),('b', 37),('c', 11), ('d',29))
(tuple6[0],tuple6[2]) = (tuple6[2],tuple6[0])
print(tuple6)

# ye concept thoda advanced hai baadme karna 


# q6 Check if all items in the tuple are the same

tuple7 = (45, 45, 45, 45)

# yw wala concpet bhi baadme aayega 