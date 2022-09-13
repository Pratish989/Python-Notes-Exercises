mydict = {
    "key" : "values", 
    "numbers" : [5,34,23],
    "anotherdict" :{"pratish" : "good boy"} ,
    1 : 6
}

print((mydict.keys())) #this will give datatype name and keys
print (list(mydict.keys())) #this will give only the list of the dictionary

print(mydict.values()) 
# for updating dictionary, first you have to make a new dictioanry wiht new name. then 
# write the contents of that dictionary #IMPNOTE
mydictnew = {
    "sam harris" : "philosopher"

}
#for updating the syntax is --> maindictionary.update(newdictionary) #IMPNOTE

mydict.update(mydictnew)
print(mydictnew.values())
print(mydict)#this is the new updated dictionary

print(mydict.get("numbers"))
#now you might ask that the above line can also be executed with the below line
print(mydict['numbers'] )
# but now if we change the key names of dictionary while print execution, we will get error. 
#because when we print like this #print(mydict['numbers']) we will get the values of that keys. and#
# if we change the ket value name to lets say numbers2 it will show error but in get method (the first method)
# we will get None as an output 

print(mydict.get("numbers2")) #check the output
# print(mydict['numbers2'] )


