import os
import pandas as pd

dataset = pd.DataFrame()
directory = os.fsencode('../../../aclImdb/train/neg/')

for fileName in os.listdir(directory):
    with open('../../../aclImdb/train/neg/'+str(fileName)[2:-1]) as f:
        review = f.read()
    dataset = pd.concat([dataset,pd.DataFrame(data={'filename': [str(fileName)[2:-1]], 'review' : [review], 'id' : [int(str(fileName)[2:-7])]})])
    f.close()

dataset.sort_values(by=['id'], inplace=True)
dataset = dataset.reset_index()
print(dataset.head())


url = []

with open('../../../aclImdb/train/urls_neg.txt') as f1:
    for line in f1:
        url.append(line)

urlFrame = pd.DataFrame({'url' : url }) 
print(urlFrame.head())

#pd.merge(dataset,urlFrame,on='')
finalDataSet = pd.concat([dataset, urlFrame], axis=1)
finalDataSet['movieName'] = finalDataSet['url'].str[26:35]
finalDataSet['isNeg'] = 1
print(finalDataSet)

#----------------------------------------------------------------------------------------------------------------------------------------------------

datasetPos = pd.DataFrame()
directoryPos = os.fsencode('../../../aclImdb/train/pos/')

for fileNamePos in os.listdir(directoryPos):
    with open('../../../aclImdb/train/pos/'+str(fileNamePos)[2:-1]) as f:
        review = f.read()
    datasetPos = pd.concat([datasetPos,pd.DataFrame(data={'filename': [str(fileNamePos)[2:-1]], 'review' : [review], 'id' : [int(str(fileNamePos)[2:str(fileNamePos).index('_')])]})])
    f.close()

datasetPos.sort_values(by=['id'], inplace=True)
datasetPos = datasetPos.reset_index()
print(datasetPos.head())


urlPos = []

with open('../../../aclImdb/train/urls_pos.txt') as f1:
    for line in f1:
        urlPos.append(line)

urlFramePos = pd.DataFrame({'url' : urlPos }) 
print(urlFramePos.head())

#pd.merge(dataset,urlFrame,on='')
finalDataSetPos = pd.concat([datasetPos, urlFramePos], axis=1)
finalDataSetPos['movieName'] = finalDataSetPos['url'].str[26:35]
finalDataSetPos['isNeg'] = 0
print(finalDataSetPos)

#---------------------------------------------------------------------------------------------------------------------------------------------------

trainingDataset = finalDataSet.append(finalDataSetPos)
print(trainingDataset)

if os.path.exists('../Data/Training_Data/Train.csv'):
    os.remove('../Data/Training_Data/Train.csv')
else:
    trainingDataset.to_csv(r'../Data/Training_Data/Train.csv')
    print('data written to file in ../Data/Training_Data/Train.csv')