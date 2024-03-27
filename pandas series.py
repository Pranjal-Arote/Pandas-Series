# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:16:30 2023


@author: Pranjal Arote
"""

import pandas as pd
df=pd.read_csv("C:/1-python/Computer_Data.csv.xls")
#df properties
df.dtypes
df.shape
df.columns
df.index
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###
#accessing the certain columns 
df["price"] 
df[["ram","screen"]]

#assigning the rows to another data frame object
df1=df[:5] 
#It will access the recored stored in the rows starting from 0 to the 4
df2=df[6:]
#It will access the records stored in the rows starting from the 6 and the last rows
df1
df2

#describe method
df.describe()


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###

#renaming the columns
df.columns({'c1':'A','c2':'B','c3':'C','c4':'D','c5':'E'})
df2=df.rename({'c1':'A','c2':'B','c3':'C','c4':'D','c5':'E'},axis=1)
df2=df.rename({'c6':'F','c7':'G'},axis="columns")
df3=df.rename(columns={'c1':'A','c2':'B','c3':'C','c4':'D','c5':'E'})
df2
df3
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##
#droping a row by its label
df.drop([['R0','R1']])
df1
#drop  by the index
df1=df.drop(df.index[1,6])
df1
#drop index by the 
df1=df.drop([2,6])
df1
#drop a row by the default index
df1=df.drop(0)

df1
df1=df.drop([1,4])
df1
df1=df.drop(df.index[3,9])
df1
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###
#drop a column  
 
#drop a column by the name
df1=df.drop(["speed"],axis=1)
print(df1)
#drop a column by the label explicitely
df1=df.drop(["hd","screen"],axis=1)
print(df1)
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###
#using inplace true drop the columns
df2=df.drop(df.columns[[1]],axis=1,inplace=True)
print(df2)
#########################################################
#drop 2 or more columns by their labels
df2=df.drop(["cd","multi","trend"],axis=1)
print(df2)
#               OR            #
lst=['cd','screen','premium']
df2=df.drop(lst,axis=1)
df2
#drop columns by their indexes
df2=df.drop([0,4])
print(df2)

#####################################################################
#ILOC
#select the rows by their labels,indexes  by using the iloc
#syntax:
# df.iloc[start_index:end_index,start_column:end_column]
df2=df.iloc[:,1:5]
print(df2) 
#here it will select all the rows from the column from 1 to 4
 
df2=df.iloc[2:4,:]
print(df2)
#here it will select 2,3 rows from all the columns
df2=df.iloc[0:3,0:3]
print(df2)
#here it will select 0,1,2 rows from 0,1,2 columns

#select row by using the index
df2=df.iloc[1,2,3] #select rows 1,2,3
df2
df2=df.iloc[1:6]
df2

df2=df.iloc[:-3]
df2
df2=df.iloc[-1:-5]
df2

#select a column by the index label
df2=df.loc['R1':'R5'] #It will select the 1,2,3,4 row
df2
df2=df.loc[:'R6'] #It will select all 5 rows
df2
df2=df.loc['R4':]
df2 #It will select rows starting from R6 to last row
df3=df.loc['R3':'R5':2] #It will select the 3,5,8 rows
df3

############################################################################
#pandas select columns by using the names

df2=df["price"]
df2
df2=df[["multi","premium","ads"]]
df2

#loc to slice
#df.loc[:,start:end:step]
#select multiple columns
df2=df.loc[:,["multi","trend"]]
df2

#select random columns
df3=df.loc[:,["ram","cd","ads"]]
df3

#select column by the range
df4=df.loc[:,["price","apeed","screen"]]
df4

#select columns between the two columns
df2=df.loc[:,'price':'premium']
df2

#select all columns after duration

df2=df.loc[:,"price":]
df2

#select all columns before duration

df3=df.loc[:, :"ads"]
df3

#query all row with course equal to spark
#pandas dataframe query()
#equal condition
df2=df.query("screen=='Good'")
df2

#not equal conditions
df2=df.query("screen!='Good'")
df2

#Adding Columns into Dataframe
df=pd.read_csv("C:/1-python/Computer_Data.csv.xls")
df

tutors=['Ram','Sham','Megha','Anay','Pallu']
df2=df2.assign(AssignTutors=tutors)
df2

#Adding multiple columns to pandas Dataframe
MNC=['Spyder','Celebal','Cipla','Chemiard','Iodine']
df2=df2.assign(MNCCompanies=MNC,AssignTutors=tutors)
df2


#Pandas add column to dataframe
df2=df.drop(df.index[5:])
df2

Add=['ABC','PQR','STU','EFG','KLM']
df2=df2.assign(Address=Add)
print(df2)

df2=df[['ram']]
df2

df2=df.loc[:,'ram':'trend']
df2

df2=df.loc[:,:'premium']
df2

df2=df.loc[:,'speed':]
df2

df3=df.iloc[5:3:2]
df3

df4=df.iloc[1:]
df4

df3=df.rename({'c1':'A','c2':'A'},axis=1)
df3

df2=df.rename({'screen':'screen_list'},axis=1,inplace=True)
df.columns

#################################################################
#count the number of rows and columns
import pandas as pd
df=pd.read_csv("C:/1-python/Computer_Data.csv.xls")
df
row_count=len(df.index)
row_count

new_count=len(df.axes[0])
new_count

#################################################
#To return no of rows and columns
#shape is used to calculate the no of rows and columns present in the dtaframe
#0=For the rows
#1=for the columns
rows=df.shape[0]
columns=df.shape[1]
print("No of rows are:",rows)
print("No of columns are:",columns)

df.columns
df.dtypes

######################################################
#Apply function to the dataframe
import numpy as np
import pandas as pd
df=pd.read_csv("C:/1-python/Computer_Data.csv.xls")
print(df)
def add_3(x):
              return x+3
df2['ads']=df['ads'].apply(add_3)
print(df2['ads'])


df2=df.apply(lambda x : x + 10)
print(df2)

def mul_3(x):
    return x*3
df2=df.transform(mul_3)
print(df2)


#############################################################
'''Pandas dataframe to get columns name from headers
For the column Headers we can use the list method and by using the list method 
inside that we can use the
1. df.columns.values=It is used for the giving the 
column names in the form of the list
2.df.columns=It is used to give the column names
3.df=Inside the list function we can use the df it is used for giving the column names 
'''

import pandas as pd
import numpy as np
df=pd.read_csv("C:/1-python/Computer_Data.csv.xls")
df
column_headers=list(df.columns.values)
print("Column headers are:",column_headers)

column_headers=list(df.columns)
print('"Column Headers are:',column_headers)

column_headers=list(df)
print("column headers are",column_headers)

#if there is less accuracy and we want to shuffle the rows
#and the columns 
#so we can use the sample(fac1) method
df1=df.sample(frac=1)
df1


pd="Just recomend what will be the output of the program just know about it"
print(pd)
st="  Will you recognize"
print(pd+st)
print("You all have to do it like this just notice this whenever you have to do the addition just use the add function")

 






