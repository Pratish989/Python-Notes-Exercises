s =  {4 , 6, 8, 10}
#sets can be created by curly braces. 

s1= set()
# this is how you can create empty set

s1.add(34) #adding elements to an empty set
s1.add(87)
print(s1)

s1.add(87) #adding the same values in set wont change the set
print(s1)  # printing the set- it will  show 87 only once. 

# s =  {}  this will create an empty dictionary 
# s = set()  this will create a new set 

# s1.add([87, True, "fatal"]) # you cannot add list to a set because it is unhashable 
# print(s1) # this will show error 


s1.add((89,45, True)) # you can add tuple to a set because it is hashable 
print(s1)


