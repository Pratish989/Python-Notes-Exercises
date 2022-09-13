#dictionary is created with curly braces with equal to sign.
# it has  keys and values
# keys ko : <-- iss sign se assign karte hai 
mydict = {
    "key" : "values", 
    "numbers" : [5,34,23],
    "anotherdict" :{"pratish" : "good boy"} # here we have created another dictionary in a dictionary
}



#printing syntax = print(variable['keys']) ---> this will print the values of that specific keys
print(mydict['key'])
print(mydict['numbers'])
#now as we know dictionary are mutable. so now we will change this dictionary keys.
mydict['numbers'] = [78,46,36] #now it has changed to what we have entered first
print(mydict['numbers'])

print(mydict['anotherdict'])
#we have also created a dictionary within a dictionary. and now if we want to 
#print specific value of the key of that dictionary, the method used is this.

print(mydict['anotherdict']['pratish'])
