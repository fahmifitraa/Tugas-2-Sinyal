import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10000  # number of sample points
T = 1.0 / 2000.0  # sample spacing
A = 1  # width of the rectangle, can adjust accordingly

# Generate the signal
x = np.linspace(-N*T/2, N*T/2, N, endpoint=False)
y = np.where(np.abs(x) < A, 1, 0)  # Rectangle function

# Compute FFT
yf = np.fft.fftshift(np.fft.fft(y))
xf = np.fft.fftshift(np.fft.fftfreq(N, T))

# Plot the Original Signal
plt.figure(figsize=(12, 6))
plt.plot(x, y)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# Plot the Magnitude of FFT
plt.figure(figsize=(12, 6))
plt.plot(xf, 2/N * np.abs(yf))
plt.title('Magnitude of FFT')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()
