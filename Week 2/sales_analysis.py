import pandas as pd

#1.Load Data And Display Basic Info
df = pd.read_excel("SQL_Sales_Dataset_200_Rows.xlsx")
print("First 5 rows:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nDataset Shape:")
print(df.shape)

#2.Handle Missing Values And Duplicates
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())

#3.Group Data By Category-Find Total Revenue
print("\nTotal Revenue by Category:")
category_revenue = df.groupby("category")["total_price"].sum()
print(category_revenue)

#4.Sort Data By Multiple Columns
print("\nData Sorted by Category and Total Price:")
sorted_data = df.sort_values(
    by=["category", "total_price"],
    ascending=[True, False]
)
print(sorted_data)

#5.Create Correlation Matrix
print("\nCorrelation Matrix:")
correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix)