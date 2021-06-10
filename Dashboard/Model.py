
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import pickle
from dateutil.parser import parse

# live model training
df= pd.read_csv('Malyria.csv',encoding = 'latin')

#Droping columns that does not seem practical to ask to a paitints.
df.drop(labels=['MRNO','CPT_ID_Result_Value','CPT_ID'],axis=1,inplace=True)
df['Day']= df['Report_verified'].str.split('/').str[0]
df['Month']= df['Report_verified'].str.split('/').str[1]
df['Year']= df['Report_verified'].str.split('/').str[2]
#df = df[~df['Year'].isnull()]
#df['Year'] = df['Year'].str.replace(r'\D', '').astype('int64')
df['Year'] = df['Year'].str[:4]
df['age'] = df['Age'].str.split().str[0]
df = df[~df['Day'].isnull()]
df['Result_txt'].replace({'Negative': 0, 'Positive': 1},inplace = True)
df['Result'].replace({'N': 0, 'Y': 1},inplace = True)
df['Gender'].replace({'Female': 0, 'Male': 1, 'Neuter':2 },inplace = True)



#Converting the datatype o newly created features
df['Day'] = df['Day'].astype(int)
df['Month'] = df['Month'].astype(int)
df['Year'] = df['Year'].astype(int)
df['Result_txt'] = df['Result_txt'].astype(int)
df['Result'] = df['Result'].astype(int)
df['Gender'] = df['Gender'].astype(int)


#Now droping the parent features since we don't need them
df.drop(['Report_verified','Age','Unnamed: 1'],axis=1,inplace=True)

#Label encoding executed manually
district_dict = {y:x for x,y in enumerate(df.District.value_counts().index.sort_values())}
#gender_dict = {y:x for x,y in enumerate(df.Gender.value_counts().index.sort_values())}
Tehsil_dict = {y:x for x,y in enumerate(df.Tehsil.value_counts().index.sort_values())}
#Result_dict = {y:x for x,y in enumerate(df.Result.value_counts().index.sort_values())}
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
#df['Gender_Encoded']= le.fit_transform(df['Gender'].values)
df['District_Encoded']= le.fit_transform(df['District'].values)
df['Tehsil_Encoded']= le.fit_transform(df['Tehsil'].values)
#df['Result_Encoded']= le.fit_transform(df['Result'].values)
#df['Result_txt_Encoded']= le.fit_transform(df['Result_txt'].values)

df3 = df[['District']].copy()
df3['Encoded']=df['District_Encoded']
df3=df3.drop_duplicates('District').reset_index().iloc[:,1:]
d5=df3.District.values
d6=df3.Encoded.values
District_dict = dict(zip(d5,d6))

df7 = df[['Tehsil']].copy()
df7['Encoded']=df['Tehsil_Encoded']
df7=df7.drop_duplicates('Tehsil').reset_index().iloc[:,1:]
d8=df7.Tehsil.values
d9=df7.Encoded.values
Tehsil_dict = dict(zip(d8,d9))
#print(Tehsil_dict)

df['District_Encoded']=df['District'].map(District_dict)
df['Tehsil_Encoded']=df['Tehsil'].map(Tehsil_dict)
df = df.drop(['District','Tehsil'],axis=1)

#Feature Selection
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
df_train = df[0:20418]
df_test = df[20418:]
X = df_train.drop(['Result_txt'],axis=1)
y = df_train.Result_txt
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model = SelectFromModel(Lasso(alpha=0.005,random_state=0))
model.fit(X_train,y_train)
features_selected = X_train.columns[model.get_support()]

##All features selected except Year
X_train = X_train.drop(['Year'],axis=1)
X_test = X_test.drop(['Year'],axis=1)

#Feature Normalization
from sklearn import preprocessing
r_scaler = preprocessing.MinMaxScaler()
r_scaler.fit(X_train)
X_train = pd.DataFrame(r_scaler.transform(X_train), index=X_train.index, columns=X_train.columns)

from sklearn import preprocessing
r_scaler = preprocessing.MinMaxScaler()
r_scaler.fit(X_test)
X_test = pd.DataFrame(r_scaler.transform(X_test), index=X_test.index, columns=X_test.columns)


##Random forest regressor model
from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor()
reg.fit(X_train,y_train)

pickle.dump(reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
