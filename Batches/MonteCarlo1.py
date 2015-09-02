import numpy as np
import os

def ZeroCross(filename, threshold):
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

    # Calculate frequency as (#crossings - 1 )/ (2*Total Time)
    Frequency = (ZC_Count - 1.)/(2*Total_Time)

    return Frequency

DATA_TABLE = [[],[],[],[]]

for sample in range(100):
    print (str(sample/100.0) + "%")
    for SampleSize in np.logscale(3.0,6.0,num=41)
        for SNR in np.linscale(1.0,4.0, num=9)
            FILENAME = "../Data/MonteCarloSNR" + str(SNR) + "SampleSize" + str(SampleSize) + "Sample" + str(sample) + ".txt"
            os.system("python ../FIDSim/FIDSim.py " + str(SampleSize) + " 5e4 5e-06 2.0 " + str(SNR) + " 0 " + FILENAME)
            DATA_TABLE[0].append(sample)
            DATA_TABLE[1].append(SampleSize)
            DATA_TABLE[2].append(SNR)
            DATA_TABLE[3].append(ZeroCross(FILENAME, 0.2))

Return_Data = np.transpose(DATA_TABLE)

np.savetxt("ZCMonteCarloResults.txt", Return_Data, header = "SampleNo.\t SampleSize \t SNR \t Frequency")
