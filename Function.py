name = "CodePRO tutorial"

print(name.upper())
print(name.lower())

print(name.title())
print(name.capitalize())

# find() and index()

print(name.find('Co'))
print(name.index('Co'))

print(name.center(20))
print(name.ljust(20),"-")
print(name.rjust(20), "-")


my = '----MSI----'

print(my)
print(my.strip())
print(my.lstrip('-'))
print(my.strip('-'))


name = "codepro lk"

print(name.startswith("code"))
print(name.endswith('lk'))

x = "kamal, 22, colombo"

print(x.replace('22', '25'))

x = 'abc'
y = 'xyz'

print(x.join(y))

name = "nimal kamal saman"

print(name.split())