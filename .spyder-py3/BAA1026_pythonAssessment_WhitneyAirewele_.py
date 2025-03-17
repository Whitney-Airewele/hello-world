# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#EX1
city = 'Paris'
print('My favourite city is ', city)

#EX2
strVal = 'data analytics'
if 'a' in strVal:
    print('True')
else:
    print('False')

for a in strVal:
    print(sum(strVal) == 'a')
print('There are ')

#EX3
numLst = []
for numLst in range(9, 40, 3):
    print(numLst)

i = 0
while i > 39:
    i+=3
    print(i)

#EX4
ProdLst = [['Bluetooth Earphones, 10, 15.99', ], ['Reusable Water Bottles', 20, 9.49], ['Coffee Mugs', 15, 12.99], ['Notebook Packs', 30, 7.99], ['Portable Phone Chargers', 25, 19.99]]
print(ProdLst)
headLst = ['Product Type', 'Quantity', 'Unit Price']
print(headLst)
import pandas as pd
prodDf = pd.DataFrame(ProdLst, index_col = headLst)
print(prodDf)
prodDf['Total Price'] = prodDf['Unit Price']/prodDf['Quantity']
print(prodDf)
prodDf.drop(columns = 'Unit Price')
Quantity_coffee = prodDf.iloc[2, 1]
print(Quantity_coffee)
price_quantity = prodDf.loc['Reusable Water Bottles', 'Coffee Mugs', 'Notebook Packs']
print(price_quantity)

#Ex5
inpath = 'C:/Users/35389/Downloads/'
inpDf = pd.read_csv(inpath + 'Laptop_price.csv')
print(inpDf)
correVal = inpDf.correcoef('Weight (kg)', 'Inches')
print('Correlation between Inches and Weight is ', correVal)
inpDf['Weight (kg)'] = 'Weight (g)'.rename(inplace=True)
inpDf['Weight (g)'] = inpDf['Weight (g)']*100
medianVal = sum(inpDf['Inches'])/len(inpDf['Inches'])
print(medianVal)
Avg_weight =sum(inpDf['Weight(g)'])/len(inpDf['Weight (g)'])
if Avg_weight > medianVal:
    print(Avg_weight)
logarithim = np.log(inpDf['Inches'])
if logarithim > 15 :
    print(logarithim)
else:
    print(inpDf['Inches'])

#EX6
prodDict = {'Year': [2019, 2020, 2021, 2022, 2023], 'RevenueTUSD':[55190, 60709, 66228, 71747, 77266], 'RevenueT-1EUR': [44000, 50000, 55000, 60000, 65000]}
prodDf = pd.DataFrame(prodDict)
print(prodDf)

def EURUSD_(prodDf):
    prodDf['RevenueT-1EUR'] = prodDf['RevenueT-1EUR']*1.1038
    print(EURUSD_)

prodDf['RevenueT-USD'] = EURUSD_(prodDf['RevenueT-1EUR'])
print(prodDf)

import matplotlib.pyplot as plt
RevenueTUSD = [55190, 60709, 66228, 71747, 77266]
RevenueT1USD = [44000, 50000, 55000, 60000, 65000]
plt.plot(RevenueTUSD, color = 'b', RevenueT1USD, color = 'y')
plt.show()

#EX7
arr1 = np.arange(115, 201, 5).reshape(3, 6)
lst2 = [4, 5, 6, 7, 8, 9]
arr2 = np.array(lst2)
print(arr1)
print(arr2)
arr3 = arr1 - arr2
print(arr3)
avg = np.mean(arr3)
print(avg)






    
