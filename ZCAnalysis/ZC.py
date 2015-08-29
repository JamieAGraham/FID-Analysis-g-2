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
numpy.loadtxt(filename)

# Crossing count initialization
