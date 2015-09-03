from __future__ import division
import numpy as np
import scipy as sci
import sys

# Python implementation of the FFT quadratic peak interpolation method. This code can be run with the following format:
# <python FFT.py [filename.txt] [Zero Padding Multiple]>
# The format of the text file is identical to that of the ZC code, see ZC.py or readme.md for reference.

# Take command line data
filename = str(sys.argv[1])
Zero_Pad_Length = float(sys.argv[2])

# Take data from file
Data_Input = np.loadtxt(filename)
Data_Input = np.transpose(Data_Input)

# Calculate the length of the data, and the timestep
n = Data_Input[1].size
timestep = Data_Input[0][1] - Data_Input[0][0]

# Create an array of the square of the FFT coefficients, and the fequency bins
FFT = [np.absolute(np.fft.rfft(Data_Input[1])), np.fft.rfftfreq(n, d=timestep)]

# Find the maximum value of this FFT
maximum = max(FFT[0])

# Find the index (or indices) to which this value is associated.
# Reminder: This requires two passes through the array, and so could be optimized by looping by hand, rather than using enumerate in this fashion.
# Currently this seems
max_indices = [i for i, j in enumerate(FFT[0]) if j == maximum]

# Output
print(np.absolute(FFT[1][max_indices[0]]))

# Calculating the interpolated peak frequency through quadratic peak interpolation, where alpha beta and gamma are the points around the theoretical maximum.

sample_frequency = 1./timestep
alpha = FFT[0][max_indices[0]-1]
beta = FFT[0][max_indices[0]]
gamma = FFT[0][max_indices[0]+1]

# See associated paper for full explanation of equation, or go to http://www.dsprelated.com/freebooks/sasp/Quadratic_Interpolation_Spectral_Peaks.html for a fantastic treatment of the subject
fractional_peak_location = 0.5*(alpha-gamma)/(alpha - 2*beta + gamma)

# Calculating the frequency by converting between bin number and frequency
Interpolated_peak_freq = FFT[1][max_indices[0]] + fractional_peak_location*sample_frequency/n

# Output:
print Interpolated_peak_freq
