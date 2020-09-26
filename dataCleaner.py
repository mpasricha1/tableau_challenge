import pandas as pd
import os 

filePath = os.getcwd()
dataFiles = os.listdir(filePath)

fileList = [ext for ext in dataFiles if ext[-3:] == 'csv']

bike_df = pd.DataFrame()
for file in fileList: 
	data = pd.read_csv(file)
	bike_df = bike_df.append(data)

bike_df.to_csv("bikeJC.csv")