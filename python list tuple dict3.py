# alternate element from given list
l=[1,2,3,4,5,6]
alt=[l[i]for i in range(len(l))if i%2 !=0]
print(alt)

# remove element from given list
l1=[1,2,3,4,5,6]
l1.remove(3)
print(l1)

# insert element in given list
l2=["java","php","net","angular"]
l2.insert(2,"python")
print(l2)

# add element in list using for loop
l3=[1,2,3,4,5,6]
for n in range(0,len(l3)):
 l3.append(7)
 print(l3)

# slicing with given tuple
t=("python",1,2,3,"java","A","B")
# alternate value
l4=list((t))
print(l4)
alt=[l4[i]for i in range(len(l4))if i%2 !=0]
print(alt)
t1=tuple(alt)
print(t1)
# last value of tuple
print("last value: ",t[-1])
# value between index 1 to 5
print("value between 1 to 5: ",t[1:5])

# convert tuple into list
t2=(1,2,3,4,5,6,7,8)
y=list((t2))
print(y)

# convert two given list into dictionary
t3=(9,0)
L=list(t3)
print(L)
y.extend(L)
print(y)
c=tuple((y))
D={1:[c]}
print(D)

# point keys from given dict
d={1:"apple",2:"banana",3:"mango"}
a=d.keys()
print(a)

# point values from given dict
b=d.values()
print(b)
