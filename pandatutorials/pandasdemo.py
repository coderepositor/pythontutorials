"""
pandas is used for data analysis , it is strong flexible python package
which helps with data cleaning and wrangling tasks

Advantages:
1. creates structured data similar to ms excel spreadsheet
2. Reads data from various sources like csv, txt,xlsx, sql database etc..
3. Selects rows and columns from dataset
4. Arranging data in ascending and descending order
5. filtering data
6. Aggregation or summarizing data
7. Transpose data into wide and long format
8. Merging and concatenating two datasets
"""

import pandas as pd
import numpy as np
df = pd.read_csv("income.csv") #reading the csv using pandas
#print(df1.head())
#print(df)
income_dc = df.columns #all data columns from the income dataset
#print(income_dc)
#first 2 columns from the  income dataset
#print(income_dc[:2])
#find datatypes for all the columns
#print(df.dtypes)
df.Y2008 = df.Y2008.astype(float) #converts integer type into float datatype
#print(df.dtypes)
#print("total number of rows and columns:",df.shape)
#print("total number of rows:",df.shape[0])
#print("total number of columns:",df.shape[1])
#print("First Five Rows from income dataset")

#print(df.head())
#print("Last Five Rows from income dataset")
#print(df.tail())
#print("First three Rows from income dataset")
#print(df.head(3))
#print("Last three Rows from income dataset")
#print(df.tail(3))
#print(df.iloc[0:5])
#print(df[0:5])

#print("Distinct values of the column index")
u_values = df.Index.unique()
#print(u_values, len(u_values))

#biverate frequency distribution
#print(pd.crosstab(df.Index,df.State))

#creating frequency distribution based on the Index
#print(df.Index.value_counts(ascending=True))

#Random Sampling
data = df.sample(n=10) #getting 10 rows as sample from entire dataset
#print(data)
data = df.sample(frac=0.1) #sample of 10% of the entire dataset
#print(data)
#print(data["State"] , data.State) #selecting columns

#multiple columns by name
#print(df[["Index","State","Y2008"]])

data = df.loc[:,["Index","State","Y2008"]]
#print(data)

data = df.loc[0:2,["Index","State","Y2008"]]
#print(data)
data = df.iloc[0:5,0:4]
#print(data)

Zodiac_data = pd.DataFrame({"Name":["John","Mary","Julia","Kenny","Henry"],
                            "Sunsign": ["Libra","Virgo", "Leo","Capricon","Aries"]})
#print(Zodiac_data)
#print(Zodiac_data.columns)
Zodiac_data.columns = ["Names","SunSigns"] #renaming the columns
#print(Zodiac_data)
Zodiac_data.rename(columns = {"Names":"Cust_Name"},inplace=True) #renaming the columns
#print(Zodiac_data)
df.columns = df.columns.str.replace('Y','Year')
#print(df.columns)
#print(df.head())
df.set_index("Index",inplace=True)
#print(df.columns)
#print(df.head())
df.reset_index(inplace=True)
#data = df.drop(['Index','State'],axis=1) #dropping columns Index and State
#data = df.drop(['Index',axis="columns") #dropping column Index
#print(data)
data = df.drop(0,axis=0) #removing first row
data = df.drop([0,1,2,4],axis=0)#removing multiple rows with given index
#print(data)
#print(df.sort_values("State",ascending=False))
#print(df.Year2008.sort_values())
#print(df.sort_values(["Index","State"]))

df["difference"] =df.Year2008 - df.Year2009
#print(df["difference"])

df["difference2"] =df.eval("Year2003-Year2002")
#print(df.head())

#df.ratio = df.Year2008/df.Year2009
#print(df.ratio)

data = df.assign(ratio = (df.Year2008/df.Year2009))
#print(data.head())

#print(df.describe()) #for numeric variables

#print(df.describe(include=['object'])) #only for strings/objects

#print(df.Year2008.mean(),df.Year2008.median(),df.Year2008.agg(["mean","median"]))

#print(df.Year2008.min())

#print(df.Year2008.agg(["mean","median","min"]))

#print(df.loc[:,["Year2002","Year2008"]].max())

""" Group By Functions """
#print(df.groupby("Index")["Year2002","Year2003"].min())

#print(df.groupby("Index")["Year2002","Year2003"].agg(["min","max","mean"]))

#print(df.groupby("Index").agg({"Year2002":[min,max],"Year2003": "mean"}))

# dt = df.groupby("Index").agg({"Year2002":[min,max],"Year2003": "mean"})
# dt.columns = ['Y2002_min', 'Y2022_max', 'Y2003_mean']
#print(dt)

#print(df.groupby(["Index","State"]).agg({"Year2002":[min,max],"Year2003": "mean"}))

""" Filtering """
#print(df[df.Index=="A"])
#print(df.loc[df.Index=="A"])#All the columns where Index is A
#print(df.loc[df.Index=="A","State"])# only State Column where Index is A
#filter the rows with index as A and salary greater than 15 lacs
#print(df.loc[(df.Index=="A") & (df.Year2002 > 1500000),:])
#filter the  rows with index either A or W
#print(df.loc[(df.Index=="A") | (df.Index=="W"),:])
##alternative
#print(df.loc[df.Index.isin(["A","W"]),:])
#alternative
#print(df.query("Year2002>1700000 & Year2003>1500000"))

mydata = {'Crop': ['Rice', 'Wheat', 'Barley', 'Maize'],
    'Yield': [1010, 1025.2, 1404.2, 1251.7],
    'cost' : [102, np.nan, 20, 68]}
crops = pd.DataFrame(mydata)
# print(crops)
# print(crops.isnull()) #return true if values is null
# print(crops.notnull()) #return true if values is not null
# print(crops.isnull().sum())#count number of missing values in dataset

# print("1",crops[crops.cost.isnull()] )#shows the rows with NAs.
# print("2",crops[crops.cost.isnull()].Crop ) #shows the rows with NAs in crops.Crop
# print("3", crops[crops.cost.notnull()].Crop) #shows the rows without NAs in crops.Crop


#crops.dropna(how = "any") #any data is  missing in the row drop that row
#print(crops.shape)
# print(crops)
# crops.dropna(how = "all").shape #if all data is missing for that row then only drop the row
# #To remove NaNs if any of 'Yield' or'cost' are missing we use the subset parameter and pass a list:
# crops.dropna(subset = ['Yield',"cost"],how = 'any').shape
# crops.dropna(subset = ['Yield',"cost"],how = 'all').shape
# crops['cost'].fillna(value = "UNKNOWN",inplace = True)
# print(crops)
data = pd.DataFrame({"Items" : ["TV","Washing Machine","Mobile","TV","TV","Washing Machine"], 
                     "Price" : [10000,50000,20000,10000,10000,40000]})
#print(data)

#print(data.loc[data.duplicated(),:])
#print(data.loc[data.duplicated(keep = "first"),:])
#x = data.loc[data.duplicated(keep = "last"),:] #last entries are not there,indices have changed.
#print(x)
# x = data.loc[data.duplicated(keep = False),:]
# print(x)
# x = data.loc[data.duplicated(keep = "first"),:]
# print(x)
# x = data.loc[data.duplicated(keep = "last"),:]
# print(x)

"""
By default keep = 'first' i.e. the first occurence is considered a unique value 
and its repetitions are considered as duplicates. 
If keep = "last" the last occurence is considered a unique value 
and all its repetitions are considered as duplicates.
"""
#print(data.drop_duplicates(keep = "first"))
#print(data.drop_duplicates(keep = "last"))
# data.drop_duplicates(keep = False,inplace = True) #by default inplace = False
# print(data)


iris = pd.read_csv("iris.csv")
print(iris)


#map( ) function is used to match the values and replace them in the new series automatically created.
# iris["setosa"] = iris.Species.map({"setosa" : 1,"versicolor":0, "virginica" : 0})
# print(iris.tail())

pd.get_dummies(iris.Species,prefix = "Species")
pd.get_dummies(iris.Species,prefix = "Species").iloc[:,0:1] #1 is not included
species_dummies = pd.get_dummies(iris.Species,prefix = "Species").iloc[:,0:]

#print(species_dummies)

iris = pd.concat([iris,species_dummies],axis=1)
#print(iris)

#print(iris.rank())

# df = pd.DataFrame({'score': [85, 90, 78, 90,90, 82,96,90]})
# #print(df)
# df['rank'] = df['score'].rank()
# print(df)

# iris['Rank2'] = iris['Sepal.Length'].groupby(iris["Species"]).rank(ascending=1)
# print(iris.head())

# iris['cum_sum'] = iris["Sepal.Length"].cumsum()
# print(iris.head())


# iris["cumsum2"] = iris.groupby(["Species"])["Sepal.Length"].cumsum()
# print(iris.head())



students = pd.DataFrame({'Names': ['John','Mary','Henry','Augustus','Kenny'],
'Zodiac Signs': ['Aquarius','Libra','Gemini','Pisces','Virgo']})

def name(row):
    if row["Names"] in ["John","Henry"]:
        return "yes"
    else:
        return "no"
# students['flag'] = students.apply(name, axis=1)
# print(students)

students['flag'] = np.where(students['Names'].isin(['John','Henry']), 'yes', 'no')
#print(students)


def mname(row):
    if row["Names"] == "John" and row["Zodiac Signs"] == "Aquarius" :
        return "yellow"
    elif row["Names"] == "Mary" and row["Zodiac Signs"] == "Libra" :
        return "blue"
    elif row["Zodiac Signs"] == "Pisces" :
        return "blue"
    else:
        return "black"
students['color'] = students.apply(mname, axis=1)
#print(students)

conditions = [
  (students['Names'] == 'John') & (students['Zodiac Signs'] == 'Aquarius'),
  (students['Names'] == 'Mary') & (students['Zodiac Signs'] == 'Libra'),
  (students['Zodiac Signs'] == 'Pisces')]
choices = ['yellow', 'blue', 'purple']
students['color'] = np.select(conditions, choices, default='black')
# print(students)

data1 = iris.select_dtypes(include=[np.number])
# print(data1.head())

# data3 = iris._get_numeric_data()
# print(data3.head(3))

data4 = iris.select_dtypes(include = ['object'])
print(data4.head(2))



























