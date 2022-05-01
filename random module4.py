# two arguments in function
def myfunction(a,b):
       print("my name is: ",a)
       print("my subject name is: ",b)
myfunction("aish","maths")

def sum(a,b):
  print(a+b)
sum(22,11)

def calculation(a,b):
  print(a+b)
  print(a-b)
  print(a/b)
calculation(20,5)

def factorial(x):
      if x==1:
             return 1
      else:
             return(x*factorial(x-1))
n=int(input("n: "))
print("the factorial of" ,n,"is: ",factorial(n))



# lambda with two arguments
x=lambda a,b:a+b
print(x(10,20))



# import random
from random import randint
OTP=randint(1000,5000)
print("your OTP is: ",OTP)



# import random module
from random import choice
c=["A","B","C","D","E"]
print(choice(c))



# import random module
from random import shuffle
a=["apple","banana","cherry","mango"]
shuffle(a)
print(a)