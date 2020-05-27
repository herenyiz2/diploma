# Elvégezzük a szükséges importálásokat
import numpy as np
import pandas as pd
import os, sys
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Egy adatframe-ba olvassa az adatokat és megkapja az elő 5 rekordot

#Beolvassa az adatokat
df=pd.read_csv('C:\Users\Ildikó\Desktop\parkinson\parkinsons.data')
df.head()

#DataFlair - szolgáltatások éa címkék beszerzése
features=df.loc[:,df.columns!='status'].values[:,1:]
labels=df.loc[:,'status'].values

#DataFlair - - az egyes címkék (0 és 1) számát szerezheti meg a címkékben
print(labels[labels==1].shape[0], labels[labels==0].shape[0])

#DataFlair - Skálázza a funkciókat -1 és 1 közé
scaler=MinMaxScaler((-1,1))
x=scaler.fit_transform(features)
y=labels

#DataFlair - Felosztja az adatkészletet
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=7)

#DataFlair - Modellképzés
model=XGBClassifier()
model.fit(x_train,y_train)

# DataFlair - kiszámolja a pontosságot
y_pred=model.predict(x_test)
print(accuracy_score(y_test, y_pred)*100)



