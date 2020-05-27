
#Name: Tausif Khan
#Rollno: 12
#Branch: SE/COMPS 
#Subject - OSTL 
#Div: B


'''
A Python program to demonstrate multiple inheritance and display the order of execution of methods in several base classes according to MRO.

'''

class A:
    def init_(self):
        self.a='a'
        print(self.a)
        super()._init_(self)
class B:
    def init_(self):
        self.b='b'
        print(self.b)
        super()._init_(self)
class C:
    def init_(self):
        self.c='c'
        print(self.c)
        super()._init_(self)
class X(A,B):
    def method(self):
         print(" X class method")
         super().method()
class Y(B,C):
    def method(self):
         print(" Y class method")
         super().method()
class P(X,Y,C):
    def method(self):
          print(" P class method")
          super().method()
print(P.mro())
'''
Output:-

[<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

'''
