# import numpy as np
# from sklearn.model_selection import train_test_split

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# y = np.array([0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1])

# x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True)

# print("x_train:", x_train)
# print("Length of x_train:", len(x_train))
# print("Length of x_train:", len(x_test))



import matplotlib.pyplot as plt
import numpy as np

age = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
job = np.array([0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1])

plt.scatter(age, job)
plt.xlabel('Age')
plt.ylabel('Job')
plt.show()

m, c = np.polyfit(age, job, 1)

plt.scatter(age, job, label='Data points')
plt.plot(age, m*age + c, color='red', label='Fitted line')
plt.xlabel('Age')
plt.ylabel('Job')
plt.legend()
plt.show()

