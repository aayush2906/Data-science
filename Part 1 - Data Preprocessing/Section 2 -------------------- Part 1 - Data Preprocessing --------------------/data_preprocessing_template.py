# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 08:06:08 2019

@author: aayus
"""
#importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#importing Datasets

dataset = pd.read_csv("Data.csv")
X= dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values
y

#taking care of missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values= "NaN",strategy="mean",axis=0)
imputer.fit(X[:, 1:3]) 
X[:,1:3] =imputer.transform(X[:,1:3])

#Encoding Categorical data 

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()
labelencoder_y=LabelEncoder()
y=labelencoder_X.fit_transform(y)

#Splitting the dataset into the training set and test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2,random_state=0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)
