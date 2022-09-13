def func1(n):
    m=[]
    l=len(n)
    for i in n:
        if i not in m:
            m.append(i) 
    print("Without set:",m)
def func2(n):
    print(set(n))
n=int(input("Enter length of list:"))
list=[]
for i in range(n):
    el=int(input("Enter the elements:"))
    list.append(el)
func1(list)
func2(list)
print ("20DCE006")


