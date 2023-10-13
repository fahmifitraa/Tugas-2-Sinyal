import numpy as np

def convolution(signal1, signal2):
    m = len(signal1)
    n = len(signal2)
    conv_size = m + n - 1
    result = [0] * conv_size

    for i in range(m):
        for j in range(n):
            result[i + j] += signal1[i] * signal2[j]

    return result

# Test the function
signal1 = [1, 2, 3]
signal2 = [2, 1]
conv_result = convolution(signal1, signal2)
print("Convolution result:", conv_result)

# Validate the result using numpy.convolve
np_conv_result = np.convolve(signal1, signal2)
print("Validating with NumPy:", np_conv_result)
