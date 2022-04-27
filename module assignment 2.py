# find even or odd number from user input
c=int(input("user input: "))
if c%2==0:
    print("your input is even number")
else:
    print("your input is odd number")


# find greather than or less than user input
a=int(input('user input A: '))
b=int(input('user input B: '))
if a>b:
    print('A is greater than B')
else:
    print('B is greater than A')


# find gread of user percentage
p=int(input('Enter your percentage: '))
if p>70:
    print('A')
elif p>70 and p<65:
    print('B+')
elif p>65 and p<65:
    print('B')
elif p<50 and p>60:
    print('c')
else:
    print('Fail')


# generate for loop from 1 to 10
for i in range(10):
    print(i)


# generate for loop from 10 to 1
for j in range(10,0,-1):
    print(j)


# generate nested for loop
for i in range(0,6,1):
    for j in range(i):
        print("*",end=" ")
    print(i)


# generate nested for loop
for a in range(0,5,):
    for b in range(a+1):
        print(b+1,end="")
    print(a)


# convert string in uppercase
x="hello python"
y=x.capitalize()
print(y)


# convert string in lowercase
v="HELLO PYTHON"
n=v.casefold()
print(n)



