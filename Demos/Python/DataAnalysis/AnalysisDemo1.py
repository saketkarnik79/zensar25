import pandas as pd

# Load CSV file
df = pd.read_csv("employees.csv")

# Display the data
print(df)

# Display first 5 records
print(df.head())

# Display information about dataset
print(df.info())

# find missing values
print(df.isnull())
print(df.isnull().sum())

# remove missing values
clean_df = df.dropna()
print(clean_df)

# replace missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

# remove duplicate records
df = df.drop_duplicates()
print(df)