import pandas as pd

# reading file
df=pd.read_csv(r'C:\Users\cvalley\Desktop\my coding\.vscode\phython\Diwali Sales Data.csv',encoding="unicode_escape")

#Reading first 5 lines of data
print(df.head())

# to see rows and columns
print(df.shape)

#seeing information about each columns
print(df.info())

# droping two null columns
df.drop(['Status',"unnamed1"],axis=1,inplace=True)

#again reading first 5 rows to check deleted column
print(df.head()) 

#getting sum of all null values
print(pd.isnull(df).sum())
print(df.shape)

# droping null values
df.dropna(inplace=True)

# seeing null values
print(pd.isnull(df).sum())

# changing datatype of Amount column
df["Amount"]=df["Amount"].astype(int)
print(df.info())

#seeing datatype of column
print(df['Amount'].dtype)

#seeing columns name
print(df.columns)

# seeing discription of each value
print(df[["Amount","Age","Orders"]].describe())

# saving file
df.to_csv("cleaned file.csv")