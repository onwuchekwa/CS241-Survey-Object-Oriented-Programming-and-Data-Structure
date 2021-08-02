''' Import libraries '''
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

''' Add header to the file '''
'''
cols = ["AGE","WORKCLASS", "FNLWGT", "EDUCATION", "EDUCATION-NUM",
        "MARITAL-STATUS", "OCCUPATION", "RELATIONSHIP", "RACE", "SEX",
        "CAPITAL-GAIN", "CAPITAL-LOSS", "HOURS-PER-WEEK",
        "NATIVE-COUNTRY", "> 50K, <= 50K"]
'''

''' Read a .CSV file '''
''' If the csv file has no header, add "header=None" to the pandas function call '''
from_csv = pd.read_csv('census.csv', header=None)

''' display the csv file content '''
print(from_csv)
mean_value = from_csv[0].mean()
print("The mean age is {}".format(mean_value))