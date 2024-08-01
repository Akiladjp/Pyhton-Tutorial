#overridding


class Parent:
    def func(self):
        print('hello')
    

class Child(Parent):
    def func(self):
        print('welcome')
        
MyObj2 = Parent()
print(MyObj2.func());

MyObj = Child()
print(MyObj.func());




#overloading


class Calc:
    def add(self, a=None, b=None, c=None):
        sum = 0
        
        if a!=None and b!=None and c!=None:
            sum = a+b+c
            print(sum)
        elif a!=None and b!=None:
            sum = a+b
            print(sum)
        else:
            sum = a
            print(sum)
    
MyObj = Calc()
MyObj.add(2, 7)
            