# class myClass:
#     x = 18
#     __y = 20;
#     def disp(self):
#         return self.__y + self.x

# myObj = myClass();
# print(myObj.disp());


class myClass:
    def meth1(self):
        print('hello')
        self.__meth2()

    def __meth2(self):
        print('welcome')


myObj = myClass();
print(myObj.meth1());


