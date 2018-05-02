# import datadotworld as dw
# ds = dw.load_dataset('https://data.world/sketchcity/city-of-houston-email-metadata-january-march-2017', auto_update=True)
# print(ds)
# print(ds.describe())

import pandas as pd
import numpy as np
import json
import re

csvIn = 'coh_email_metadata_1Q17.csv'

# COLUMNS: Sender To CC BCC Sent Received

# parse CSV into pandas dataframe format
#dataframe = pd.read_csv(csvIn, header=0, names=['Sender', 'To', 'CC', 'BCC', 'Sent', 'Received'], nrows=1000)
# dataframe = pd.read_csv(csvIn, header=0, dtype={'Sender':'String', 'To': 'String', 'CC': 'String', 'BCC':'String', 'Sent':'datetime64[ns]', 'Received':'datetime64[ns]'}, nrows=1000)
# dataframe = pd.read_csv(csvIn, parse_dates=True, header=0, nrows=1000)
dataframe = pd.read_csv(csvIn, parse_dates=True, header=0)

def splitEmails(x):
    if isinstance(x, str):
        emailList = [ item[item.find('<')+1:item.find('>')] for item in x.split(';')]
        return emailList

# https://stackoverflow.com/questions/38203352/expand-pandas-dataframe-column-into-multiple-rows
# function for expanding the To, CC and BCC columns to better analyze the receipient data
def splitRecipients(df, colName):

    dataframe[colName] = dataframe[colName].apply(splitEmails)

    lens = [len(emails) if emails else 0 for emails in df[colName]]
    senderList = np.repeat(df['Sender Email'].values, lens)
    recipientList = []

    for recipientCell in df[colName].values:
        if recipientCell:
            recipientList.extend(recipientCell)

    return pd.DataFrame( {"Sender": senderList,
                            colName: recipientList})

# format columns
# dataframe['Sent'] = pd.to_datetime(dataframe['Sent'])
# dataframe['Received'] = pd.to_datetime(dataframe['Received'])
dataframe['Sender Email'] = dataframe.Sender.str.extract(r'\<(.*?)\>', expand=False)

# Clean up the sender columns
# if sender does not have email address, discard info
dataframe = dataframe[pd.notnull(dataframe['Sender Email'])]
dataframe = dataframe.apply(lambda x: x.astype(str).str.lower())

whoSendsMostEmails = dataframe['Sender Email'].value_counts()

# Extract emails
toDF = splitRecipients(dataframe, 'To')
# ccDF = splitRecipients(dataframe, 'CC')
# bccDF = splitRecipients(dataframe, 'BCC')

# print(toDF)

whoReceivesMostEmails = toDF['To'].value_counts()
whoReceivesMostEmails.to_csv('receives_emails.csv')
print(whoReceivesMostEmails)
# whoCCMostEmails = ccDF['CC'].value_counts()
# whoBCCMostEmails = bccDF['BCC'].value_counts()

toDF['Counter'] = 1
emailCount = pd.DataFrame(toDF.groupby(['Sender', 'To'])['Counter'].sum())
emailCount = emailCount.sort_values(['Counter'], ascending=False)
emailCount.to_csv('email_count.csv')
# print(emailCount)

# filter out automatic emails into separate dataframe


# find out what times are most emails sent

# a list of emails that sent the most to least amount of emails
# print(dataframe['Sender'].value_counts())

# recipients = .split(';')
# for(recipient of recipients)

# output as a json