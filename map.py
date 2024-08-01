from functools import reduce

number = [1, 2, 3, 4, 5, 6]

y = list(map(lambda x: x* 2, number))

print(y)


sum = reduce(lambda x,y: x+y, number)

print(sum)