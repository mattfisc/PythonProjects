import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

for x in np.nditer(arr[1::2]):
    print(x)
