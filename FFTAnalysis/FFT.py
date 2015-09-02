from __future__ import division
import numpy as np
import scipy as sci
import sys

# Take command line data
filename = str(sys.argv[1])

# Take data from file
Data_Input = np.loadtxt(filename)
Data_Input = np.transpose(Data_Input)

# Calculate the length of the data, and the timestep
n = Data_Input[1].size
timestep = Data_Input[0][1] - Data_Input[0][0]

# Create an array of the square of the FFT coefficients, and the fequency bins
FFT = [np.absolute(np.fft.fft(Data_Input[1])), np.fft.fftfreq(n, d=timestep)]

# Find the maximum value of this FFT
maximum = max(FFT[0])

# Find the index (or indices) to which this value is associated.
# Reminder: This requires two passes through the array, and so could be optimized by looping by hand, rather than using enumerate in this fashion.
max_indices = [i for i, j in enumerate(FFT[0]) if j == maximum]

# Output
print(np.absolute(FFT[1][max_indices[0]]))
