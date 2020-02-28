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
print(dataset.head())


url = []

with open('../../../aclImdb/train/urls_neg.txt') as f1:
    for line in f1:
        url.append(line)

urlFrame = pd.DataFrame({'url' : url }) 
print(urlFrame.head())

finalDataSet = pd.concat([dataset, urlFrame], axis=1)
print(finalDataSet)

    #print(str(fileName)[2:-1])
    #f = open('../../../aclImdb/train/neg/'+str(fileName)[2:-1], 'r')
    #print(f.read())
    #f.close