# FID-Analysis-g-2
Analysis code for use on a Free Induction Decay signal from an NMR magnetometer

This repository contains the main code used in producing plots for an internal note for the g-2 collaboration. There are 3 files:

###############################################################################
FIDSim.py:
###############################################################################

This is a simulated decaying sinusoid (FID signal) with Gaussian noise added. The parameters required on running are as follows.

< python FIDSim.py [Number of points] [Frequency] [Timestep] [Decay Constant (Tau)] [SNR (dB)] [Phase Offset (radians)] [Output Filename] >

Number of points: The required number of samples

Frequency: The frequency of the returned sinusoid, in Hz

Timestep: The time elapsed between samples, in Seconds.

Decay Constant: The decay constant, or mean lifetime, tau. This is the denominator in the exponential decay, exp^(-t / tau). Measured in Seconds.

SNR: This is the required signal-to-noise ratio of the Gaussian applied to the signal. This SNR specifically refers to the maximum input amplitude, automatically set to 1. Measured in dB.

Phase Offset: This allows all values of phase offsets to be introduced to the starting value, in Radians.

Output Filename: This is the path of the output file relative to the directory the program is run from. e.g. "../Data/Sim001.txt"

An example of running this code from the terminal would be:

~$ python FIDSim.py 1e6 5e4 1e-5 1.0 2.0 0.0 ../Data/SimData001.txt

###############################################################################
ZC.py
###############################################################################

This analysis code applied a zero crossing counting method to find the frequency from the FID data. It is run from the terminal with the command:

< python ZC.py [Filename] [Threshold] >

Filename: The input file for which the frequency will be calculated. e.g. ../Data/SimData001.txt

Threshold: The level of the hysteresis threshold. The higher this value is set, the more robust the algorithm will be to noise. However due to the decay period, it is also possible that if the amplitude of the signal decreases below your given threshold value, you could lose the use of a longer data set from this fact. There will be no issues with the frequency being calculated as too long due to this, as the time period from the first to last zero crossing is measured.


###############################################################################
FFT.py
###############################################################################

This presents another method of frequency extraction, that through finding the peak of the discrete Fourier Transform of the data. This can be run with the terminal command:

< python FFT.py [Filename] [Zero Padding Multiple] >

Filename: The input file for which the frequency will be calculated. e.g. ../Data/SimData001.txt

Zero Padding Multiple: Given a data set of length N, and a Zero Padding Multiple Z, the final data will have (Z+1)* N points of data.

The code finds both the maximum of the FFT, and the quadratic peak estimation. Currently the default output returns the quadratically interpolated peak. This method does have bias when the true peak is not in a half bin. Zero padding interpolation is ideal, but can lead to severely increased execution times. By allowing zero padding and then using QPE, this should allow the user to find a suitable middle ground of execution time and accuracy.
