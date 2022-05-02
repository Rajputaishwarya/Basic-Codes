# exception handling
try:
   a=int(input("integer input A: "))
   b=int(input("integer input B: "))
   c=a/b
   print("your input is: ",c)
except exception as d:
   print("exception caught: ",d)
print("bye")

try:
    z="hello"
    print(z)
except a:
    print("type error: ",a)
print("bye")

try:
   x=int(input("enter your input A: "))
   y=int(input("enter your input B: "))
   z=x+y
   print(z)
except:
   print("something went wrong")
finally:
   print("finally block")

try:
    a1=int(input("put your input: "))
    a2=int(input("put your input: "))
    a3=a1+a2
    print(a3)
except:
    print("something went wrong")
else:
    print("nothing went wrong")

try:
    print(f)
except:
    print("veriable is not define")
finally:
    print("finally block")
