import numpy as np
import os
import sys

def JFFT(filename, Zero_Pad_Length):
    # Take data from file
    Data_Input = np.loadtxt(filename)
    Data_Input = np.transpose(Data_Input)

    # Calculate the length of the data, and the timestep
    n = Data_Input[1].size
    N = int(np.ceil(n*(Zero_Pad_Length+1)))
    timestep = Data_Input[0][1] - Data_Input[0][0]

    # Create an array of the square of the FFT coefficients, and the fequency bins
    FFT = [np.absolute(np.fft.rfft(Data_Input[1], n=N)), np.fft.rfftfreq(N, d=timestep)]

    # Find the maximum value of this FFT
    maximum = max(FFT[0])

    # Find the index (or indices) to which this value is associated.
    # Reminder: This requires two passes through the array, and so could be optimized by looping by hand, rather than using enumerate in this fashion.
    # Currently this seems
    max_indices = [i for i, j in enumerate(FFT[0]) if j == maximum]

    # Output
    max_freq = (np.absolute(FFT[1][max_indices[0]]))

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
    return max_freq, Interpolated_peak_freq

DATA_TABLE = [[],[],[],[],[],[]]

for sample in range(100):
    print (str(sample) + "%")
    for SampleSize in np.logspace(3.0,6.0,num=13):
        print SampleSize
        print "out of 13"
        for SNR in np.linspace(1.0,4.0, num=9):
            for Zero_Pad in [1]:
                FILENAME = "../Data/MonteCarloSNR" + str(SNR) + "SampleSize" + str(SampleSize) + "Sample" + str(sample) + ".txt"
                first_freq, second_freq = JFFT(FILENAME, Zero_Pad)
                DATA_TABLE[0].append(sample)
                DATA_TABLE[1].append(SampleSize)
                DATA_TABLE[2].append(SNR)
                DATA_TABLE[3].append(Zero_Pad)
                DATA_TABLE[4].append(first_freq)
                DATA_TABLE[5].append(second_freq)

Return_Data = np.transpose(DATA_TABLE)

np.savetxt("FFTMonteCarloResults.txt", Return_Data, header = "SampleNo.\t SampleSize \t SNR \t ZeroPaddingLength \t MaxFreq \t InterpFreq")
