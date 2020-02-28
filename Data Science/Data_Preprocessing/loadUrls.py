import os
import pandas as pd

url = []

with open('../../../aclImdb/train/urls_neg.txt') as f1:
    for line in f1:
        url.append(line)

urlFrame = pd.DataFrame({'url' : url }) 

print(urlFrame.head())