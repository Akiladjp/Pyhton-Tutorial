from array import  *

x = array('i', [1, 2, 3, 4])

x.append(6)
x.extend([5, 6, 7])
x.insert(0,11)
x.pop(2)
x.remove(1)



arr = array('i', [2,5,4,1,6])

for a in arr:
    print(a)

# for a in range(3):
#     print(arr[a])