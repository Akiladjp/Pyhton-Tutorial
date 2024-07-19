# def functionName(arg1):
#     print(arg1)


# functionName('HELLO')

# print('----------------')

# def sum(num1, num2):
#     print(num1 + num2)


# sum(2 , 5)

# print('---------------')

# def sub(num2, num1):
#     return(num1 - num2)

# answer = sub(3, 8)
# print(answer)

# print('-----------------')

# def perimeter(num2, num1):
#     perimeter = (num2 + num1)*2
#     area = num1 * num2
#     return(perimeter, area)


# result = perimeter(1, 3);

# print(result[0]);
# print(result[1]);


def student(name, age, grade):
    print(f'Student name is {name} and {age} years old');
    print(f'{grade} class');

student('kamal', 15, 10)

print('--------------------------')

# def total_marks(mark1= 0, mark2 = 0, mark3 = 0):
#     total = mark1 + mark2 + mark3;
#     return(total)

# print(total_marks(55,44))


def total_marks(*marks):
    total = 0;
    average = 0;
    for mark in marks:
        total = total + mark
    print(total)
    average = total / len(marks)
    print(average)

total_marks(56, 56, 56)


print('--------------------')

def keyword(**kwarg):
    for sub, mark in kwarg.items():
        print(sub, mark)


keyword(maths=87, english=55, science=33)



