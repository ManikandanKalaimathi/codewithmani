import numpy as np

def transpose(array, axes):
    ndim = len(axes)
    if ndim == 1:
        raise ValueError("Cannot transport a 1D array.")
    permutation = [axes.index(i) for i in range(ndim)]
    transposed_shape = tuple([array.shape[i] for i in permutation])
    transposed = np.zeros(transposed_shape, dtype=array.dtype)
    it = np.nditer(array, flages=['multi_index'])
    while not it.finished:
        idx = tuple([it.multi_index[i] for i in permutation])
        transposed[idx] = it.value
        it.iternext()
    return transposed

# Prompt the user to enter the array
array_str = input("Enter the array in the format '[1,2],[3,4]': ")
array = np.array(eval(array_str))

# Prompt the user to enter the permutations of axes 
axes_str = input("Enter the permutation of axes as a list, e.g., '[1,0]': ")
axes = eval(axes_str)

# Transpose the array
transposed = transpose(array, axes)

# Print the results
print("Input array:\n", array)
print("Transposed array:\n", transposed)  