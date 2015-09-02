import numpy as np
import random
import sys
import matplotlib.pyplot as plt

# This code is run using the following input format:
# < python FIDSim.py [Number of points] [Frequency] [Timestep] [Decay Constant (Tau)] [SNR (dB)] [Phase Offset (radians)] [Output Filename]>

# Take inputs:
NumPoints = int(sys.argv[1])
Freq = float(sys.argv[2])
Timestep = float(sys.argv[3])
Decay_Time = float(sys.argv[4])
SNR = float(sys.argv[5])
PhaseOffset = float(sys.argv[6])
OutFile = str(sys.argv[7])

# Calculate the variance from the given SNR value in order to set the width of the Gaussian noise to be added
Variance = (1.0/(2.0*SNR))

# Prepare return lists
Sim_FID_Data = []
Time = []

# For each required data point, calculate the sinusoid, add noise and calculate the time. Store these in their respective arrays
for sample in range(NumPoints):
    Sim_FID_Data.append(np.sin(2.0*np.pi*Freq*Timestep*sample + PhaseOffset) + np.random.normal(0,Variance))
    Time.append(sample*Timestep)

# Output
np.savetxt(OutFile, np.transpose(np.array([Time,Sim_FID_Data])))
