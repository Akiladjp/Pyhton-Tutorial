# class Phone1:
#     def feature1(self):
#         print('camera')

# class Phone2(Phone1):
#     def feature2(self):
#         print('internet')

# class Phone3(Phone2):
#     def feature3(self):
#         print('Bluetooth')

# myObj = Phone3()
# myObj.feature3()
# myObj.feature2()
# myObj.feature1()


# class Parent:
#     def func1(self):
#         print('hello')

# class Child(Parent):
#     def func2(self):
#         super().func1()
#         print('how are you')

# child1 = Child();
# child1.func2();


class Fruit:
    quantity = None
    unitPrice = None
    def set_value(self, x, y):
        self.quantity = x
        self.unitPrice = y

class Apple(Fruit):
    def func1(self):
        print('Price for Apple : ', self.quantity*self.unitPrice)
    
class Orange(Fruit):
    def func1(self):
        print('Price for Orange : ', self.quantity*self.unitPrice)

class Grapes(Fruit):
    def func1(self):
        print('Price for Grapes : ', self.quantity*self.unitPrice)


myFruit1 = Apple();
myFruit2 = Orange();
myFruit3 = Grapes();

myFruit1.set_value(12, 40);
myFruit2.set_value(8, 30);
myFruit3.set_value(40, 3);


myFruit1.func1()
myFruit2.func1()
myFruit3.func1()