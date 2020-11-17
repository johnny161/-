import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import re
import pickle

user_title = ['UserID','Age','Gender','Job','Zip-code']
users = pd.read_table('./userInfo.csv', sep=',', header=None, names=user_title, engine='python')
users = users.filter(regex='UserID|Gender|Age|Job')
print(users)
age2int = {val: ii for ii, val in enumerate(set(users['Age']))}
print(len(age2int))