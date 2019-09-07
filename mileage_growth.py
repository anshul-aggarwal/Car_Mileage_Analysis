import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd


#Extract models, price and mileage
df = pd.read_csv('fullspecs.csv',sep=',', header = None, nrows=3)

#Transpose data
df = df.transpose()

#Fix headers
df.columns = df.iloc[0]
df = df.rename(columns={np.NaN : "Model"})
df = df[1:]

# Remove specs from Model
df["Model"] = df["Model"].replace(to_replace =' Specs:.*', value = '', regex = True)


#Fix Make names
df["Model"] = df["Model"].replace(to_replace ='Alfa Romeo', value = 'Alfa-Romeo', regex = True)
df["Model"] = df["Model"].replace(to_replace ='Aston Martin', value = 'Aston-Martin', regex = True)
df["Model"] = df["Model"].replace(to_replace ='Land Rover', value = 'Land-Rover', regex = True)

#Split Year, Make and Model
model_split = df['Model'].str.split(" ", n=2, expand=True)
df["Year"] = model_split[0]
df["Make"] = model_split[1]
df["Model"] = model_split[2]

#Discover incorrect splits, fix above
#print(df.Make.unique())
#print(df[df.Model.str.contains(" ")].Model.unique())

#Split Highway and city mileage
mileage_split = df['Gas Mileage'].str.split("/", n=1, expand=True)
df["City mpg"] = mileage_split[0].replace(to_replace=' mpg City', value='', regex=True)
df["Highway mpg"] = mileage_split[1].replace(to_replace=' mpg Hwy', value='', regex=True)
df = df.drop('Gas Mileage', 1)



all_car_count=df.shape[0]
df = df.dropna()
non_ev_count=df.shape[0]
print("{0} EVs out of total {1} vehicles removed".format(all_car_count-non_ev_count, all_car_count))



#print(df[1800:1820])

