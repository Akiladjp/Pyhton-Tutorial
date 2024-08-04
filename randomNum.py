import random

# x = int(random.random() * 10)
# y = int(random.uniform(1, 10))
# z = random.randint(1, 10)

# print(x)
# print(y)
# print(z)

name = ['kamal', 'amal', 'nimal', 'sunil', 'saman', 'kamal']

winner = random.choices(name, k=2)

print(winner)
    