# price = lambda x,y : x * y

# print(price(2,30)); 


# def apple(unitPrice, quantity):
#     total = (lambda: unitPrice * quantity)()
#     return total;

# print(apple(2, 20))
    

def apple(unit_price):
    return(lambda number_of_apples : number_of_apples * unit_price)

x = apple(20)
print(x(2))