names = ['kamal', 'amal', 'nimal']

age = [34, 46, 52]

marks = [88, 66, 78]

details1 = dict(zip(names, age))
details2 = list(zip(names, age, marks))
print(details1)
print(details2)


unzip = list(zip (*details2))
print(unzip)