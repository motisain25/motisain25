#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[26]:


data=pd.read_csv('diabetes.csv')
X = data.iloc[:, [2, 3]].values
y = data.iloc[:, -1].values


# In[28]:


data


# In[43]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,0] = le.fit_transform(X[:,0])


# In[44]:


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


# In[45]:


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[46]:


# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)


# In[47]:


# Predicting the Test set results
y_pred = classifier.predict(X_test)


# In[48]:


y_pred  


# In[49]:


y_test


# In[50]:


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
ac = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test, y_pred)


# In[51]:


ac


# In[41]:


cm


# In[ ]:




