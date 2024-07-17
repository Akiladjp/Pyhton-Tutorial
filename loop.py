# while loop

i = 0;
while(i < 6):
    print(i)
    i += 1;

sum = 0

i = 0;
while(i<6):
    number = int(input('Enter a number'))
    sum = sum + number
    print(number)
    i = i + 1
print('Answer is : ', sum)


# for loop

sum = 0;

x = [1, 2, 3, 4, 5]
for num in x:
    sum = sum + num
print(sum)


x = {'name' : 'kamal',
     'age' : 40,
     'gender' : 'male'}

for i,j in x.items():
    print(i, ':', j)


