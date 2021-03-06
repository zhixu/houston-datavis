import pandas as pd
import numpy as np
import json
import re

import pdb
"""
csvIn = 'email_count.csv'
dataframe = pd.read_csv(csvIn, parse_dates=True, header=0)

mask = (dataframe['Sender'] + dataframe['To']).isin(dataframe['To'] + dataframe['Sender'])

autoGenerated = dataframe[~mask]
autoGenerated = autoGenerated.groupby(['Sender']).count()
autoGenerated = autoGenerated.sort_values(['Counter'], ascending=False)
autoGenerated.to_csv('no_replies.csv')

print("finished autoGenerated")

humanDF = dataframe[mask]
humanDF = humanDF[humanDF['Sender'] != humanDF['To']]
humanDF['Counter2'] = 0

print("right before iterating")
humanDF.to_csv('humanDF.csv')
"""
"""
csvIn = 'humanDF.csv'
humanDF = pd.read_csv(csvIn, parse_dates=True, header=0)
print(humanDF.info())
atob = humanDF['Sender'] + humanDF['To']
test1 = pd.DataFrame({'Email Key': atob,
                    'Sender': humanDF['Sender'],
                    'To': humanDF['To'],
                    'Count': humanDF['Counter']})

btoa = humanDF['To'] + humanDF['Sender']
test2 = pd.DataFrame({'Email Key': btoa,
                    'Count': humanDF['Counter']})

test1 = test1.sort_values('Email Key')
test2 = test2.sort_values('Email Key')
test1.to_csv("test1.csv")
test2.to_csv("test2.csv")

count2 = test2['Count'].tolist()
test1['Count2'] = count2
"""


# following http://www.austintaylor.io/d3/python/pandas/2016/02/01/create-d3-chart-python-force-directed/
# test1.to_csv('humans.csv')
csvIn = 'humans.csv'
test1 = pd.read_csv(csvIn, parse_dates=True, header=0)
test1 = test1[(test1['Sender'].notnull() & test1['To'].notnull())]

print(test1.info())

groupedList = test1.groupby(['Sender', 'To']).size().reset_index()
groupOfEmails = groupedList['Sender'].append(groupedList['To'])
uniqueEmails = pd.Index((groupOfEmails.reset_index(drop=True)).unique())

tempLinksList = list(test1.apply(lambda row: {"source": row['Sender'], "target": row['To'], "value": row['Count']}, axis=1))
linksList = []
for link in tempLinksList:
    record = {"value":link['value'], "source":uniqueEmails.get_loc(link['source']),
    "target": uniqueEmails.get_loc(link['target'])}
    linksList.append(record)



# uniqueEmails = pd.Index(groupedList['Sender']
#                         .append(groupedList['To']
#                         .reset_index(drop=True).unique()))


nodesList = []
counter = 0
domainDict = {}
for email in uniqueEmails:
    domain = (email.split('@'))[-1]
    group = 0
    if domain in domainDict:
        group = domainDict[domain]
    else:
        counter += 1
        domainDict[domain] = counter
        group = counter
    nodesList.append({"email": email, "group": group})

jsonList = {"nodes": nodesList, "links": linksList}
jsonOut = open('houstondata.json', 'w')
jsonOut.write(json.dumps(jsonList))
jsonOut.close()


# for index, row in humanDF.iterrows():

#     if (index % 5000 == 0): print(index)
#     # key = (row['Sender'], row['To'])
#     # value = row['Count']

#     sender = row['Sender']
#     receiver = row['To']
#     # pdb.set_trace()

#     flippedRow = humanDF[(humanDF['Sender'] == receiver) & (humanDF['To'] == sender)]

#     if (len(flippedRow) == 1):

#         value = flippedRow.loc[flippedRow.index,'Counter'].values[0]
#         # pdb.set_trace()
#         humanDF.set_value(index, 'Counter2', value)
#         # pdb.set_trace()
#         # print(index)
#         # print(flippedRow)

#         humanDF.drop(index=flippedRow.index, inplace=True)

#         # print(humanDF)
#         # pdb.set_trace()

#     # if (index == flippedIndex): 
#     #     humanDF.drop(index=index)
#     # elif(len(flippedIndex) > 0):
#     #     pdb.set_trace()
#     #     row['Counter2'] = humanDF['Counter'][flippedIndex]
#     #     humanDF.drop(index=flippedIndex)

# print("==============")
# humanDF.to_csv('humans.csv')
# print(humanDF.info())
    # dataframe.drop(, axis=0)

# print(test)
# dataframe = dataframe.apply(condense, axis=1)