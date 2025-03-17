arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([100, 200, 300, 400, 500])
correlation = np.corrcoef(arr1, arr2)
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([100, 200, 300, 400, 500])
correlation = np.corrcoef(arr1, arr2)
print("Correlation coefficient between arr1 and arr2:\n", correlation)
np.corrcoef(arr1, arr2)
arrZ1 = (arr1 - np.mean(arr1)) / np.std(arr1)
arrZ2 = (arr2 - np.mean(arr2)) / np.std(arr2)
print("Standardized arr1 (arrZ1):", arrZ1)
print("Standardized arr2 (arrZ2):", arrZ2)
print("Standardized arr1 (arrZ1):", arrZ1)
print("Standardized arr2 (arrZ2):", arrZ2)
import pandas as pd
inPath = "C:/Users/35389/Downloads/"
inPath2 = inPath + "Input File Pandas Ex3.csv"
print(inPath2)
pd.read_csv(inPath2)
import pandas as pd
inPath = "C:/Users/35389/Downloads/"
inPath2 = inPath + "Input File Pandas Ex3.csv"
print(inPath2)
pd.read_csv(inPath2)
populationLst = [339996563, 1425671352, 123294513]
gdpLst = [26854599, 19373586, 4409738]
AvgincLst = [46625, 4484, 21694]
datadict{'Population': populationLst, 'GDP(mil. $)': gdpLst, 'Avg. inc. ($, PPP)'}
dataDict = {'Population': populationLst, 'GDP(mil. $)': gdpLst, 'Avg. inc. ($, PPP)'}
dataDict = {'Population': populationLst, 'GDP(mil. $)': gdpLst, 'Avg. inc. ($, PPP)': AvgincLst}
df = pd.DataFrame(dataDict)
populationLst = [339996563, 1425671352, 123294513]
gdpLst = [26854599, 19373586, 4409738]
AvgincLst = [46625, 4484, 21694]
dataDict = {'Population': populationLst, 'GDP(mil. $)': gdpLst, 'Avg. inc. ($, PPP)': AvgincLst}
df = pd.DataFrame(dataDict)
dataLst = [[339996563, 26854599, 46625],[1425671352, 19373586, 4484],[123294513, 4409738, 21694]]
Df = pd.DataFrame(dataLst)
columnLst = ['population', 'GDP(mil. $)', 'Avg.inc. ($, PPP)']
Df = pd.DataFrame(dataLst, columns=columnLst)
print(dataLst)
print(df)
print(Df)
df.GDP(mil. $) = 1000000
df.'GDP(mil. $)'*1000000
print(df)
df['GDP(mil. $)'] = df['GDP(mil. $)']*1000000
print(df)
df.rename(columns={'GDP(mil. $': 'GDP ($)'})
print(df)
df.rename(columns={'GDP(mil. $)': 'GDP ($)'})
df['GDP per Cap'] = df['GDP ($)']/df['Population']
print(df)
df['GDP(mil. $)'] = df['GDP(mil. $)']*1000000
print(df)
df.rename(columns={'GDP(mil. $)': 'GDP ($)'})
print(df)
df.rename(columns={'GDP(mil. $)': 'GDP ($)'})
df['GDP per Cap'] = df['GDP ($)']/df['Population']
df.rename(columns={'GDP(mil. $)': 'GDP ($)'})
df.rename(columns={'GDP(mil. $)': 'GDP ($)'}, inplace=True)
print(df)
df['GDP per Cap'] = df['GDP ($)']/df['Population']
print(df)
print(inPath2)
pd.read_csv(inPath2)
pd.read_csv(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + "Input File Pandas Ex3.csv"
print(inpDf)
pd.read_csv(inpDf)
df.set_index(inpDf.index, inplace=True)
pd.read_csv(inpDf)
df.set_index(inpDf.index, inplace=True)
print(df)
df.columns
print(df)
outDf = pd.concat([inpDf, df['GDP per Cap']], axis=1)
print(outDf)
outDf = pd.concat([inpDf, df['GDP per Cap']], axis=1)
print(outDf)
print(arr2.std())
correlation = np.corrcoef(arr1, arr2)
lst2 = [100, 200, 300, 400, 500, 600]
arr2 = np.array(lst2)
print(arr2.mean())
correlation = np.corrcoef(arr1, arr2)
print(correlation)
print(arrZ1)
print(arrZ2)
print(round(arrZ1.mean(),4))
print(round(arrZ2.mean(),4))
print(round(arrZ1.std(),4))
print(round(arrZ2.std(),4))
print(arrZ1)
arrZ1[1] = np.nan
arrZ2[4] = np.nan
arrZ1[1] = np.nan
arrZ1[4] = np.nan
print(arrZ1)
np.isan(arrZ1)
np.isnan(arrZ1)
print(np.isnan(arrZ1))
print(sum(np.isnan(arrZ1)))
np.std(arrZ1)
np.nanstd(arrZ1)
arrZ1.std()
arrZ1.nanstd()
print(arrZ1.nanstd())
print(arrZ1.std())
np.nanstd(arrZ1)
np.std(arrZ1)
np.std(arrZ1, where=np.isan(arrZ1))
np.std(arrZ1, where=~np.isan(arrZ1))
np.std(arrZ1, where=np.isnan(arrZ1))
np.std(arrZ1, where=~np.isnan(arrZ1))
print(yVal)
yVal = 6*9
print(yVal)
print(strVal)
strVal = 'Business Analytics'
print(strVal)
if 'z' == strVal:
print('True')
else:
print('False')
if 'z' in strVal:
    print('True')
else:
    print('False')
if 'u' in strVal:
    print('True')
else:
    print('False')
print(strVal[2])
print(len(strVal))
print(strVal[:])
print(strVal[:5])
print(strVal[5:])
print(strVal[-5:])
print(strVal[-6:])
print(strVal[12:16])
print(strVal[12:])
print(strVal[:6])
print(strVal[-6:])
for cpt in range([3], 22,[3]):
    print(cpt)
for cpt in range(3, 22,3):
    print(cpt)
for cpt in range (100, 21, -5):
    print(cpt)
for cpt in range (100, 19, -5):
       print(cpt)
print(cpt)
for cpt in range (100, 22, -5):
    print(cpt)
for cpt in range (100, 19, -5):
    print(cpt)
for cpt in range (100, 21, -5):
    print(cpt)
for cpt in reversed(range(20,101.5)):
    print(cpt)
for cpt in reversed(range(20,101, -5)):
    print(cpt)
print(cpt)
for cpt in reversed(range(20,101, -5)):
    print(cpt)
for cpt in reversed(range(20,101, -5))
for cpt in reversed(range(20,101, -5)):
print(cpt)
for cpt in range (100, 19, -5):
    print(cpt)
for cpt in reversed(range(20,101, -5)):
    print(cpt)
for cpt in reversed(range(101, 20, -5)):
    print(cpt)
for cpt in reversed(range(20, 101, -5)):
    print(cpt)
i = 50
while i > 19:
    print(i)
    i -=5
i = 50
while i > 19:
    print(i)
    i =-5
i = 50
while i > 19:
    print(i)
    i +=5
i = 50
while i > 19:
    print(i)
    i -=5
Lst = [1, 2, 3, 4, 'Hello', 5.4, 6]
print(Lst)
if 8 in Lst:
    print('True')
else:
    print('False')
if 'Hello' in Lst:
    print('True')
else:
    print('False')
if 'hello' in Lst:
    print('True')
else:
    print('False')
for cpt in range(len(Lst)):
    print(cpt)
print(cpt, Lst)
for cpt in range(len(Lst)):
    print(Lst[cpt])
for cpt in range(len(Lst)):
    print(Lst(cpt))
for cpt in range(len(Lst)):
    print(Lst[cpt])
for cpt in range(len(Lst)):
    print(cpt, Lst[cpt])
for cpt in range(len(Lst)):
    print(Lst[cpt])
for cpt in Lst:
    print(cpt)
for cpt in range(1,6):
    Lst2.append(cpt)
    print(Lst2)
Lst2 = []
for cpt in range(1,6):
    Lst2.append(cpt)
    print(Lst2)
my_list = []
for i in range(1, 6):
    my_list.append(i)
    print(my_list)
print(Lst3)
Lst3 = [cpt for cpt in range(1,6)]
print(Lst3)
Lst4 = []
I = 1
I < 9
print(I)
Lst4 = []
I = 1
while I > 7:
     print(I)
Lst4 = []
I = 1
while I > 7:
    Lst4.append(I)
    print(I)
Lst4 = []
I = 1
while I <= 8:
    Lst4.append(I)
    I+=1
    print(I)
Lst4 = []
I = 1
while I > 7:
    Lst4.append(I)
    I+=1
    print(I)
print(I)
Lst4 = []
I = 1
while I > 7:
    Lst4.append(I)
    I+=1
    print(I)
Lst4 = []
I = 1
while I < 9:
    Lst4.append(I)
    I+=1
    print(I)
Lst4 = []
I = 0
while I <=8:
    Lst4.append(I)
    I+=1
    print(I)
Lst4 = []
I = 0
while I <=7:
    Lst4.append(I)
    I+=1
    print(I)
tmpLst1 = [1, 2, 3, 4, 5, 6]
tmpLst2 = []
a = 6
while a <=9:
    tmpLst2.append(a)
    a+=1 
    tmpLst1.extend(tmpLst2)
    print(tmpLst1)
print(tmpLst1)
tmpLst1 = [1, 2, 3, 4, 5, 6]
tmpLst2 = []
a = 6
while a <=9:
    tmpLst2.append(a)
    a+=1 
    tmpLst1.extend(tmpLst2)
    print(tmpLst1)
a = 7
while a <=10:
    tmpLst2.append(a)
    a += 1
tmpLst2=[]
a = 7
while a <=10:
    tmpLst2.append(a)
    a += 1
print(tmpLst1)
tmpLst1 = [1, 2, 3, 4, 5, 6]
a = 7
tmpLst2=[]
while a <=10:
    tmpLst2.append(a)
    a += 1 
    print(tmpLst1)
    print(tmpLst2)
    tmpLst1.extend(tmpLst2)
    print(tmpLst1)
print(tmpLst1)
help(tmpLst1.sorted)
tmpLst1.sort(reverse=True)
print(tmpLst1)
tmpLst1.insert(6, 100)
print(tmpLst1)
print(a*b)
lista = [11, 12, 13, 14, 15]
listb = [24, 27, 30, 33, 36]
for a in lista:
    for b in listb:
        if a*b > 400:
            print(a*b)
mytext[:2]
my_list = ['newspaper', 9.2, 4, 'pi']
mytext = my_list[0] + " " + str(my_list[1])
mytext[2]
mytext[:2]
my_dict['country'] = 'Ireland'
print(my_dict)
my_dict = {'name':'john', 'age': 21, 'city':'dublin'}
my_dict['name']
print(my_dict.keys())
print(my_dict.items())
for key, value in my_dict.items():
    print(key, value)

my_dict['country'] = 'Ireland'
print(my_dict)
my_dict2 = {1:['john', 21, 'dublin', 'ireland'],  2:['Jack', 22, 'London', 'England'], 
           3:['Iris', 21, 'Cork', 'Ireland']}
my_dict2[2]
my_dict2[4] = 'dan', 20, 'dublin', 'ireland' 
print(my_dict2)
def Mean_(lst5):
    if len(lst5) == 0:
        raise RuntimeError('List must be non-empty')
    else:
        return(sum(lst5) / len(lst5))

print(Mean_(lst5))
lst5 = [12, 15, 6, 13, 12, 18, 2, 15, 8, 9, 16, 14, 16]
num = 0
for elt in lst5:
    num+=elt
    print(num/len(lst5))

def Mean_(lst5):
    if len(lst5) == 0:
        raise RuntimeError('List must be non-empty')
    else:
        return(sum(lst5) / len(lst5))

print(Mean_(lst5))
print(Mean_(lst5))
np.array([0, 11, 3])
array=np.arange([0, 12, 3])
print(array)
array=np.arange(0, 12, 3)
print(array)
array1 = np.arange(0, 12).reshape(3,4)
print(array1)
array2 = np.arange(3, 75, 3).reshape(4, 3, 2)
print(array2)
array3 = np.random.random(3)
print(array3)
array4 = np.random.random(3).reshape(2)
print(array4)
array4 = np.random.random(3, 3)
print(array4)
array4 = np.random.rand(3, 3)
print(array4)
Lst = [1, 2, 3, 4, 5, 6]
array5 = np.array(Lst)
print(array5)
print(array5.mean())
print(array5.median())
Lst = [1, 2, 3, 4, 5, 6]
array5 = np.array(Lst)
print(array5)
print(array5.mean())
print(array5.median())
print(array5.median)
np.median(array5)
print(array5.mean())
np.std(array5)
Lst1 = [100, 200, 300, 400, 500, 600]
array6 = np.array(Lst1)
array6 = np.array(Lst1)
print(array6)
print(correlation)
print(covariance)
covariance = np.cov(array5, array6)
print(covariance)
print('Numpy Version:',np._version_)
print(array7)
Lst2 = [1, 2, 3, 4, 5, 6]
array7 = np.array(Lst2)
print(array7)
reshape = np.array7.reshape(2,3)
print(reshape)
print(reshape)
reshape = np.array(Lst2).reshape(2,3)
print(reshape)
row_sum = array7.sum(axis=1)
print(row_sum)
row_sum = array7.sum(axis=0)
print(row_sum)
column_sum = array7.sum(axis=0)
print(column_sum)
column_sum = array7.sum(axis=1)
print(column_sum)
print(reshape)
print(row_sum)
row_sum = reshape.sum(axis=1) #1 means rows 0 means columns
print(row_sum)
column_sum = reshape.sum(axis=0)
print(column_sum)
print(column_sum)
array7 = np.array(Lst2).reshape(2,3)
print(array7)
row_sum = array7.sum(axis=1) #1 means rows 0 means columns
print(row_sum)
print(df)
NameLst = ['Alice', 'Bob', 'Charlie', 'Diana']
DepartLst = ['HR', 'IT', 'Finance', 'IT']
AgeLst = [30, 25, 35, 40]
SalaryLst = [50000, 60000, 75000, 80000]
ExpLst = [5, 3, 10, 15]
datadict = {'Name': NameLst, 'Department': DepartLst, 'Age':AgeLst, 'Salary':SalaryLst, 'Experience (Years)':ExpLst}
df = pd.DataFrame(datadict)
print(df)
df['Bonus'] = df['Salary']*0.1
print(df)
it_employees = df[df['Department']=='IT']
print(it_employees)
Avg_salary = df['Salary'].average
print(Avg_salary)
Avg_salary = df['Salary'].mean()
print(Avg_salary)
df.sort(reverse=True)
print(df)
Exp_sort = df.sort_values(by='Experience (Years)', reverse=True)
print(Exp_sort)
Exp_sort = df.sort_values(by='Experience (Years)', ascending=False)
print(Exp_sort)
age = int(input('How old are you?'))
if age < 18:
    print('Minor')
else:
    print('Adult')
for i in range (1, 6):
    for j in range (1, 6):
        print(i*j)
print(i*j)
age = int(input('How old are you?'))
if age < 18:
    print('Minor')
else:
    print('Adult')
for i in range (1, 6):
    for j in range (1, 6):
        print(i * j, end='\t')
Exp_sort = df.sort_values(by='Experience (Years)', ascending=False)
print(Exp_sort)
print(df)
for i in range (1, 6):
    for j in range (1, 6):
        print(i * j, end='\t')
for i in range (1, 6):
    for j in range (1, 6):
        print(i * j)
for i in range (1, 6):
    for j in range (1, 6):
        print(i * j, end='\t')
print(str(i) + " * " + str(j) + " = " + str(i*j))
for i in range (1, 6):
    for j in range (1, 6):
        
        print(str(i) + " * " + str(j) + " = " + str(i*j))
datadict = {'a': 1, 'b': 2, 'c': 3}
for key, value in datadict.items():
    print(key, value)
array1 = np.array([5, 10, 15, 20, 25, 30])
third_element = array1[2]
print(third_element)
print(array1[2:])
print(array1[3:])
array2 = np.arange(1, 12)
print(array2)
array2 = np.arange(1, 13)
print(array2)
reshaped = np.array2.reshape(3, 4)
print(reshaped)
array2 = np.arange(1, 13)
print(array2)
reshaped = np.array2.reshape(3, 4)
print(reshaped)
array2 = np.arange(1, 13)
print(array2)
reshaped = array2.reshape(3, 4)
print(reshaped)
print(reshaped)
array3 = np.array([10, 20, 30, 40, 50])
print(array3)
array25 = array3[array3>25]
print(array25)
array4 = np.arange(1, 26)
print(array4)
reshaped1 = array4.reshaped(5, 5)
print(reshaped1)
array4 = np.arange(1, 26)
print(array4)
reshaped1 = array4.reshaped(5, 5)
print(reshaped1)
array4 = np.arange(1, 26)
print(array4)
reshaped1 = array4.reshape(5, 5)
print(reshaped1)
subarray = array4[1, 2, 3]
print(subarray)
subarray= array4[1:4]
print(subarray)
subarray= array4[1:4, 1:4]
print(subarray)
subarray= reshaped1[1:4]
print(subarray)
subarray= reshaped1[1:4, 1:4]
print(subarray)
sort = subarray.sort(ascending=False)
print(sort)
sort = subarray[::-1, :]
print(sort)
data = {'Product': ['Laptop', 'Tablet', 'Smartphone'], 'Price': [1000, 500, 800]}
df = pd.dataframe(data)
print(df)
data = {'Product': ['Laptop', 'Tablet', 'Smartphone'], 'Price': [1000, 500, 800]}
df = pd.DataFrame(data)
print(df)
print(df['product'])
print(df['Product'])
print(df['Price'].mean())
data2 = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 70, 90]}
df2 = pd.DataFrame(data2)
print(df2)
Score80 = df[df['Score'] >80]
print(Score80)
data2 = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 70, 90]}
df2 = pd.DataFrame(data2)
print(df2)
Score80 = df[df['Score'] >80]
print(Score80)
dfFlt = df[df['Score'] >80]
print(dfFlt)
data2 = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 70, 90]}
df2 = pd.DataFrame(data2)
print(df2)
dfFlt = df[df['Score'] >80]
print(dfFlt)
data3 = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df3 = pd.DataFrame(data3)
print(df3
data3 = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df3 = pd.DataFrame(data3)
print(df3)
df3['Salary'] = [50000, 60000, 70000]
print(df3)
data4 = {'Na(me': ['Alice', 'Bob', 'Charlie', 'David'],
 'Age': [25, 30, 35, 40],
 'Score': [85, 90, 95, 80]}
df4 = pd.DataFrame(data4)
print(df4)
rows = df4.iloc[:2]
print(rows)
rows = df4.iloc[:2, :]
print(rows)
print(df)
columns = df4.iloc[:,-2:]
print(columns)
rows_loc = df4.loc[df4['Score'] > 85]
print(rows_loc)
print(df4)
row_loc = df4.loc[df4['Name'] == 'David', 'Score'] = 85
print(row_loc)
row_loc = df4.loc[df4['Na(me'] == 'David', 'Score'] = 85
print(row_loc)
row_loc = df4.loc[df4['Na(me'] == 'David', 'Score'] = 85
print(df4)
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
plt.plot(X, Y)
plt.show()
plt.show()
import matplotlib.pyplot as plt
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
plt.plot(X, Y)
plt.show()
import matplotlib.pyplot as plt
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
plt.plot(X, Y, marker ='s')
plt.show()
import matplotlib.pyplot as plt
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
plt.plot(X, Y, marker ='s', linestyle = '--', colour = 'green')
plt.show()
import matplotlib.pyplot as plt
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
plt.plot(X, Y, marker ='s', linestyle = '--', color = 'green')
plt.show()
import matplotlib.pyplot as plt
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
plt.plot(X, Y, marker ='s', linestyle = '--', color = 'green', linewidth = 10)
plt.show()
dataDict = {"Years": [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016],
"Women": [175.7, 176.4, 176.5, 176.2, 175.9, 175.9, 175.7, 175.8, 175.3],
"Men": [189.1, 191.8, 193.5, 196.0, 194.7, 196.3, 194.4, 197.0, 197.8]}
heightsDf = pd.DataFrame(dataDict)
plt.plot("Years", "Women", data=heightsDf)
import pandas as pd
dataDict = {"Years": [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016],
"Women": [175.7, 176.4, 176.5, 176.2, 175.9, 175.9, 175.7, 175.8, 175.3],
"Men": [189.1, 191.8, 193.5, 196.0, 194.7, 196.3, 194.4, 197.0, 197.8]}
heightsDf = pd.DataFrame(dataDict)
plt.plot("Years", "Women", data=heightsDf)
plt.plot("Years", "Women", data=heightsDf)
import pandas as pd
import matplotlib.pyplot as plt
dataDict = {"Years": [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016],
"Women": [175.7, 176.4, 176.5, 176.2, 175.9, 175.9, 175.7, 175.8, 175.3],
"Men": [189.1, 191.8, 193.5, 196.0, 194.7, 196.3, 194.4, 197.0, 197.8]}
heightsDf = pd.DataFrame(dataDict)
plt.plot("Years", "Women", data=heightsDf)
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
X1 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y2 = [90, 89, 87, 82, 72, 60, 45, 28, 10, 0]
plt.plot(X, Y, marker='s', linestyle='-.', color='r')
plt.plot(X1, Y2, marker='^', linestyle=':', color='k')
import matplotlib.pyplot as plt
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
X1 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y2 = [90, 89, 87, 82, 72, 60, 45, 28, 10, 0]
plt.plot(X, Y, marker='s', linestyle='-.', color='r')
plt.plot(X1, Y2, marker='^', linestyle=':', color='k')
plt.plot(X, Y, marker='s', linestyle='-.', color='r')
plt.plot(X1, Y2, marker='^', linestyle=':', color='k')
import matplotlib.pyplot as plt
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
X1 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y2 = [90, 89, 87, 82, 72, 60, 45, 28, 10, 0]
plt.plot(X, Y, marker='s', linestyle='-.', color='r')
plt.plot(X1, Y2, marker='^', linestyle=':', color='k')
plt.show()
plt.plot(X, Y, marker='s', linestyle='-.', color='r')
plt.plot(X1, Y2, marker='^', linestyle=':', color='k')
plt.show()
plt.plot(X, Y, fmt1)
plt.plot(X1, Y2, fmt2)
plt.show()
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
fmt1 = 's-.r'
X1 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y2 = [90, 89, 87, 82, 72, 60, 45, 28, 10, 0]
fmt2 = '^k:'
plt.plot(X, Y, fmt1)
plt.plot(X1, Y2, fmt2)
plt.show()
plt.plot(X, Y, fmt1)
plt.plot(X1, Y2, fmt2)
plt.show()
plt.plot(X, Y, fmt1, X1, Y2, fmt2)
plt.show()
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.title('Line plot')
plt.xlabel['x-axis']
plt.ylabel['y-axis']
plt.show()
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.show()
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [3, 2, 1]
plt.plot(x1, y1, color = 'k')
plt.plot(x2, y2, color = 'r')
plt.show()
arr = np.array(42)
print(arr)
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = np.array.reshape(2,3)
print(reshaped_arr)
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(np._version_)
print(np.__version__)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print(arr.ndim)
print(len(strVal))
tmpLst1.sort(reverse=True)
print(tmpLst1)
tmpLst1.sort(reverse=True)
print(tmpLst1)
tmpLst1.pop(3)
tmpLst1.insert(6, 100)
print(tmpLst1)
arrZ1[1] = np.nan
arrZ1[4] = np.nan
print(arrZ1)
np.isnan(arrZ1)
print(sum(np.isnan(arrZ1)))
column_sum = array7.sum(axis=0)
print(column_sum)
print(a.ndim)
inPath = "C:/Users/35389/Downloads/"
inPath + 'Input File Pandas Ex3
pd.read_csv(inPath + 'Input File Pandas Ex3' )
inPath = "C:/Users/35389/Downloads/"
inPath + 'Input File Pandas Ex3'
pd.read_csv(inPath + 'Input File Pandas Ex3' )
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + 'Input File Pandas Ex3'
print(inpDf)
pd.read_csv(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + 'Input File Pandas Ex3'
print(inpDf)
pd.read_csv(inpDf)
df.set_index(inpDf.index, inplace=True)
print(df)
inPath = 'C:/Users/35389/Downloads/'
inpDf = pd.read_csv(inpPath + 'Input File Pandas Ex3 (1)', sep=',', header=0, index_col=0)
inPath = 'C:/Users/35389/Downloads/'
inpDf = pd.read_csv(inPath + 'Input File Pandas Ex3 (1)', sep=',', header=0, index_col=0)
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + 'Input File Pandas Ex3'
print(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + 'Input File Pandas Ex3'
print(inpDf)
pd.read_csv(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + 'Input File Pandas Ex3'
print(inpDf)
pd.read_csv(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = pd.read_csv(inPath + 'Input File Pandas Ex3')
print(inpDf)
import pandas as pd
inPath = "C:/Users/35389/Downloads/"
inpDf = pd.read_csv(inPath + 'Input File Pandas Ex3')
print(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = pd.read_csv(inPath + 'Input File Pandas Ex3 (1)')
print(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = pd.read_csv(inPath + 'Input File Pandas Ex3 (1)', sep=',', header=0, index_col=0)
print(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + 'Input File Pandas Ex3 (1).csv'
print(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + 'Input File Pandas Ex3 (1).csv'
print(inpDf)
pd.read_csv(inpDf, sep=',', header=0, index_col=0)
import pandas as pd
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + 'Input File Pandas Ex3 (1).csv'
print(inpDf)
pd.read_csv(inpDf)
inPath = "C:/Users/35389/Downloads/"
inpDf = inPath + 'Input File Pandas Ex3 (1).csv'
print(inpDf)
pd.read_csv(inpDf, delimiter=',', header=0, index_col=0)
array = np.arange(0, 12, 3)
print(array)
array1 = np.arange(0, 12).reshape(3, 4)
print(array1)
array2 = np.arange(3, 76).reshape(4, 3, 2)
print(array2)
array2 = np.arange(3, 76, 3).reshape(4, 3, 2)
print(array2)
array2 = np.arange(3, 75, 3).reshape(4, 3, 2)
print(array2)
np.random.random[3]
ra = np.random.random[3]
print(ra)
ra = np.random.random(3)
print(ra)
ra2 = np.random.random(3, 2)
print(ra2)
ra2 = np.random.random(3, 3)
print(ra2)
ra2 = np.random.rand(3, 3)
print(ra2)
ra2 = np.random.rand(3, 2)
print(ra2)
lst = [1, 2, 3, 4, 5, 6]
arr1 = np.array(lst)
print(arr1)
np_mean = np.mean(arr1)
print(np_mean)
np_median = np.median(arr1)
print(np_median)
np_std = np.std(arr1)
print(arr1)
np_std = np.std(arr1)
print(np_std)
lst2 = [100, 200, 300, 400, 500, 600]
arr2 = np.array(lst2)
print(arr2)
cov = np.cov(arr1, arr1)
print(cov)
corr = np.corrcoef(arr1, arr2)
print(corr)
print(np.__version__)
lst3 = [1, 2, 3, 4, 5, 6]
array3 = np.array(lst3)
print(array3)
reshaped = np.array3.reshape(2, 3)
print(reshaped)
reshaped = np.array(lst3).reshape(2, 3)
print(reshaped)
sum_row = array3.sum(axis=1)
print(sum_row)
sum_col = array3.col(axis=0)
print(sum_col)
sum_col = array3.sum(axis=0)
print(sum_col)
data= {'Name': ['Alice', 'Bob', 'Charlie', 'Diana'], 'Department': ['HR', 'IT', 'Finance', 'IT'], 'Age':[30, 25, 35, 40], 'Salary':[50000, 60000, 75000, 80000], 'Experience (Years)': [5, 3, 10, 15]}
df = pd.DataFrame(data)
data= {'Name': ['Alice', 'Bob', 'Charlie', 'Diana'], 'Department': ['HR', 'IT', 'Finance', 'IT'], 'Age':[30, 25, 35, 40], 'Salary':[50000, 60000, 75000, 80000], 'Experience (Years)': [5, 3, 10, 15]}
df = pd.DataFrame(data)
print(df)
df['Bonus'] = df['Salary']*0.1 
print(df)
avg_sal = df['Salary'].mean()
print(avg_sal)
sort = df.sort_values(by = 'Experience (Years)', ascending=False )
print(sort)
print(b.shape)
arr1 = np.arange(0, 12, 3)
print(arr1)
rand_val = np.random.rand[3]
print(rand_val)
rand_val = np.random.rand(3)
print(rand_val)
lst = [1, 2, 3, 4, 5, 6]
arr = np.array(lst)
print(arr)
avg = np.array(lst).mean()
print(avg)
std = np.array(lst).std()
print(std)
inPath = "C:/Users/35389/Downloads/"
inpDf = pd.read_csv(inPath + 'Input File Pandas Ex3.csv')
print(inpDf)
print(strVal[:5])
print(strVal[9:])
print(strVal[10:])
print(strVal[12:])
mytext = my_list.concat(0,1)
print(mytext)
my_dict['country'] = 'Ireland'
print(my_dict)
my_dict2[2]
subarray= reshaped1[1:4, 1:4]
print(subarray)
sort = subarray[::-1, :]
print(sort)
subarray= reshaped1[1:4, 1:4]
print(subarray)
sort = subarray[::-1, :]
print(sort)
sort =subarray(reverse = True)
print(sort)
df4 = pd.DataFrame(data4)
print(df4)
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.show()
plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.show()
plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [3, 2, 1]
plt.plot(x1, y1, color = 'k')
plt.plot(x2, y2, color = 'r')
plt.legend()
plt.show()
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [3, 2, 1]
plt.plot(x1, y1, color = 'k')
plt.plot(x2, y2, color = 'r')
plt.legend(['x y', 'x1 y1'])
plt.show()
inPath = "C:/Users/35389/Downloads/"
inpDf = pd.read_csv(inPath + 'Input File Pandas Ex3.csv')
print(inpDf)
array4 = np.arange(1, 26)
print(array4)
reshaped1 = array4.reshape(5, 5)
print(reshaped1)
subarray= reshaped1[1:4, 1:4]
print(subarray)
sort = subarray[::-1, :]

## ---(Wed Nov 27 09:00:11 2024)---
print('My favourite city is ' + '' + 'city')
print('My favourite city is ' + '', city)
print('My favourite city is ' + '', 'city')
print(city)
city = 'Paris'
print(city)
city = 'Paris'
print('My favourite city is ', city)
strVal = 'data analytics'
if 'a' in strVal:
    print('True')
else:
    print('False')
print(sum(strVal) == 'a')
for a in strVal:
    print(sum(strVal))
for a in strVal:
    print(sum(strVal) == 'a')
ProdLst = [['Bluetooth Earphones, 10, 15.99', ], ['Reusable Water Bottles', 20, 9.49], ['Coffee Mugs', 15, 12.99], ['Notebook Packs', 30, 7.99], ['Portable Phone Chargers', 25, 19.99]]
print(ProdLst)
headLst = ['Product Type', 'Quantity', 'Unit Price']
print(headLst)
prodDf = pd.DataFrame(ProdLst)
print(prodDf)
import pandas as pd
prodDf = pd.DataFrame(ProdLst)
print(prodDf)
prodDf.set(headLst)
print(prodDf)
prodDf = pd.set(headLst)
print(prodDf)
import pandas as pd
prodDf = pd.DataFrame(ProdLst)
print(prodDf, columns= headLst)
print(prodDf, col= headLst)
import pandas as pd
prodDf = pd.DataFrame(ProdLst).set(columns = headLst)
print(prodDf)
import pandas as pd
prodDf = pd.DataFrame(ProdLst, index_col = headLst)
print(prodDf)
import pandas as pd
prodDf = pd.DataFrame(ProdLst, col_index = headLst)
print(prodDf)
prodDf['Total Price'] = prodDf['Unit Price']/prodDf['Quantity']
print(prodDf)
prodDf.drop(columns = 'Unit Price')
Quantity_coffee = prodDf.iloc['Coffee Mugs']
print(Quantity_coffee)
Quantity_coffee = prodDf.iloc[1]
print(Quantity_coffee)
Quantity_coffee = prodDf.iloc[2]
print(Quantity_coffee)
Quantity_coffee = prodDf.iloc[2, 1]
print(Quantity_coffee)
prodDf.loc['Reusable Water Bottles', 'Coffee Mugs', 'Notebook Packs']
price_quantity = prodDf.loc['Reusable Water Bottles', 'Coffee Mugs', 'Notebook Packs']
print(price_quantity)
for numLst in range(9, 40, 3):
    print(numLst)
i = 0
while i > 39:
    i+=3
    print(i)
inpath = 'C:/Users/35389/'
inpDf = pd.read_csv(inpath + 'Laptop_Price.csv')
print(inpDf)
inpath = 'C:/Users/35389/'
inpDf = pd.read_csv(inpath + 'Laptop_price.csv')
print(inpDf)
inpath = 'C:/Users/35389/Downloads/'
inpDf = pd.read_csv(inpath + 'Laptop_price.csv')
print(inpDf)
correVal = inpDf.corrcoef('Weight (kg)', 'Inches')
print(correVal)
correVal = inpDf.correcoef('Weight (kg)', 'Inches')
print(correVal)
correVal = pd.correcoef('Weight (kg)', 'Inches')
print(correVal)
correVal = np.correcoef('Weight (kg)', 'Inches')
print(correVal)
import numpy as np
correVal = np.correcoef('Weight (kg)', 'Inches')
print(correVal)
inpDf['Weight (g)'] = inpDf['Weight (kg)']*100
prodDict = {'Year': [2019, 2020, 2021, 2022, 2023], 'RevenueTUSD':[55190, 60709, 66228, 71747, 77266], 'RevenueT-1EUR': [44000, 50000, 60000, 65000]}
prodDf = pd.DataFrame(prodDict)
print(prodDf)
prodDict = {'Year': [2019, 2020, 2021, 2022, 2023], 'RevenueTUSD':[55190, 60709, 66228, 71747, 77266], 'RevenueT-1EUR': [44000, 50000, 55000, 60000, 65000]}
prodDf = pd.DataFrame(prodDict)
print(prodDf)
def EURUSD_(prodDf):
    prodDf['RevenueT-1EUR'] = prodDf['RevenueT-1EUR']*1.1038
    print(EURUSD_)
def EURUSD_(prodDf):
    prodDf['RevenueT-1EUR'] = prodDf['RevenueT-1EUR']*1.1038
    print(EURUSD_)
    print(prodDf)
prodDf['RevenueT-USD'] = EURUSD_(prodDf['RevenueT-1EUR'])
print(prodDf)
print((44000*1.1038), (50000*1.1038), (55000*`1.1038), (60000*1.1038), (65000*1.1038))
import matplotlip.pyplot as plt
RevenueTUSD = [55190, 60709, 66228, 71747, 77266]
RevenueT-1USD = [(44000*1.1038), (50000*1.1038), (55000*`1.1038), (60000*1.1038), (65000*1.1038)]
plt.plot(RevenueTUSD, RevenueT-1USD)
Plt.show()
import matplotlip.pyplot as plt
RevenueTUSD = [55190, 60709, 66228, 71747, 77266]
RevenueT1USD = [44000, 50000, 55000, 60000, 65000]
plt.plot(RevenueTUSD, RevenueT1USD)
plt.show()
import matplotlib.pyplot as plt
RevenueTUSD = [55190, 60709, 66228, 71747, 77266]
RevenueT1USD = [44000, 50000, 55000, 60000, 65000]
plt.plot(RevenueTUSD, RevenueT1USD)
plt.show()
arr1 = np.arange(115, 201, 5).reshape(3, 6)
lst2 = [4, 5, 6, 7, 8, 9]
arr2 = np.array(lst2)
print(arr1)
print(arr2)
arr3 = arr2 - arr1
print(arr3)
arr3 = arr1 - arr2
print(arr3)
avg = np.mean(arr3)
print(avg)
avg = np.mean(arr3)[0]
print(avg)
avg = np.mean(arr3)
print(avg)