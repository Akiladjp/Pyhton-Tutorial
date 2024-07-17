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

def perimeter(num2, num1):
    perimeter = (num2 + num1)*2
    area = num1 * num2
    return(perimeter, area)


result = perimeter(1, 3);

print(result[0]);
print(result[1]);