# match function
import re
patter=r"^abcd"
mystring="abcdef"
x=re.match(patter,mystring)
print(x)


# search function
import re
text="We are learning python"
x=re.search("\s",text)
print("The first whitespace: ",x.start())


# Replace Function
import re
str="I am happy"
result=re.sub(r"happy","sharpshooter",str)
print("After replace: ",result)


# Replace function
import re
pattern="Goa Is Smart City"
Result=re.sub(r"[a-z]","0",pattern)
print(Result)


import re
pattern="1234"
mylist="12345678"
x=re.match(pattern,mylist)
print(x)

import re
myself="my name is aishwarya"
y=re.search("aishwarya",myself)
print(y)
v=re.search("careless",myself)
print(v)

import re
a="i am learning python language"
q=re.sub(r"language","code",a)
print(q)

import re
j="1233l44a55u6678h89976h5"
p=re.sub(r"[0-9]","A",j)
print(p)

import re
g=re.split('\W+','Hello,hello,hello')
print(g)