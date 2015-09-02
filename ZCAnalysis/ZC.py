from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys

# Analysis code that takes an input .csv, .txt, or .dat file in the format (using "#" as a comment character):
# #Time  Voltage
# 0.0   0.012
# 0.1   0.232
#  .     .
#  .     .
#  .     .
#
# Function is called using:
# < python ZC.py [Filename] [Threshold]>
# where Filename is the name of the input file, e.g. "DataFile001.txt"
#       Threshold is hysteresis level the state machine uses to filter out small deviations, c.f. Schmidt Filters

# Take input data and type it
filename = str(sys.argv[1])
thresh = float(sys.argv[2])

# Set up a state boolean such that True corresponds to the voltage being positive, and False corresponds to the voltage being negative
Data_State = True

# Load the data file
Data_Input = np.loadtxt(filename)
Data_Input = np.transpose(Data_Input)
# Crossing count initialization
if (Data_Input[1][0] <= 0):
    Data_State = False

#Initialise variables to store the total number of crossings (ZC_Count) and a list to store the indices of the crossings
ZC_Count = 0
Crossings = []

# Iterate through the data set, updating the zero crossing count and state machine each time we pass the threshold
for index, datum in enumerate(Data_Input[1]):
    if Data_State == True and datum <= -thresh:
        Data_State = False
        ZC_Count += 1
        Crossings.append(index)
    if Data_State == False and datum >= thresh:
        Data_State = True
        ZC_Count += 1
        Crossings.append(index)

# Find the total time from the first crossing to the last crossing as stored in Crossings
Total_Time = Data_Input[ 0 ][ Crossings[-1] ] - Data_Input[ 0 ][ Crossings[0] ]

# Calculate frequency as ()#crossings - 1 )/ (2*Total Time)
Frequency = (ZC_Count - 1.)/(2*Total_Time)

print Frequency
