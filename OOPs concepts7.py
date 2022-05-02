class vehical:
    a = 5
v1=vehical()
print(v1.a)


# single inheritance
class parentclass:
    def myfunction1(self):
        print("parent class function called")
class childclass(parentclass):
    def myfunction2(self):
        print("child class function called ")
c1=childclass()
c1.myfunction1()
c1.myfunction2()



# multilevel inheritance:
class A:
    def myfunction3(self):
        print("calling a parent class function")
class B(A):
    def myfunction4(self):
        print("calling a sub-parent class function")
class C(B):
    def myfunction5(self):
        print("calling a child class function")
C1=C()
C1.myfunction3()
C1.myfunction4()
C1.myfunction5()



# multiple inheritance:
class Q:
    def parentclass1(self):
        print("calling a classQ function")
class W:
    def parentclass2(self):
        print("calling a classW function")
class E(Q,W):
    def childclass(self):
        print("calling a classE function")
q=E()
q.parentclass1()
q.parentclass2()
q.childclass()



# hierarchical inheritance
class D:
    def myfunction6(self):
        print("parent class called")
class E(D):
    def myfunction7(self):
        print("child class E called")
class F(D):
    def myfunction8(self):
        print("child class F called")
f=F()
e=E()
e.myfunction6()
e.myfunction7()
f.myfunction6()
f.myfunction8()



# hybrid inheritance
class l:
    def lion(self):
        print("I am lion")
class p(l):
    def parrot(self):
        print("I am parrot")
class o(l):
    def owl(self):
        print("I am parrot")
class k(p,o):
    def kingfisher(self):
        print("I am kingfisher")
K=k()
K.kingfisher()
K.lion()
K.parrot()
K.owl()



# polymorphism
# method overloading
class MO:
    def overloading(self):
        print("function with no arguments")
    def overloading1(self,a):
        print("function with one argument")
    def overloading2(self,a,b):
        print("function with one arguments")
m=MO()
m.overloading1(30.20)



# method overriding
class MO1:
    def overriding(self,a):
        print("class MO1 function called")
class MO2(MO1):
    def overriding(self,a,):
        print("class MO2 function called")
class MO3(MO2):
    def overriding(self,a):
        print("class MO3 function called")

m=MO3()
m.overriding(20)

