import pandas as pd
import numpy as np
import json
import re

import pdb

csvIn = 'humans.csv'
dataframe = pd.read_csv(csvIn, header=0)
pdb.set_trace()

dataframe['Ratio'] = dataframe['Count'] / (dataframe['Count'] + dataframe['Count'])

probablyAuto = dataframe[dataframe['Ratio'] >= 0.99]
human = dataframe[dataframe['Ratio'] < 0.99]



# the most well-connected/trustworthy people are the people who receive emails from
# a wide variety of emails, so we find the emails that appear the most in the
# 'to' column
whoReceivesMostEmails = dataframe['To'].value_counts()
#whoReceivesMostEmails = whoReceivesMostEmails[whoReceivesMostEmails > 100]

print(whoReceivesMostEmails.head())