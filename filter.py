number = [1, 2, 3, 4, 5, 6, 7, 8]

# def even():
    
#     even_number = []
    
#     for a in number:
#         if(a%2 == 0):
#             even_number.append(a);
#     return even_number;

# print(even());


def even_number(x):
    return x % 2 == 0;

y = list(filter(even_number, number))
print(y)