import numpy as np
from helpers import visualize_array

# Input
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Filter array and replace filtered value
#result = arr[arr % 2 == 1]
arr[arr % 2 == 1] = 1337
# replace without changing original array
arr1 = np.where(arr % 2 == 1, -1, arr)

# Reshape(split) array into 2 arrays
arr2 = arr.reshape(2, -1) # Setting to -1 automatically decides the number of cols

# mean, median, std deviation
mu, med, sd = np.mean(arr), np.median(arr), np.std(arr)

# Output
print("mean = ", mu, "; median = ", med, "; deviation = ", sd)

# Visualize
visualize_array(arr1)